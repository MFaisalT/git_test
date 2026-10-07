import copy
import json
import os

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)
FIX = os.path.join(HERE, "fixtures")


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def bible():
    return load(os.path.join(ROOT, "eval", "bibles", "inspector-v1.json"))


def brief_silent():
    return load(os.path.join(ROOT, "eval", "briefs", "B1_silent_gag.json"))


def brief_commercial():
    return load(os.path.join(ROOT, "eval", "briefs", "B3_commercial.json"))


def valid_packet():
    """A complete, gate-passing planning-ready packet assembled from fixtures (used to derive negatives)."""
    from engine.adapters import plan
    from engine.pipeline import QUOTES_2026_10_07
    prem, hooks, ss = load(os.path.join(FIX, "premises.json")), load(os.path.join(FIX, "hooks.json")), load(os.path.join(FIX, "script_storyboard.json"))
    b, bb = brief_silent(), bible()
    packet = {
        "packet_version": "1.0", "packet_id": "test-packet", "status": "planning-ready; render unverified",
        "brief": {k: b[k] for k in b}, "bible_version": {"bible_id": bb["bible_id"], "version": 1, "sha256": "x"},
        "evidence": ss["evidence"], "premises": prem["premises"], "hook_variants": hooks["hook_variants"], "selected": hooks["selected"],
        "script": ss["script"], "scenes": copy.deepcopy(ss["scenes"]), "continuity": ss["continuity"], "asset_rights": ss["asset_rights"],
        "tool_mapping": {"adapter": "", "verified_on": "", "units": []},
        "approval": {"render_approved": False, "spend_approved": False, "publish_approved": False, "approved_by": "", "approved_at": "", "credit_cap": None},
        "export": ss["export"], "qa": {"deterministic": {}, "creative": {}, "repetition": {}, "render_inspection": None},
        "growth_hypotheses": ss["growth_hypotheses"],
        "provenance": {"generated_at": "2026-10-07T00:00:00Z", "provider": "manual", "requested_model": "n/a", "observed_model": "n/a", "demonstrations_used": [], "stage_log": [], "repair_passes": 0, "engine_version": "test"},
        "negative_constraints": b["negative_constraints"],
    }
    packet["tool_mapping"] = plan(packet, bb, QUOTES_2026_10_07)
    return packet
