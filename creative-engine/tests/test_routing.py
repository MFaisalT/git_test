import unittest

from engine.adapters import plan
from engine.routing import CATALOGUE, REJECTED_MODELS, asset_requests, character_sheet_prompt, quote_for, route_image_asset, route_video_unit
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


class TestRejectedModels(unittest.TestCase):
    def test_rejected_models_stay_out_of_the_catalogue(self):
        self.assertFalse(set(REJECTED_MODELS) & set(CATALOGUE))


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
        self.assertEqual(meta["over_budget"], meta["words"] > meta["word_budget"])  # every word counts (2026-10-08); over budget is flagged, not hidden
        self.assertGreater(meta["shrink_level"], 0)

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
        self.assertIn("extra hands", txt.lower())  # long or short negative tail


class TestPromptCarriesProps(unittest.TestCase):
    def test_props_line_and_spoken_once(self):
        p = valid_packet()
        for s in p["scenes"]:
            s["physical_beat"] = "Right hand holds the clipboard at chest height, left hand rests at her side, feet planted."
        p["continuity"]["props"] = ["large wooden scoring paddle with a 0-10 dial"]
        for s in p["scenes"]:
            s["props_from_frame_one"] = []  # fall back to the continuity list
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
        self.assertIn("one slow continuous move from pointing at 2 to pointing at 1", u["prompt_text"])
        self.assertTrue("shown slowly from the start frame to the end frame" in u["prompt_text"] or "the only state change is the one movement described" in u["prompt_text"])

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


class TestVoiceLock(unittest.TestCase):
    """Owner rule 2026-10-08: a character never changes voice id between generations or scenes."""
    LOCK = {"voice_id": "v-123", "voice_type": "element", "name": "Test Voice", "reference_audio": "aud-1", "status": "locked", "provenance": "designed_from_character"}

    def test_preset_voice_is_refused_and_voices_are_not_shared(self):
        from engine.voice import project_voice_findings, voice_findings
        b = {"approved_assets": {"voice": dict(self.LOCK, voice_type="preset")}}
        self.assertIn("VOICE_NOT_CUSTOM", {f["code"] for f in voice_findings({"scenes": []}, b)})
        b1 = {"bible_id": "a", "approved_assets": {"voice": dict(self.LOCK)}}
        b2 = {"bible_id": "b", "approved_assets": {"voice": dict(self.LOCK)}}
        self.assertEqual(project_voice_findings([b1, b2])[0]["code"], "VOICE_SHARED")

    def _spoken(self):
        p = valid_packet()
        p["production_format"] = {"shot_architecture": "single_take_static", "audio_mode": "on_camera_dialogue", "camera_style": "propped phone",
                                  "continuity_reuse": {"voice": "same", "location": "same", "costume": "same"}, "trend_refs": [], "rationale": "test"}
        p["scenes"][0]["dialogue"] = [{"speaker": "X", "line": "Hello there.", "on_camera": True}]
        return p

    def test_spoken_packet_without_lock_is_blocked(self):
        from engine.validators import validate_all
        p = self._spoken()
        b = bible(); b.setdefault("approved_assets", {}).pop("voice", None)
        p["tool_mapping"] = plan(p, b)
        codes = {f.code for f in validate_all(p, b).errors}
        self.assertIn("VOICE_LOCK_MISSING", codes)
        self.assertIn("RENDER_BLOCKED", codes)

    def test_locked_voice_rides_every_spoken_unit(self):
        p = self._spoken()
        b = bible(); b.setdefault("approved_assets", {})["voice"] = dict(self.LOCK)
        for u in plan(p, b)["units"]:
            if any(s.get("dialogue") for s in p["scenes"] if s["scene_id"] in u["scene_ids"]):
                self.assertIn({"value": "aud-1", "role": "audio_references", "voice_id": "v-123", "voice_name": "Test Voice"}, u["medias"])
                self.assertIsNone(u["render_blocked"])
                self.assertIn("exactly the voice of @audio1", u["prompt_text"])

    def test_store_refuses_voice_change(self):
        import tempfile
        from engine.store import Store
        from engine.voice import VoiceLockError
        st = Store(tempfile.mkdtemp())
        b = bible(); b.setdefault("approved_assets", {})["voice"] = dict(self.LOCK)
        st.save_bible("t", b)
        b2 = bible(); b2.setdefault("approved_assets", {})["voice"] = dict(self.LOCK, voice_id="v-999")
        with self.assertRaises(VoiceLockError):
            st.save_bible("t", b2)
        b3 = bible(); b3.setdefault("approved_assets", {}).pop("voice", None)
        with self.assertRaises(VoiceLockError):
            st.save_bible("t", b3)
        st.save_bible("t", b)  # same voice: fine

    def test_render_drift_and_forbidden_voice(self):
        from engine.voice import render_voice_findings, voice_findings
        b = {"approved_assets": {"voice": dict(self.LOCK)}}
        self.assertEqual(render_voice_findings([{"job_id": "j1", "voice_id": "v-123"}], b), [])
        self.assertEqual(render_voice_findings([{"job_id": "j2", "voice_id": None}], b)[0]["code"], "VOICE_DRIFT")
        bad = {"approved_assets": {"voice": dict(self.LOCK, name="Elias Hale")}}
        self.assertIn("VOICE_FORBIDDEN", {f["code"] for f in voice_findings({"scenes": []}, bad)})

    def test_interaction_states_opening_position_and_one_direction(self):
        from engine.interaction import interaction_beat
        s = {"interaction": dict(TestShownInteraction.SPEC)}
        t = interaction_beat(s)
        self.assertIn("At 0 s the pointer is exactly pointing at 2", t)
        self.assertIn("never any other position", t)


