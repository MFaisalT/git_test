"""Timing and continuity rules from the 2026-10-08 renders and the independent skills review.

- Speech must fit its scene at the character's real speaking rate. The locked Uncle Verdict voice runs about 2.1 words/s, and
  his 12-word verdict took 5.8 s, which squeezed out the rain beat. Higgsfield's own monologue guidance and the ugc-influencer-video
  skill put the ceiling at 2.3-2.8 words/s. Hard ceiling 2.8 w/s; when the locked voice has a measured rate, use that.
- A world event the joke depends on (rain starts, a stranger passes) happens UNDER the line, not in a short silent scene after it
  (Higgsfield ugc-clip "sound intrusion": the event happens and the voice talks over it).
- Prop states are continuous across cuts: the pointer reads the same number at the end of one unit and the start of the next
  (owner frames 2026-10-08: about 2.5 before the cut, about 3 after it).
"""
from __future__ import annotations

import re

SPEECH_WPS_CEILING = 2.8
WORLD_EVENT_WORDS = re.compile(r"\b(rain|drops?|passes|slides past|walks past|enters|arrives|falls|bursts|thunder|splash|honks?)\b", re.I)


def _words(s: dict) -> int:
    return sum(len(str(d.get("line", "")).split()) for d in (s.get("dialogue") or []))


def _units(packet: dict) -> dict[str, str]:
    return {sid: u.get("generation_unit") for u in (packet.get("tool_mapping") or {}).get("units", []) or [] for sid in (u.get("scene_ids") or [])}


def speech_fit_findings(packet: dict, bible: dict | None) -> list[dict]:
    out = []
    v = ((bible or {}).get("approved_assets") or {}).get("voice") or {}
    rate = float(v.get("measured_wps") or 0) or None
    for s in packet.get("scenes", []) or []:
        w = _words(s)
        if not w:
            continue
        dur = float(s["end_s"]) - float(s["start_s"])
        if w / max(dur, 1e-6) > SPEECH_WPS_CEILING:
            out.append({"code": "SPEECH_TOO_FAST", "severity": "error", "path": f"scenes.{s.get('scene_id')}",
                        "message": f"{w} words in {dur:.1f} s = {w / dur:.1f} w/s (ceiling {SPEECH_WPS_CEILING})"})
        if rate:
            need = w / rate + 0.4  # breath before + settle after
            if need > dur:
                out.append({"code": "SPEECH_OVERRUNS_SCENE", "severity": "error", "path": f"scenes.{s.get('scene_id')}",
                            "message": f"the locked voice speaks about {rate:.1f} w/s, so {w} words need {need:.1f} s; the scene has {dur:.1f} s. "
                                       "Lengthen the scene, cut words, or run the next beat under the line"})
    return out


def world_event_findings(packet: dict) -> list[dict]:
    out = []
    scenes = sorted(packet.get("scenes", []) or [], key=lambda s: s.get("start_s", 0))
    for prev, s in zip(scenes, scenes[1:]):
        dur = float(s["end_s"]) - float(s["start_s"])
        if prev.get("dialogue") and not s.get("dialogue") and "cut" not in str(prev.get("transition_out", "")).lower() \
                and dur < 2.5 and WORLD_EVENT_WORDS.search(str(s.get("physical_beat") or s.get("action") or "")):
            out.append({"code": "WORLD_EVENT_AFTER_SPEECH", "severity": "warning", "path": f"scenes.{s.get('scene_id')}",
                        "message": f"a {dur:.1f} s world event right after the line gets squeezed out when speech runs long; start it under the line "
                                   "(the event happens, he talks over it) and keep this scene as its payoff"})
    return out


def _end_states(s: dict) -> dict:
    st = dict(s.get("prop_states") or {})
    it = s.get("interaction") or {}
    if it.get("object") and it.get("part") and it.get("to_state"):
        st[f"{it['object']}.{it['part']}"] = it["to_state"]
    return st


def _start_states(s: dict) -> dict:
    st = dict(s.get("prop_states") or {})
    it = s.get("interaction") or {}
    if it.get("object") and it.get("part") and it.get("from_state"):
        st[f"{it['object']}.{it['part']}"] = it["from_state"]
    return st


def _norm(v: str) -> str:
    m = re.search(r"-?\d+(?:\.\d+)?", str(v))
    return m.group(0) if m else str(v).strip().lower()


def prop_state_findings(packet: dict) -> list[dict]:
    out = []
    scenes = sorted(packet.get("scenes", []) or [], key=lambda s: s.get("start_s", 0))
    for prev, s in zip(scenes, scenes[1:]):
        if s.get("state_change_by_cut"):
            continue  # an intended change across the cut
        a, b = _end_states(prev), _start_states(s)
        for k in set(a) & set(b):
            if _norm(a[k]) != _norm(b[k]):
                out.append({"code": "PROP_STATE_DISCONTINUITY", "severity": "error", "path": f"scenes.{s.get('scene_id')}",
                            "message": f"{k} ends {a[k]!r} in {prev.get('scene_id')} but starts {b[k]!r} in {s.get('scene_id')}; the viewer sees it jump"})
    return out
