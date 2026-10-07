"""LLM providers.

broker     - writes a request file; a Claude Code session (or a human) answers into responses/. Default here,
             because this build runs inside an authorised Claude Code session whose Agent tool is the available
             Claude workflow. Nothing is replayed silently: a missing response halts the run with exit code 2.
claude_cli - `claude -p --output-format json`; reads modelUsage for the served model. Not exercised live in this
             build (non-interactive Fable runs may bill usage credits; see docs/MODEL-EVIDENCE.md).
fixture    - test plumbing only. Packets it produces can never leave 'draft'.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass


class PendingResponse(Exception):
    def __init__(self, request_path: str, response_path: str):
        super().__init__(f"awaiting response: write JSON to {response_path} (prompt at {request_path})")
        self.request_path, self.response_path = request_path, response_path


@dataclass
class Completion:
    text: str
    requested_model: str
    observed_model: str  # "not independently observable" unless the runtime exposes it
    usage: dict
    provider: str


def parse_json_object(text: str) -> dict:
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    a, b = t.find("{"), t.rfind("}")
    if a < 0 or b < 0:
        raise ValueError("no JSON object found in response")
    return json.loads(t[a:b + 1])


class BrokerProvider:
    name = "broker"

    def __init__(self, episode_dir: str, requested_model: str = "sonnet", effort: str = "medium"):
        self.dir = episode_dir
        self.requested_model, self.effort = requested_model, effort

    def complete(self, prompt: str, tag: str) -> Completion:
        req = os.path.join(self.dir, "requests", f"{tag}.request.md")
        resp = os.path.join(self.dir, "responses", f"{tag}.response.json")
        os.makedirs(os.path.dirname(req), exist_ok=True); os.makedirs(os.path.dirname(resp), exist_ok=True)
        if not os.path.exists(req):
            with open(req, "w", encoding="utf-8") as fh:
                fh.write(f"<!-- requested_model: {self.requested_model}; effort: {self.effort}; tag: {tag} -->\n\n" + prompt)
        if not os.path.exists(resp):
            raise PendingResponse(req, resp)
        with open(resp, encoding="utf-8") as fh:
            raw = fh.read()
        meta = {}
        m = re.search(r"<!--\s*meta:(\{.*?\})\s*-->", raw, re.S)
        if m:
            try:
                meta = json.loads(m.group(1))
            except json.JSONDecodeError:
                meta = {}
            raw = raw[:m.start()] + raw[m.end():]
        return Completion(raw, meta.get("requested_model", self.requested_model),
                          meta.get("observed_model", "not independently observable"), meta.get("usage", {}), self.name)


class ClaudeCliProvider:
    name = "claude_cli"

    def __init__(self, requested_model: str = "sonnet", effort: str = "medium", timeout_s: int = 600):
        self.requested_model, self.effort, self.timeout_s = requested_model, effort, timeout_s
        if not shutil.which("claude"):
            raise RuntimeError("claude CLI not found on PATH")

    def complete(self, prompt: str, tag: str) -> Completion:
        cmd = ["claude", "-p", "--output-format", "json", "--model", self.requested_model, "--effort", self.effort, "--tools", ""]
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=self.timeout_s)
        if proc.returncode != 0:
            raise RuntimeError(f"claude -p failed ({proc.returncode}): {proc.stderr[:500]}")
        payload = json.loads(proc.stdout)
        usage = payload.get("modelUsage", {}) or {}
        observed = ", ".join(usage.keys()) if usage else "not independently observable"
        return Completion(payload.get("result", ""), self.requested_model, observed,
                          {"modelUsage": usage, "total_cost_usd": payload.get("total_cost_usd"), "duration_ms": payload.get("duration_ms")}, self.name)


class FixtureProvider:
    """Replays canned stage outputs. Only for plumbing tests; provenance is marked and status is capped at draft."""
    name = "fixture"

    def __init__(self, fixture_dir: str):
        self.dir = fixture_dir

    def complete(self, prompt: str, tag: str) -> Completion:
        stage = tag.split("-")[0]
        p = os.path.join(self.dir, f"{stage}.json")
        with open(p, encoding="utf-8") as fh:
            return Completion(fh.read(), "fixture", "fixture (no model)", {}, self.name)
