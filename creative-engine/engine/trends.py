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
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

TREND_TYPES = ["format", "style", "edit_move", "hook_pattern", "word_or_phrase", "topic", "sound", "dance_or_move", "product", "meme", "platform_feature"]
RIGHTS = ["free_to_adapt", "license_required", "do_not_copy", "unknown"]
EVIDENCE = ["platform_official", "creator_observed", "press", "aggregator", "inference"]
DEFAULT_FRESH_DAYS = 14
STALE_WARN_DAYS = 21

REQUIRED = ("trend_id", "type", "label", "platforms", "captured_at", "sources", "evidence_class", "rights_status", "why_it_works", "how_to_adapt", "decay_horizon_days")
ACCESS = ["fetched", "index_only", "secondhand"]
MAX_LEN = {"label": 140, "why_it_works": 400, "how_to_adapt": 400}
INJECTION_RX = re.compile(r"(ignore (all |any )?(previous|prior|above) instructions|you are now|system prompt|<\/?script|disregard)", re.I)


def _valid_url(u: str) -> bool:
    try:
        pr = urlparse(str(u))
    except ValueError:
        return False
    host = (pr.hostname or "").lower()
    return pr.scheme in ("http", "https") and "." in host and host not in ("localhost",) and not host.startswith("127.")


def validate_entry(e: dict) -> list[str]:
    errs = [f"missing {k}" for k in REQUIRED if k not in e or e[k] in ("", [], None)]
    if e.get("type") not in TREND_TYPES:
        errs.append(f"type must be one of {TREND_TYPES}")
    if e.get("rights_status") not in RIGHTS:
        errs.append(f"rights_status must be one of {RIGHTS}")
    if e.get("evidence_class") not in EVIDENCE:
        errs.append(f"evidence_class must be one of {EVIDENCE}")
    try:
        cap = _parse(e.get("captured_at", ""))
        if cap > datetime.now(timezone.utc) + timedelta(hours=12):
            errs.append("captured_at is in the future")
    except ValueError:
        errs.append("captured_at must be ISO date (YYYY-MM-DD or full timestamp)")
    if e.get("origin_date"):
        try:
            _parse(e["origin_date"])
        except ValueError:
            errs.append("origin_date must be ISO date")
    for s in e.get("sources", []) or []:
        if not _valid_url(s):
            errs.append(f"source must be an http(s) URL with a real host: {s}")
    dh = e.get("decay_horizon_days")
    if not isinstance(dh, (int, float)) or dh <= 0 or dh > 365:
        errs.append("decay_horizon_days must be a number in (0, 365]")
    if e.get("access_level", "fetched") not in ACCESS:
        errs.append(f"access_level must be one of {ACCESS}")
    if e.get("type") in ("sound", "dance_or_move") and e.get("rights_status") == "free_to_adapt" and e.get("evidence_class") != "platform_official":
        errs.append("sound/dance entries may be free_to_adapt only with a platform_official source")
    for k, n in MAX_LEN.items():
        if len(str(e.get(k, ""))) > n:
            errs.append(f"{k} longer than {n} chars")
    if INJECTION_RX.search(json.dumps(e)):
        errs.append("entry text looks like an instruction injection")
    return errs


def _parse(d: str) -> datetime:
    d = d.strip()
    if len(d) == 10:
        return datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return datetime.fromisoformat(d.replace("Z", "+00:00"))


def age_days(e: dict, now: datetime | None = None) -> float:
    """Age since the trend was observed to START (origin_date) when known, else since capture."""
    now = now or datetime.now(timezone.utc)
    base = _parse(e["origin_date"]) if e.get("origin_date") else _parse(e["captured_at"])
    return (now - base).total_seconds() / 86400


def is_fresh(e: dict, now: datetime | None = None, default_days: int = DEFAULT_FRESH_DAYS) -> bool:
    horizon = min(float(e.get("decay_horizon_days", default_days)), float(default_days)) if e.get("decay_horizon_days") else default_days
    return age_days(e, now) <= horizon


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
        if e["rights_status"] == "do_not_copy":
            continue  # excluded from injection entirely; only the ledger keeps it for reviewers
        if e["rights_status"] == "license_required":
            s -= 1
        s += max(0, 2 - age_days(e, now) / 7)  # recency bonus
        scored.append((s, e))
    scored.sort(key=lambda x: (-x[0], x[1]["trend_id"]))
    fresh = [e for s, e in scored if is_fresh(e, now, fresh_days)][:k]
    stale = [e for s, e in scored if not is_fresh(e, now, fresh_days)][:3]
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


def parse_refresh_response(obj: dict, existing_ids: set[str] | None = None) -> tuple[list[dict], list[str]]:
    entries, errs = [], []
    seen = set(existing_ids or set())
    for e in obj.get("entries", []):
        v = validate_entry(e)
        if e.get("trend_id") in seen:
            v.append("duplicate trend_id")
        if v:
            errs.append(f"{e.get('trend_id', '?')}: {'; '.join(v)}")
        else:
            entries.append(e); seen.add(e["trend_id"])
    return entries, errs
