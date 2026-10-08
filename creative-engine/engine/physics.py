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
    from .interaction import interaction_findings
    for s in sorted(packet.get("scenes", []), key=lambda x: x.get("start_s", 0)):
        out.extend(scene_physics_findings(s, tier))
        out.extend(dict(f, severity="warning") for f in interaction_findings(s))
    return out


# Word budgets per audio mode. Public Seedance guides (vendor/blog grade) put useful prompts at ~60-260 words; the clip's
# words go to picture when there is no speech, so non-spoken modes get tighter budgets (owner note 2026-10-08: silent clips
# may still carry a custom soundtrack, which is laid in the edit and must never be generated or described as sung/spoken).
PROMPT_BUDGET = {"on_camera_dialogue": 260, "off_camera_dialogue": 240, "voiceover_narration": 220,
                 "silent_ambience": 220, "text_over_broll": 200, "music_driven": 220}
SPOKEN_ON_CAMERA = ("on_camera_dialogue", "off_camera_dialogue")
PHYSICS_LONG = ("Physics: every held object is gripped by a named hand and has weight; objects rest on a surface, a strap or a lap when not held; "
                "nothing floats, appears or vanishes; an object in the mouth means no speech and no open grin in that beat; feet keep contact "
                "with the ground except for the steps or stomps described; everything not described holds still.")
PHYSICS_SHORT = ("Physics: each held object stays in a named hand or rests on a surface; nothing floats or vanishes; mouth closed on anything "
                 "in it; feet grounded except described steps; everything else holds still.")


def _audio_mode(packet: dict) -> str:
    am = (packet.get("production_format") or {}).get("audio_mode")
    if am:
        return am
    return "silent_ambience" if (packet.get("brief") or {}).get("format") == "silent_gag" else "on_camera_dialogue"


def _sound_line(packet: dict, am: str, first: dict) -> str:
    amb = (first.get("sound") or {}).get("ambience") or "real ambience"
    if am == "music_driven":
        st = (packet.get("production_format") or {}).get("soundtrack") or {}
        beats = st.get("beat_times_s") or []
        bpm = st.get("bpm")
        timing = (f" Motion accents land on {', '.join(f'{float(b):.1f}s' for b in beats[:8])}." if beats else (f" Motion follows a steady {bpm} BPM pulse." if bpm else ""))
        return "Sound: silent picture; no speech, no singing, no generated music; a soundtrack is added in the edit." + timing
    if am in ("silent_ambience", "text_over_broll"):
        return f"Sound: no speech, no music; {amb} and natural foley only."
    if am == "voiceover_narration":
        return f"Sound: nobody on screen speaks; lips stay closed; {amb}; narration and music are added in the edit."
    return f"Sound: only the quoted lines are spoken, each exactly once, then silence; {amb}; no music."


def bible_props(bible: dict | None) -> list[dict]:
    return [p for p in ((bible or {}).get("props") or []) if isinstance(p, dict)]


def referenced_props(bible: dict | None) -> list[dict]:
    """Bible props with a reference still, in media order (image_references after the character reference)."""
    return [p for p in bible_props(bible) if ((p.get("reference_asset") or {}).get("job_id") or (p.get("reference_asset") or {}).get("media_id"))]


def bible_prop_text(prop: str, bible: dict | None) -> str:
    """Replace a short prop name with the bible's exact design (owner frames 2026-10-08: 'paddle with a dial' rendered as a
    clock face with random numerals and no pointer). A prop with a reference still is tied to its @image slot."""
    low = prop.lower()
    refs = referenced_props(bible)
    for bp in bible_props(bible):
        if any(m.lower() in low for m in (bp.get("match") or [bp.get("id", "")]) if m):
            tag = f" (exactly as @image{2 + refs.index(bp)})" if bp in refs else ""
            return f"{bp.get('design', prop).rstrip('.')}{tag}"
    return prop


