import copy
import unittest

from engine.validators import validate_all, validate_approval, validate_rights, validate_schema, validate_timing, validate_tool_mapping
from tests.helpers import bible, valid_packet


def codes(rep):
    return {f.code for f in rep.errors}


class TestSchema(unittest.TestCase):
    def test_valid_packet_passes_all_gates(self):
        rep = validate_all(valid_packet(), bible())
        self.assertTrue(rep.ok, rep.as_dict())

    def test_missing_required_field(self):
        p = valid_packet(); del p["scenes"]
        self.assertFalse(validate_schema(p).ok)

    def test_bad_enum(self):
        p = valid_packet(); p["status"] = "shipped"
        self.assertFalse(validate_schema(p).ok)

    def test_additional_scene_field_rejected(self):
        p = valid_packet(); p["scenes"][0]["vibe"] = "cool"
        self.assertFalse(validate_schema(p).ok)


class TestTiming(unittest.TestCase):
    def test_gap(self):
        p = valid_packet(); p["scenes"][1]["start_s"] = 5.0
        self.assertIn("TIMING_GAP", codes(validate_timing(p)))

    def test_overlap(self):
        p = valid_packet(); p["scenes"][1]["start_s"] = 3.0
        self.assertIn("TIMING_OVERLAP", codes(validate_timing(p)))

    def test_total_off_target(self):
        p = valid_packet(); p["scenes"][2]["end_s"] = 20
        self.assertIn("TIMING_TOTAL", codes(validate_timing(p)))

    def test_speech_too_fast(self):
        p = valid_packet(); p["brief"]["format"] = "spoken_episode"
        p["scenes"][0]["dialogue"] = [{"speaker": "Inspector", "line": " ".join(["word"] * 30), "on_camera": True}]
        self.assertIn("SPEECH_TOO_FAST", codes(validate_timing(p)))

    def test_silent_with_dialogue(self):
        p = valid_packet(); p["scenes"][0]["dialogue"] = [{"speaker": "Inspector", "line": "Hmm.", "on_camera": True}]
        self.assertIn("SILENT_HAS_DIALOGUE", codes(validate_timing(p)))

    def test_too_many_cuts(self):
        p = valid_packet(); p["scenes"][0]["cuts_inside_clip"] = 2
        self.assertIn("TOO_MANY_CUTS", codes(validate_timing(p)))


class TestDirectionContinuity(unittest.TestCase):
    def test_missing_camera(self):
        p = valid_packet(); p["scenes"][1]["camera"]["lens"] = ""
        self.assertIn("MISSING_CAMERA", codes(validate_all(p, bible())))

    def test_missing_audio(self):
        p = valid_packet(); p["scenes"][1]["sound"]["ambience"] = "n/a"
        self.assertIn("MISSING_AUDIO", codes(validate_all(p, bible())))

    def test_multi_speaker_shot(self):
        p = valid_packet(); p["brief"]["format"] = "spoken_episode"
        p["scenes"][0]["dialogue"] = [{"speaker": "A", "line": "hi", "on_camera": True}, {"speaker": "B", "line": "hi", "on_camera": True}]
        self.assertIn("MULTI_SPEAKER_SHOT", codes(validate_all(p, bible())))

    def test_undeclared_prop(self):
        p = valid_packet(); p["scenes"][0]["props_from_frame_one"].append("umbrella")
        self.assertIn("PROP_UNDECLARED", codes(validate_all(p, bible())))

    def test_identity_anchor_drift(self):
        p = valid_packet(); p["continuity"]["identity_anchors"] = "a face"
        self.assertIn("CONTINUITY_ANCHORS", codes(validate_all(p, bible())))

    def test_bible_do_not_token(self):
        p = valid_packet(); p["scenes"][0]["action"] += " He strokes his moustache."
        self.assertIn("BIBLE_DO_NOT", codes(validate_all(p, bible())))


