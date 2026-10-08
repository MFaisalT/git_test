"""Hand-object interaction staging rules (2026-10-08).

Owner requirement: the influencer must eventually review, unbox and try on products, so interaction is not avoided; it is staged
the way the platform's own production references stage it. Source: Higgsfield's bundled `ugc-video` workflow references
(ugc-unboxing-board.md, ugc-unboxing-clip.md, ugc-try-clip.md, boards.md; read in full 2026-10-08 via get_workflow_bundle_file),
which name these failure modes and fixes for Seedance 2.5:
  - phantom third arm  -> hand-count law: at most two hand roles, each named; the free hand is parked somewhere specific;
                          an unheld object beside busy hands also spawns a third hand, so every object is held or resting, explicitly
  - motion loops       -> one interaction per cut; no repetition words ("again", "repeatedly", "back and forth", "twice")
  - forked object state (both states rendered, e.g. an extra clock arm) -> every state change is a shown action, cause before
                          effect; fiddly mechanics happen across a hard cut (state A, hard cut, state B)
  - product multiplying / morphing -> exactly one product instance, front label side only, never rotated or spun
  - limb factory       -> no mirrors or reflections
  - stiff presenters   -> every cut opens mid-event
Research context (peer-reviewed/preprint, see docs/HAND-OBJECT-INTERACTION.md): hand-object contact and hand structure remain
the weakest region of current video diffusion models; research fixes condition on keyframes, contact maps or 3D structure,
none of which Higgsfield exposes except image references, so keyframe boards are the available equivalent.
"""
from __future__ import annotations

import re

LOOP_WORDS = ("again", "repeatedly", "back and forth", "twice", "over and over", "opens and closes", "keeps tapping", "taps twice", "several times")
MECHANISM_WORDS = ("dial", "knob", "clock hand", "dial arm", "dial hand", "button", "zip", "zipper", "buckle", "lace", "tie", "cable tie", "plug", "cap",
                   "lid", "screw", "switch", "latch", "clasp", "pump", "nozzle", "dropper", "hinge")
MANIPULATE_VERBS = ("turns", "turn", "twists", "twist", "rotates", "rotate", "unscrews", "screws", "zips", "unzips", "buckles", "ties", "unties",
                    "plugs", "unplugs", "presses", "clicks", "flips open", "snaps", "winds", "cinches", "snips", "opens", "closes")
MIRROR_WORDS = ("mirror", "reflection", "reflected")
PARK_WORDS = ("rests", "resting", "parked", "at her side", "at his side", "flat on", "in her lap", "in his lap", "on the table", "on the counter",
              "on his thigh", "on her thigh", "hangs", "relaxed")
HEAVY_WORDS = ("heavy", "appliance", "dumbbell", "kettle", "crate", "suitcase", "litre", "liter")

NEGATIVE_TAIL = ("No third arm, no extra hands, no duplicated limbs, no extra fingers, no deformed hands; objects never merge with hands; "
                 "exactly one of each prop; no mirrors or reflections; no slow motion.")


