import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

from engine.prompts import render_stage
from engine.store import Store
from engine.trends import parse_refresh_response, render_for_prompt, select_relevant, staleness_findings, validate_entry
from tests.helpers import bible, brief_silent

NOW = datetime(2026, 10, 7, tzinfo=timezone.utc)


def entry(i, days_old, typ="hook_pattern", rights="free_to_adapt", platforms=("instagram_reels",)):
    return {"trend_id": f"T-{i}", "type": typ, "label": f"trend {i}", "platforms": list(platforms), "captured_at": (NOW - timedelta(days=days_old)).strftime("%Y-%m-%d"),
            "sources": ["https://example.org/x"], "evidence_class": "press", "rights_status": rights, "why_it_works": "w", "how_to_adapt": "a", "decay_horizon_days": 14}


class TestTrends(unittest.TestCase):
    def test_validate_entry_rejects_bad(self):
        e = entry(1, 1); e["sources"] = ["not-a-url"]; e["rights_status"] = "whatever"
        errs = validate_entry(e)
        self.assertTrue(any("URL" in x for x in errs)); self.assertTrue(any("rights_status" in x for x in errs))
        self.assertEqual(validate_entry(entry(2, 1)), [])

    def test_selection_prefers_fresh_relevant_and_caps(self):
        ledger = [entry(i, i) for i in range(1, 10)] + [entry(99, 40)] + [entry(50, 1, typ="sound", rights="do_not_copy")]
        fresh, stale = select_relevant(brief_silent(), ledger, k=6, now=NOW)
        self.assertEqual(len(fresh), 6)
        self.assertNotIn("T-99", [e["trend_id"] for e in fresh]); self.assertIn("T-99", [e["trend_id"] for e in stale])
        self.assertNotIn("T-50", [e["trend_id"] for e in fresh][:5], "do_not_copy sound should rank low for a silent brief")

    def test_prompt_section_conditional(self):
        txt, _ = render_stage("premises", brief_silent(), bible(), {}, [], 0, trends_text="")
        self.assertNotIn("Current trend radar", txt)
        txt2, _ = render_stage("premises", brief_silent(), bible(), {}, [], 0, trends_text=render_for_prompt([entry(1, 1)], [], NOW))
        self.assertIn("Current trend radar", txt2); self.assertIn("[T-1]", txt2); self.assertIn("never copy", txt2)

    def test_staleness_and_rights_findings(self):
        ledger = [entry(1, 30), entry(2, 1, typ="sound", rights="do_not_copy")]
        codes = {f["code"] for f in staleness_findings(["T-1", "T-2", "T-404"], ledger, NOW)}
        self.assertEqual(codes, {"TREND_STALE", "TREND_RIGHTS", "TREND_UNKNOWN"})

    def test_parse_refresh_response_filters(self):
        good, bad = parse_refresh_response({"entries": [entry(1, 0), {"trend_id": "x"}]})
        self.assertEqual(len(good), 1); self.assertEqual(len(bad), 1)

    def test_ledger_round_trip_and_provenance(self):
        tmp = tempfile.mkdtemp()
        try:
            s = Store(tmp); s.project_dir("t", create=True)
            s.append("t", "trends", entry(1, 2))
            self.assertEqual(s.read_ledger("t", "trends")[0]["trend_id"], "T-1")
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