def compact_prompt(packet: dict, scenes: list[dict], bible: dict | None, return_meta: bool = False):
    """Physics-first render prompt held to a per-audio-mode word budget. Returns None when any scene lacks a physical_beat
    (caller falls back to the dense prompt). Shrinks deterministically: delivery notes -> long costume -> long physics block -> setting light."""
    if not scenes or any(not s.get("physical_beat") for s in scenes):
        return None
    cont = packet.get("continuity", {})
    am = _audio_mode(packet)
    budget = PROMPT_BUDGET.get(am, 240)
    speak = am in SPOKEN_ON_CAMERA
    first = scenes[0]
    cam0 = first.get("camera", {})

    def build(level: int) -> str:
        lines = []
        costume = cont.get("costume", "")
        if level < 2 and costume:
            lines.append(f"Identity: the person in @image1, exactly; same face and costume for the whole clip. {costume}".strip())
        else:
            lines.append("Identity: the person in @image1, exactly; same face and costume as the reference for the whole clip; no rings, watches, microphones or accessories that are not in the reference.")
        light = first.get("lighting", "").split(";")[0]
        lines.append(f"Setting: {first.get('location', '')}." + (f" {light}." if level < 4 and light else "") + " Passers-by, if any, are soft blurred shapes who never react.")
        cuts = any("cut" in str(s.get("transition_out", "")).lower() for s in scenes[:-1])
        lines.append(f"Camera: starts {cam0.get('shot', '')}; {cam0.get('movement', '')}." + ("" if cuts else " No cuts."))
        props = [bible_prop_text(str(x).strip(), bible) for x in (cont.get("props") or []) if str(x).strip()]
        if props:
            lines.append("Props (exact design, exactly one of each, nothing else added): " + "; ".join(props) + ".")
        lines.append(PHYSICS_LONG if level < 3 else PHYSICS_SHORT)
        for s in scenes:
            fmt = lambda v: f"{float(v):.0f}" if float(v).is_integer() else f"{float(v):.1f}"
            t0 = float(scenes[0]["start_s"])  # times are relative to this clip (a unit after a cut starts at 0 in its own render)
            t = f"{fmt(float(s['start_s']) - t0)}-{fmt(float(s['end_s']) - t0)}s"
            mv = str((s.get("camera") or {}).get("movement", "")).strip()
            cam_note = f" Camera: {mv.split(';')[0].strip().rstrip('.')}." if (mv and s is not first) else ""  # camera moves are never trimmed (owner values camera motion)
            line = f"{t}: {str(s['physical_beat']).strip().rstrip('.')}.{cam_note}"
            if s.get("interaction"):
                from .interaction import interaction_beat
                line += " " + interaction_beat(s)  # never trimmed: the mechanics are the point of the shot
            if speak:
                for d in s.get("dialogue", []) or []:
                    if not d.get("on_camera", True) and am == "off_camera_dialogue":
                        line += f" An unseen voice off camera says: \"{d['line']}\"."
                        continue
                    note = f" ({d['delivery']})" if (level < 1 and d.get("delivery")) else ""
                    line += f" {d.get('speaker', 'She')} says once: \"{d['line']}\"{note}."
            if s is not scenes[-1] and "cut" in str(s.get("transition_out", "")).lower():
                line += " Hard cut to."
            lines.append(line)
        lines.append(_sound_line(packet, am, first))
        if speak:
            from .voice import voice_prompt_line
            vl = voice_prompt_line(bible)
            if vl:
                lines.append(vl)  # never trimmed
        from .interaction import NEGATIVE_TAIL, interaction_rule_line
        lines.insert(4, interaction_rule_line(packet, scenes))  # never trimmed
        lines.append("No readable text, logos or signage except a product's own label. Natural skin, no blur on the face. " + NEGATIVE_TAIL)
        return "\n".join(lines)

    from .interaction import NEGATIVE_TAIL, interaction_rule_line
    from .interaction import interaction_beat
    fixed = len(NEGATIVE_TAIL.split()) + len(interaction_rule_line(packet, scenes).split()) + sum(len(interaction_beat(s).split()) for s in scenes)  # safety lines from the platform recipe: outside the descriptive budget

    def wc(t: str) -> int:
        return len(t.split()) - fixed

    level, text = 0, build(0)
    while wc(text) > budget and level < 4:
        level += 1
        text = build(level)
    meta = {"audio_mode": am, "word_budget": budget, "words": wc(text), "words_total_incl_safety_lines": len(text.split()), "shrink_level": level, "over_budget": wc(text) > budget}
    return (text, meta) if return_meta else text
