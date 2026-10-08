import unittest

from engine.adapters import plan
from engine.routing import CATALOGUE, asset_requests, character_sheet_prompt, quote_for, route_image_asset, route_video_unit
from tests.helpers import bible, valid_packet


class TestRouting(unittest.TestCase):
    def test_short_silent_goes_to_mini(self):
        r = route_video_unit({"shot_architecture": "single_take_static"}, 12, "silent_ambience", False)
        self.assertEqual(r["model"], "seedance_2_0_mini"); self.assertFalse(r["generate_audio"])

    def test_long_take_goes_to_seedance_25_with_draft_optimisation(self):
        r = route_video_unit({"shot_architecture": "single_take_moving_camera"}, 20, "on_camera_dialogue", False)
        self.assertEqual((r["model"], r["mode"]), ("seedance_2_5", "omni_reference")); self.assertIn("draft", r["optimisation"])

    def test_dialogue_short_identity_critical_uses_seedance_25(self):
        r = route_video_unit({"shot_architecture": "multi_scene_cut"}, 8, "off_camera_dialogue", False)
        self.assertEqual(r["model"], "seedance_2_5")

    def test_driving_footage_and_continuation(self):
        self.assertEqual(route_video_unit({}, 10, "silent_ambience", True)["model"], "hf_mult_motion_control")
        r = route_video_unit({"shot_architecture": "continuation_from_last_frame"}, 10, "on_camera_dialogue", False)
        self.assertEqual(r["mode"], "video_extension")

    def test_image_routing_and_nb2_flag(self):
        self.assertEqual(route_image_asset("character_reference")["model"], "nano_banana_pro")
        self.assertEqual(route_image_asset("character_reference", nb2_testing=True)["model"], "nano_banana_2_1")
        self.assertIn("original", character_sheet_prompt(bible()))

    def test_quotes_scale_and_missing(self):
        self.assertEqual(quote_for("seedance_2_0_mini", 15), 15); self.assertEqual(quote_for("seedance_2_5", 8), 56)
        self.assertIsNone(quote_for("kling3_0", 10))

    def test_plan_carries_routing_and_assets(self):
        p = valid_packet(); p["production_format"] = {"shot_architecture": "single_take_static", "audio_mode": "silent_ambience", "continuity_reuse": {"voice": "none", "location": "same", "costume": "same"}, "rationale": "t"}
        tm = plan(p, bible())
        u = tm["units"][0]
        self.assertEqual(u["model"], "seedance_2_5"); self.assertFalse(u["controls"]["generate_audio"]); self.assertIn("why", u["routing"])  # handled props -> 2.5; silent keeps audio off
        kinds = {a["kind"] for a in tm["asset_requests"]}
        self.assertEqual(kinds, {"character_reference", "location_still"})
        self.assertTrue(all(a["model"] == "nano_banana_pro" for a in tm["asset_requests"]))
        self.assertTrue(all(m in CATALOGUE for m in [u["model"]] + [a["model"] for a in tm["asset_requests"]]))


if __name__ == "__main__":
    unittest.main()


class TestRegistryRights(unittest.TestCase):
    def test_pending_asset_cannot_be_owned(self):
        from engine.pipeline import _normalise_rights_against_registry
        p = valid_packet()
        p["asset_rights"] = [{"asset": "loc-kitchen-01 still", "kind": "location_still", "source": "x", "rights_status": "owned", "scope": "s"},
                             {"asset": "Inspector character reference per bible", "kind": "character_reference", "source": "x", "rights_status": "owned", "scope": "s"}]
        _normalise_rights_against_registry(p, bible())
        self.assertEqual({r["rights_status"] for r in p["asset_rights"]}, {"unresolved"})
        self.assertTrue(any("downgraded" in e["claim"] for e in p["evidence"]))


