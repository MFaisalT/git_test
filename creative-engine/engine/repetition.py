"""Semantic-repetition check against episode history.

Evidence for a human reviewer, not deterministic proof of originality.
Uses lexical shingles (word 3-grams + content-word Jaccard) over the fields that
tend to repeat: hook, premise logline, payoff, joke/surprise, shot list, product pitch.
"""
from __future__ import annotations

import re

STOP = set("the a an and or of to in on at for with by from as is are was be it its this that these those she he they her his their into onto over under up down out off then than so very just not no".split())
FIELDS = ("hook", "premise", "payoff", "surprise", "shots", "pitch")


def _norm(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOP]


def _shingles(words: list[str], n=3) -> set[tuple]:
    return {tuple(words[i:i + n]) for i in range(max(0, len(words) - n + 1))}


def _jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def fingerprint(packet: dict) -> dict[str, str]:
    sel = packet.get("selected", {})
    prem = next((p for p in packet.get("premises", []) if p["id"] == sel.get("premise_id")), {})
    hook = next((h for h in packet.get("hook_variants", []) if h["id"] == sel.get("hook_id")), {})
    shots = " | ".join(f"{s.get('camera', {}).get('shot', '')} {s.get('camera', {}).get('movement', '')} {s.get('action', '')}" for s in packet.get("scenes", []))
    pitch = ""
    if packet.get("brief", {}).get("commercial"):
        pitch = " ".join(d.get("line", "") for d in packet.get("script", {}).get("dialogue", []) or []) + " " + packet.get("script", {}).get("disclosure_line", "")
    return {
        "hook": f"{hook.get('first_frame', '')} {hook.get('first_line_or_action', '')}",
        "premise": prem.get("logline", ""),
        "payoff": prem.get("payoff", ""),
        "surprise": prem.get("surprise", ""),
        "shots": shots,
        "pitch": pitch,
    }


def compare(new: dict, history: list[dict], threshold: float = 0.35) -> dict:
    """Return per-field max similarity vs history plus flags over threshold."""
    fp_new = fingerprint(new)
    results = {f: {"max_similarity": 0.0, "closest_packet": None} for f in FIELDS}
    for old in history:
        if old.get("packet_id") == new.get("packet_id"):
            continue
        fp_old = fingerprint(old)
        for f in FIELDS:
            a, b = _norm(fp_new[f]), _norm(fp_old[f])
            if not a or not b:
                continue
            sim = 0.5 * _jaccard(_shingles(a), _shingles(b)) + 0.5 * _jaccard(set(a), set(b))
            if sim > results[f]["max_similarity"]:
                results[f] = {"max_similarity": round(sim, 3), "closest_packet": old.get("packet_id")}
    flags = [f for f in FIELDS if results[f]["max_similarity"] >= threshold]
    return {"threshold": threshold, "fields": results, "flagged_fields": flags,
            "verdict": "review" if flags else "no-lexical-repetition-detected",
            "note": "Lexical similarity only; a reviewer must judge whether flagged overlap is identity (allowed) or a repeated joke/plot (not)."}
