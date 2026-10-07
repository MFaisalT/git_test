# Final report: reusable short-form creative engine (2026-10-07 UTC)

## 1. Outcome in one paragraph

A working local creative engine exists, is tested, and has repeatedly turned new briefs — including one authored by an independent reviewer and never seen by the generator or demonstrations — into complete, gate-passing, **planning-ready episode packets** (scripts, timed audiovisual storyboards, verified tool mappings, rights/approval checklists, growth hypotheses) through the real Claude workflow. Nothing has been rendered, published or spent; every packet carries the label **"planning-ready; render unverified."** Research informed the product; it does not claim virality or profit.

## 2. Status matrix (what is implemented, actually tested, mock-tested, planning-ready, rendered)

| Item | Status |
|---|---|
| Engine code (schema, validators, pipeline, adapters, prompts, retrieval, repetition, trend radar, store, CLI) | **Implemented**; 60 unit/contract tests pass (`python3 -m unittest discover -s . -p "test_*.py"`) |
| Deterministic gates (schema, timing gaps/overlaps/total, speech rate, missing camera/audio, continuity/props, unsupported tool controls, unit cut limits, rights, approval order, fixture quarantine, format-aware beats) | **Implemented and actually tested** with positive and negative cases; also exercised on 9 bake-off outputs and 5 real packets |
| Broker provider (live Claude path via Agent-tool workers inside this authorised session) | **Actually used**: 28 worker calls for generation/QA (+3 blind judges, 1 held-out author, 1 trend refresh, 1 independent reviewer) |
| `claude_cli` provider (`claude -p --output-format json`) | **Implemented, not exercised live** (non-interactive Fable may bill usage credits; see docs/MODEL-EVIDENCE.md) |
| Fixture provider | **Mock-tested only**; packets it produces are quarantined at `draft` by a validator |
| Three deliverable packets (silent gag, spoken episode, sponsored episode) | **Planning-ready; render unverified** — `projects/bakeoff/episodes/c-b1-silent-gag`, `c-b2-dialogue-episode`, `c-b3-commercial` |
| Anti-template perturbation packet | **Planning-ready; render unverified** — `projects/acceptance/episodes/p-b1p-perturbed` (1 bounded repair) |
| Held-out acceptance packet | **Planning-ready; render unverified** — `projects/acceptance/episodes/h-heldout` (0 creative repairs; two engine gate bugs found and fixed) |
| Trend-aware packet | see §6 |
| Higgsfield adapter | **Dry-run only**; no job submitted, no media uploaded; controls verified read-only via MCP catalogue |
| Rendered media | **None.** Requires owner approval, uploaded references, `get_cost` preflight, credit cap, then post-render inspection |
| Drive copy into the lab folder | **Not done** (upload needs approval); everything is in the git branch |

## 3. Exact saved paths (repo `MFaisalT/git_test`, branch `claude/routing-mode-code-7atd07`, folder `creative-engine/`)

- Engine: `engine/` (validators.py, pipeline.py, adapters.py, prompts.py, retrieval.py, repetition.py, trends.py, render.py, store.py, cli.py, providers/__init__.py)
- Contract: `schema/episode_packet.schema.json`
- Prompt modules: `prompts/{premises,hooks,script_storyboard,qa_review,repair,trend_refresh}.md`
- Demonstrations: `demos/D1_silent_gag.json`, `D2_spoken_tool_honesty.json`, `D3_commercial_mechanism.json`
- Predeclared rubric and briefs: `eval/rubric.md`, `eval/briefs/B1..B4`, `eval/bibles/inspector-v1.json`
- Bake-off: `eval/bakeoff_runs/` (A/B requests+responses, sealed `judge-*/mapping.json`, judge responses, `structural.json`, `results.json`, `worker_usage.tsv`, `tuning_log.txt`), `docs/ARCHITECTURE-BAKEOFF.md`
- Packets: `projects/bakeoff/episodes/*/`, `projects/acceptance/episodes/*/` (each: `packet.json`, `storyboard.md`, `adapter_plan.json`, `state.json`, `requests/`, `responses/`)
- Held-out: `eval/heldout/HELDOUT_brief.json`, `eval/heldout/ACCEPTANCE-RESULTS.md`, `eval/heldout/independent-review.json`
- Trend radar: `projects/acceptance/trends.jsonl`, `projects/acceptance/trends_requests/2026-10-07.{request.md,response.json}`
- Decision docs: `docs/MODEL-EVIDENCE.md`, `docs/TOOL-CAPABILITIES.md`, `docs/NICHE-DECISION.md`, `docs/EVIDENCE-LEDGER.md`, `docs/LAUNCH-EXPERIMENT.md`, this file
- Tests: `tests/test_validators.py`, `tests/test_engine.py`, `tests/test_trends.py`, fixtures in `tests/fixtures/`

## 4. Setup and run commands