def _has(text: str, words) -> list[str]:
    t = f" {text.lower()} "
    return [w for w in words if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", t)]


def interaction_findings(scene: dict) -> list[dict]:
    """Warnings on the text the render prompt sends (physical_beat when present, else action)."""
    sid = scene.get("scene_id", "?")
    text = str(scene.get("physical_beat") or scene.get("action") or "")
    out = []
    loops = _has(text, LOOP_WORDS)
    if loops:
        out.append({"code": "INTERACTION_LOOP_WORD", "path": f"scenes.{sid}", "message": f"repetition wording {loops} makes Seedance loop the motion; one interaction per cut"})
    mech = _has(text, MECHANISM_WORDS)
    manip = _has(text, MANIPULATE_VERBS)
    if mech and manip and not scene.get("state_change_by_cut") and not scene.get("interaction"):
        out.append({"code": "INTERACTION_ONSCREEN_STATE_CHANGE", "path": f"scenes.{sid}",
                    "message": f"a mechanism ({', '.join(mech)}) changes state on screen ({', '.join(manip)}); stage it as state A, hard cut, state B with the hands already in the end pose (state_change_by_cut), or the model may render both states"})
    if _has(text, MIRROR_WORDS):
        out.append({"code": "INTERACTION_MIRROR", "path": f"scenes.{sid}", "message": "mirrors and reflections duplicate limbs and bodies; remove them"})
    HAND = r"\b(left|right) (?:hand|palm|index|thumb|fingers?|fingertip)\b"  # "right index fingertip" names the right hand too
    hands = len(re.findall(HAND + r"|\bboth hands\b", text.lower()))
    if manip and hands == 0:
        out.append({"code": "INTERACTION_HAND_UNNAMED", "path": f"scenes.{sid}", "message": "an object is manipulated but no hand is named; name the acting hand and park the other"})
    if re.search(HAND, text.lower()) and not re.search(r"\bboth hands\b", text.lower()):
        named = set(re.findall(HAND, text.lower()))
        if len(named) == 1 and not _has(text, PARK_WORDS):
            out.append({"code": "INTERACTION_FREE_HAND_UNPARKED", "path": f"scenes.{sid}", "message": f"only the {next(iter(named))} hand has a role; say where the other hand rests (an unassigned hand invites a phantom third)"})
    if _has(text, HEAVY_WORDS) and not re.search(r"\bboth hands\b", text.lower()):
        out.append({"code": "INTERACTION_HEAVY_ONE_HAND", "path": f"scenes.{sid}", "message": "heavy item lifted without both hands; heavy = both hands and visible effort"})
    return out


# Owner decision 2026-10-08: the character must actually handle props (turn the dial, open the box), not have the change hidden
# behind a cut. The platform recipe and the research both point to the same control: a keyframe board. A shown interaction is
# allowed when it is the only interaction in its own generation unit, fully specified (acting hand + contact point, moving part,
# from/to state, path, what the other hand does) and animated between an approved start frame and end frame (start_image/end_image).
INTERACTION_FIELDS = ("actor_hand", "contact", "object", "part", "from_state", "to_state", "motion", "support_hand")
INTERACTION_MIN_S = 3.0  # a slow continuous push plus a held end beat; shorter shots rush the hand and the model snaps the part


def interaction_spec_findings(scene: dict, unit_scene_ids: list[str] | None = None) -> list[dict]:
    """Errors and warnings for a scene's explicit `interaction` spec. Errors block finalisation: an under-specified or
    un-keyframed interaction is exactly what forked the dial in the owner's frames."""
    it = scene.get("interaction")
    if not it:
        return []
    sid = scene.get("scene_id", "?")
    out = []
    missing = [f for f in INTERACTION_FIELDS if not str(it.get(f) or "").strip()]
    if missing:
        out.append({"code": "INTERACTION_SPEC_INCOMPLETE", "severity": "error", "path": f"scenes.{sid}.interaction", "message": f"missing {', '.join(missing)}; name the hand, the contact point, the moving part, both states, the path and the other hand"})
    kf = it.get("keyframes") or {}
    if not (kf.get("start") and kf.get("end")):
        out.append({"code": "INTERACTION_KEYFRAMES_MISSING", "severity": "error", "path": f"scenes.{sid}.interaction.keyframes", "message": "a shown interaction is animated between a start frame and an end frame; generate the keyframe board and have the owner inspect it before any video"})
    elif kf.get("status") != "owner_approved":
        out.append({"code": "INTERACTION_KEYFRAMES_UNAPPROVED", "severity": "warning", "path": f"scenes.{sid}.interaction.keyframes", "message": "keyframes exist but the owner has not approved them; do not animate yet"})
    dur = float(scene.get("end_s", 0)) - float(scene.get("start_s", 0))
    if dur < INTERACTION_MIN_S:
        out.append({"code": "INTERACTION_TOO_SHORT", "severity": "warning", "path": f"scenes.{sid}", "message": f"{dur:.1f} s for a shown interaction; give it at least {INTERACTION_MIN_S:.0f} s (slow move plus a held end beat)"})
    if unit_scene_ids is not None and len(unit_scene_ids) > 1:
        out.append({"code": "INTERACTION_SHARED_UNIT", "severity": "error", "path": f"scenes.{sid}", "message": f"the interaction shares generation unit with {', '.join(x for x in unit_scene_ids if x != sid)}; it needs its own unit so the start and end frames bound exactly this move"})
    return out


def interaction_beat(scene: dict, prop_design: str = "") -> str:
    """Deterministic sentence for the render prompt; the model gets the mechanics, not a paraphrase."""
    it = scene.get("interaction") or {}
    if not it:
        return ""
    obj = it.get("object", "object")
    return (f"The one movement: {it.get('contact')}; {it.get('motion')}; the {it.get('part')} goes from {it.get('from_state')} to {it.get('to_state')} "
            f"in one slow continuous move and stops. {str(it.get('support_hand')).rstrip('.')}. Nothing else on the {obj} moves or changes; "
            f"the clip starts on the start frame and ends on the end frame.")


def interaction_rule_line(packet: dict, scenes: list[dict] | None = None) -> str:
    shown = any((s or {}).get("interaction") for s in (scenes or []))
    tail = ("one interaction per shot; the only state change is the one movement described, shown slowly from the start frame to the end frame."
            if shown else "one interaction per shot; state changes happen across the hard cuts, never mid-shot.")
    return ("Hands: at most two hands act; each named hand does one thing; the other hand rests where stated; every object is either held or resting on a surface; " + tail)
