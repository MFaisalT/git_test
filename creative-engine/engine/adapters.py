"""Tool adapters. Map packet fields to verified native controls, manual steps, or explicit gaps.

Verified 2026-10-07 through the Higgsfield MCP server (models_explore, read-only):
  generate_video params: model, prompt (free text), duration, aspect_ratio, resolution, generate_audio,
  medias[{value, role}], mode, bitrate_mode, genre (seedance 2.0), sound (kling), get_cost, use_unlim.
Internal packet JSON is NOT a native Higgsfield payload; prompt_text below is the only creative control.
A dry run produces a checked plan and adapter requests. It never submits a job.
"""
from __future__ import annotations

from .validators import TOOL_LIMITS
from .routing import asset_requests, quote_for, route_video_unit
from .physics import compact_prompt

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


def build_prompt_text(packet: dict, scenes: list[dict], bible: dict | None) -> str:
    """Compose a free-text prompt in the house order; this IS the payload the tool accepts."""
    b = packet["brief"]
    cont = packet["continuity"]
    char = (bible or {}).get("character", {})
    am = (packet.get("production_format") or {}).get("audio_mode")
    silent = b.get("format") == "silent_gag" or am in ("silent_ambience", "text_over_broll", "music_driven")
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
        if "cut" in str(s.get("transition_out", "")).lower():
            flush()  # any cut between scenes ends a generation unit; one hard cut inside a clip must be declared via cuts_inside_clip
    flush()
    # merge a too-short unit into its predecessor only if that keeps the predecessor at <=1 internal cut
    out_units = []
    for u in units:
        dur = u[-1]["end_s"] - u[0]["start_s"]
        if out_units and dur < 4 and sum(1 for sc in out_units[-1][:-1] if "cut" in str(sc.get("transition_out", "")).lower()) == 0:
            out_units[-1].extend(u)
        else:
            out_units.append(u)
    plan_units = []
    needs_driving = any(r["kind"] == "driving_footage" for r in packet.get("asset_rights", []))
    pf = packet.get("production_format") or {}
    audio_mode = pf.get("audio_mode") or ("silent_ambience" if packet["brief"].get("format") == "silent_gag" else "on_camera_dialogue")
    for i, u in enumerate(out_units, 1):
        dur = round(u[-1]["end_s"] - u[0]["start_s"], 1)
        budget = str((packet.get("brief") or {}).get("render_tier", "")).lower() == "draft_mini"  # cost-capped test render requested by the brief
        # Owner inspection 2026-10-08 (Uncle Verdict v3): Seedance 2.0 Mini rendered both prop states at once, invented text and duplicate
        # props, dropped a passer-by mid-shot and repeated the last word; Seedance 2.5 draft held the cut-staged state change.
        # So Mini is kept only for units with no dialogue and no handled props; everything else uses Seedance 2.5 (draft 480p for tests).
        from .physics import HELD_PROPS
        handled = any(any(h in str(s.get("physical_beat") or s.get("action") or "").lower() for h in HELD_PROPS) for s in u)
        speaks = any(s.get("dialogue") for s in u)
        if budget and (handled or speaks):
            budget = False
        route = route_video_unit(pf, dur, audio_mode, needs_driving, identity_critical=True, budget_mode=budget, handles_props=handled)
        model = route["model"]
        lim = TOOL_LIMITS[model]
        controls = {"duration": max(lim["min_s"], min(lim["max_s"], int(round(dur)))), "aspect_ratio": packet["export"]["aspect_ratio"] if packet["export"]["aspect_ratio"] in (lim["aspect"] or [packet["export"]["aspect_ratio"]]) else "9:16",
                    "resolution": "720p", "generate_audio": bool(route.get("generate_audio", True))}
        if route.get("mode"):
            controls["mode"] = route["mode"]
        if route.get("mode") == "video_extension":
            controls["extension_mode"] = "forward"
        if model == "hf_mult_motion_control":
            controls = {"resolution": "720p"}
        medias = []
        if "image_references" in lim["media_roles"]:
            reg = (bible or {}).get("approved_assets", {}) if isinstance(bible, dict) else {}
            char = reg.get("character_reference") or {}
            cand = (char.get("candidates") or [{}])[0].get("job_id")
            medias.append({"value": f"<media_id or job_id of approved character reference (asset {char.get('asset_id', 'char-ref')}{'; candidate job ' + cand if cand else ''})>", "role": "image_references"})
            if any(r["kind"] == "location_still" for r in packet.get("asset_rights", [])):
                medias.append({"value": "<media_id of approved location still>", "role": "image_references"})
            if (pf.get("continuity_reuse") or {}).get("voice") == "same" and "audio_references" in lim["media_roles"] and audio_mode not in ("silent_ambience", "text_over_broll", "music_driven"):
                medias.append({"value": f"<media_id of approved voice asset {((reg.get('voice') or {}).get('asset_id') or 'voice-ref')}>", "role": "audio_references"})
        elif "start_image" in lim["media_roles"]:
            medias.append({"value": "<media_id of approved first-frame still>", "role": "start_image"})
        if model == "hf_mult_motion_control":
            medias.append({"value": "<media_id of OWNED/LICENSED driving footage>", "role": "video_references"})
        if route.get("mode") == "video_extension":
            medias.append({"value": "<job_id of the approved previous clip>", "role": "video_references"})
        manual = ["Upload approved reference stills via media_upload (owner action; upload requires approval).",
                  "Burn captions/on-screen text in edit.", "Add licensed music in edit if any.",
                  "Assemble generation units with hard cuts in edit; verify total duration and loop.",
                  "Run get_cost:true preflight and record quote before any submit; submit only after render_approved and credit_cap."]
        gaps = ["No fps/container control; inspect exported file.", "Lip-sync and exact SFX timing are not controllable; inspect output.",
                "Lens is prompt language only."]
        if dur > lim["max_s"] or dur < lim["min_s"]:
            gaps.append(f"unit duration {dur}s outside {model} range {lim['min_s']}-{lim['max_s']}s; re-split scenes")
        if route.get("status") == "gap":
            gaps.append("Cinema Studio 4.0 native camera/lighting controls need creative-control ids not retrieved in this build; pass as prompt text meanwhile")
        est = quote_for(model, controls.get("duration", int(round(dur))), "720p")
        draft_est = quote_for(model, controls.get("duration", int(round(dur))), "480p-draft")
        _cp = compact_prompt(packet, u, bible, return_meta=True)
        if audio_mode == "music_driven":
            manual = list(manual) + ["Lay the soundtrack in the edit (never generated by the video model); align picture accents to production_format.soundtrack beat times; confirm soundtrack rights before publish."]
        plan_units.append({
            "generation_unit": f"U{i}", "scene_ids": [s["scene_id"] for s in u], "model": model, "routing": {k: route.get(k) for k in ("why", "status", "fallback", "optimisation") if route.get(k)},
            "controls": controls, "prompt_text": (_cp[0] if _cp else build_prompt_text(packet, u, bible)), "prompt_style": ("compact_physics_first" if _cp else "dense_legacy"), "prompt_budget": (_cp[1] if _cp else None), "prompt_text_full": build_prompt_text(packet, u, bible), "medias": medias,
            "manual_steps": manual, "gaps": gaps,
            "estimated_credits": est, "estimated_credits_draft": draft_est,
            "quote_source": "generate_video get_cost preflights 2026-10-07 (9:16/720p), linearly scaled by duration; quotes, not measured completed-output costs; retakes multiply",
        })
    return {"adapter": "higgsfield-mcp/generate_video + generate_image", "verified_on": "2026-10-07", "units": plan_units,
            "asset_requests": asset_requests(packet, bible or {}, nb2_testing=False),
            "notes": "DRY RUN. No job submitted. prompt_text is free text, the only creative payload the tool accepts; internal JSON is not a native format. Field map: " +
                     "; ".join(f"{k}->{v[0]}" for k, v in FIELD_MAP.items())}
