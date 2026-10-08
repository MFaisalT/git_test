"""Filesystem persistence: projects, versioned bibles, episode history, decisions, evidence, outputs, approved assets.

Layout (under <root>/projects/<project>/):
  project.json
  bibles/<bible_id>.v<N>.json
  briefs/<brief_id>.json
  episodes/<packet_id>/packet.json | storyboard.md | adapter_plan.json | requests/ | responses/ | qa.json
  decisions.jsonl   evidence.jsonl   approved_assets.jsonl   runs.jsonl
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
from typing import Any


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "x"


def sha256_json(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


class Store:
    def __init__(self, root: str):
        self.root = os.path.abspath(root)
        os.makedirs(os.path.join(self.root, "projects"), exist_ok=True)

    # -- projects
    def project_dir(self, project: str, create=False) -> str:
        d = os.path.join(self.root, "projects", slug(project))
        if create:
            for sub in ("bibles", "briefs", "episodes"):
                os.makedirs(os.path.join(d, sub), exist_ok=True)
            pj = os.path.join(d, "project.json")
            if not os.path.exists(pj):
                self._write_json(pj, {"project": project, "created": now_iso(), "niche": "", "notes": ""})
        if not os.path.isdir(d):
            raise FileNotFoundError(f"project '{project}' not found at {d}")
        return d

    def list_projects(self) -> list[str]:
        p = os.path.join(self.root, "projects")
        return sorted(x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x)))

    # -- bibles (versioned, append-only)
    def save_bible(self, project: str, bible: dict, reason: str = "") -> dict:
        d = self.project_dir(project, create=True)
        bid = bible["bible_id"]
        existing = self.bible_versions(project, bid)
        if existing:  # voice lock: a locked voice never changes or disappears (owner rule 2026-10-08)
            from .voice import assert_voice_unchanged
            assert_voice_unchanged(self.load_bible(project, bid), bible)
        version = (max(existing) + 1) if existing else int(bible.get("version", 1))
        bible = dict(bible, version=version)
        bible.setdefault("provenance", {})
        bible["provenance"]["saved_at"] = now_iso()
        if reason:
            bible["provenance"]["bump_reason"] = reason
        self._write_json(os.path.join(d, "bibles", f"{bid}.v{version}.json"), bible)
        self.append(project, "decisions", {"type": "bible_version", "bible_id": bid, "version": version, "reason": reason})
        return bible

    def bible_versions(self, project: str, bible_id: str) -> list[int]:
        d = os.path.join(self.project_dir(project), "bibles")
        out = []
        for f in os.listdir(d):
            m = re.match(rf"{re.escape(bible_id)}\.v(\d+)\.json$", f)
            if m:
                out.append(int(m.group(1)))
        return sorted(out)

    def load_bible(self, project: str, bible_id: str, version: int | None = None) -> dict:
        vs = self.bible_versions(project, bible_id)
        if not vs:
            raise FileNotFoundError(f"bible {bible_id} not found in project {project}")
        v = version or vs[-1]
        return self._read_json(os.path.join(self.project_dir(project), "bibles", f"{bible_id}.v{v}.json"))

    # -- briefs
    def save_brief(self, project: str, brief: dict) -> str:
        d = self.project_dir(project, create=True)
        p = os.path.join(d, "briefs", f"{slug(brief['brief_id'])}.json")
        self._write_json(p, brief)
        return p

    def load_brief(self, project: str, brief_id: str) -> dict:
        return self._read_json(os.path.join(self.project_dir(project), "briefs", f"{slug(brief_id)}.json"))

    # -- episodes
    def episode_dir(self, project: str, packet_id: str, create=False) -> str:
        d = os.path.join(self.project_dir(project, create=create), "episodes", slug(packet_id))
        if create:
            for sub in ("requests", "responses"):
                os.makedirs(os.path.join(d, sub), exist_ok=True)
        return d

    def save_packet(self, project: str, packet: dict) -> str:
        d = self.episode_dir(project, packet["packet_id"], create=True)
        p = os.path.join(d, "packet.json")
        self._write_json(p, packet)
        return p

    def load_packet(self, project: str, packet_id: str) -> dict:
        return self._read_json(os.path.join(self.episode_dir(project, packet_id), "packet.json"))

    def list_packets(self, project: str) -> list[dict]:
        d = os.path.join(self.project_dir(project), "episodes")
        out = []
        for e in sorted(os.listdir(d)):
            p = os.path.join(d, e, "packet.json")
            if os.path.exists(p):
                out.append(self._read_json(p))
        return out

    # -- append-only ledgers
    def append(self, project: str, ledger: str, record: dict) -> None:
        d = self.project_dir(project, create=True)
        record = dict(record, at=now_iso())
        with open(os.path.join(d, f"{ledger}.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    def read_ledger(self, project: str, ledger: str) -> list[dict]:
        p = os.path.join(self.project_dir(project), f"{ledger}.jsonl")
        if not os.path.exists(p):
            return []
        with open(p, encoding="utf-8") as fh:
            return [json.loads(l) for l in fh if l.strip()]

    # -- io
    @staticmethod
    def _write_json(path: str, obj: Any) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, indent=2, ensure_ascii=False)
        os.replace(tmp, path)

    @staticmethod
    def _read_json(path: str) -> Any:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)

    @staticmethod
    def write_text(path: str, text: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
