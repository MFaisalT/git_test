# Viral Character Lab - creative engine

A local, reusable short-form creative engine: a new brief goes in; a distinctive, coherent, **planning-ready episode packet** comes out (full script, timed audiovisual storyboard, tool mapping, rights/approval checklist, growth hypotheses). Rendered media is a separate, owner-approved step and is never claimed by this engine.

Intended home: `AI influencer/Viral Character Research/creative-engine/` (new subfolder; nothing in the lab is modified). Built in `MFaisalT/git_test` on branch `claude/routing-mode-code-7atd07` because the lab's Windows path is not reachable from the cloud container; a human-readable mirror was uploaded to Drive on 2026-10-08 with owner approval (folder `creative-engine/` in the lab); the git branch is the source of truth.

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

## Production-format variety (single take vs multi-scene, silent vs spoken, same or new voice/location)

Format is a first-class, tracked decision, not a side effect of the brief. `engine/formats.py` holds the catalogue: shot architectures (`single_take_static`, `single_take_moving_camera`, `multi_scene_cut`, `jump_cut_timelapse`, `pov_handheld`, `interview_offcamera`, `montage`, `loop`, `continuation_from_last_frame`, `split_or_insert`, `motion_transfer_owned_footage`, `other`), audio modes (`silent_ambience`, `voiceover_narration`, `on_camera_dialogue`, `off_camera_dialogue`, `text_over_broll`, `music_driven`) and continuity reuse (`voice`/`location`/`costume` = same | new | none, resolved against the bible's `approved_assets`).

- A brief may **fix** any field (`"production_format": {"shot_architecture": "jump_cut_timelapse"}`) or leave it **open** (`{}`); open fields are chosen by the engine per premise with a stated rationale, and the five premises must span >=3 architectures and >=2 audio modes.
- **Diversity rule**: the top-ranked premise must not repeat a (shot_architecture, audio_mode) pair used in the last 4 episodes unless the brief fixes it (`FORMAT_REPEATS_RECENT`); the recurring-motif report also tracks format pairs.
- **Realisation gates**: single takes have no cuts and one generation unit with the camera move written into every scene; jump-cut needs >=3 cuts; loop ends on "loop"; silent/text-over has no speech; VO/off-camera/on-camera modes need matching lines; music-driven needs a declared licensed cue; "same voice/location" needs the corresponding approved asset declared.
- Trend entries of type `format` / `edit_move` / `style` extend the menu at run time (cite `trend_refs`).

## Higgsfield production routing

`engine/routing.py` routes every reference asset and video unit to a verified Higgsfield model with a stated reason, status (verified controls / recommended-untested / gap) and a credit estimate from `get_cost` preflights: Nano Banana Pro (NB 2.1 switchable for testing) for character sheets and location stills; Seedance 2.5 `omni_reference` for dialogue, voice-lock and >15 s units with a 480p draft -> 1080p finalize optimisation; Seedance 2.0 Mini for short silent units and drafts; Cinema Studio 4.0 flagged as a gap until its creative-control ids are retrieved; Genjutsu for owned footage. See docs/TOOL-CAPABILITIES.md.

## Trend radar (fresh research when needed)

The engine keeps a dated, sourced, decaying ledger of trend *observations* (what a bounded, web-searching refresh could verify on a given day — not a live feed of what is viral) (formats, styles, edit moves, hook patterns, words/phrases, topics, sounds, dances/moves, products, memes, platform features) per project in `projects/<project>/trends.jsonl`.

- `engine trends refresh <project> --bible <id>` writes a bounded research request (`trends_requests/<date>.request.md`). A Claude session with web search (or a human) answers it; `engine trends ingest` validates every entry (URL sources, capture date, evidence class, rights status) and appends it. No scheduler is created; recommended cadence is in docs/LAUNCH-EXPERIMENT.md.
- At run time the premises and hooks stages receive a small relevant selection (k<=6, fresh <=14 days, scored by platform/format/rights/recency) plus a short "stale" list for reference. Nothing older is silently used.
- Rights rule: `do_not_copy` entries are excluded from prompts entirely; `license_required` entries are down-ranked and injected only as mechanisms; sound/dance entries can be `free_to_adapt` only with a platform-official source. Validation rejects bad URLs, future dates, duplicate ids, over-long or instruction-like text. Packets record `provenance.trends_used` and snapshot age; QA warns on `TREND_STALE` (>21 days) and `TREND_RIGHTS`.
- Freshness: per-entry `decay_horizon_days` (capped by the 14-day window) measured from `origin_date` when known, else from capture. Limits: the engine itself has no web access; a refresh is only as good as the worker's sources (the one real refresh so far is aggregator/press grade with 11 declared gaps).

## Flow (modular, versioned)

brief + constraints → trend radar + research check (dated evidence carried in the packet) → 5 divergent premises, each with its own production format → 6 scored hook variants → selected idea + script → complete timed storyboard → verified tool adapter (dry run) → edit/export plan → deterministic QA + creative QA + repetition check → learning loop (`engine learn`).

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