class TestToolMapping(unittest.TestCase):
    def test_unsupported_control(self):
        p = valid_packet(); p["tool_mapping"]["units"][0]["controls"]["lens_mm"] = 35
        self.assertIn("TOOL_UNSUPPORTED_CONTROL", codes(validate_tool_mapping(p)))

    def test_unknown_model(self):
        p = valid_packet(); p["tool_mapping"]["units"][0]["model"] = "sora_9000"
        self.assertIn("TOOL_UNKNOWN_MODEL", codes(validate_tool_mapping(p)))

    def test_duration_out_of_range(self):
        p = valid_packet(); p["tool_mapping"]["units"][0]["model"] = "kling3_0"
        p["scenes"][2]["end_s"] = 30; p["brief"]["duration_target_s"] = 30
        self.assertIn("TOOL_DURATION", codes(validate_tool_mapping(p)))

    def test_unmapped_scene(self):
        p = valid_packet(); p["tool_mapping"]["units"][0]["scene_ids"].remove("S3")
        self.assertIn("TOOL_UNMAPPED_SCENES", codes(validate_tool_mapping(p)))

    def test_motion_transfer_needs_driving_video(self):
        p = valid_packet(); u = p["tool_mapping"]["units"][0]; u["model"] = "hf_mult_motion_control"; u["controls"] = {"resolution": "720p"}
        u["medias"] = [m for m in u["medias"] if m["role"] != "video_references"]
        self.assertIn("TOOL_NEEDS_DRIVING_VIDEO", codes(validate_tool_mapping(p)))


class TestRightsApproval(unittest.TestCase):
    def test_music_undeclared(self):
        p = valid_packet(); p["scenes"][0]["sound"]["music"] = "upbeat sting"
        self.assertIn("RIGHTS_MUSIC_UNDECLARED", codes(validate_rights(p)))

    def test_driving_footage_rights(self):
        p = valid_packet(); p["tool_mapping"]["units"][0]["model"] = "hf_mult_motion_control"
        self.assertIn("RIGHTS_DRIVING_FOOTAGE", codes(validate_rights(p)))

    def test_unresolved_rights_block_render_status(self):
        p = valid_packet(); p["status"] = "approved-for-render"
        self.assertIn("RIGHTS_UNRESOLVED_AT_RENDER", codes(validate_rights(p)))

    def test_commercial_firsthand_claim(self):
        p = valid_packet(); p["brief"]["commercial"] = {"verified_facts": ["holds six cables"], "forbidden_claims": ["price"]}
        p["script"]["dialogue"] = [{"speaker": "Inspector", "line": "I use this every day.", "on_camera": True}]
        p["script"]["disclosure_line"] = "Paid partnership."
        self.assertIn("COMMERCIAL_FIRSTHAND_CLAIM", codes(validate_rights(p)))

    def test_commercial_requires_disclosure(self):
        p = valid_packet(); p["brief"]["commercial"] = {"verified_facts": [], "forbidden_claims": []}; p["export"]["disclosure_plan"] = []
        self.assertIn("COMMERCIAL_NO_DISCLOSURE", codes(validate_rights(p)))

    def test_commercial_forbidden_claim(self):
        p = valid_packet(); p["brief"]["commercial"] = {"verified_facts": [], "forbidden_claims": ["durability"]}
        p["script"]["synopsis"] = "a box of legendary durability"; p["script"]["disclosure_line"] = "Paid partnership."
        self.assertIn("COMMERCIAL_FORBIDDEN_CLAIM", codes(validate_rights(p)))

    def test_render_status_without_approval(self):
        p = valid_packet(); p["status"] = "approved-for-render"
        c = codes(validate_approval(p))
        self.assertTrue({"APPROVAL_RENDER", "APPROVAL_WHO", "APPROVAL_CAP"} <= c)

    def test_rendered_verified_needs_inspection(self):
        p = valid_packet(); p["status"] = "rendered-verified"
        p["approval"].update({"render_approved": True, "approved_by": "owner", "credit_cap": 50})
        self.assertIn("RENDER_NOT_INSPECTED", codes(validate_approval(p)))

    def test_fixture_cannot_be_planning_ready(self):
        p = valid_packet(); p["provenance"]["provider"] = "fixture"
        self.assertIn("FIXTURE_NOT_PLANNING_READY", codes(validate_approval(p)))


class TestSelection(unittest.TestCase):
    def test_hook_premise_mismatch(self):
        p = valid_packet(); p["selected"]["hook_id"] = "H3"
        self.assertIn("SELECT_MISMATCH", codes(validate_all(p, bible())))

    def test_missing_payoff_beat(self):
        p = valid_packet(); [b.update(function="button") for b in p["script"]["beats"] if b["function"] == "payoff"]
        self.assertIn("SCRIPT_BEATS", codes(validate_all(p, bible())))


if __name__ == "__main__":
    unittest.main()
