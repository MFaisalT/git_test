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

    def test_dialogue_short_identity_critical_uses_cinema_studio_4(self):
        r = route_video_unit({"shot_architecture": "multi_scene_cut"}, 8, "off_camera_dialogue", False)
        self.assertEqual(r["model"], "cinematic_studio_video_4_0")  # owner ranking 2026-10-08: CS4 first, Seedance 2.5 second
        self.assertIn("seedance_2_5", r["fallback"])

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
        self.assertEqual(u["model"], "cinematic_studio_video_4_0"); self.assertFalse(u["controls"]["generate_audio"]); self.assertIn("why", u["routing"])  # handled props -> 2.5; silent keeps audio off
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
        self.assertEqual(plan(p, bible())["units"][0]["model"], "cinematic_studio_video_4_0")


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


class TestShownInteraction(unittest.TestCase):
    """Owner 2026-10-08: the character must handle props on screen; keyframed, own unit, fully specified."""
    SPEC = {"actor_hand": "right", "contact": "right index fingertip rests on the pointer tip", "object": "scoring paddle", "part": "pointer",
            "from_state": "pointing at 2", "to_state": "pointing at 1", "motion": "pushes the pointer tip slowly left; it pivots on the brass pin",
            "support_hand": "Left hand holds the handle still"}

    def _packet(self, keyframes=True):
        import copy
        p = valid_packet()
        last = p["scenes"][-1]
        it = copy.deepcopy(self.SPEC)
        if keyframes:
            it["keyframes"] = {"start": "kf-start", "end": "kf-end", "status": "owner_approved"}
        last["interaction"] = it
        last["physical_beat"] = "Left hand holds the paddle up, right index fingertip on the pointer tip, body still."
        return p

    def test_spec_errors(self):
        from engine.interaction import interaction_spec_findings
        s = {"scene_id": "S9", "start_s": 0, "end_s": 2, "interaction": {"actor_hand": "right"}}
        codes = {f["code"]: f["severity"] for f in interaction_spec_findings(s, ["S8", "S9"])}
        self.assertEqual(codes["INTERACTION_SPEC_INCOMPLETE"], "error")
        self.assertEqual(codes["INTERACTION_KEYFRAMES_MISSING"], "error")
        self.assertEqual(codes["INTERACTION_SHARED_UNIT"], "error")
        self.assertEqual(codes["INTERACTION_TOO_SHORT"], "warning")

    def test_keyframed_interaction_is_not_flagged_as_onscreen_change(self):
        from engine.interaction import interaction_findings
        s = {"scene_id": "S3", "interaction": dict(self.SPEC), "physical_beat": "Left hand holds the paddle up; right index finger turns the dial from 2 to 1."}
        self.assertNotIn("INTERACTION_ONSCREEN_STATE_CHANGE", {f["code"] for f in interaction_findings(s)})

    def test_fingertip_names_the_hand(self):
        from engine.interaction import interaction_findings
        s = {"scene_id": "S3", "physical_beat": "Left hand holds the paddle up; right index fingertip on the pointer tip."}
        self.assertNotIn("INTERACTION_FREE_HAND_UNPARKED", {f["code"] for f in interaction_findings(s)})

    def test_plan_gives_interaction_its_own_keyframed_cs4_unit(self):
        p = self._packet()
        units = plan(p, bible())["units"]
        u = units[-1]
        self.assertEqual(u["scene_ids"], [p["scenes"][-1]["scene_id"]])
        self.assertEqual(u["model"], "cinematic_studio_video_4_0")
        roles = {m["role"]: m["value"] for m in u["medias"]}
        self.assertEqual((roles.get("start_image"), roles.get("end_image")), ("kf-start", "kf-end"))
        self.assertTrue(u["manual_steps"][0].startswith("Keyframe board first"))
        self.assertIn("the pointer goes from pointing at 2 to pointing at 1", u["prompt_text"])
        self.assertIn("shown slowly from the start frame to the end frame", u["prompt_text"])

    def test_missing_keyframes_blocks_validation(self):
        from engine.validators import validate_all
        p = self._packet(keyframes=False)
        p["tool_mapping"] = plan(p, bible())
        self.assertIn("INTERACTION_KEYFRAMES_MISSING", {f.code for f in validate_all(p, bible()).errors})

    def test_bible_prop_design_replaces_short_name(self):
        from engine.physics import bible_prop_text
        b = {"props": [{"id": "scoring-paddle", "match": ["paddle"], "design": "oak paddle with a 0-10 semicircular gauge and one pointer",
                        "reference_asset": {"job_id": "j1"}}]}
        self.assertEqual(bible_prop_text("large wooden scoring paddle with a 0-10 dial", b), "oak paddle with a 0-10 semicircular gauge and one pointer (exactly as @image2)")
        self.assertEqual(bible_prop_text("white chair", b), "white chair")


class TestUnitRelativeTimes(unittest.TestCase):
    def test_second_unit_prompt_times_start_at_zero(self):
        p = TestShownInteraction()._packet()
        last = p["scenes"][-1]
        u = plan(p, bible())["units"][-1]
        dur = float(last["end_s"]) - float(last["start_s"])
        if float(last["start_s"]) > 0:
            self.assertIn(f"0-{dur:.0f}s:" if dur.is_integer() else f"0-{dur:.1f}s:", u["prompt_text"])
