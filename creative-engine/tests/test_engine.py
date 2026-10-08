import copy
import json
import os
import shutil
import tempfile
import unittest

from engine.adapters import build_prompt_text, plan
from engine.pipeline import Pipeline, QUOTES_2026_10_07
from engine.prompts import render_stage
from engine.providers import BrokerProvider, FixtureProvider, PendingResponse, parse_json_object
from engine.repetition import compare
from engine.retrieval import load_demos, select_demos
from engine.render import storyboard_md
from engine.store import Store
from tests.helpers import FIX, ROOT, bible, brief_commercial, brief_silent, valid_packet


class TestRepetition(unittest.TestCase):
    def test_identical_flags_all_fields(self):
        p = valid_packet(); q = copy.deepcopy(p); q["packet_id"] = "other"
        r = compare(p, [q])
        self.assertEqual(r["verdict"], "review")
        self.assertIn("hook", r["flagged_fields"]); self.assertIn("payoff", r["flagged_fields"])

    def test_different_not_flagged(self):
        p = valid_packet(); q = copy.deepcopy(p); q["packet_id"] = "other"
        for pr in q["premises"]:
            pr["logline"] = "a curator unveils a forgotten voice note as an artefact"; pr["payoff"] = "her microphone was live"; pr["surprise"] = "the exhibit is her own complaint"
        q["hook_variants"][0].update({"first_frame": "velvet rope around a phone", "first_line_or_action": "white glove lifts the phone"})
        for s in q["scenes"]:
            s["action"] = "glove lifts phone from plinth"; s["camera"]["shot"] = "close up"; s["camera"]["movement"] = "slow dolly"; s["lighting"] = "museum spot from above, cool fill, contact shadow on plinth"
        q["continuity"]["props"] = ["velvet rope", "plinth", "white glove", "phone"]; q["hook_variants"][0]["mechanism"] = "curiosity_gap"
        r = compare(p, [q])
        self.assertEqual(r["flagged_fields"], [])

    def test_ignores_self(self):
        p = valid_packet()
        self.assertEqual(compare(p, [p])["flagged_fields"], [])


class TestRetrieval(unittest.TestCase):
    def test_diverse_and_relevant(self):
        demos = select_demos(brief_silent(), k=2)
        self.assertEqual(demos[0]["demo_id"], "D1_silent_gag")
        self.assertEqual(len({d["format"] for d in demos}), len(demos))

    def test_commercial_brief_pulls_commercial_demo(self):
        ids = [d["demo_id"] for d in select_demos(brief_commercial(), k=2)]
        self.assertIn("D3_commercial_mechanism", ids)

    def test_eval_brief_never_used_as_demo(self):
        for d in load_demos():
            self.assertFalse(d["brief_id"].startswith("B"), "demo derived from an eval brief")
        demos = load_demos(); demos.append({"demo_id": "leak", "brief_id": brief_silent()["brief_id"], "format": "silent_gag", "tags": ["silent_gag", "silent"], "input": "", "accepted_output": {}, "justification": ""})
        self.assertNotIn("leak", [d["demo_id"] for d in select_demos(brief_silent(), k=3, demos=demos)])


class TestPrompts(unittest.TestCase):
    def test_conditional_sections(self):
        txt, demos = render_stage("script_storyboard", brief_silent(), bible(), {}, [], 2)
        self.assertIn("Silent gag: dialogue arrays must be empty", txt)
        self.assertNotIn("Commercial: product solves", txt)
        self.assertNotIn("<<IF", txt)
        self.assertIn("D1_silent_gag", demos)
        txt2, _ = render_stage("script_storyboard", brief_commercial(), bible(), {}, [], 2)
        self.assertIn("holds up to six cables", txt2)
        self.assertNotIn("Silent gag:", txt2)

    def test_history_section_only_when_history(self):
        a, _ = render_stage("premises", brief_silent(), bible(), {}, [], 0)
        b, _ = render_stage("premises", brief_silent(), bible(), {}, [{"hook": "x"}], 0)
        self.assertNotIn("Episode history fingerprints", a); self.assertIn("Episode history fingerprints", b)

    def test_parse_json_with_fences(self):
        self.assertEqual(parse_json_object("```json\n{\"a\": 1}\n```"), {"a": 1})
        with self.assertRaises(ValueError):
            parse_json_object("no json here")


class TestAdapter(unittest.TestCase):
    def test_dry_run_plan_uses_verified_controls_only(self):
        p = valid_packet()
        tm = plan(p, bible(), QUOTES_2026_10_07)
        self.assertEqual(tm["units"][0]["model"], "seedance_2_5")  # silent fixture handles props -> Seedance 2.5 (owner inspection 2026-10-08)
        self.assertTrue(set(tm["units"][0]["controls"]) <= {"duration", "aspect_ratio", "resolution", "generate_audio", "mode"})
        self.assertIn("NO job submitted", tm["notes"].replace("No job submitted", "NO job submitted"))
        self.assertIn("not a native format", tm["notes"])

    def test_prompt_text_silent_has_no_dialogue_and_has_relight(self):
        p = valid_packet()
        t = build_prompt_text(p, p["scenes"], bible())
        self.assertIn("NO dialogue", t); self.assertIn("RELIGHT", t); self.assertNotIn("Dialogue (", t)

    def test_long_episode_routes_to_seedance_2_5(self):
        p = valid_packet(); p["brief"]["duration_target_s"] = 20; p["scenes"][2]["end_s"] = 20
        self.assertEqual(plan(p, bible())["units"][0]["model"], "seedance_2_5")

    def test_driving_footage_routes_to_motion_control(self):
        p = valid_packet(); p["asset_rights"].append({"asset": "owned clip", "kind": "driving_footage", "source": "owner", "rights_status": "owned", "scope": "all"})
        u = plan(p, bible())["units"][0]
        self.assertEqual(u["model"], "hf_mult_motion_control")
        self.assertTrue(any(m["role"] == "video_references" for m in u["medias"]))


