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


# Owner rule 2026-10-08: camera and lens are named in plain language (device, zoom factor, equivalent focal length), never as
# Cinema Studio creative-control ids; and every phone-look production is "shot on an iPhone 18 Pro Max".
# The equivalent focal lengths are the usual approximations for recent Pro Max phones (0.5x ~13 mm, 1x ~24 mm, 2x ~48 mm crop,
# 5x ~120 mm); they are prompt language for the look, not a claim about the exact optics of that model.
PHONE_DEVICE = "iPhone 18 Pro Max"
ZOOM_LENSES = [(0.5, 13, "0.5x ultra-wide lens (about 13 mm equivalent)"), (1.0, 24, "1x main lens (about 24 mm equivalent)"),
               (2.0, 48, "2x lens (about 48 mm equivalent)"), (5.0, 120, "5x telephoto lens (about 120 mm equivalent)")]
PHONE_WORDS = re.compile(r"\b(phone|iphone|handheld|hand-held|selfie|ugc|propped)\b", re.I)


def is_phone_look(packet: dict, scene: dict | None = None) -> bool:
    cam = (scene or {}).get("camera") or {}
    style = ((packet.get("production_format") or {}).get("camera_style") or "")
    return bool(PHONE_WORDS.search(" ".join(str(cam.get(k, "")) for k in ("lens", "rig", "movement", "shot")) + " " + style))


def lens_phrase(lens: str) -> str | None:
    """Map free lens text to a plain zoom-factor phrase: '26mm' -> 1x, '0.5x' -> ultra-wide, 'telephoto' -> 5x."""
    t = str(lens or "").lower()
    m = re.search(r"(\d+(?:\.\d+)?)\s*x\b", t)
    if m:
        z = float(m.group(1)); return min(ZOOM_LENSES, key=lambda r: abs(r[0] - z))[2]
    m = re.search(r"(\d+(?:\.\d+)?)\s*mm", t)
    if m:
        mm = float(m.group(1)); return min(ZOOM_LENSES, key=lambda r: abs(r[1] - mm))[2]
    if "ultra" in t or "wide" in t:
        return ZOOM_LENSES[0][2]
    if "tele" in t:
        return ZOOM_LENSES[3][2]
    if "main" in t:
        return ZOOM_LENSES[1][2]
    return None


def camera_device_clause(packet: dict, scene: dict) -> str:
    """'Shot on an iPhone 18 Pro Max, 1x main lens (about 24 mm equivalent)' for phone looks; the plain lens otherwise."""
    lp = lens_phrase((scene.get("camera") or {}).get("lens", ""))
    if is_phone_look(packet, scene):
        return f"shot on an {PHONE_DEVICE}, {lp or ZOOM_LENSES[1][2]}"
    return lp or str((scene.get("camera") or {}).get("lens", "")).strip()


def lens_findings(packet: dict) -> list[dict]:
    out = []
    for s in packet.get("scenes", []) or []:
        lens = (s.get("camera") or {}).get("lens", "")
        if lens and not lens_phrase(lens):
            out.append({"code": "CAMERA_LENS_UNNAMED", "severity": "warning", "path": f"scenes.{s.get('scene_id')}.camera.lens",
                        "message": "name the lens in plain terms: a zoom factor (0.5x, 1x, 2x, 5x) or an equivalent focal length in mm"})
    return out


# Higgsfield ugc-video/references/ugc-clip.md (read at source 2026-10-08, owner asked to recheck): handheld/selfie shots carry
# "slight natural handheld micro-shake from the grip" (L187-188, L543); locked-off/static shots are "absolutely frozen" and must not
# contain handheld/shake/drift/wobble/sway words, which "leak motion into the render" (L177-181); a single deliberate slow push-in
# is the sole exception on a locked shot, and a candid handheld zoom-in is allowed as an opener (L145-151).
STATIC_WORDS = re.compile(r"\b(propped|locked|locked-off|static|tripod)\b", re.I)
MOTION_LEAK = re.compile(r"\b(handheld|hand-held|shake|micro-shake|drift|drifting|wobble|sway|breathing sway|subtle movement|natural movement)\b", re.I)


def camera_mode_findings(packet: dict) -> list[dict]:
    out = []
    for s in packet.get("scenes", []) or []:
        cam = s.get("camera") or {}
        mv = f"{cam.get('movement', '')} {cam.get('rig', '')}"
        if STATIC_WORDS.search(mv) and MOTION_LEAK.search(mv):
            out.append({"code": "CAMERA_STATIC_MOTION_LEAK", "severity": "warning", "path": f"scenes.{s.get('scene_id')}.camera",
                        "message": "a locked/propped shot also names handheld/sway/shake words; pick one: handheld with micro-shake from the grip, "
                                   "or locked-off with zero motion (one deliberate push-in is the only exception)"})
    return out
