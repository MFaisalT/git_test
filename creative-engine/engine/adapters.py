"""Tool adapters. Map packet fields to verified native controls, manual steps, or explicit gaps.

Verified 2026-10-07 through the Higgsfield MCP server (models_explore, read-only):
  generate_video params: model, prompt (free text), duration, aspect_ratio, resolution, generate_audio,
  medias[{value, role}], mode, bitrate_mode, genre (seedance 2.0), sound (kling), get_cost, use_unlim.
Internal packet JSON is NOT a native Higgsfield payload; prompt_text below is the only creative control.
A dry run produces a checked plan and adapter requests. It never submits a job.
"""
from __future__ import annotations

from .validators import TOOL_LIMITS

FIELD_MAP = {
    # packet field -> ("native" | "prompt_text" | "manual" | "gap", note)
    "scene.action": ("prompt_text", "described in prompt"),
    "scene.performance": ("prompt_text", "ACTING TASK block in prompt; not a separate control"),
    "scene.microexpression": ("prompt_text", "prompt only; no facial-rig control"),
    "scene.camera.shot": ("prompt_text", "prompt only"),
    "scene.camera.lens": ("prompt_text", "no numeric lens control; lens language in prompt is a hint"),
    "scene.camera.movement": ("prompt_text", "prompt only; multi-shot only on kling3_0"),
    "scene.lighting": ("prompt_text", "RELIGHT block in prompt"),
    "scene.environment": ("prompt_text", "prompt + optional location still as image_references"),
    "scene.sound.ambience": ("native+prompt_text", "generate_audio=true + described ambience; exact SFX not controllable"),
    "scene.sound.music": ("manual", "add licensed music in edit; never rely on generated music for rights"),
    "scene.dialogue": ("prompt_text", "quoted verbatim in prompt; lip-sync quality unverified; audio_references role exists on seedance for a pre-generated voice"),
    "scene.captions": ("manual", "burn in edit; models render unreliable text"),
    "scene.transition_out": ("manual", "cuts between generation units happen in edit"),
    "scene.cuts_inside_clip": ("prompt_text", "<=1 hard cut per clip described in prompt"),
    "continuity.identity_anchors": ("native+prompt_text", "image_references character still + verbatim anchor wording"),
    "duration": ("native", "duration (model range)"),
    "aspect_ratio": ("native", "aspect_ratio (9:16 for vertical)"),
    "resolution": ("native", "resolution"),
    "export.fps": ("gap", "no fps control exposed; verify on exported file"),
    "export.container": ("gap", "export container not controllable; inspect downloaded file"),
    "disclosure": ("manual", "platform branded-content tool + caption/spoken line; outside generation"),
}


def _clamp_model(duration: float, needs_audio: bool, driving_video: bool) -> str:
    if driving_video:
        return "hf_mult_motion_control"
    if duration <= 15:
        return "seedance_2_0_mini"  # cheapest adequate (quoted 8 credits/8s/720p on 2026-10-07; quote, not measured cost)
    return "seedance_2_5"


def build_prompt_text(packet: dict, scenes: list[dict], bible: dict | None) -> str:
    """Compose a free-text prompt in the house order; this IS the payload the tool accepts."""
    b = packet["brief"]
    cont = packet["continuity"]
    char = (bible or {}).get("character", {})
    silent = b.get("format") == "silent_gag"
    lines = ["TOP PRIORITY (read first):"]
    lines.append("1. Face and identity match @image1 100% for the entire take; identity reference ONLY, never its lighting.")
    lines.append("2. " + ("NO dialogue anywhere; ambient SFX and foley only." if silent else "Speak ONLY the quoted lines, in English, lips still when no line is spoken."))
    lines.append("3. Props exist from frame one and never appear, disappear or change design: " + ", ".join(cont.get("props", [])) + ".")
    lines.append("4. Never staged, never stiff, never puppet-like; the comedy is in disproportion, not mugging.")
    lines.append("5. No readable brand text, logos or signage anywhere in frame.")
    lines.append("=== REFERENCE KEY === @image1 character reference; @image2 location still (scene reference only).")
    lines.append(f"CHARACTER: {cont.get('identity_anchors')} Costume: {cont.get('costume')}. Register: {char.get('performance_register', '')}")
    lines.append("CRITICAL - RELIGHT: discard the reference's lighting; relight to the scene as described per shot, with true contact shadows; must look physically present, never a cut-out.")
    for s in scenes:
        cam = s["camera"]
        snd = s["sound"]
        lines.append(f"--- {s['scene_id']} ({s['start_s']:.1f}-{s['end_s']:.1f}s) ---")
        lines.append(f"Location: {s['location']}. Environment: {s['environment']}")
        lines.append(f"Action: {s['action']}")
        lines.append(f"Performance: {s['performance']} Micro-expression: {s['microexpression']}")
        lines.append(f"Camera: {cam['shot']}; lens feel {cam['lens']}; movement {cam['movement']}" + (f"; rig {cam.get('rig')}" if cam.get("rig") else ""))
        lines.append(f"Lighting: {s['lighting']}")
        lines.append(f"Audio: ambience {snd['ambience']}; foley: {', '.join(snd.get('foley', []))}" + ("; no music" if not snd.get("music") or snd.get("music", "").lower() in ("none", "no music") else "; music added in post, do not generate music"))
        for d in s.get("dialogue", []) or []:
            lines.append(f"Dialogue ({d['speaker']}, {'on' if d.get('on_camera', True) else 'off'}-camera): \"{d['line']}\"" + (f" - {d['delivery']}" if d.get("delivery") else ""))
    lines.append("ON-SCREEN TEXT: none (added in post).")
    return "\n".join(lines)


