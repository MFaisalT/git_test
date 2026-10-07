"""Deterministic validators for episode packets.

These are algorithmic gates. They say nothing about creativity or virality;
they only establish that a packet is structurally complete, internally
consistent, feasible against verified tool controls, and that approval and
rights gates are respected.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from typing import Any

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "schema", "episode_packet.schema.json")

# Verified 2026-10-07 via Higgsfield MCP models_explore (read-only). See docs/TOOL-CAPABILITIES.md.
TOOL_LIMITS = {
    "seedance_2_5": {"min_s": 4, "max_s": 30, "aspect": ["auto", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"], "res": ["480p", "720p", "1080p"], "audio": True,
                     "media_roles": ["start_image", "end_image", "image_references", "video_references", "audio_references"]},
    "seedance_2_0_mini": {"min_s": 4, "max_s": 15, "aspect": ["auto", "16:9", "9:16", "4:3", "3:4", "1:1", "21:9"], "res": ["480p", "720p"], "audio": True,
                          "media_roles": ["start_image", "end_image", "image_references", "video_references", "audio_references"]},
    "kling3_0": {"min_s": 3, "max_s": 15, "aspect": ["16:9", "9:16", "1:1"], "res": ["std", "pro", "4k"], "audio": True, "media_roles": ["start_image", "end_image"]},
    "hf_mult_motion_control": {"min_s": 4, "max_s": 30, "aspect": [], "res": ["480p", "720p", "1080p"], "audio": False, "media_roles": ["image_references", "video_references"],
                               "requires_driving_video": True},
}
SUPPORTED_CONTROLS = {"model", "prompt", "duration", "aspect_ratio", "resolution", "generate_audio", "medias", "mode", "sound", "bitrate_mode", "genre"}
SPEECH_WPS_MAX = 3.3   # ~200 wpm brisk ceiling
SPEECH_WPS_MIN = 1.6   # below this, dialogue leaves dead air that must be deliberate
TIMING_TOLERANCE_S = 0.05


@dataclass
class Finding:
    code: str
    severity: str  # error | warning
    message: str
    path: str = ""

    def as_dict(self) -> dict:
        return {"code": self.code, "severity": self.severity, "message": self.message, "path": self.path}


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)

    def error(self, code, msg, path=""):
        self.findings.append(Finding(code, "error", msg, path))

    def warn(self, code, msg, path=""):
        self.findings.append(Finding(code, "warning", msg, path))

    @property
    def errors(self):
        return [f for f in self.findings if f.severity == "error"]

    @property
    def ok(self):
        return not self.errors

    def as_dict(self):
        return {"ok": self.ok, "error_count": len(self.errors), "warning_count": len(self.findings) - len(self.errors),
                "findings": [f.as_dict() for f in self.findings]}


def load_schema() -> dict:
    with open(SCHEMA_PATH, encoding="utf-8") as fh:
        return json.load(fh)


# --- 1. Schema -------------------------------------------------------------

def _walk(schema: dict, inst: Any, path: str, rep: Report, root: dict):
    """Minimal JSON-Schema subset walker (type, required, enum, const, min/max, items, additionalProperties)."""
    t = schema.get("type")
    if "const" in schema and inst != schema["const"]:
        rep.error("SCHEMA_CONST", f"expected {schema['const']!r}, got {inst!r}", path)
        return
    if "enum" in schema and inst not in schema["enum"]:
        rep.error("SCHEMA_ENUM", f"{inst!r} not in {schema['enum']}", path)
        return
    types = t if isinstance(t, list) else ([t] if t else [])
    if types:
        pymap = {"object": dict, "array": list, "string": str, "number": (int, float), "integer": int, "boolean": bool, "null": type(None)}
        ok = any(isinstance(inst, pymap[x]) and not (x in ("number", "integer") and isinstance(inst, bool)) for x in types)
        if not ok:
            rep.error("SCHEMA_TYPE", f"expected {types}, got {type(inst).__name__}", path)
            return
    if isinstance(inst, dict):
        for req in schema.get("required", []):
            if req not in inst:
                rep.error("SCHEMA_REQUIRED", f"missing required field '{req}'", path)
        props = schema.get("properties", {})
        for k, v in inst.items():
            if k in props:
                _walk(props[k], v, f"{path}/{k}", rep, root)
            elif schema.get("additionalProperties") is False:
                rep.error("SCHEMA_ADDITIONAL", f"unexpected field '{k}'", path)
    if isinstance(inst, list):
        if "minItems" in schema and len(inst) < schema["minItems"]:
            rep.error("SCHEMA_MINITEMS", f"needs at least {schema['minItems']} items, has {len(inst)}", path)
        if "items" in schema:
            for i, it in enumerate(inst):
                _walk(schema["items"], it, f"{path}[{i}]", rep, root)
    if isinstance(inst, str):
        if "minLength" in schema and len(inst) < schema["minLength"]:
            rep.error("SCHEMA_MINLENGTH", "string too short", path)
    if isinstance(inst, (int, float)) and not isinstance(inst, bool):
        if "minimum" in schema and inst < schema["minimum"]:
            rep.error("SCHEMA_MIN", f"{inst} < {schema['minimum']}", path)
        if "maximum" in schema and inst > schema["maximum"]:
            rep.error("SCHEMA_MAX", f"{inst} > {schema['maximum']}", path)


def validate_schema(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    schema = load_schema()
    try:  # prefer the full library when present; fall back to the subset walker
        import jsonschema  # type: ignore
        v = jsonschema.Draft202012Validator(schema)
        for e in sorted(v.iter_errors(packet), key=lambda e: list(e.path)):
            rep.error("SCHEMA", e.message, "/" + "/".join(str(p) for p in e.path))
    except ImportError:
        _walk(schema, packet, "", rep, schema)
    return rep


# --- 2. Timing ---------------------------------------------------------------

def _word_count(text: str) -> int:
    return len([w for w in re.split(r"\s+", text.strip()) if w])


def _dialogue(s: dict, rep: Report, path: str) -> list[dict]:
    """Return dialogue entries that are dicts; record malformed entries instead of crashing."""
    out = []
    for d in s.get("dialogue", []) or []:
        if isinstance(d, dict):
            out.append(d)
        else:
            rep.error("DIALOGUE_SHAPE", f"dialogue entry is {type(d).__name__}, expected object with speaker/line", path)
    return out


def validate_timing(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    scenes = sorted(packet.get("scenes", []), key=lambda s: s.get("start_s", 0))
    if not scenes:
        rep.error("TIMING_NO_SCENES", "packet has no scenes")
        return rep
    target = float(packet["brief"]["duration_target_s"])
    total = 0.0
    prev_end = None
    for s in scenes:
        st, en = float(s["start_s"]), float(s["end_s"])
        p = f"/scenes/{s.get('scene_id')}"
        if en <= st:
            rep.error("TIMING_NONPOSITIVE", f"end_s {en} <= start_s {st}", p)
        if prev_end is not None:
            if st > prev_end + TIMING_TOLERANCE_S:
                rep.error("TIMING_GAP", f"gap of {st - prev_end:.2f}s before scene", p)
            elif st < prev_end - TIMING_TOLERANCE_S:
                rep.error("TIMING_OVERLAP", f"overlaps previous scene by {prev_end - st:.2f}s", p)
        prev_end = en
        total = max(total, en)
        # speech feasibility
        words = sum(_word_count(d.get("line", "")) for d in _dialogue(s, rep, p))
        dur = max(en - st, 1e-6)
        if words:
            wps = words / dur
            if wps > SPEECH_WPS_MAX:
                rep.error("SPEECH_TOO_FAST", f"{words} words in {dur:.1f}s = {wps:.1f} w/s (> {SPEECH_WPS_MAX})", p)
        if s.get("cuts_inside_clip", 0) > 1:
            rep.error("TOO_MANY_CUTS", "more than one cut inside a single generated clip", p)
    if scenes[0]["start_s"] > TIMING_TOLERANCE_S:
        rep.error("TIMING_LATE_START", f"first scene starts at {scenes[0]['start_s']}s, not 0")
    if abs(total - target) > max(1.0, 0.1 * target):
        rep.error("TIMING_TOTAL", f"scenes total {total:.1f}s vs brief target {target}s (tolerance max(1s,10%))")
    fmt = packet["brief"].get("format")
    if fmt == "silent_gag":
        spoken = [d for s in scenes for d in _dialogue(s, rep, "") if str(d.get("line", "")).strip()]
        spoken += [d for d in (packet.get("script", {}).get("dialogue") or []) if isinstance(d, dict) and str(d.get("line", "")).strip()]
        if spoken:
            rep.error("SILENT_HAS_DIALOGUE", f"silent_gag brief contains {len(spoken)} dialogue line(s)")
    return rep


# --- 3. Direction completeness ----------------------------------------------

VAGUE = {"", "tbd", "n/a", "none", "same", "-", "various", "standard"}


def validate_direction(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    for s in packet.get("scenes", []):
        p = f"/scenes/{s.get('scene_id')}"
        cam = s.get("camera", {}) or {}
        for k in ("shot", "lens", "movement"):
            if str(cam.get(k, "")).strip().lower() in VAGUE:
                rep.error("MISSING_CAMERA", f"camera.{k} missing or vague", p)
        snd = s.get("sound", {}) or {}
        if str(snd.get("ambience", "")).strip().lower() in VAGUE:
            rep.error("MISSING_AUDIO", "sound.ambience missing or vague", p)
        if not snd.get("foley"):
            rep.warn("THIN_AUDIO", "no foley listed; silent-feeling scenes often read as unfinished", p)
        for k in ("action", "performance", "microexpression", "lighting", "environment"):
            if str(s.get(k, "")).strip().lower() in VAGUE or len(str(s.get(k, ""))) < 12:
                rep.error("MISSING_DIRECTION", f"{k} missing or too thin", p)
        on_cam_speakers = {d.get("speaker") for d in _dialogue(s, rep, p) if d.get("on_camera", True)}
        if len(on_cam_speakers) > 1:
            rep.error("MULTI_SPEAKER_SHOT", f"{len(on_cam_speakers)} on-camera speakers in one scene; verified tools handle one reliably", p)
    return rep


# --- 4. Continuity -------------------------------------------------------------

def validate_continuity(packet: dict, bible: dict | None, rep: Report | None = None) -> Report:
    rep = rep or Report()
    cont = packet.get("continuity", {})
    if bible:
        anchors = bible.get("character", {}).get("identity_anchors", "")
        if anchors and anchors.split(",")[0].strip().lower() not in cont.get("identity_anchors", "").lower():
            rep.error("CONTINUITY_ANCHORS", "continuity.identity_anchors does not restate the bible's first identity anchor verbatim")
        creative_blob = json.dumps({k: packet.get(k) for k in ("script", "scenes", "premises", "hook_variants", "continuity")}).lower()
        for forbidden in bible.get("do_not", []):
            key = forbidden.lower()
            blob = creative_blob
            for tok in ("moustache", "white tunic", "bowl haircut"):
                if tok in key and tok in blob:
                    rep.error("BIBLE_DO_NOT", f"packet mentions forbidden identity token '{tok}'")
    def _words(t: str) -> set[str]:
        return set(re.findall(r"[a-z0-9]+", re.sub(r"\(.*?\)", " ", t.lower())))
    declared = [_words(p) for p in cont.get("props", [])]
    for s in packet.get("scenes", []):
        for prop in s.get("props_from_frame_one", []) or []:
            pw = _words(prop)
            # a used prop matches a declared prop when its words are a subset of the declared prop's words (parentheticals ignored)
            if not pw or not any(pw <= d for d in declared):
                rep.error("PROP_UNDECLARED", f"prop '{prop}' used in {s.get('scene_id')} but not in continuity.props", f"/scenes/{s.get('scene_id')}")
    costumes = {s.get("environment", "") for s in packet.get("scenes", [])}
    if cont.get("costume", "").strip().lower() in VAGUE:
        rep.error("CONTINUITY_COSTUME", "continuity.costume missing")
    return rep


# --- 5. Tool mapping ----------------------------------------------------------

def validate_tool_mapping(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    tm = packet.get("tool_mapping", {})
    scene_ids = {s["scene_id"] for s in packet.get("scenes", [])}
    scene_by_id = {s["scene_id"]: s for s in packet.get("scenes", [])}
    covered = set()
    for u in tm.get("units", []):
        p = f"/tool_mapping/units/{u.get('generation_unit')}"
        model = u.get("model")
        limits = TOOL_LIMITS.get(model)
        if not limits:
            rep.error("TOOL_UNKNOWN_MODEL", f"model '{model}' is not in the verified catalog", p)
            continue
        unknown = set(u.get("controls", {}).keys()) - SUPPORTED_CONTROLS
        if unknown:
            rep.error("TOOL_UNSUPPORTED_CONTROL", f"controls {sorted(unknown)} are not verified native controls; move to manual_steps or gaps", p)
        dur = sum(float(scene_by_id[sid]["end_s"]) - float(scene_by_id[sid]["start_s"]) for sid in u.get("scene_ids", []) if sid in scene_by_id)
        if dur and (dur < limits["min_s"] - TIMING_TOLERANCE_S or dur > limits["max_s"] + TIMING_TOLERANCE_S):
            rep.error("TOOL_DURATION", f"unit covers {dur:.1f}s; {model} supports {limits['min_s']}-{limits['max_s']}s", p)
        ar = u.get("controls", {}).get("aspect_ratio")
        if ar and limits["aspect"] and ar not in limits["aspect"]:
            rep.error("TOOL_ASPECT", f"aspect {ar} unsupported by {model}", p)
        res = u.get("controls", {}).get("resolution")
        if res and res not in limits["res"]:
            rep.error("TOOL_RESOLUTION", f"resolution {res} unsupported by {model}", p)
        for m in u.get("medias", []) or []:
            if m.get("role") not in limits["media_roles"]:
                rep.error("TOOL_MEDIA_ROLE", f"media role {m.get('role')} unsupported by {model}", p)
        if limits.get("requires_driving_video") and not any(m.get("role") == "video_references" for m in u.get("medias", []) or []):
            rep.error("TOOL_NEEDS_DRIVING_VIDEO", "motion transfer requires a video_references input (owned/licensed footage)", p)
        if not u.get("prompt_text", "").strip():
            rep.error("TOOL_EMPTY_PROMPT", "prompt_text is empty", p)
        if "json" in u.get("prompt_text", "").lower()[:40]:
            rep.warn("TOOL_JSON_IN_PROMPT", "prompt_text appears to embed JSON; Higgsfield prompt is free text, not a native JSON payload", p)
        for sid in u.get("scene_ids", []):
            if sid not in scene_ids:
                rep.error("TOOL_UNKNOWN_SCENE", f"scene {sid} not in packet", p)
            covered.add(sid)
    missing = scene_ids - covered
    if missing:
        rep.error("TOOL_UNMAPPED_SCENES", f"scenes without a generation unit or manual mapping: {sorted(missing)}")
    return rep


# --- 6. Rights and approval ---------------------------------------------------

def validate_rights(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    rights = packet.get("asset_rights", [])
    kinds = {r["kind"] for r in rights}
    if "character_reference" not in kinds:
        rep.error("RIGHTS_NO_CHARACTER_REF", "no character_reference asset declared")
    uses_music = any((s.get("sound", {}) or {}).get("music", "").strip().lower() not in VAGUE | {"no music"} for s in packet.get("scenes", []))
    if uses_music and "music" not in kinds:
        rep.error("RIGHTS_MUSIC_UNDECLARED", "scenes reference music but no music asset/rights entry exists")
    for u in packet.get("tool_mapping", {}).get("units", []):
        if u.get("model") == "hf_mult_motion_control" and "driving_footage" not in kinds:
            rep.error("RIGHTS_DRIVING_FOOTAGE", "motion transfer planned but no driving_footage rights entry")
    unresolved = [r["asset"] for r in rights if r["rights_status"] == "unresolved"]
    status = packet.get("status")
    if unresolved and status in ("approved-for-render", "rendered-unverified", "rendered-verified"):
        rep.error("RIGHTS_UNRESOLVED_AT_RENDER", f"unresolved rights {unresolved} but status is {status}")
    elif unresolved:
        rep.warn("RIGHTS_UNRESOLVED", f"unresolved rights: {unresolved} (acceptable while planning)")
    com = packet.get("brief", {}).get("commercial")
    if com:
        blob = (json.dumps(packet.get("script", {})) + json.dumps(packet.get("scenes", []))).lower()
        for phrase in ("i use", "i've used", "i tested", "changed my life", "it worked for me", "i love this", "i tried"):
            if phrase in blob:
                rep.error("COMMERCIAL_FIRSTHAND_CLAIM", f"fictional character implies firsthand experience: '{phrase}'")
        if not packet.get("script", {}).get("disclosure_line") and not packet.get("export", {}).get("disclosure_plan"):
            rep.error("COMMERCIAL_NO_DISCLOSURE", "commercial brief without disclosure_line or disclosure_plan")
        plan_blob = " ".join(packet.get("export", {}).get("disclosure_plan", []) or []).lower()
        if not any(k in plan_blob for k in ("paid partnership", "branded content", "platform tool", "partnership label", "paid-partnership")):
            rep.warn("COMMERCIAL_NO_PLATFORM_TOOL", "disclosure_plan does not name the platform paid-partnership/branded-content tool")
        allowed = [f.lower() for f in com.get("verified_facts", [])]
        for forb in com.get("forbidden_claims", []):
            if forb.lower() in blob:
                rep.error("COMMERCIAL_FORBIDDEN_CLAIM", f"forbidden claim topic '{forb}' appears in script/scenes")
    return rep


def validate_approval(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    ap = packet.get("approval", {})
    status = packet.get("status")
    if status in ("approved-for-render", "rendered-unverified", "rendered-verified"):
        if not ap.get("render_approved"):
            rep.error("APPROVAL_RENDER", f"status {status} requires approval.render_approved=true")
        if not ap.get("approved_by"):
            rep.error("APPROVAL_WHO", "approved_by missing")
        if ap.get("credit_cap") is None:
            rep.error("APPROVAL_CAP", "credit_cap must be set before render")
    if status == "rendered-verified":
        ri = packet.get("qa", {}).get("render_inspection")
        if not ri or not all(ri.get(k) for k in ("identity", "continuity", "timing", "audio", "artifacts", "readability", "music_rights", "tech_specs", "disclosure")):
            rep.error("RENDER_NOT_INSPECTED", "rendered-verified requires a complete render_inspection record")
    prov = packet.get("provenance", {})
    if prov.get("provider") == "fixture" and status != "draft":
        rep.error("FIXTURE_NOT_PLANNING_READY", "fixture-generated packets may only be 'draft'; they are plumbing tests, not creative output")
    return rep


# --- 7. Selection integrity ------------------------------------------------------

def validate_selection(packet: dict, rep: Report | None = None) -> Report:
    rep = rep or Report()
    pids = {p["id"] for p in packet.get("premises", [])}
    hids = {h["id"]: h for h in packet.get("hook_variants", [])}
    sel = packet.get("selected", {})
    if sel.get("premise_id") not in pids:
        rep.error("SELECT_PREMISE", "selected.premise_id not among premises")
    if sel.get("hook_id") not in hids:
        rep.error("SELECT_HOOK", "selected.hook_id not among hook_variants")
    elif hids[sel["hook_id"]]["premise_id"] != sel.get("premise_id"):
        rep.error("SELECT_MISMATCH", "selected hook belongs to a different premise")
    for h in hids.values():
        if h["premise_id"] not in pids:
            rep.error("HOOK_ORPHAN", f"hook {h['id']} references unknown premise {h['premise_id']}")
    funcs = [b["function"] for b in packet.get("script", {}).get("beats", [])]
    for need in ("hook", "payoff"):
        if need not in funcs:
            rep.error("SCRIPT_BEATS", f"script beats lack a '{need}' beat")
    return rep


def validate_all(packet: dict, bible: dict | None = None) -> Report:
    rep = Report()
    validate_schema(packet, rep)
    if rep.errors:
        return rep  # structure first; the rest assumes shape
    validate_timing(packet, rep)
    validate_direction(packet, rep)
    validate_continuity(packet, bible, rep)
    validate_tool_mapping(packet, rep)
    validate_rights(packet, rep)
    validate_approval(packet, rep)
    validate_selection(packet, rep)
    return rep
