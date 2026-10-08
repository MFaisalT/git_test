"""Physics-realism gates and the compact, physics-first render prompt (added 2026-10-08 after the owner's inspection of the
character bake-off renders: floating props, a whistle hovering in an open mouth, objects without hands).

Evidence basis (public prompting guides for Seedance 2.x, read 2026-10-08; vendor/blog grade): keep prompts roughly 60-260 words
with the important visuals first; one main action beat per short clip; describe the chain cause -> movement -> contact -> consequence
with explicit support/contact points and weight; say what stays still, otherwise the model keeps things drifting; describe what to see,
not what to avoid. Our bake-off prompts were ~1,000 words with four multi-action scenes in 12 s on the cheapest model, and one
contained a literal contradiction (whistle clamped in the teeth while shouting and grinning)."""
from __future__ import annotations

import re

HELD_PROPS = ("clipboard", "paddle", "umbrella", "phone", "pen", "tape", "whistle", "metronome", "scissors", "stub", "ticket",
              "cable", "plug", "carton", "box", "sock", "coat", "bag", "cup", "mug", "tape measure")  # worn items (lamp on a strap) and furniture (chair) are not held
HAND_VERBS = ("hold", "holds", "holding", "lift", "lifts", "raise", "raises", "pick", "picks", "grip", "grips", "carries", "carry",
              "writes", "write", "taps", "tap", "turns", "turn", "snips", "cuts", "wraps", "tears", "presses", "pushes", "clamps")
CONTACT_WORDS = ("hand", "hands", "finger", "fingers", "palm", "grip", "grips", "fist", "thumb", "forearm", "knee", "teeth", "lips", "shoulder")
MOUTH_WORDS = ("in her teeth", "in his teeth", "in her mouth", "in his mouth", "clamps the whistle", "whistle in", "between her teeth", "between his teeth")
OPEN_MOUTH_WORDS = ("grin", "grins", "grinning", "beaming", "smile", "smiles", "shout", "shouts", "roar", "roars", "bellows", "says", "speaks", "laugh")
STATIC_WORDS = ("holds still", "stays still", "remain still", "remains still", "stay still", "locked", "does not move", "static", "nothing else moves")


def _sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if s]


def scene_physics_findings(scene: dict, tier: str = "") -> list[dict]:
    """Warnings only: these are heuristics for a reviewer and for the repair prompt, not proofs."""
    out = []
    sid = scene.get("scene_id", "?")
    beat = str(scene.get("physical_beat", "") or "")
    action = str(scene.get("action", ""))
    perf = str(scene.get("performance", ""))
    # when a physical_beat exists it is the only motion text the compact render prompt sends, so judge that
    text = (beat if beat else f"{action} {perf}").lower()
    dur = max(0.1, float(scene.get("end_s", 0)) - float(scene.get("start_s", 0)))
    has_speech = bool(scene.get("dialogue"))
    # 1. object in the mouth while speaking / grinning / shouting
    if any(w in text for w in MOUTH_WORDS) and (has_speech or any(w in text for w in OPEN_MOUTH_WORDS)):
        out.append({"code": "PHYSICS_MOUTH_CONFLICT", "severity": "warning", "path": f"scenes.{sid}",
                    "message": "an object is held in the mouth in the same beat as speech, a shout or an open grin; split the beats (object on its cord while speaking)"})
    # 2. too many handheld props handled in one scene
    handled = {p for p in HELD_PROPS if p in text}
    if len(handled) > 2 and any(v in text.split() for v in HAND_VERBS):
        out.append({"code": "PHYSICS_HANDS_OVERLOAD", "severity": "warning", "path": f"scenes.{sid}",
                    "message": f"{len(handled)} handheld props handled in one scene ({', '.join(sorted(handled))}); two hands, so at most two held objects per beat, the rest on a strap, lap or surface"})
    # 3. held object without any contact wording
    if any(v in text.split() for v in HAND_VERBS) and handled and not any(w in text for w in CONTACT_WORDS):
        out.append({"code": "PHYSICS_NO_CONTACT", "severity": "warning", "path": f"scenes.{sid}",
                    "message": "a prop is handled but no hand/finger/contact point is named; say which hand grips what and where it rests"})
    # 4. action density: one main beat per ~3 s for the draft tier, per ~2 s otherwise
    if beat:
        if len(beat.split()) > 42:
            out.append({"code": "PHYSICS_BEAT_TOO_LONG", "severity": "warning", "path": f"scenes.{sid}", "message": f"physical_beat is {len(beat.split())} words; keep it to one <=40-word chain"})
        sents = []
    else:
        sents = _sentences(action)
    limit = dur / (3.0 if tier == "draft_mini" else 2.0)
    if sents and len(sents) > max(1, round(limit)):
        out.append({"code": "PHYSICS_ACTION_DENSITY", "severity": "warning", "path": f"scenes.{sid}",
                    "message": f"{len(sents)} action sentences in {dur:.0f} s (limit {max(1, round(limit))} for tier '{tier or 'standard'}'); dense choreography is where cheap models drift and props float"})
    # 5. nothing declared still
    if not any(w in text for w in STATIC_WORDS) and not scene.get("physical_beat"):
        out.append({"code": "PHYSICS_NO_STATIC", "severity": "warning", "path": f"scenes.{sid}",
                    "message": "nothing is declared to hold still; the model keeps undirected elements drifting unless told"})
    if not scene.get("physical_beat"):
        out.append({"code": "PHYSICS_BEAT_MISSING", "severity": "warning", "path": f"scenes.{sid}",
                    "message": "scene has no physical_beat (one <=30-word sentence: who moves what, with which hand, contact point, what stays still); the compact render prompt needs it"})
    return out


