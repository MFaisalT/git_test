"""Modular, versioned flow:
brief+constraints -> research check -> premises -> hooks -> script+storyboard -> adapter plan -> export -> QA -> learning loop.
Each LLM stage is validated; repair is bounded (default 2). Missing evidence/approvals are never invented.
"""
from __future__ import annotations

import json
import os
import time
from typing import Any

from . import ENGINE_VERSION
from .adapters import plan as adapter_plan
from .prompts import render_stage, repair_prompt
from .providers import Completion, PendingResponse, parse_json_object
from .repetition import compare, fingerprint
from .render import storyboard_md
from .store import Store, now_iso, sha256_json
from .trends import render_for_prompt, select_relevant, staleness_findings
from .formats import catalogue_text, diversity_findings, realisation_findings, recent_formats
from .validators import (Report, validate_all, validate_continuity, validate_direction, validate_rights, validate_selection, validate_timing)

QUOTES_2026_10_07 = {"seedance_2_0_mini": 8, "seedance_2_5": 56}  # 8 s / 720p / 9:16 preflight quotes, not measured costs


class StageFailure(Exception):
    pass


def _stage_check(stage: str, out: dict, brief: dict, bible: dict | None = None, context: dict | None = None) -> Report:
    rep = Report()
    if stage == "premises":
        ps = out.get("premises", [])
        if len(ps) < 5:
            rep.error("PREMISE_COUNT", f"need 5 premises, got {len(ps)}")
        for p in ps:
            for k in ("id", "logline", "audience_emotion", "character_desire", "obstacle", "escalation", "surprise", "payoff", "structure", "why_send_it"):
                if not str(p.get(k, "")).strip():
                    rep.error("PREMISE_FIELD", f"{p.get('id')} missing {k}")
        ids = [p.get("id") for p in ps]
        if len(set(ids)) != len(ids):
            rep.error("PREMISE_DUP_ID", "duplicate premise ids")
        fixed = brief.get("production_format") or {}
        archs, modes = set(), set()
        for p in ps:
            pf = p.get("production_format") or {}
            for k in ("shot_architecture", "audio_mode", "continuity_reuse", "rationale"):
                if not pf.get(k):
                    rep.error("PREMISE_FORMAT", f"{p.get('id')} production_format.{k} missing")
            for k in ("shot_architecture", "audio_mode"):
                if fixed.get(k) and pf.get(k) and pf[k] != fixed[k]:
                    rep.error("PREMISE_FORMAT_FIXED", f"{p.get('id')} ignores brief-fixed {k}={fixed[k]}")
            archs.add(pf.get("shot_architecture")); modes.add(pf.get("audio_mode"))
        if not fixed.get("shot_architecture") and len(archs - {None}) < 3:
            rep.error("PREMISE_FORMAT_VARIETY", f"premises use only {len(archs - {None})} shot architectures; need >=3 when open")
        if not fixed.get("audio_mode") and len(modes - {None}) < 2:
            rep.error("PREMISE_FORMAT_VARIETY", f"premises use only {len(modes - {None})} audio modes; need >=2 when open")
        if not out.get("ranking"):
            rep.error("PREMISE_RANKING", "ranking missing")
    elif stage == "hooks":
        hs = out.get("hook_variants", [])
        if len(hs) < 3:
            rep.error("HOOK_COUNT", f"need >=3 hooks, got {len(hs)}")
        sel = out.get("selected", {})
        if not sel.get("premise_id") or not sel.get("hook_id"):
            rep.error("HOOK_SELECT", "selected premise/hook missing")
        if brief.get("format") == "silent_gag":
            for h in hs:
                if '"' in h.get("first_line_or_action", "") or "says" in h.get("first_line_or_action", "").lower():
                    rep.warn("HOOK_SILENT_LINE", f"{h.get('id')} looks like a spoken line in a silent brief")
    elif stage == "script_storyboard":
        shell = {"brief": brief, "script": out.get("script", {}), "scenes": out.get("scenes", []), "continuity": out.get("continuity", {}),
                 "asset_rights": out.get("asset_rights", []), "export": out.get("export", {}), "tool_mapping": {"units": []}, "status": "draft",
                 "premises": [], "hook_variants": [], "selected": {}}
        validate_timing(shell, rep); validate_direction(shell, rep); validate_rights(shell, rep); validate_continuity(shell, bible, rep)
        from .formats import realisation_findings as _rf
        from .adapters import plan as _plan
        pf = (context or {}).get("production_format") or {}
        if pf.get("shot_architecture"):
            try:
                shell["tool_mapping"] = _plan(dict(shell, export=out.get("export", {"aspect_ratio": "9:16"}), continuity=out.get("continuity", {})), bible)
            except Exception:
                shell["tool_mapping"] = {"units": []}
            for f in _rf(pf, shell):
                (rep.error if f["severity"] == "error" else rep.warn)(f["code"], f["message"])
        funcs = [b.get("function") for b in (out.get("script") or {}).get("beats", [])]
        need = "turn" if brief.get("format") == "serial_cliffhanger" else "payoff"
        if "hook" not in funcs or need not in funcs:
            rep.error("SCRIPT_BEATS", f"script beats need 'hook' and '{need}' for format {brief.get('format')}")
        rep.findings = [f for f in rep.findings if f.code not in ("TOOL_UNMAPPED_SCENES",)]
        for k in ("identity_anchors", "costume", "props", "notes"):
            if k not in (out.get("continuity") or {}):
                rep.error("CONTINUITY_FIELD", f"continuity.{k} missing")
        for k in ("aspect_ratio", "resolution", "fps", "container", "max_duration_s", "edit_plan"):
            if k not in (out.get("export") or {}):
                rep.error("EXPORT_FIELD", f"export.{k} missing")
    return rep


