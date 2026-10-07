# Viral Character Lab - creative engine

A local, reusable short-form creative engine: a new brief goes in; a distinctive, coherent, **planning-ready episode packet** comes out (full script, timed audiovisual storyboard, tool mapping, rights/approval checklist, growth hypotheses). Rendered media is a separate, owner-approved step and is never claimed by this engine.

Intended home: `AI influencer/Viral Character Research/creative-engine/` (new subfolder; nothing in the lab is modified). Built in `MFaisalT/git_test` on branch `claude/routing-mode-code-7atd07` because the lab's Windows path is not reachable from the cloud container; copying to Drive is an upload and waits for owner approval.

## Setup

Python 3.13 standard library only (`jsonschema` is used if present, otherwise a built-in subset validator). No install step.

```bash
cd creative-engine
python3 -m unittest discover -s . -p "test_*.py"      # offline contract tests
python3 -m engine --help
```

## Runnable commands

```bash
python3 -m engine init <project>
python3 -m engine bible add <project> eval/bibles/inspector-v1.json [--reason "..."]   # versioned, append-only
python3 -m engine brief add <project> eval/briefs/B1_silent_gag.json
python3 -m engine run   <project> B1_silent_gag inspector-v1 --packet-id EP01 --provider broker --model sonnet
python3 -m engine resume <project> B1_silent_gag inspector-v1 --packet-id EP01      # after answering the pending request
python3 -m engine validate projects/<project>/episodes/ep01/packet.json --bible eval/bibles/inspector-v1.json
python3 -m engine render   projects/<project>/episodes/ep01/packet.json --out storyboard.md
python3 -m engine adapter  projects/<project>/episodes/ep01/packet.json            # dry run; no job submitted
python3 -m engine history  <project> --packet-id EP01                              # repetition evidence vs episode history
python3 -m engine approve  <project> EP01 --by "owner" --credit-cap 60 --render     # refuses drafts and unresolved rights
python3 -m engine learn    <project> EP01 --json '{"shares_7d": 0, "lesson": "..."}'
```

### Providers (the creative path genuinely invokes Claude; nothing is replayed silently)

| Provider | What it does | Status in this build |
|---|---|---|
| `broker` (default) | Writes `requests/<stage>-<n>.request.md`; halts with exit 2 until `responses/<stage>-<n>.response.json` exists. In an authorised Claude Code session the orchestrator fulfils requests with Agent-tool workers and records model evidence in a `<!-- meta:{...} -->` trailer. | **Used live** for the bake-off, the three packets and the held-out test |
| `claude_cli` | `claude -p --output-format json --model <m>`; records `modelUsage` as the served-model evidence | Implemented, **not exercised live** (non-interactive Fable may bill usage credits) |
| `fixture` | Replays `tests/fixtures/*.json` | Plumbing tests only; packets can never leave `draft` |

## Flow (modular, versioned)

brief + constraints → research check (evidence list carried in the packet) → 5 divergent premises → 6 scored hook variants → selected idea + script → complete timed storyboard → verified tool adapter (dry run) → edit/export plan → deterministic QA + creative QA + repetition check → learning loop (`engine learn`).

Each LLM stage has a typed contract, a stage validator and at most two repair passes. Missing evidence, rights or approvals are never invented; the run fails with diagnostics instead.

## Layout

```
engine/            validators.py (deterministic gates) · pipeline.py · adapters.py (Higgsfield dry-run) · prompts.py · retrieval.py · repetition.py · render.py · store.py · cli.py · providers/
schema/            episode_packet.schema.json (typed contract incl. negative constraints + provenance)
prompts/           premises.md · hooks.md · script_storyboard.md · qa_review.md · repair.md  (conditional sections <<IF SILENT>> <<IF COMMERCIAL>> <<IF HISTORY>>)
demos/             3 approved demonstrations (observable outputs + justification); never derived from eval briefs
eval/              rubric.md (predeclared) · briefs/ · bibles/ · arch_*.md · judge_prompt.md · bakeoff_runs/ · heldout/
tests/             51 unit/contract tests (positive and negative)
projects/          runtime store: bibles (versioned) · briefs · episodes/<id>/{packet.json, storyboard.md, adapter_plan.json, requests/, responses/, state.json} · decisions.jsonl · evidence.jsonl · runs.jsonl
docs/              MODEL-EVIDENCE · TOOL-CAPABILITIES · ARCHITECTURE-BAKEOFF · NICHE-DECISION · EVIDENCE-LEDGER · LAUNCH-EXPERIMENT · FINAL-REPORT
```

## What the gates can and cannot establish

Deterministic validators prove structure, timing, feasibility against verified controls, rights declarations and approval order. The repetition checker is lexical evidence for a reviewer. Neither establishes creativity, virality or profit. Every unrendered packet is labelled **"planning-ready; render unverified."**