class TestUGCCameraAndPayoff(unittest.TestCase):
    """Owner 2026-10-08: camera micro-movement, a push-in to a close-up before the last line, and the last line must land."""

    def test_locked_camera_and_flat_punchline_are_flagged(self):
        from engine.camera import camera_findings
        p = {"scenes": [{"scene_id": "S1", "start_s": 0, "camera": {"shot": "medium", "movement": "propped phone, locked"}, "dialogue": [{"line": "Final."}]}]}
        codes = {f["code"] for f in camera_findings(p)}
        self.assertEqual(codes, {"CAMERA_DEAD", "CAMERA_PUNCHLINE_FLAT"})
        p["scenes"][0]["camera"] = {"shot": "tight close-up", "movement": "handheld push-in, breathing sway"}
        self.assertEqual(camera_findings(p), [])

    def test_line_inside_the_move_is_flagged_and_payoff_scene_may_follow_in_unit(self):
        from engine.interaction import interaction_spec_findings
        s = {"scene_id": "S3", "start_s": 6, "end_s": 9, "interaction": dict(TestShownInteraction.SPEC, keyframes={"start": "a", "end": "b", "status": "owner_approved"}),
             "dialogue": [{"line": "Final."}]}
        codes = {f["code"] for f in interaction_spec_findings(s, ["S3", "S4"])}
        self.assertIn("INTERACTION_LINE_CROWDED", codes)
        self.assertNotIn("INTERACTION_SHARED_UNIT", codes)
        self.assertIn("INTERACTION_SHARED_UNIT", {f["code"] for f in interaction_spec_findings(s, ["S2", "S3"])})

    def test_per_beat_camera_direction_is_not_truncated_at_commas(self):
        p = TestShownInteraction()._packet()
        p["scenes"][1]["camera"]["movement"] = "handheld on her hip, slow breathing sway, small reframe to the plug"
        for s in p["scenes"]:
            s.setdefault("physical_beat", "She stands still, hands at her sides.")
        txt = "\n".join(u["prompt_text"] for u in plan(p, bible())["units"])
        self.assertIn("handheld on her hip, slow breathing sway, small reframe to the plug", txt)


