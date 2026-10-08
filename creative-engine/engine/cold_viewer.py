"""Cold-viewer check (S7b). Owner 2026-10-08: viewers "didn't get the point" without context; agreed earlier, now built.
A fresh-context reviewer (no brief, no bible, no packet) sees what a scrolling viewer sees, in three rounds (prompts/cold_viewer.md):
2 s muted, whole clip muted, then with the transcript. The engine compares its answers with the packet's own synopsis.
Sources: content-engine kill filter ("would a stranger stop scrolling within 2 s") and muted-first viewing; the skills review."""
from __future__ import annotations

import re

ROUND_FRAMES = {"r1": [0.1, 0.6, 1.2, 1.9], "r2_every_s": 1.0}


def sample_times(duration_s: float) -> dict:
    r2 = [round(t + 0.25, 2) for t in range(0, int(duration_s))]
    return {"r1": ROUND_FRAMES["r1"], "r2": r2}


def _terms(text: str) -> set[str]:
    stop = {"the", "a", "an", "and", "of", "to", "is", "it", "he", "she", "his", "her", "on", "in", "for", "with", "out", "that", "this", "at", "as", "by"}
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in stop and len(w) > 2}


def score(answers: dict, premise_terms: list[str]) -> dict:
    """premise_terms: the few words a viewer must land on (e.g. ['rates', 'wrong', 'umbrella', 'rain']).
    Coverage counts a term when it (or its stem) appears; a viewer may paraphrase, so this is a screen, not a verdict."""
    def cov(text: str) -> float:
        t = _terms(text)
        hit = sum(1 for p in premise_terms if any(x.startswith(p[:5]) for x in t))
        return hit / max(1, len(premise_terms))
    muted = cov(f"{answers.get('muted_what_happens', '')} {answers.get('muted_joke', '')}")
    full = cov(f"{answers.get('joke', '')} {answers.get('comment', '')}")
    verdict = "strong" if muted >= 0.5 else ("pass" if full >= 0.5 else "fail")
    return {"muted_coverage": round(muted, 2), "full_coverage": round(full, 2), "stop_scroll": bool(answers.get("stop_scroll")), "verdict": verdict,
            "problems": answers.get("problems", [])}
