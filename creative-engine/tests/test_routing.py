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
        p["production_format"] = {"shot_architecture": "single_take_static", "audio_mode": "on_camera_dialogue", "continuity_reuse": {"voice": "new", "location": "new", "costume": "same"}, "rationale": "t"}
        tm = plan(p, bible())
        self.assertEqual(tm["units"][0]["model"], "seedance_2_0_mini")