class TestLockedPlateFraming(unittest.TestCase):
    def test_regenerated_closer_end_frame_is_flagged_and_crop_passes(self):
        from engine.interaction import interaction_spec_findings
        kf = {"start": "a", "end": "b", "status": "owner_approved"}
        s = {"scene_id": "S3", "start_s": 6, "end_s": 9, "interaction": dict(TestShownInteraction.SPEC, keyframes=dict(kf))}
        self.assertIn("KEYFRAME_FRAMING_REGENERATED", {f["code"] for f in interaction_spec_findings(s, ["S3", "S4"])})
        s["interaction"]["keyframes"]["end_derivation"] = {"method": "crop", "source": "a", "box": [0, 0, 10, 18]}
        self.assertNotIn("KEYFRAME_FRAMING_REGENERATED", {f["code"] for f in interaction_spec_findings(s, ["S3", "S4"])})


class TestRotationDirection(unittest.TestCase):
    def test_direction_is_stated_and_end_state_restated(self):
        from engine.interaction import interaction_beat
        t = interaction_beat({"interaction": dict(TestShownInteraction.SPEC, direction="counter-clockwise, one notch (about 18 degrees), toward the 0 end")})
        self.assertIn("counter-clockwise, one notch (about 18 degrees), toward the 0 end", t)
        self.assertIn("then it stops and stays exactly pointing at 1", t)


class TestPlainCameraNaming(unittest.TestCase):
    """Owner rule 2026-10-08: plain lens naming; phone looks are always shot on an iPhone 18 Pro Max."""

    def test_lens_phrases(self):
        from engine.camera import lens_phrase
        self.assertIn("1x main", lens_phrase("phone main lens, about 26mm equivalent"))
        self.assertIn("0.5x ultra-wide", lens_phrase("0.5x"))
        self.assertIn("5x telephoto", lens_phrase("tele"))
        self.assertIsNone(lens_phrase("cinematic"))

    def test_phone_look_names_device_in_prompt(self):
        p = TestShownInteraction()._packet()
        for s in p["scenes"]:
            s.setdefault("physical_beat", "She stands still, hands at her sides.")
            s["camera"]["rig"] = "handheld phone"
        txt = plan(p, bible())["units"][0]["prompt_text"]
        self.assertIn("shot on an iPhone 18 Pro Max", txt)

    def test_unnamed_lens_warns(self):
        from engine.camera import lens_findings
        self.assertEqual(lens_findings({"scenes": [{"scene_id": "S1", "camera": {"lens": "cinematic glass"}}]})[0]["code"], "CAMERA_LENS_UNNAMED")


class TestContinuityAndTiming(unittest.TestCase):
    """2026-10-08: prop states continuous across cuts; speech fits the locked voice's real rate; world events under the line."""

    def test_prop_state_jump_across_cut(self):
        from engine.continuity import prop_state_findings
        a = {"scene_id": "S2", "start_s": 0, "end_s": 6, "prop_states": {"scoring paddle.pointer": "pointing at 2"}, "transition_out": "hard cut"}
        b = {"scene_id": "S3", "start_s": 6, "end_s": 9, "interaction": dict(TestShownInteraction.SPEC, from_state="pointing at 3")}
        self.assertEqual(prop_state_findings({"scenes": [a, b]})[0]["code"], "PROP_STATE_DISCONTINUITY")
        b["interaction"]["from_state"] = "pointing at 2"
        self.assertEqual(prop_state_findings({"scenes": [a, b]}), [])

    def test_speech_overruns_at_measured_voice_rate(self):
        from engine.continuity import speech_fit_findings
        s = {"scene_id": "S1", "start_s": 0, "end_s": 4.5, "dialogue": [{"line": "Umbrella. Two out of ten. Correct answer: a tiny roof for nobody."}]}
        b = {"approved_assets": {"voice": {"measured_wps": 2.1}}}
        self.assertIn("SPEECH_OVERRUNS_SCENE", {f["code"] for f in speech_fit_findings({"scenes": [s]}, b)})
        s["end_s"] = 6.5
        self.assertEqual(speech_fit_findings({"scenes": [s]}, b), [])

    def test_world_event_after_speech_warns(self):
        from engine.continuity import world_event_findings
        a = {"scene_id": "S1", "start_s": 0, "end_s": 4.5, "dialogue": [{"line": "x"}], "transition_out": "continuous"}
        b = {"scene_id": "S2", "start_s": 4.5, "end_s": 6, "physical_beat": "Rain starts; a stranger's umbrella slides past."}
        self.assertEqual(world_event_findings({"scenes": [a, b]})[0]["code"], "WORLD_EVENT_AFTER_SPEECH")

    def test_keyframed_unit_does_not_redescribe_setting(self):
        p = TestShownInteraction()._packet()
        u = plan(p, bible())["units"][-1]
        self.assertIn("Setting: exactly as in the start frame", u["prompt_text"])
        self.assertTrue(u["prompt_budget"]["keyframed"])


