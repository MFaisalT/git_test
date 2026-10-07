"""Semantic-repetition check against episode history.

Evidence for a human reviewer, not deterministic proof of originality.
Uses lexical shingles (word 3-grams + content-word Jaccard) over the fields that
tend to repeat: hook, premise logline, payoff, joke/surprise, shot list, product pitch.
"""
from __future__ import annotations

import re

STOP = set("the a an and or of to in on at for with by from as is are was be it its this that these those she he they her his their into onto over under up down out off then than so very just not no".split())
FIELDS = ("hook", "premise", "payoff", "surprise", "shots", "pitch", "devices")


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
    devices = " ".join([
        f"mechanism_{hook.get('mechanism', '')}",
        " ".join(packet.get("continuity", {}).get("props", [])),
        " ".join(s.get("lighting", "") for s in packet.get("scenes", [])),
        "offcamera_voice" if any(not d.get("on_camera", True) for s in packet.get("scenes", []) for d in (s.get("dialogue") or []) if isinstance(d, dict)) else "",
        prem.get("surprise", ""),
    ])
    return {
        "devices": devices,
        "hook": f"{hook.get('first_frame', '')} {hook.get('first_line_or_action', '')}",
        "premise": prem.get("logline", ""),
        "payoff": prem.get("payoff", ""),
        "surprise": prem.get("surprise", ""),
        "shots": shots,
        "pitch": pitch,
    }


def recurring_motifs(new: dict, history: list[dict], last_n: int = 6, min_share: float = 0.5) -> list[dict]:
    """Props / mechanism / device tokens that recur across the recent episodes INCLUDING the new one.
    Evidence for a reviewer: identity props (e.g. the chest lamp) are allowed; a repeated reveal device is not."""
    recent = [p for p in history if p.get("packet_id") != new.get("packet_id")][-last_n:] + [new]
    def toks(p):
        hook = next((h for h in p.get("hook_variants", []) if h["id"] == p.get("selected", {}).get("hook_id")), {})
        t = {f"mechanism:{hook.get('mechanism', '')}"}
        for pr in p.get("continuity", {}).get("props", []):
            t |= {f"prop:{w}" for w in _norm(re.sub(r"\(.*?\)", " ", pr)) if len(w) > 3}
        if any(not d.get("on_camera", True) for s in p.get("scenes", []) for d in (s.get("dialogue") or []) if isinstance(d, dict)):
            t.add("device:offcamera_voice")
        return t
    counts: dict[str, int] = {}
    for p in recent:
        for t in toks(p):
            counts[t] = counts.get(t, 0) + 1
    n = len(recent)
    return sorted(({"motif": k, "episodes": v, "share": round(v / n, 2)} for k, v in counts.items() if n >= 2 and v / n >= min_share and v >= 2), key=lambda x: -x["share"])


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
    motifs = recurring_motifs(new, history)
    return {"threshold": threshold, "fields": results, "flagged_fields": flags, "recurring_motifs": motifs,
            "verdict": "review" if flags else "no-lexical-repetition-detected",
            "note": "Lexical similarity only; a reviewer must judge whether flagged overlap is identity (allowed) or a repeated joke/plot/device (not). 'devices' covers hook mechanism, props, lighting language, off-camera-voice use and the surprise device."}
