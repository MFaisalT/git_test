"""Production-format catalogue and diversity policy.

A brief may FIX any of these (then the engine obeys) or leave them OPEN (then the engine chooses, and must vary
against the recent episode history). Trend entries of type `format`/`edit_move`/`style` extend the menu at run time.
Validators check that the storyboard actually realises the declared format.
"""
from __future__ import annotations

SHOT_ARCHITECTURES = {
    "single_take_static": "one continuous take, locked-off camera, no cuts (one generation unit)",
    "single_take_moving_camera": "one continuous take with a motivated camera move (push-in, orbit, handheld follow, tilt reveal); no cuts",
    "multi_scene_cut": "several scenes joined by hard cuts in edit; each scene is its own generation unit",
    "jump_cut_timelapse": "same framing, 3+ jump cuts marking time passing; change accumulates between cuts",
    "pov_handheld": "character-held or companion-held phone; angle changes come from the character, not cuts",
    "interview_offcamera": "character answers an unseen interviewer; one on-camera speaker",
    "montage": "rapid series of short shots over one audio bed (voice-over or music) building one idea",
    "loop": "ending matches the opening frame so autoplay repeats seamlessly",
    "continuation_from_last_frame": "part 2 picks up from the last frame of an earlier approved clip (reference clip required)",
    "split_or_insert": "main shot plus one insert/close-up or a split frame assembled in edit",
    "motion_transfer_owned_footage": "owned/licensed driving footage re-cast with the character via Genjutsu (rights required)",
    "other": "a format proposed from the trend radar or the brief; must be described",
}
AUDIO_MODES = {
    "silent_ambience": "no speech; ambience + foley only; optional caption added in post",
    "voiceover_narration": "character or narrator voice-over recorded separately; mouth not synced on camera",
    "on_camera_dialogue": "character speaks to camera; one on-camera speaker",
    "off_camera_dialogue": "a second voice off camera; character may reply on camera",
    "text_over_broll": "no speech; the script becomes on-screen text added in post",
    "music_driven": "licensed/owned music carries the rhythm; cuts or actions land on beats; little or no speech",
}
REUSE = ("same", "new", "none")
DIVERSITY_WINDOW = 4  # do not repeat the same (shot_architecture, audio_mode) pair within the last N episodes unless the brief fixes it


def catalogue_text(trend_formats: list[dict] | None = None) -> str:
    L = ["Shot architectures:"] + [f"- {k}: {v}" for k, v in SHOT_ARCHITECTURES.items()]
    L += ["Audio modes:"] + [f"- {k}: {v}" for k, v in AUDIO_MODES.items()]
    if trend_formats:
        L += ["Trending format options from the radar (adapt the mechanism; cite the trend_id):"] + [f"- [{t['trend_id']}] {t['label']}: {t['how_to_adapt']}" for t in trend_formats]
    return "\n".join(L)


def recent_formats(history: list[dict], n: int = DIVERSITY_WINDOW) -> list[dict]:
    out = []
    for p in history[-n:]:
        pf = p.get("production_format") or {}
        out.append({"packet_id": p.get("packet_id"), "shot_architecture": pf.get("shot_architecture", "unspecified"), "audio_mode": pf.get("audio_mode", "unspecified")})
    return out


def diversity_findings(pf: dict, history: list[dict], fixed: dict) -> list[dict]:
    """Warn (not error) when an open format repeats a recent pair; error when a fixed field was not obeyed."""
    out = []
    for k in ("shot_architecture", "audio_mode"):
        if fixed.get(k) and pf.get(k) != fixed[k]:
            out.append({"code": "FORMAT_FIXED_IGNORED", "severity": "error", "message": f"brief fixed {k}={fixed[k]} but packet declares {pf.get(k)}"})
    if not fixed.get("shot_architecture") and not fixed.get("audio_mode"):
        pair = (pf.get("shot_architecture"), pf.get("audio_mode"))
        for r in recent_formats(history):
            if (r["shot_architecture"], r["audio_mode"]) == pair:
                out.append({"code": "FORMAT_REPEATS_RECENT", "severity": "warning", "message": f"format pair {pair} already used in {r['packet_id']} within the last {DIVERSITY_WINDOW} episodes"})
                break
    return out