class TestBakeoffAdditions(unittest.TestCase):
    def test_character_sheet_prompt_uses_bible_presentation(self):
        from engine.routing import character_sheet_prompt
        b = {"character": {"sex_presentation": "man", "age_range": "52-58", "identity_anchors": "round soft face", "hair": "bald crown with a ring of grey hair", "lower_body": "mustard trousers, loafers", "silhouette": "mustard suit"}}
        p = character_sheet_prompt(b)
        self.assertIn("adult man aged 52-58", p); self.assertIn("bald crown", p); self.assertIn("mustard trousers", p)
        self.assertNotIn("woman", p); self.assertNotIn("low bun", p)
        d = character_sheet_prompt({"character": {}})
        self.assertIn("adult woman", d); self.assertIn("low bun", d)

    def test_draft_mini_render_tier_routes_dialogue_to_mini(self):
        p = valid_packet(); p["brief"]["render_tier"] = "draft_mini"
        p["production_format"] = {"shot_architecture": "single_take_static", "audio_mode": "silent_ambience", "continuity_reuse": {"voice": "none", "location": "new", "costume": "same"}, "rationale": "t"}
        for s in p["scenes"]:
            s["dialogue"] = []; s["physical_beat"] = "She stands still at the window, arms at her sides, looking out; nothing moves."
        self.assertEqual(plan(p, bible())["units"][0]["model"], "seedance_2_0_mini")
        p["scenes"][0]["physical_beat"] = "Right hand lifts the clipboard to chest height, left hand at her side."
        self.assertEqual(plan(p, bible())["units"][0]["model"], "seedance_2_5")


    def test_asset_without_registry_entry_cannot_be_owned(self):
        from engine.pipeline import _normalise_rights_against_registry
        p = valid_packet()
        p["asset_rights"] = [{"asset": "Captain voice", "kind": "voice", "source": "x", "rights_status": "owned", "scope": "s"},
                             {"asset": "Foley", "kind": "other", "source": "x", "rights_status": "owned", "scope": "s"}]
        _normalise_rights_against_registry(p, {"approved_assets": {"locations": []}})
        self.assertEqual([r["rights_status"] for r in p["asset_rights"]], ["unresolved", "owned"])


class TestPhysics(unittest.TestCase):
    def test_mouth_conflict_and_overload(self):
        from engine.physics import scene_physics_findings
        s = {"scene_id": "S3", "start_s": 6, "end_s": 9, "action": "She clamps the whistle in her teeth and blasts it. She grins wide and shouts AND. She lifts the paddle, the umbrella and the clipboard.", "performance": "", "dialogue": [{"speaker": "x", "line": "AND!"}]}
        codes = {f["code"] for f in scene_physics_findings(s, "draft_mini")}
        self.assertIn("PHYSICS_MOUTH_CONFLICT", codes); self.assertIn("PHYSICS_HANDS_OVERLOAD", codes); self.assertIn("PHYSICS_ACTION_DENSITY", codes)
        s2 = {"scene_id": "S2", "start_s": 0, "end_s": 3, "action": "She lifts the paddle and writes with the pen.", "performance": ""}
        self.assertIn("PHYSICS_NO_CONTACT", {f["code"] for f in scene_physics_findings(s2, "draft_mini")})

    def test_clean_beat_passes(self):
        from engine.physics import scene_physics_findings
        s = {"scene_id": "S1", "start_s": 0, "end_s": 3, "action": "Her right hand grips the paddle shaft on her thigh; the umbrella rests across her lap; everything else holds still.", "performance": "", "dialogue": [], "physical_beat": "Right hand grips the paddle on her thigh, left hand flat on the umbrella across her lap, body still."}
        self.assertEqual(scene_physics_findings(s, "draft_mini"), [])

    def test_compact_prompt_used_when_beats_exist(self):
        p = valid_packet()
        for s in p["scenes"]:
            s["physical_beat"] = "Right hand grips the clipboard at chest height, left hand still at her side, feet planted."
        tm = plan(p, bible())
        u = tm["units"][0]
        self.assertEqual(u["prompt_style"], "compact_physics_first")
        self.assertLess(len(u["prompt_text"].split()), 320); self.assertIn("Physics:", u["prompt_text"]); self.assertIn("TOP PRIORITY", u["prompt_text_full"])
        for s in p["scenes"]:
            s.pop("physical_beat")
        self.assertEqual(plan(p, bible())["units"][0]["prompt_style"], "dense_legacy")


