"""Parameterised prompt modules with conditional sections.

Applies prompt-engineering-patterns (wshobson/agents, read 2026-10-07): structured output against a
typed contract, progressive disclosure (constraints before examples), dynamic few-shot selection,
self-verification checklist, concise role framing with concrete responsibilities, and token economy.
"""
from __future__ import annotations

import json
import os

from .retrieval import render_demo, select_demos

PROMPT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts")

STAGES = ["trend_refresh", "premises", "hooks", "script_storyboard", "qa_review"]


def _load(name: str) -> str:
    with open(os.path.join(PROMPT_DIR, f"{name}.md"), encoding="utf-8") as fh:
        return fh.read()


def _cond(text: str, flag: str, on: bool) -> str:
    """Conditional sections: <<IF flag>> ... <<ENDIF flag>>"""
    start, end = f"<<IF {flag}>>", f"<<ENDIF {flag}>>"
    while start in text:
        a = text.index(start); b = text.index(end) + len(end)
        inner = text[a + len(start):b - len(end)]
        text = text[:a] + (inner if on else "") + text[b:]
    return text


def _fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace("{{" + k + "}}", v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, indent=2))
    return text


def render_stage(stage: str, brief: dict, bible: dict, context: dict, history_fingerprints: list[dict], demos_k: int = 2, trends_text: str = "", formats: dict | None = None) -> tuple[str, list[str]]:
    """Return (prompt_text, demo_ids_used). context carries prior stage outputs."""
    tpl = _load(stage)
    silent = brief.get("format") == "silent_gag"
    commercial = bool(brief.get("commercial"))
    tpl = _cond(tpl, "SILENT", silent)
    tpl = _cond(tpl, "SPOKEN", not silent)
    tpl = _cond(tpl, "COMMERCIAL", commercial)
    tpl = _cond(tpl, "HISTORY", bool(history_fingerprints))
    tpl = _cond(tpl, "TRENDS", bool(trends_text))
    demos = select_demos(brief, k=demos_k) if stage in ("premises", "script_storyboard") else []
    demo_text = "\n".join(render_demo(d) for d in demos) if demos else "(no demonstrations retrieved)"
    formats = formats or {}
    text = _fill(tpl, BRIEF=brief, BIBLE=bible, CONTEXT=context, HISTORY=history_fingerprints, DEMOS=demo_text, TRENDS=trends_text,
                 FORMAT_CATALOGUE=formats.get("catalogue", ""), FORMAT_FIXED=formats.get("fixed", {}), FORMAT_RECENT=formats.get("recent", []), FORMAT_SELECTED=formats.get("selected", {}),
                 COMMERCIAL_FACTS=(brief.get("commercial") or {}).get("verified_facts", []),
                 FORBIDDEN=(brief.get("commercial") or {}).get("forbidden_claims", []))
    return text, [d["demo_id"] for d in demos]


def repair_prompt(stage: str, previous_output: dict, findings: list[dict]) -> str:
    return _fill(_load("repair"), STAGE=stage, PREVIOUS=previous_output, FINDINGS=findings)


def render_trend_refresh(project_meta: dict, bible: dict, existing_labels: list[str]) -> str:
    return _fill(_load("trend_refresh"), NICHE=project_meta.get("niche") or "original short-form character comedy",
                 PLATFORMS=project_meta.get("platforms") or ["instagram_reels", "tiktok", "youtube_shorts"],
                 BIBLE_SUMMARY={"logline": bible.get("logline"), "rule": bible.get("character", {}).get("rule"), "do_not": bible.get("do_not")},
                 EXISTING_LABELS=existing_labels)
