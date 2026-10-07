"""Demonstration retrieval: a small, diverse set of approved exemplars per request.

Demos live in demos/*.json with tags; evaluation briefs live in eval/ and are never used as demos.
Selection: score by tag overlap with the brief (format, platform, commercial, silent), then enforce
diversity (no two demos with the same format) and cap at k.
"""
from __future__ import annotations

import json
import os

DEMO_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "demos")


def load_demos(demo_dir: str = DEMO_DIR) -> list[dict]:
    out = []
    if not os.path.isdir(demo_dir):
        return out
    for f in sorted(os.listdir(demo_dir)):
        if f.endswith(".json"):
            with open(os.path.join(demo_dir, f), encoding="utf-8") as fh:
                d = json.load(fh)
                d["_file"] = f
                out.append(d)
    return out


def brief_tags(brief: dict) -> set[str]:
    tags = {brief.get("format", ""), brief.get("platform", "")}
    tags.add("commercial" if brief.get("commercial") else "organic")
    if brief.get("format") == "silent_gag":
        tags.add("silent")
    if (brief.get("duration_target_s") or 0) <= 12:
        tags.add("short")
    return {t for t in tags if t}


def select_demos(brief: dict, k: int = 2, demos: list[dict] | None = None, exclude_ids: set[str] | None = None) -> list[dict]:
    demos = demos if demos is not None else load_demos()
    exclude_ids = exclude_ids or set()
    bt = brief_tags(brief)
    scored = []
    for d in demos:
        if d.get("demo_id") in exclude_ids or d.get("brief_id") == brief.get("brief_id"):
            continue  # never show a demo derived from the brief under evaluation
        overlap = len(bt & set(d.get("tags", [])))
        scored.append((overlap, d))
    scored.sort(key=lambda x: (-x[0], x[1].get("demo_id", "")))
    chosen, formats = [], set()
    for overlap, d in scored:
        if d.get("format") in formats:
            continue
        chosen.append(d)
        formats.add(d.get("format"))
        if len(chosen) >= k:
            break
    return chosen


def render_demo(d: dict) -> str:
    """Observable input/output + concise justification only; never private reasoning."""
    return (f"### Demonstration {d['demo_id']} ({d.get('format')})\n"
            f"Input brief: {d['input']}\n"
            f"Accepted output (excerpt): {json.dumps(d['accepted_output'], ensure_ascii=False)}\n"
            f"Why it was accepted: {d['justification']}\n"
            + (f"Rejected alternative: {d['rejected']}\n" if d.get("rejected") else ""))
