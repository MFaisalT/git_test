"""CLI. Run from the creative-engine directory:  python -m engine <command> ...

Commands:
  init <project>                         create project
  bible add <project> <file> [--reason]  save a bible as the next version
  brief add <project> <file>             save a brief
  run <project> <brief_id> <bible_id> [--packet-id] [--provider broker|claude_cli|fixture] [--model] [--effort] [--fixtures DIR]
  resume <project> <brief_id> <bible_id> --packet-id ID   (same as run; completes pending broker stages)
  validate <packet.json> [--bible bible.json]
  render <packet.json> [--out storyboard.md]
  adapter <packet.json> [--bible bible.json]  dry-run tool mapping (no job submitted)
  history <project> [--packet-id ID]          repetition check against episode history
  approve <project> <packet_id> --by NAME --credit-cap N [--render] [--spend] [--publish]
  learn <project> <packet_id> --json '{...}'  append dated outcome/lesson
  list <project>
  trends refresh <project> [--bible ID]      write a dated trend-research request (answered by the Claude workflow)
  trends ingest  <project> <response.json>   validate and append sourced trend entries (dated, rights-flagged)
  trends show    <project> [--max-age-days N]
  trends add     <project> --json '{...}'
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from . import ENGINE_VERSION
from .adapters import plan as adapter_plan
from .pipeline import QUOTES_2026_10_07, Pipeline, StageFailure
from .providers import BrokerProvider, ClaudeCliProvider, FixtureProvider, PendingResponse
from .render import storyboard_md
from .repetition import compare
from .store import Store, now_iso
from .prompts import render_trend_refresh
from .trends import DEFAULT_FRESH_DAYS, age_days, parse_refresh_response, select_relevant, validate_entry
from .validators import validate_all

DEFAULT_ROOT = os.environ.get("CE_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def cmd_init(a, store):
    store.project_dir(a.project, create=True)
    print(f"project '{a.project}' ready at {store.project_dir(a.project)}")


def cmd_bible(a, store):
    b = store.save_bible(a.project, _load(a.file), a.reason or "")
    print(f"saved bible {b['bible_id']} v{b['version']}")


def cmd_brief(a, store):
    print("saved brief at", store.save_brief(a.project, _load(a.file)))


def _provider(a, store, packet_id):
    if a.provider == "broker":
        return BrokerProvider(store.episode_dir(a.project, packet_id, create=True), a.model, a.effort)
    if a.provider == "claude_cli":
        return ClaudeCliProvider(a.model, a.effort)
    if a.provider == "fixture":
        if not a.fixtures:
            sys.exit("--fixtures DIR is required for the fixture provider")
        return FixtureProvider(a.fixtures)
    sys.exit(f"unknown provider {a.provider}")


def cmd_run(a, store):
    import time
    packet_id = a.packet_id or f"{a.brief_id}-{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}"
    prov = _provider(a, store, packet_id)
    pipe = Pipeline(store, a.project, prov, max_repairs=a.max_repairs, requested_model=a.model, effort=a.effort)
    try:
        packet = pipe.run(a.brief_id, a.bible_id, packet_id)
    except PendingResponse as e:
        print(f"[pending] packet {packet_id}: {e}")
        print("Fulfil the request with the Claude workflow, write the JSON response, then re-run with --packet-id", packet_id)
        sys.exit(2)
    except StageFailure as e:
        print(f"[failed] {e}")
        sys.exit(3)
    d = store.episode_dir(a.project, packet_id)
    det = packet["qa"]["deterministic"]
    print(f"[{packet['status']}] packet {packet_id}")
    print(f"  deterministic: {'PASS' if det['ok'] else 'FAIL'} errors={det['error_count']} warnings={det['warning_count']}")
    print(f"  repetition: {packet['qa']['repetition']['verdict']} {packet['qa']['repetition']['flagged_fields']}")
    print(f"  provenance: provider={packet['provenance']['provider']} requested={packet['provenance']['requested_model']} observed={packet['provenance']['observed_model']} repairs={packet['provenance']['repair_passes']}")
    print(f"  files: {os.path.join(d, 'packet.json')}  {os.path.join(d, 'storyboard.md')}  {os.path.join(d, 'adapter_plan.json')}")
    if not det["ok"]:
        for f in det["findings"]:
            if f["severity"] == "error":
                print(f"   - {f['code']} {f['path']}: {f['message']}")
        sys.exit(4)


def cmd_validate(a, store):
    packet = _load(a.packet)
    bible = _load(a.bible) if a.bible else None
    rep = validate_all(packet, bible)
    print(json.dumps(rep.as_dict(), indent=2))
    sys.exit(0 if rep.ok else 4)


def cmd_render(a, store):
    md = storyboard_md(_load(a.packet))
    if a.out:
        Store.write_text(a.out, md); print("wrote", a.out)
    else:
        print(md)


def cmd_adapter(a, store):
    packet = _load(a.packet)
    bible = _load(a.bible) if a.bible else None
    print(json.dumps(adapter_plan(packet, bible, QUOTES_2026_10_07), indent=2))


def cmd_history(a, store):
    packets = store.list_packets(a.project)
    if a.packet_id:
        new = store.load_packet(a.project, a.packet_id)
        print(json.dumps(compare(new, packets), indent=2))
    else:
        for p in packets:
            print(f"{p['packet_id']:50s} {p['status']:35s} {p['brief']['format']}")


def cmd_approve(a, store):
    p = store.load_packet(a.project, a.packet_id)
    if p["status"] == "draft":
        sys.exit("refusing: packet is 'draft' (fails deterministic gates or fixture-generated); fix first")
    unresolved = [r["asset"] for r in p["asset_rights"] if r["rights_status"] == "unresolved"]
    if a.render and unresolved:
        sys.exit(f"refusing render approval: unresolved rights {unresolved}")
    ap = p["approval"]
    ap.update({"approved_by": a.by, "approved_at": now_iso(), "credit_cap": a.credit_cap})
    if a.render: ap["render_approved"] = True; p["status"] = "approved-for-render"
    if a.spend: ap["spend_approved"] = True
    if a.publish: ap["publish_approved"] = True
    rep = validate_all(p)
    if not rep.ok:
        sys.exit("approval would violate gates: " + json.dumps([f.as_dict() for f in rep.errors]))
    store.save_packet(a.project, p)
    store.append(a.project, "decisions", {"type": "approval", "packet_id": a.packet_id, "by": a.by, "render": a.render, "spend": a.spend, "publish": a.publish, "credit_cap": a.credit_cap})
    print(f"approval recorded; status={p['status']}. Rendering still requires the owner to run the tool; this engine never submits a job.")


def cmd_learn(a, store):
    Pipeline(store, a.project, None).learn(a.packet_id, json.loads(a.json))
    print("recorded")


def cmd_trends(a, store):
    ledger = store.read_ledger(a.project, "trends")
    if a.action == "refresh":
        # creates a research request for the Claude workflow (or a human); no automation, no web access from the engine itself
        d = os.path.join(store.project_dir(a.project), "trends_requests"); os.makedirs(d, exist_ok=True)
        meta = _load(os.path.join(store.project_dir(a.project), "project.json"))
        bible = store.load_bible(a.project, a.bible) if a.bible else {}
        labels = sorted({e["label"] for e in ledger})
        path = os.path.join(d, f"{now_iso()[:10]}.request.md")
        Store.write_text(path, render_trend_refresh(meta, bible, labels))
        print("trend refresh request written:", path)
        print("Answer it (web-sourced JSON) and run: engine trends ingest", a.project, path.replace(".request.md", ".response.json"))
    elif a.action == "ingest":
        entries, errs = parse_refresh_response(_load(a.file))
        for e in errs:
            print("rejected:", e)
        for e in entries:
            store.append(a.project, "trends", e)
        store.append(a.project, "evidence", {"type": "trend_refresh", "file": a.file, "accepted": len(entries), "rejected": len(errs)})
        print(f"ingested {len(entries)} entries, rejected {len(errs)}")
        sys.exit(0 if entries or not errs else 4)
    elif a.action == "add":
        e = json.loads(a.json); v = validate_entry(e)
        if v: sys.exit("invalid entry: " + "; ".join(v))
        store.append(a.project, "trends", e); print("added", e["trend_id"])
    elif a.action == "show":
        fresh_days = a.max_age_days or DEFAULT_FRESH_DAYS
        for e in sorted(ledger, key=lambda x: x["captured_at"], reverse=True):
            age = age_days(e)
            print(f"{'FRESH' if age <= fresh_days else 'stale'} {age:5.1f}d  {e['trend_id']:16s} {e['type']:16s} {e['rights_status']:16s} {e['label']}")
        if not ledger:
            print("(empty ledger) run: engine trends refresh", a.project)


def cmd_list(a, store):
    for p in store.list_packets(a.project):
        print(f"{p['packet_id']:50s} {p['status']}")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="engine", description=f"Viral Character Lab creative engine v{ENGINE_VERSION}")
    ap.add_argument("--root", default=DEFAULT_ROOT)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("init"); s.add_argument("project"); s.set_defaults(fn=cmd_init)
    s = sub.add_parser("bible"); s.add_argument("action", choices=["add"]); s.add_argument("project"); s.add_argument("file"); s.add_argument("--reason"); s.set_defaults(fn=cmd_bible)
    s = sub.add_parser("brief"); s.add_argument("action", choices=["add"]); s.add_argument("project"); s.add_argument("file"); s.set_defaults(fn=cmd_brief)
    for name in ("run", "resume"):
        s = sub.add_parser(name); s.add_argument("project"); s.add_argument("brief_id"); s.add_argument("bible_id")
        s.add_argument("--packet-id"); s.add_argument("--provider", default="broker", choices=["broker", "claude_cli", "fixture"])
        s.add_argument("--model", default="sonnet"); s.add_argument("--effort", default="medium"); s.add_argument("--fixtures"); s.add_argument("--max-repairs", type=int, default=2)
        s.set_defaults(fn=cmd_run)
    s = sub.add_parser("validate"); s.add_argument("packet"); s.add_argument("--bible"); s.set_defaults(fn=cmd_validate)
    s = sub.add_parser("render"); s.add_argument("packet"); s.add_argument("--out"); s.set_defaults(fn=cmd_render)
    s = sub.add_parser("adapter"); s.add_argument("packet"); s.add_argument("--bible"); s.set_defaults(fn=cmd_adapter)
    s = sub.add_parser("history"); s.add_argument("project"); s.add_argument("--packet-id"); s.set_defaults(fn=cmd_history)
    s = sub.add_parser("approve"); s.add_argument("project"); s.add_argument("packet_id"); s.add_argument("--by", required=True); s.add_argument("--credit-cap", type=float, required=True)
    s.add_argument("--render", action="store_true"); s.add_argument("--spend", action="store_true"); s.add_argument("--publish", action="store_true"); s.set_defaults(fn=cmd_approve)
    s = sub.add_parser("learn"); s.add_argument("project"); s.add_argument("packet_id"); s.add_argument("--json", required=True); s.set_defaults(fn=cmd_learn)
    s = sub.add_parser("list"); s.add_argument("project"); s.set_defaults(fn=cmd_list)
    s = sub.add_parser("trends"); s.add_argument("action", choices=["refresh", "ingest", "add", "show"]); s.add_argument("project")
    s.add_argument("file", nargs="?"); s.add_argument("--json"); s.add_argument("--bible"); s.add_argument("--max-age-days", type=int); s.set_defaults(fn=cmd_trends)
    a = ap.parse_args(argv)
    a.fn(a, Store(a.root))


if __name__ == "__main__":
    main()
