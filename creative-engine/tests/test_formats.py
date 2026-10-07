import copy
import unittest

from engine.formats import diversity_findings, realisation_findings, recent_formats
from tests.helpers import valid_packet


def codes(fs):
    return {f["code"] for f in fs}


def pf(**kw):
    d = {"shot_architecture": "single_take_static", "audio_mode": "silent_ambience", "continuity_reuse": {"voice": "none", "location": "same", "costume": "same"}, "rationale": "t"}
    d.update(kw); return d


class TestFormats(unittest.TestCase):
    def test_single_take_realised(self):
        p = valid_packet()
        self.assertEqual(codes(realisation_findings(pf(), p)), set())

    def test_single_take_with_cuts_rejected(self):
        p = valid_packet(); p["scenes"][0]["transition_out"] = "hard cut"
        self.assertIn("FORMAT_SINGLE_TAKE_HAS_CUTS", codes(realisation_findings(pf(), p)))

    def test_moving_camera_needs_movement(self):
        p = valid_packet()
        self.assertIn("FORMAT_NO_CAMERA_MOVE", codes(realisation_findings(pf(shot_architecture="single_take_moving_camera"), p)))
        for s in p["scenes"]: s["camera"]["movement"] = "slow handheld push-in following her lean"
        self.assertNotIn("FORMAT_NO_CAMERA_MOVE", codes(realisation_findings(pf(shot_architecture="single_take_moving_camera"), p)))

    def test_jumpcut_needs_three_cuts(self):
        p = valid_packet()
        self.assertIn("FORMAT_JUMPCUT_TOO_FEW", codes(realisation_findings(pf(shot_architecture="jump_cut_timelapse"), p)))

    def test_silent_mode_rejects_speech_and_offcamera_needs_line(self):
        p = valid_packet(); p["scenes"][0]["dialogue"] = [{"speaker": "Flatmate", "line": "what is that", "on_camera": False}]
        self.assertIn("FORMAT_SILENT_HAS_SPEECH", codes(realisation_findings(pf(), p)))
        self.assertNotIn("FORMAT_NO_OFFCAMERA_LINE", codes(realisation_findings(pf(audio_mode="off_camera_dialogue"), p)))
        p["scenes"][0]["dialogue"] = []
        self.assertIn("FORMAT_NO_OFFCAMERA_LINE", codes(realisation_findings(pf(audio_mode="off_camera_dialogue"), p)))

    def test_reuse_requires_assets(self):
        p = valid_packet(); p["asset_rights"] = [r for r in p["asset_rights"] if r["kind"] != "location_still"]
        self.assertIn("FORMAT_REUSE_LOCATION_ASSET", codes(realisation_findings(pf(), p)))
        self.assertIn("FORMAT_REUSE_VOICE_ASSET", codes(realisation_findings(pf(continuity_reuse={"voice": "same", "location": "new"}), p)))

    def test_music_driven_needs_cue(self):
        p = valid_packet()
        self.assertIn("FORMAT_NO_MUSIC", codes(realisation_findings(pf(audio_mode="music_driven"), p)))

    def test_diversity_warns_on_repeat_and_errors_on_ignored_fixed(self):
        p = valid_packet(); q = copy.deepcopy(p); q["packet_id"] = "old"; q["production_format"] = pf()
        fs = diversity_findings(pf(), [q], fixed={})
        self.assertIn("FORMAT_REPEATS_RECENT", codes(fs)); self.assertTrue(all(f["severity"] == "warning" for f in fs))
        fs = diversity_findings(pf(), [q], fixed={"shot_architecture": "multi_scene_cut"})
        self.assertIn("FORMAT_FIXED_IGNORED", codes(fs))
        self.assertEqual(recent_formats([q])[0]["shot_architecture"], "single_take_static")


if __name__ == "__main__":
    unittest.main()