def physics_findings(packet: dict) -> list[dict]:
    tier = str((packet.get("brief") or {}).get("render_tier", "")).lower()
    out = []
    for s in sorted(packet.get("scenes", []), key=lambda x: x.get("start_s", 0)):
        out.extend(scene_physics_findings(s, tier))
    return out


def compact_prompt(packet: dict, scenes: list[dict], bible: dict | None) -> str | None:
    """Physics-first render prompt, ~150-260 words. Returns None when any scene lacks a physical_beat (caller falls back to the dense prompt)."""
    if not scenes or any(not s.get("physical_beat") for s in scenes):
        return None
    cont = packet.get("continuity", {})
    b = packet.get("brief", {})
    am = (packet.get("production_format") or {}).get("audio_mode")
    silent = b.get("format") == "silent_gag" or am in ("silent_ambience", "text_over_broll", "music_driven")
    first = scenes[0]
    lines = []
    lines.append(f"Identity: the person in @image1, exactly; same face and costume for the whole clip. {cont.get('costume', '')}".strip())
    lines.append(f"Setting: {first.get('location', '')}. {first.get('lighting', '').split(';')[0]}. Passers-by, if any, are soft blurred shapes who never react.")
    cam0 = first.get("camera", {})
    lines.append(f"Camera: {cam0.get('shot', '')}; {cam0.get('movement', '')}. No cuts.")
    lines.append("Physics: every held object is gripped by a named hand and has weight; objects rest on a surface, a strap or a lap when not held; nothing floats, appears or vanishes; an object in the mouth means no speech and no open grin in that beat; feet keep contact with the ground except for the steps or stomps described; everything not described holds still.")
    for s in scenes:
        t = f"{float(s['start_s']):.0f}-{float(s['end_s']):.0f}s"
        beat = str(s["physical_beat"]).strip().rstrip(".")
        line = f"{t}: {beat}."
        for d in s.get("dialogue", []) or []:
            if not silent:
                line += f" {d.get('speaker', 'She')} says: \"{d['line']}\"" + (f" ({d['delivery']})" if d.get("delivery") else "") + "."
        lines.append(line)
    lines.append("Sound: " + ("no speech; " if silent else "only the quoted lines are spoken; ") + f"{first.get('sound', {}).get('ambience', 'real ambience')}; no music.")
    lines.append("No readable text, logos or signage. Natural skin, natural hands, no blur on the face.")
    return "\n".join(lines)