class TestStoreAndPipeline(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(); self.store = Store(self.tmp)
        self.store.save_brief("t", brief_silent()); self.store.save_bible("t", bible())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_bible_versioning_is_append_only(self):
        b2 = self.store.save_bible("t", bible(), reason="costume tweak")
        self.assertEqual(b2["version"], 2)
        self.assertEqual(self.store.bible_versions("t", "inspector-v1"), [1, 2])
        self.assertEqual(self.store.load_bible("t", "inspector-v1", 1)["version"], 1)
        self.assertEqual(self.store.read_ledger("t", "decisions")[-1]["reason"], "costume tweak")

    def test_fixture_pipeline_runs_but_stays_draft(self):
        pipe = Pipeline(self.store, "t", FixtureProvider(FIX), requested_model="fixture")
        packet = pipe.run("B1_silent_gag", "inspector-v1", "fx1")
        self.assertEqual(packet["status"], "draft")
        self.assertEqual(packet["provenance"]["provider"], "fixture")
        self.assertTrue(packet["qa"]["deterministic"]["ok"], packet["qa"]["deterministic"])
        d = self.store.episode_dir("t", "fx1")
        self.assertTrue(os.path.exists(os.path.join(d, "storyboard.md")))
        self.assertIn("One Centimetre", open(os.path.join(d, "storyboard.md"), encoding="utf-8").read())
        self.assertEqual(self.store.read_ledger("t", "runs")[-1]["provider"], "fixture")

    def test_broker_halts_pending_then_resumes(self):
        d = self.store.episode_dir("t", "bk1", create=True)
        pipe = Pipeline(self.store, "t", BrokerProvider(d, "sonnet"), requested_model="sonnet")
        with self.assertRaises(PendingResponse) as cm:
            pipe.run("B1_silent_gag", "inspector-v1", "bk1")
        self.assertTrue(os.path.exists(cm.exception.request_path))
        self.assertIn("Divergent premises", open(cm.exception.request_path, encoding="utf-8").read())
        # fulfil each stage from fixtures, with a meta block recording model evidence, and resume
        for stage in ("premises", "hooks", "script_storyboard", "qa_review"):
            with self.assertRaises(PendingResponse) as cm2:
                pipe.run("B1_silent_gag", "inspector-v1", "bk1")
            self.assertTrue(cm2.exception.response_path.endswith(f"{stage}-0.response.json"))
            src = open(os.path.join(FIX, f"{stage}.json"), encoding="utf-8").read()
            with open(cm2.exception.response_path, "w", encoding="utf-8") as fh:
                fh.write(src + '\n<!-- meta:{"requested_model":"sonnet","observed_model":"claude-sonnet-5-5 (session metadata)"} -->')
        packet = pipe.run("B1_silent_gag", "inspector-v1", "bk1")
        self.assertEqual(packet["status"], "planning-ready; render unverified")
        self.assertEqual(packet["provenance"]["observed_model"], "claude-sonnet-5-5 (session metadata)")
        self.assertEqual(packet["provenance"]["repair_passes"], 0)

    def test_repair_is_bounded(self):
        d = self.store.episode_dir("t", "bk2", create=True)
        pipe = Pipeline(self.store, "t", BrokerProvider(d, "sonnet"), max_repairs=1)
        bad = json.dumps({"premises": [], "ranking": []})
        for n in (0, 1):
            with self.assertRaises(PendingResponse) as cm:
                pipe.run("B1_silent_gag", "inspector-v1", "bk2")
            self.assertTrue(cm.exception.response_path.endswith(f"premises-{n}.response.json"))
            if n == 1:
                self.assertIn("Repair pass", open(cm.exception.request_path, encoding="utf-8").read())
            open(cm.exception.response_path, "w").write(bad)
        from engine.pipeline import StageFailure
        with self.assertRaises(StageFailure):
            pipe.run("B1_silent_gag", "inspector-v1", "bk2")

    def test_history_feeds_repetition_check(self):
        pipe = Pipeline(self.store, "t", FixtureProvider(FIX))
        pipe.run("B1_silent_gag", "inspector-v1", "fxA")
        p2 = pipe.run("B1_silent_gag", "inspector-v1", "fxB")
        self.assertEqual(p2["qa"]["repetition"]["verdict"], "review")
        self.assertEqual(p2["qa"]["repetition"]["fields"]["hook"]["closest_packet"], "fxA")

    def test_render_markdown_is_self_contained(self):
        md = storyboard_md(valid_packet())
        for needle in ("Timed storyboard", "Rights and approval checklist", "Tool mapping (dry run)", "PLANNING-READY; RENDER UNVERIFIED"):
            self.assertIn(needle, md)


if __name__ == "__main__":
    unittest.main()