class Pipeline:
    def __init__(self, store: Store, project: str, provider, max_repairs: int = 2, demos_k: int = 2, requested_model: str = "sonnet", effort: str = "medium"):
        self.store, self.project, self.provider = store, project, provider
        self.max_repairs, self.demos_k = max_repairs, demos_k
        self.requested_model, self.effort = requested_model, effort

    # -- state
    def _state_path(self, packet_id):
        return os.path.join(self.store.episode_dir(self.project, packet_id, create=True), "state.json")

    def _load_state(self, packet_id) -> dict:
        p = self._state_path(packet_id)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                return json.load(fh)
        return {"stages": {}, "log": [], "demos": []}

    def _save_state(self, packet_id, st):
        Store._write_json(self._state_path(packet_id), st)

    # -- one stage with bounded repair
    def _run_stage(self, stage: str, packet_id: str, brief: dict, bible: dict, context: dict, history_fp: list[dict], st: dict, trends_text: str = "", formats: dict | None = None) -> dict:
        if stage in st["stages"]:
            return st["stages"][stage]
        prompt, demo_ids = render_stage(stage, brief, bible, context, history_fp, self.demos_k, trends_text, formats)
        st["demos"] = sorted(set(st["demos"]) | set(demo_ids))
        attempt = 0
        out: dict | None = None
        last_findings: list[dict] = []
        while attempt <= self.max_repairs:
            tag = f"{stage}-{attempt}"
            t0 = time.time()
            comp: Completion = self.provider.complete(prompt if attempt == 0 else repair_prompt(stage, out or {}, last_findings), tag)
            try:
                out = parse_json_object(comp.text)
            except (ValueError, json.JSONDecodeError) as e:
                last_findings = [{"code": "PARSE", "severity": "error", "message": str(e)}]
                st["log"].append({"stage": stage, "attempt": attempt, "result": "parse_error", "at": now_iso()})
                attempt += 1
                continue
            rep = _stage_check(stage, out, brief, bible, context)
            st["log"].append({"stage": stage, "attempt": attempt, "result": "ok" if rep.ok else "invalid", "errors": len(rep.errors),
                              "requested_model": comp.requested_model, "observed_model": comp.observed_model, "usage": comp.usage,
                              "provider": comp.provider, "latency_s": round(time.time() - t0, 2), "at": now_iso()})
            self._save_state(packet_id, st)
            if rep.ok:
                st["stages"][stage] = out
                self._save_state(packet_id, st)
                return out
            last_findings = [f.as_dict() for f in rep.findings]
            attempt += 1
        raise StageFailure(f"stage '{stage}' failed after {self.max_repairs} repair passes; last findings: {json.dumps(last_findings)[:1500]}")

    # -- full run (idempotent / resumable)
    def run(self, brief_id: str, bible_id: str, packet_id: str | None = None, bible_version: int | None = None) -> dict:
        brief = self.store.load_brief(self.project, brief_id)
        bible = self.store.load_bible(self.project, bible_id, bible_version)
        packet_id = packet_id or f"{brief_id}-{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}"
        st = self._load_state(packet_id)
        history = [p for p in self.store.list_packets(self.project) if p["packet_id"] != packet_id and p["status"] != "rejected"]
        history_fp = [dict(fingerprint(p), packet_id=p["packet_id"]) for p in history]
        ledger = self.store.read_ledger(self.project, "trends")
        fresh, stale = select_relevant(brief, ledger)
        trends_text = render_for_prompt(fresh, stale) if fresh or stale else ""
        # Record the trend ids at the moment the premises request is FIRST rendered and persist immediately.
        # A later ingest must never be retrofitted onto a request that was written before it.
        if "trends_used" not in st:
            st["trends_used"] = [e["trend_id"] for e in fresh]
            st["trends_snapshot_age_days"] = (min(__import__("engine.trends", fromlist=["age_days"]).age_days(e) for e in fresh) if fresh else None)
            self._save_state(packet_id, st)
        else:
            fresh = [e for e in ledger if e["trend_id"] in st["trends_used"]]
            trends_text = render_for_prompt(fresh, []) if fresh else ""
        trend_formats = [e for e in fresh if e.get("type") in ("format", "edit_move", "style")]
        formats = {"catalogue": catalogue_text(trend_formats), "fixed": brief.get("production_format") or {}, "recent": recent_formats(history)}
        try:
            prem = self._run_stage("premises", packet_id, brief, bible, {}, history_fp, st, trends_text, formats)
            hooks = self._run_stage("hooks", packet_id, brief, bible, {"premises": prem}, history_fp, st, trends_text, formats)
            sel_prem = next((x for x in prem["premises"] if x["id"] == hooks["selected"]["premise_id"]), {})
            formats["selected"] = sel_prem.get("production_format") or formats["fixed"] or {"note": "no format declared; realise the brief literally"}
            ss = self._run_stage("script_storyboard", packet_id, brief, bible, {"premises": prem, "hooks": hooks, "production_format": formats["selected"]}, history_fp, st, "", formats)
        except PendingResponse as e:
            self._save_state(packet_id, st)
            raise
        packet = self._assemble(packet_id, brief, bible, prem, hooks, ss, st, history)
        # creative QA is a separate subjective stage; deterministic gates decide status, QA only annotates
        try:
            qa = self._run_stage("qa_review", packet_id, brief, bible, {"packet": {k: packet[k] for k in ("brief", "selected", "premises", "script", "scenes", "continuity", "growth_hypotheses")}}, [], st)
            packet["qa"]["creative"] = qa
        except PendingResponse:
            self._save_state(packet_id, st)
            self.store.save_packet(self.project, packet)
            raise
        self._finalise(packet, bible)
        return packet

    def _assemble(self, packet_id, brief, bible, prem, hooks, ss, st, history) -> dict:
        provider_name = getattr(self.provider, "name", "manual")
        packet = {
            "packet_version": "1.0", "packet_id": packet_id, "status": "draft",
            "brief": {k: brief[k] for k in brief if k in ("brief_id", "title", "project", "bible_ref", "format", "platform", "duration_target_s", "language", "objective", "constraints", "commercial", "negative_constraints")},
            "bible_version": {"bible_id": bible["bible_id"], "version": bible["version"], "sha256": sha256_json(bible)},
            "evidence": ss.get("evidence", []),
            "premises": prem["premises"], "hook_variants": hooks["hook_variants"], "selected": hooks["selected"],
            "script": ss["script"], "scenes": ss["scenes"], "continuity": ss["continuity"], "asset_rights": ss.get("asset_rights", []),
            "tool_mapping": {"adapter": "", "verified_on": "", "units": []},
            "approval": {"render_approved": False, "spend_approved": False, "publish_approved": False, "approved_by": "", "approved_at": "", "credit_cap": None},
            "export": ss["export"], "qa": {"deterministic": {}, "creative": {}, "repetition": {}, "render_inspection": None},
            "growth_hypotheses": ss.get("growth_hypotheses", []),
            "provenance": {"generated_at": now_iso(), "provider": provider_name, "requested_model": self.requested_model,
                           "observed_model": next((l.get("observed_model") for l in reversed(st["log"]) if l.get("observed_model")), "not independently observable"),
                           "effort": self.effort, "demonstrations_used": st["demos"], "trends_used": st.get("trends_used", []), "trends_snapshot_age_days": st.get("trends_snapshot_age_days"), "stage_log": st["log"],
                           "repair_passes": sum(1 for l in st["log"] if l.get("attempt", 0) > 0), "engine_version": ENGINE_VERSION},
            "negative_constraints": list(brief.get("negative_constraints", [])) + list(bible.get("do_not", [])),
        }
        sel_prem = next((x for x in prem["premises"] if x["id"] == hooks["selected"]["premise_id"]), {})
        pf = dict(sel_prem.get("production_format") or {})
        if pf:
            pf.setdefault("chosen_by", "brief" if (brief.get("production_format") or {}).get("shot_architecture") else "engine")
            packet["production_format"] = pf
        packet["tool_mapping"] = adapter_plan(packet, bible, QUOTES_2026_10_07)
        packet["qa"]["repetition"] = compare(packet, history)
        return packet

    def _finalise(self, packet: dict, bible: dict) -> None:
        rep = validate_all(packet, bible)
        if packet.get("production_format"):
            hist = [p for p in self.store.list_packets(self.project) if p["packet_id"] != packet["packet_id"] and p["status"] != "rejected"]
            for f in diversity_findings(packet["production_format"], hist, packet["brief"].get("production_format") or {}) + realisation_findings(packet["production_format"], packet):
                (rep.error if f["severity"] == "error" else rep.warn)(f["code"], f["message"])
        for f in staleness_findings(packet["provenance"].get("trends_used", []), self.store.read_ledger(self.project, "trends")):
            (rep.error if f["severity"] == "error" else rep.warn)(f["code"], f["message"])
        packet["qa"]["deterministic"] = rep.as_dict()
        if rep.ok and packet["provenance"]["provider"] != "fixture":
            packet["status"] = "planning-ready; render unverified"
        else:
            packet["status"] = "draft"
        self.store.save_packet(self.project, packet)
        d = self.store.episode_dir(self.project, packet["packet_id"])
        Store.write_text(os.path.join(d, "storyboard.md"), storyboard_md(packet))
        Store._write_json(os.path.join(d, "adapter_plan.json"), packet["tool_mapping"])
        self.store.append(self.project, "runs", {"packet_id": packet["packet_id"], "status": packet["status"], "errors": rep.as_dict()["error_count"],
                                                 "provider": packet["provenance"]["provider"], "requested_model": packet["provenance"]["requested_model"],
                                                 "observed_model": packet["provenance"]["observed_model"], "repair_passes": packet["provenance"]["repair_passes"]})

    # -- learning loop
    def learn(self, packet_id: str, outcome: dict) -> None:
        """Record observed outcomes (owner-supplied metrics) and creative decisions as dated evidence; never rewrite history."""
        self.store.append(self.project, "evidence", {"packet_id": packet_id, "type": "outcome", **outcome})
        self.store.append(self.project, "decisions", {"packet_id": packet_id, "type": "learning", "note": outcome.get("lesson", "")})