class TestUnitProps(unittest.TestCase):
    def test_props_line_lists_only_this_clips_props(self):
        p = valid_packet()
        for s in p["scenes"]:
            s["physical_beat"] = "Right hand holds the clipboard at chest height, left hand rests at her side, feet planted."
            s["props_from_frame_one"] = ["clipboard"]
        txt = plan(p, bible())["units"][0]["prompt_text"]
        line = [l for l in txt.splitlines() if l.startswith("Props")][0]
        self.assertIn("clipboard", line); self.assertNotIn("cones", line)


class TestAssemblyAndColdViewer(unittest.TestCase):
    def test_captions_off_by_default_and_guarded_when_on(self):
        from engine.assembly import AssemblyPlan, caption_commands, concat_commands
        p = AssemblyPlan(unit_urls=["https://x/a.mp4", "https://x/b.mp4"])
        self.assertEqual(caption_commands(p), [])
        self.assertIn("concat=n=2", concat_commands(p)[-1])
        p.captions = "subtitles"; p.script_lines = ["Umbrella. Two out of ten."]
        cmds = caption_commands(p)
        self.assertTrue(any("--profile safe" in c for c in cmds)); self.assertTrue(sum(c.startswith("# REVIEW") for c in cmds) == 3)

    def test_cold_viewer_scoring(self):
        from engine.cold_viewer import score
        terms = ["rates", "wrong", "umbrella", "rain"]
        s = score({"muted_what_happens": "an old man sits in the rain holding a score paddle", "muted_joke": "",
                   "joke": "he rates the umbrella badly while getting rained on, so he is wrong", "stop_scroll": True}, terms)
        self.assertEqual(s["verdict"], "pass")
        self.assertEqual(score({"joke": "a man sits outside"}, terms)["verdict"], "fail")


class TestCameraModes(unittest.TestCase):
    def test_static_with_sway_words_warns(self):
        from engine.camera import camera_mode_findings
        p = {"scenes": [{"scene_id": "S1", "camera": {"movement": "propped phone, locked, gentle breathing sway"}}]}
        self.assertEqual(camera_mode_findings(p)[0]["code"], "CAMERA_STATIC_MOTION_LEAK")
        p["scenes"][0]["camera"]["movement"] = "handheld with slight natural micro-shake from the grip"
        self.assertEqual(camera_mode_findings(p), [])


class TestKpiReminders(unittest.TestCase):
    def test_rival_move_waits_for_traction_and_mastery(self):
        from engine.reminders import due_reminders
        posts = [{"views": 30000, "shares": 300}] * 5
        good = {"followers": 6000, "last_posts": posts, "episodes_published": 7, "first_pass_qa_rate": 0.7}
        r = due_reminders({"vince": good})[0]
        self.assertTrue(r["due"]) ; self.assertIn("owner approval", r["ask_owner"])
        early = dict(good, followers=800, first_pass_qa_rate=0.3)
        r = due_reminders({"vince": early})[0]
        self.assertFalse(r["due"]); self.assertEqual(len(r["unmet"]), 2)
        self.assertFalse(due_reminders({})[0]["due"])
