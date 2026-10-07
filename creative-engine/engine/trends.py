"""Trend radar: a dated, sourced, decaying ledger of what is currently viral, used to choose and tailor topics.

Design rules
- Every entry has: type, label, platforms, captured_at, source URL(s), evidence class, rights status, decay horizon.
- Entries age out: default freshness window 14 days; stale entries are shown as stale and never silently used.
- Small, relevant selection per request (k<=6), never the whole ledger.
- "Adapt, don't imitate": trends inform topic/style/pacing; copying a copyrighted sound, choreography or another
  creator's identity is blocked by rights_status and the bible's do_not list.
- No automation: `engine trends refresh` creates a research request; a Claude session (or a human) answers it with
  web-sourced entries. Cadence is a recommendation, not a scheduler.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

TREND_TYPES = ["format", "style", "edit_move", "hook_pattern", "word_or_phrase", "topic", "sound", "dance_or_move", "product", "meme", "platform_feature"]
RIGHTS = ["free_to_adapt", "license_required", "do_not_copy", "unknown"]
EVIDENCE = ["platform_official", "creator_observed", "press", "aggregator", "inference"]
DEFAULT_FRESH_DAYS = 14
STALE_WARN_DAYS = 21

REQUIRED = ("trend_id", "type", "label", "platforms", "captured_at", "sources", "evidence_class", "rights_status", "why_it_works", "how_to_adapt")


def validate_entry(e: dict) -> list[str]:
    errs = [f"missing {k}" for k in REQUIRED if k not in e or e[k] in ("", [], None)]
    if e.get("type") not in TREND_TYPES:
        errs.append(f"type must be one of {TREND_TYPES}")
    if e.get("rights_status") not in RIGHTS:
        errs.append(f"rights_status must be one of {RIGHTS}")
    if e.get("evidence_class") not in EVIDENCE:
        errs.append(f"evidence_class must be one of {EVIDENCE}")
    try:
        _parse(e.get("captured_at", ""))
    except ValueError:
        errs.append("captured_at must be ISO date (YYYY-MM-DD or full timestamp)")
    for s in e.get("sources", []) or []:
        if not str(s).startswith("http"):
            errs.append(f"source must be a URL: {s}")
    return errs


def _parse(d: str) -> datetime:
    d = d.strip()
    if len(d) == 10:
        return datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return datetime.fromisoformat(d.replace("Z", "+00:00"))


def age_days(e: dict, now: datetime | None = None) -> float:
    now = now or datetime.now(timezone.utc)
    return (now - _parse(e["captured_at"])).total_seconds() / 86400


def select_relevant(brief: dict, ledger: list[dict], k: int = 6, fresh_days: int = DEFAULT_FRESH_DAYS, now: datetime | None = None) -> tuple[list[dict], list[dict]]:
    """Return (fresh_relevant, stale_relevant). Scoring: platform match, format relevance, rights usable, recency."""
    plat = brief.get("platform", "")
    fmt = brief.get("format", "")
    commercial = bool(brief.get("commercial"))
    scored = []
    for e in ledger:
        if validate_entry(e):
            continue
        s = 0
        if plat in e.get("platforms", []) or "multi" in e.get("platforms", []) or plat == "multi":
            s += 2
        if e["type"] in ("format", "hook_pattern", "edit_move", "style"):
            s += 2
        if fmt == "silent_gag" and e["type"] in ("sound", "word_or_phrase"):
            s -= 1
        if commercial and e["type"] == "product":
            s += 1
        if e["rights_status"] in ("do_not_copy",):
            s -= 2
        s += max(0, 2 - age_days(e, now) / 7)  # recency bonus
        scored.append((s, e))
    scored.sort(key=lambda x: (-x[0], x[1]["trend_id"]))
    fresh = [e for s, e in scored if age_days(e, now) <= fresh_days][:k]
    stale = [e for s, e in scored if age_days(e, now) > fresh_days][:3]
    return fresh, stale


def render_for_prompt(fresh: list[dict], stale: list[dict], now: datetime | None = None) -> str:
    if not fresh and not stale:
        return "(no trend radar entries; propose timeless premises and mark any topical guess as a hypothesis)"
    L = ["Dated entries. Use them to choose and tailor topics, hooks, pacing and vocabulary. ADAPT the mechanism; never copy a protected sound, choreography or identity. Cite trend_id in the premise's commercial_fit or why_send_it when used."]
    for e in fresh:
        L.append(f"- [{e['trend_id']}] {e['type']}: {e['label']} ({', '.join(e['platforms'])}; captured {e['captured_at'][:10]}, {age_days(e, now):.0f}d old; evidence {e['evidence_class']}; rights {e['rights_status']}). Why: {e['why_it_works']} Adapt: {e['how_to_adapt']}")
    if stale:
        L.append("STALE (older than the freshness window; reference only, do not rely on):")
        for e in stale:
            L.append(f"- [{e['trend_id']}] {e['label']} (captured {e['captured_at'][:10]})")
    return "\n".join(L)


def staleness_findings(used_ids: list[str], ledger: list[dict], now: datetime | None = None) -> list[dict]:
    by_id = {e["trend_id"]: e for e in ledger}
    out = []
    for tid in used_ids:
        e = by_id.get(tid)
        if not e:
            out.append({"code": "TREND_UNKNOWN", "severity": "error", "message": f"trend {tid} not in ledger"})
            continue
        if age_days(e, now) > STALE_WARN_DAYS:
            out.append({"code": "TREND_STALE", "severity": "warning", "message": f"trend {tid} captured {e['captured_at'][:10]} is older than {STALE_WARN_DAYS} days"})
        if e["rights_status"] == "do_not_copy":
            out.append({"code": "TREND_RIGHTS", "severity": "warning", "message": f"trend {tid} is do_not_copy; confirm only the mechanism was adapted"})
    return out


def parse_refresh_response(obj: dict) -> tuple[list[dict], list[str]]:
    entries, errs = [], []
    for e in obj.get("entries", []):
        v = validate_entry(e)
        if v:
            errs.append(f"{e.get('trend_id', '?')}: {'; '.join(v)}")
        else:
            entries.append(e)
    return entries, errs