class TestAudioModePrompts(unittest.TestCase):
    def _pk(self, am, dialogue=True):
        p = valid_packet()
        p["production_format"] = {"shot_architecture": "single_take_static", "audio_mode": am, "continuity_reuse": {"voice": "none", "location": "new", "costume": "same"}, "rationale": "t"}
        for s in p["scenes"]:
            s["physical_beat"] = "Right hand grips the clipboard at chest height, left hand still at her side, feet planted, everything else still."
            if not dialogue:
                s["dialogue"] = []
        return p

    def test_music_driven_prompt_has_no_speech_and_beats(self):
        from engine.physics import compact_prompt
        p = self._pk("music_driven", dialogue=False)
        p["production_format"]["soundtrack"] = {"source": "custom", "title": "t", "rights_status": "owned", "bpm": 100, "beat_times_s": [0.6, 1.8, 3.0]}
        text, meta = compact_prompt(p, sorted(p["scenes"], key=lambda s: s["start_s"]), bible(), return_meta=True)
        self.assertIn("no generated music", text); self.assertIn("1.8s", text); self.assertNotIn(" says:", text)
        self.assertLessEqual(meta["words"], meta["word_budget"])

    def test_voiceover_lines_never_reach_render_prompt(self):
        from engine.physics import compact_prompt
        p = self._pk("voiceover_narration")
        p["scenes"][0]["dialogue"] = [{"speaker": "VO", "line": "Case closed.", "on_camera": False}]
        text = compact_prompt(p, sorted(p["scenes"], key=lambda s: s["start_s"]), bible())
        self.assertNotIn("Case closed", text); self.assertIn("lips stay closed", text)

    def test_budget_shrinks_long_prompts(self):
        from engine.physics import compact_prompt
        p = self._pk("on_camera_dialogue")
        p["continuity"]["costume"] = "long costume " * 60
        text, meta = compact_prompt(p, sorted(p["scenes"], key=lambda s: s["start_s"]), bible(), return_meta=True)
        self.assertGreater(meta["shrink_level"], 0); self.assertNotIn("long costume long costume", text)

    def test_music_driven_requires_soundtrack_spec(self):
        from engine.formats import realisation_findings
        p = self._pk("music_driven", dialogue=False)
        for s in p["scenes"]:
            s["sound"]["music"] = "custom track"
        codes = {f["code"] for f in realisation_findings(p["production_format"], p)}
        self.assertIn("FORMAT_SOUNDTRACK_SPEC", codes)


class TestInteraction(unittest.TestCase):
    def test_dial_turn_on_screen_is_flagged_and_cut_staging_passes(self):
        from engine.interaction import interaction_findings
        bad = {"scene_id": "S3", "physical_beat": "Left hand lifts the paddle toward the lens, right index finger turns the dial from 2 to 1, umbrella rests across his lap."}
        self.assertIn("INTERACTION_ONSCREEN_STATE_CHANGE", {f["code"] for f in interaction_findings(bad)})
        good = {"scene_id": "S4", "state_change_by_cut": True, "physical_beat": "Left hand holds the paddle up at chest height, dial already at 1; right hand rests flat on the umbrella in his lap; body still."}
        self.assertEqual(interaction_findings(good), [])

    def test_loop_mirror_unparked(self):
        from engine.interaction import interaction_findings
        s = {"scene_id": "S1", "physical_beat": "Right hand presses the pump twice in front of the mirror."}
        codes = {f["code"] for f in interaction_findings(s)}
        self.assertTrue({"INTERACTION_LOOP_WORD", "INTERACTION_MIRROR", "INTERACTION_FREE_HAND_UNPARKED"} <= codes)

    def test_prompt_has_hard_cut_hand_rule_and_negative_tail(self):
        p = valid_packet()
        for s in p["scenes"]:
            s["physical_beat"] = "Right hand holds the clipboard at chest height, left hand rests at her side, feet planted."
        p["scenes"][0]["transition_out"] = "hard cut"
        txt = plan(p, bible())["units"][0]["prompt_text"]
        self.assertIn("no third arm", txt.lower())


class TestPromptCarriesProps(unittest.TestCase):
    def test_props_line_and_spoken_once(self):
        p = valid_packet()
        for s in p["scenes"]:
            s["physical_beat"] = "Right hand holds the clipboard at chest height, left hand rests at her side, feet planted."
        p["continuity"]["props"] = ["large wooden scoring paddle with a 0-10 dial"]
        txt = plan(p, bible())["units"][0]["prompt_text"]
        self.assertIn("scoring paddle with a 0-10 dial", txt)
