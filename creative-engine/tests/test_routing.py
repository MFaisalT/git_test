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
        self.assertEqual(u["model"], "seedance_2_0_mini"); self.assertFalse(u["controls"]["generate_audio"]); self.assertIn("why", u["routing"])
        kinds = {a["kind"] for a in tm["asset_requests"]}
        self.assertEqual(kinds, {"character_reference", "location_still"})
        self.assertTrue(all(a["model"] == "nano_banana_pro" for a in tm["asset_requests"]))
        self.assertTrue(all(m in CATALOGUE for m in [u["model"]] + [a["model"] for a in tm["asset_requests"]]))


if __name__ == "__main__":
    unittest.main()
