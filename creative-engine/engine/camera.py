"""UGC camera direction checks (owner 2026-10-08: "missing creative camera micro movement", "the camera transition to a close-up
before he says 'Final' is missing", "it needs more artistic UGC style direction").

The camera is a character in UGC: a phone in a hand or on a knee, never a tripod. Every shot carries micro-movement (breathing sway,
small reframes, focus breathing) and at most one motivated move (creep-in, push-in, punch-in, tilt to a reveal, whip reframe).
Punchlines land on a closer framing reached by a move or a cut.
"""
from __future__ import annotations

import re

DEAD = re.compile(r"\b(locked|lock(ed)?-off|static|tripod|no move|does not move|still camera)\b", re.I)
ALIVE = re.compile(r"\b(handheld|hand-held|sway|drift|creep|push|punch|breath|reframe|tilt|pan|zoom|whip|wobble|bob|orbit|dolly|track|follow|settle|nudge)", re.I)
CLOSE = re.compile(r"\b(close-up|close up|closeup|tight|ecu|cu\b|punch-in|punch in|push-in|push in|push(es)? in)", re.I)


def camera_findings(packet: dict) -> list[dict]:
    out = []
    scenes = sorted(packet.get("scenes", []) or [], key=lambda s: s.get("start_s", 0))
    for s in scenes:
        cam = s.get("camera") or {}
        mv = f"{cam.get('movement', '')} {cam.get('rig', '')}"
        if DEAD.search(mv) and not ALIVE.search(mv):
            out.append({"code": "CAMERA_DEAD", "severity": "warning", "path": f"scenes.{s.get('scene_id')}.camera",
                        "message": "camera is locked with no micro-movement; UGC camera is a hand or a knee: breathing sway, small reframes, one motivated move"})
    spoken = [s for s in scenes if s.get("dialogue")]
    if spoken:
        last = spoken[-1]
        cam = last.get("camera") or {}
        if not CLOSE.search(f"{cam.get('shot', '')} {cam.get('movement', '')}"):
            out.append({"code": "CAMERA_PUNCHLINE_FLAT", "severity": "warning", "path": f"scenes.{last.get('scene_id')}.camera",
                        "message": "the last line lands in the same framing; reach a closer framing (push-in, punch-in or cut to a close-up) before the payoff line"})
    return out