def plan(packet: dict, bible: dict | None = None, quote_credits: dict | None = None) -> dict:
    """Group scenes into generation units and produce a dry-run adapter plan. No tool call is made."""
    scenes = sorted(packet["scenes"], key=lambda s: s["start_s"])
    units, cur = [], []
    def flush():
        if cur:
            units.append(list(cur)); cur.clear()
    for s in scenes:
        cur.append(s)
        if s.get("transition_out", "").lower().startswith("cut") or s.get("transition_out", "").lower() in ("hard cut", "cut to", "cut"):
            flush()
    flush()
    # merge tiny trailing units into previous when under min duration
    out_units = []
    for u in units:
        dur = u[-1]["end_s"] - u[0]["start_s"]
        if out_units and dur < 4:
            out_units[-1].extend(u)
        else:
            out_units.append(u)
    plan_units = []
    needs_driving = any(r["kind"] == "driving_footage" for r in packet.get("asset_rights", []))
    for i, u in enumerate(out_units, 1):
        dur = round(u[-1]["end_s"] - u[0]["start_s"], 1)
        model = _clamp_model(dur, True, needs_driving)
        lim = TOOL_LIMITS[model]
        controls = {"duration": max(lim["min_s"], min(lim["max_s"], int(round(dur)))), "aspect_ratio": packet["export"]["aspect_ratio"],
                    "resolution": "720p", "generate_audio": packet["brief"].get("format") != "silent_gag" or True}
        if model == "hf_mult_motion_control":
            controls = {"resolution": "720p"}
        medias = [{"value": "<media_id of approved character reference>", "role": "image_references"}]
        if any(r["kind"] == "location_still" for r in packet.get("asset_rights", [])):
            medias.append({"value": "<media_id of approved location still>", "role": "image_references"})
        if model == "hf_mult_motion_control":
            medias.append({"value": "<media_id of OWNED/LICENSED driving footage>", "role": "video_references"})
        manual = ["Upload approved reference stills via media_upload (owner action; upload requires approval).",
                  "Burn captions/on-screen text in edit.", "Add licensed music in edit if any.",
                  "Assemble generation units with hard cuts in edit; verify total duration and loop.",
                  "Run get_cost:true preflight and record quote before any submit; submit only after render_approved and credit_cap."]
        gaps = ["No fps/container control; inspect exported file.", "Lip-sync and exact SFX timing are not controllable; inspect output.",
                "Lens is prompt language only."]
        if dur > lim["max_s"] or dur < lim["min_s"]:
            gaps.append(f"unit duration {dur}s outside {model} range {lim['min_s']}-{lim['max_s']}s; re-split scenes")
        plan_units.append({
            "generation_unit": f"U{i}", "scene_ids": [s["scene_id"] for s in u], "model": model,
            "controls": controls, "prompt_text": build_prompt_text(packet, u, bible), "medias": medias,
            "manual_steps": manual, "gaps": gaps,
            "estimated_credits": (quote_credits or {}).get(model), "quote_source": "cost-quotes.json 2026-10-07 (8s/720p: mini 8, seedance_2_5 56); not a measured completed-output cost" if quote_credits else "no quote captured for this run",
        })
    return {"adapter": "higgsfield-mcp/generate_video", "verified_on": "2026-10-07", "units": plan_units,
            "notes": "DRY RUN. No job submitted. prompt_text is free text, the only creative payload the tool accepts; internal JSON is not a native format. Field map: " +
                     "; ".join(f"{k}->{v[0]}" for k, v in FIELD_MAP.items())}