```bash
git clone <repo> && git checkout claude/routing-mode-code-7atd07 && cd creative-engine
python3 -m unittest discover -s . -p "test_*.py"            # 60 tests, 0 failures (Python 3.13, stdlib only)
python3 -m engine init myshow
python3 -m engine bible add myshow eval/bibles/inspector-v1.json
python3 -m engine brief add myshow eval/briefs/B1_silent_gag.json
python3 -m engine trends refresh myshow --bible inspector-v1   # then answer the request with a web-enabled Claude session; engine trends ingest ...
python3 -m engine run myshow B1_silent_gag inspector-v1 --packet-id EP01 --provider broker --model sonnet
#   -> exit 2 with the path of requests/premises-0.request.md; fulfil it (Claude Code Agent, claude -p, or paste into ChatGPT), write responses/premises-0.response.json, then:
python3 -m engine resume myshow B1_silent_gag inspector-v1 --packet-id EP01
python3 -m engine render projects/myshow/episodes/ep01/packet.json --out ep01.md
python3 -m engine adapter projects/myshow/episodes/ep01/packet.json          # dry run
python3 -m engine approve myshow EP01 --by "owner" --credit-cap 60 --render  # refuses drafts / unresolved rights
```

## 5. Architecture chosen, with the measured comparison

Chosen: **scripted multi-stage workflow with validators (C), with the skill-assisted single-agent's craft rules folded in**. Blind opus judge on three identical briefs: fixed template A 2.68, skill-assisted single-agent B 4.14, engine C 3.98 (C won B1; B won B2/B3; C was handicapped on one dimension by a judge-assembly omission). Only C passed deterministic gates on all briefs (A/B emitted malformed dialogue on spoken briefs). C costs ~4× B's worker tokens (~293K vs ~74K per packet). Generation workers: `sonnet`, default effort, 0–1 repair per packet. Details and limits: `docs/ARCHITECTURE-BAKEOFF.md`.

## 6. Packets delivered

See `eval/heldout/ACCEPTANCE-RESULTS.md` §1–§4 for the three deliverables, the anti-template comparison (structure, actions, performance, camera, sound and payoff all changed under a constraint perturbation; lexical overlap ≤0.12), the held-out result (QA 3.48, thresholds pass, gates pass after two engine bug fixes) and the trend-aware run.

## 7. Tests: commands, counts, failures

`python3 -m unittest discover -s . -p "test_*.py"` → **60 tests, 0 failures, 0 errors** (validators 29 incl. 3 added post-freeze; engine/pipeline 25; trends 6). Negative tests cover schema errors, gaps/overlaps/total, speech too fast, silent-with-dialogue, >1 cut, missing camera/audio, multi-speaker shot, undeclared prop, anchor drift, bible do-not token, unsupported control, unknown model, duration out of range, unmapped scene, motion transfer without driving video, music undeclared, driving-footage rights, unresolved rights at render, firsthand claim, missing disclosure, forbidden claim, render status without approval, rendered-verified without inspection, fixture quarantine, hook/premise mismatch, missing payoff/turn beat, unit with two cuts, trend staleness/rights/unknown. Independent reviewer's adversarial results: `eval/heldout/independent-review.json`.

## 8. Evidence limitations (honest)

- No video was watched with audio in this session (platform playback and official help pages are egress-blocked from the container); the growth refresh is index/text-level and labelled per claim (`docs/EVIDENCE-LEDGER.md`). Zero verified strict cold-start cases remains the state of evidence.
- Served model for workers is not independently observable through the Agent tool; only the orchestrator's `claude-fable-5-1` is (`docs/MODEL-EVIDENCE.md`).
- Judge scores are one opus reading per brief; n=3 briefs. The B/C convergence on B3 shows same-model same-brief runs can agree on an idea.
- Trend radar entries from the one real refresh are aggregator/press grade with 11 declared gaps; sounds/dances could not be verified.
- Owner region unknown → native payouts remain $0 and disclosure law unresolved (`docs/NICHE-DECISION.md`).
- Credits quotes (8 / 56 credits per 8 s) are quotes, not measured costs; retake rates untested.

## 9. Independent review

Recorded verbatim in `eval/heldout/independent-review.json`; repairs made in response are listed at the end of `eval/bakeoff_runs/tuning_log.txt` and summarised in §10.

## 10. Next owner decisions (nothing below has been done)

1. **Region / entity / audience language** — needed to resolve payouts and disclosure rules.
2. **Copy `creative-engine/` into the lab folder on Drive** (an upload; needs your approval) and register it in RESEARCH-INDEX.md / PROJECT-FILE-CATALOG.csv.
3. **Render approval for one packet** (suggest `C-B1_silent_gag`, 12 s, one mini unit, quoted 8 credits/attempt): approve a credit cap, upload an approved character reference still, run `get_cost` preflight, then one generation; inspect the output against `qa.render_inspection` before any further spend.
4. **Niche path** — primary N1 character page with N3 service wrapper, fallback N2 (`docs/NICHE-DECISION.md`); say yes/no or redirect.
5. **Trend refresh cadence** — recommended every two weeks during the pilot plus event triggers; no automation created.
6. **GitHub**: pushes work now; if you want a PR, say so.