def realisation_findings(pf: dict, packet: dict) -> list[dict]:
    """Deterministic checks that scenes realise the declared format."""
    out = []
    scenes = sorted(packet.get("scenes", []), key=lambda s: s.get("start_s", 0))
    cuts = sum(1 for s in scenes[:-1] if "cut" in str(s.get("transition_out", "")).lower()) + sum(int(s.get("cuts_inside_clip", 0) or 0) for s in scenes)
    units = len(packet.get("tool_mapping", {}).get("units", []) or [])
    sa, am = pf.get("shot_architecture"), pf.get("audio_mode")
    if sa in ("single_take_static", "single_take_moving_camera", "loop", "pov_handheld") and cuts > 0:
        out.append({"code": "FORMAT_SINGLE_TAKE_HAS_CUTS", "severity": "error", "message": f"{sa} declared but {cuts} cut(s) present"})
    if sa in ("single_take_static", "single_take_moving_camera") and units > 1:
        out.append({"code": "FORMAT_SINGLE_TAKE_UNITS", "severity": "error", "message": f"{sa} must be one generation unit (<=30 s); plan has {units}"})
    if sa == "single_take_moving_camera":
        moves = " ".join(str((s.get("camera") or {}).get("movement", "")).lower() for s in scenes)
        if not any(w in moves for w in ("push", "orbit", "track", "follow", "tilt", "pan", "dolly", "handheld", "drift", "crane", "pull")):
            out.append({"code": "FORMAT_NO_CAMERA_MOVE", "severity": "error", "message": "single_take_moving_camera declared but no camera movement described"})
    if sa == "single_take_static":
        moves = " ".join(str((s.get("camera") or {}).get("movement", "")).lower() for s in scenes)
        if any(w in moves for w in ("push-in", "orbit", "track", "dolly", "pan ")):
            out.append({"code": "FORMAT_STATIC_MOVES", "severity": "warning", "message": "single_take_static declared but camera movement described"})
    if sa == "jump_cut_timelapse" and cuts < 3:
        out.append({"code": "FORMAT_JUMPCUT_TOO_FEW", "severity": "error", "message": f"jump_cut_timelapse needs >=3 cuts, has {cuts}"})
    if sa == "multi_scene_cut" and cuts < 1:
        out.append({"code": "FORMAT_MULTISCENE_NO_CUT", "severity": "error", "message": "multi_scene_cut declared but no cut between scenes"})
    if sa == "loop" and "loop" not in str(scenes[-1].get("transition_out", "")).lower() if scenes else False:
        out.append({"code": "FORMAT_LOOP_END", "severity": "error", "message": "loop declared but last transition_out does not say loop"})
    if sa == "motion_transfer_owned_footage" and not any(r.get("kind") == "driving_footage" for r in packet.get("asset_rights", [])):
        out.append({"code": "FORMAT_MOTION_TRANSFER_RIGHTS", "severity": "error", "message": "motion transfer declared without a driving_footage rights entry"})
    if sa == "continuation_from_last_frame" and not any(r.get("kind") in ("other", "driving_footage") and "clip" in str(r.get("asset", "")).lower() for r in packet.get("asset_rights", [])):
        out.append({"code": "FORMAT_CONTINUATION_REF", "severity": "error", "message": "continuation declared without a reference clip asset"})
    dialogue = [d for s in scenes for d in (s.get("dialogue") or []) if isinstance(d, dict) and str(d.get("line", "")).strip()]
    dialogue += [d for d in (packet.get("script", {}).get("dialogue") or []) if isinstance(d, dict) and str(d.get("line", "")).strip()]
    if am in ("silent_ambience", "text_over_broll") and dialogue:
        out.append({"code": "FORMAT_SILENT_HAS_SPEECH", "severity": "error", "message": f"{am} declared but {len(dialogue)} dialogue line(s) present"})
    if am == "text_over_broll" and not (packet.get("script", {}).get("caption_text") or any(s.get("captions") for s in scenes)):
        out.append({"code": "FORMAT_TEXTOVER_NO_TEXT", "severity": "error", "message": "text_over_broll declared but no caption text provided"})
    if am == "off_camera_dialogue" and not any(not d.get("on_camera", True) for d in dialogue):
        out.append({"code": "FORMAT_NO_OFFCAMERA_LINE", "severity": "error", "message": "off_camera_dialogue declared but no off-camera line"})
    if am == "on_camera_dialogue" and not any(d.get("on_camera", True) for d in dialogue):
        out.append({"code": "FORMAT_NO_ONCAMERA_LINE", "severity": "error", "message": "on_camera_dialogue declared but no on-camera line"})
    if am == "voiceover_narration" and not any(str(d.get("speaker", "")).lower().startswith(("vo", "narrat")) or not d.get("on_camera", True) for d in dialogue):
        out.append({"code": "FORMAT_NO_VO", "severity": "error", "message": "voiceover_narration declared but no VO/narrator line"})
    if am == "music_driven" and not any(str((s.get("sound") or {}).get("music", "")).strip().lower() not in ("", "none", "no music") for s in scenes):
        out.append({"code": "FORMAT_NO_MUSIC", "severity": "error", "message": "music_driven declared but no scene names a (licensed) music cue"})
    if am == "music_driven":
        st = pf.get("soundtrack") or {}
        if not st:
            out.append({"code": "FORMAT_SOUNDTRACK_SPEC", "severity": "error", "message": "music_driven declared but production_format.soundtrack is missing (source, title, rights_status, bpm or beat_times_s)"})
        else:
            if st.get("source") not in ("custom", "licensed", "owned", "platform_library"):
                out.append({"code": "FORMAT_SOUNDTRACK_SOURCE", "severity": "error", "message": "soundtrack.source must be custom | licensed | owned | platform_library"})
            if st.get("rights_status") not in ("owned", "licensed", "cleared"):
                out.append({"code": "FORMAT_SOUNDTRACK_RIGHTS", "severity": "warning", "message": f"soundtrack rights_status is '{st.get('rights_status')}'; render may proceed but publish needs owned/licensed/cleared"})
            if not st.get("bpm") and not st.get("beat_times_s"):
                out.append({"code": "FORMAT_SOUNDTRACK_TIMING", "severity": "warning", "message": "soundtrack has no bpm or beat_times_s; picture cannot be timed to the track"})
            dur = max([float(s.get("end_s", 0)) for s in scenes] or [0])
            bad = [b for b in (st.get("beat_times_s") or []) if not (0 <= float(b) <= dur)]
            if bad:
                out.append({"code": "FORMAT_SOUNDTRACK_BEATS_RANGE", "severity": "error", "message": f"beat times outside the clip: {bad}"})
        if dialogue and not all(str(d.get("speaker", "")).lower().startswith(("vo", "narrat")) or not d.get("on_camera", True) for d in dialogue):
            out.append({"code": "FORMAT_MUSIC_ONCAMERA_SPEECH", "severity": "warning", "message": "music_driven with on-camera speech: generation audio is off, so lips would move with no sound; move lines to captions or VO"})
    reuse = pf.get("continuity_reuse") or {}
    kinds = {r.get("kind"): r for r in packet.get("asset_rights", [])}
    if reuse.get("voice") == "same" and "voice" not in kinds:
        out.append({"code": "FORMAT_REUSE_VOICE_ASSET", "severity": "error", "message": "continuity_reuse.voice=same but no voice asset declared"})
    if reuse.get("location") == "same" and "location_still" not in kinds:
        out.append({"code": "FORMAT_REUSE_LOCATION_ASSET", "severity": "error", "message": "continuity_reuse.location=same but no location_still asset declared"})
    return out
