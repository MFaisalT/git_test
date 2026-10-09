# Final report: reusable short-form creative engine (2026-10-07 UTC; updated 2026-10-08 after the owner's first decisions)

## 1. Outcome in one paragraph

A working local creative engine exists, is tested, and has repeatedly turned new briefs — including one authored by an independent reviewer and never seen by the generator or demonstrations — into complete, gate-passing, **planning-ready episode packets** (scripts, timed audiovisual storyboards, verified tool mappings, rights/approval checklists, growth hypotheses) through the real Claude workflow. Nothing has been published. On 2026-10-08, with owner approval, 20 credits were spent on four reference stills and one 12 s test render (section 11); every packet still carries the label **"planning-ready; render unverified"** because the render has not yet been inspected by the owner and the reference assets are not yet approved into the registry. Research informed the product; it does not claim virality or profit.

## 2. Status matrix (what is implemented, actually tested, mock-tested, planning-ready, rendered)

| Item | Status |
|---|---|
| Engine code (schema, validators, pipeline, adapters, prompts, retrieval, repetition, trend radar, store, CLI) | **Implemented**; 94 unit/contract tests passed at this report (142 as of 2026-10-09) (`python3 -m unittest discover -s . -p "test_*.py"`) |
| Deterministic gates (schema, timing gaps/overlaps/total, speech rate, missing camera/audio, continuity/props, unsupported tool controls, unit cut limits, rights, approval order, fixture quarantine, format-aware beats) | **Implemented and actually tested** with positive and negative cases; also exercised on 9 bake-off outputs and 5 real packets |
| Broker provider (live Claude path via Agent-tool workers inside this authorised session) | **Actually used**: 31 worker calls for generation/QA (incl. 1 repair and the trend-aware run) (+3 blind judges, 1 held-out author, 1 trend refresh, 1 independent reviewer) |
| `claude_cli` provider (`claude -p --output-format json`) | **Implemented, not exercised live** (non-interactive Fable may bill usage credits; see docs/MODEL-EVIDENCE.md) |
| Fixture provider | **Mock-tested only**; packets it produces are quarantined at `draft` by a validator |
| Three deliverable packets (silent gag, spoken episode, sponsored episode) | **Planning-ready; render unverified** — `projects/bakeoff/episodes/c-b1-silent-gag`, `c-b2-dialogue-episode`, `c-b3-commercial` |
| Anti-template perturbation packet | **Planning-ready; render unverified** — `projects/acceptance/episodes/p-b1p-perturbed` (1 bounded repair) |
| Held-out acceptance packet | **Planning-ready; render unverified** — `projects/acceptance/episodes/h-heldout` (0 creative repairs; two engine gate bugs found and fixed) |
| Production-format variety (shot architecture / audio mode / voice-location reuse as a tracked, diversified, validated decision) | **Implemented and tested** (`engine/formats.py`, 8 tests); **demonstrated live** on `F-B5_format_open`: engine chose single_take_moving_camera + silent, 0 gate errors, QA 3.78 (ACCEPTANCE-RESULTS §7) |
| Higgsfield production routing (Nano Banana Pro / NB 2.1 / Seedance 2.5 & Mini / Cinema Studio 4.0 & 3.0 / Genjutsu) with get_cost preflights | **Implemented and tested** (`engine/routing.py`, 9 tests); catalogue verified read-only; first paid generations done 2026-10-08 (section 11); Cinema Studio 4.0 control ids = gap (two retrieval attempts) |
| Trend-aware packet | **Planning-ready; render unverified** — `projects/acceptance/episodes/t-b4-trend-aware` (0 repairs; cites 5 dated trend ids; rights warnings surfaced) |
| Higgsfield adapter | **Dry-run only**; no job submitted, no media uploaded; controls verified read-only via MCP catalogue; per-unit routing + image asset requests with credit estimates |
| Rendered media | **One owner-approved test render** (C-B1 U1, Seedance 2.0 Mini, 12 s, 720p, silent; job `0455d48d`; charged 12 credits = quote) + 4 reference stills (8 credits). **Inspection pending owner**; the session cannot view pixels. Record: `projects/bakeoff/episodes/c-b1-silent-gag/renders/` |
| Drive copy into the lab folder | **Done 2026-10-08** as a human-readable mirror (folder `creative-engine/` id `1s9H5G2_kvZcu0M01h01RKg8cETm-DXAA`: MANIFEST, README, FINAL-REPORT, NICHE-DECISION, TOOL-CAPABILITIES, RESOLUTION-POLICY, ACCEPTANCE-RESULTS, `storyboards/` x7). Git branch remains the source of truth; lab index files not modified |

## 3. Exact saved paths (repo `MFaisalT/git_test`, branch `claude/routing-mode-code-7atd07`, folder `creative-engine/`)

- Engine: `engine/` (validators.py, pipeline.py, adapters.py, prompts.py, retrieval.py, repetition.py, trends.py, render.py, store.py, cli.py, providers/__init__.py)
- Contract: `schema/episode_packet.schema.json`
- Prompt modules: `prompts/{premises,hooks,script_storyboard,qa_review,repair,trend_refresh}.md`
- Demonstrations: `demos/D1_silent_gag.json`, `D2_spoken_tool_honesty.json`, `D3_commercial_mechanism.json`
- Predeclared rubric and briefs: `eval/rubric.md`, `eval/briefs/B1..B4`, `eval/bibles/inspector-v1.json`
- Bake-off: `eval/bakeoff_runs/` (A/B requests+responses, sealed `judge-*/mapping.json`, judge responses, `structural.json`, `results.json`, `worker_usage.tsv`, `tuning_log.txt`), `docs/ARCHITECTURE-BAKEOFF.md`
- Packets: `projects/bakeoff/episodes/*/`, `projects/acceptance/episodes/*/` (each: `packet.json`, `requests/`, `responses/`; all but acceptance c-b1/c-b2/c-b3 also have `storyboard.md`, `adapter_plan.json`, `state.json`)
- Held-out: `eval/heldout/HELDOUT_brief.json`, `eval/heldout/ACCEPTANCE-RESULTS.md`, `eval/heldout/independent-review.json`
- Trend radar: `projects/acceptance/trends.jsonl`, `projects/acceptance/trends_requests/2026-10-07.{request.md,response.json}`
- Decision docs: `docs/MODEL-EVIDENCE.md`, `docs/TOOL-CAPABILITIES.md`, `docs/NICHE-DECISION.md`, `docs/EVIDENCE-LEDGER.md`, `docs/LAUNCH-EXPERIMENT.md`, this file
- Tests: `tests/test_validators.py`, `tests/test_engine.py`, `tests/test_trends.py`, fixtures in `tests/fixtures/`

## 4. Setup and run commands

```bash
git clone <repo> && git checkout claude/routing-mode-code-7atd07 && cd creative-engine
python3 -m unittest discover -s . -p "test_*.py"            # 94 tests at this report, 142 as of 2026-10-09; 0 failures (Python 3.13, stdlib only)
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

`python3 -m unittest discover -s . -p "test_*.py"` → **94 tests, 0 failures, 0 errors** (validators 35; engine/pipeline 19; trends 6; review-driven regressions 18; formats 8; routing 8). Negative tests cover schema errors, gaps/overlaps/total, speech too fast, silent-with-dialogue, >1 cut, missing camera/audio, multi-speaker shot, undeclared prop, anchor drift, bible do-not token, unsupported control, unknown model, duration out of range, unmapped scene, motion transfer without driving video, music undeclared, driving-footage rights, unresolved rights at render, firsthand claim, missing disclosure, forbidden claim, render status without approval, rendered-verified without inspection, fixture quarantine, hook/premise mismatch, missing payoff/turn beat, unit with two cuts, trend staleness/rights/unknown. Independent reviewer's adversarial results: `eval/heldout/independent-review.json`.

## 8. Evidence limitations (honest)

- No video was watched with audio in this session (platform playback and official help pages are egress-blocked from the container); the growth refresh is index/text-level and labelled per claim (`docs/EVIDENCE-LEDGER.md`). Zero verified strict cold-start cases remains the state of evidence.
- Served model for workers is not independently observable through the Agent tool; only the orchestrator's `claude-fable-5-1` is (`docs/MODEL-EVIDENCE.md`).
- Judge scores are one opus reading per brief; n=3 briefs. The B/C convergence on B3 shows same-model same-brief runs can agree on an idea.
- Trend radar entries from the one real refresh are aggregator/press grade with 11 declared gaps; sounds/dances could not be verified.
- Owner region unknown → native payouts remain $0 and disclosure law unresolved (`docs/NICHE-DECISION.md`).
- Credit quotes are preflights; the one measured render (12 credits for Mini 12 s 720p) matched its quote exactly, which is one data point. Seedance 2.5 and Cinema Studio costs remain quotes (112-192 credits per 16 s); retake rates untested.

## 9. Independent review

Opus reviewer, separate from the builder: **accept-with-fixes** (0 fatal, 13 material, 9 minor; 15 adversarial probes, 4 caught before repairs, 10/10 saved probes caught after). Verbatim report: `eval/heldout/independent-review.json`. Repairs and the one accepted-but-not-fully-repaired finding (bake-off trio shares a production template; now surfaced by a recurring-motif report rather than blocked) are itemised in `eval/heldout/ACCEPTANCE-RESULTS.md` §6. The niche recommendation was revised on the reviewer's evidence point: **N3 (productized service) is the stronger business bet; N1 is kept as the learning engine for a stated reason, not sunk cost.**

## 10. Owner decisions as of 2026-10-07 (superseded by section 11)

1. **Region / entity / audience language** — needed to resolve payouts and disclosure rules.
2. **Copy `creative-engine/` into the lab folder on Drive** (an upload; needs your approval) and register it in RESEARCH-INDEX.md / PROJECT-FILE-CATALOG.csv.
3. **First render approval** - suggested order: (a) character sheet on Nano Banana Pro (2 credits) and the kitchen/living-room stills (2 each), approve them into the registry; (b) `C-B1_silent_gag` on Seedance 2.0 Mini (12 s, ~12 credits) or `F-B5_format_open` as a Seedance 2.5 480p draft (~48 credits); inspect against `qa.render_inspection` before any further spend. Say a credit cap and whether to run the NB 2.1 comparison.
7. **Cinema Studio 4.0**: approve a read-only retrieval of its creative-control ids (lens/lighting/pacing) so the packet's camera and lighting fields can map to native controls instead of prompt text.
4. **Niche path** — revised: N3 productized service as the business bet, N1 character pilot as the learning engine, N2 fallback (`docs/NICHE-DECISION.md`); say yes/no or redirect.
5. **Trend refresh cadence** — recommended every two weeks during the pilot plus event triggers; no automation created.
6. **GitHub**: pushes work now; if you want a PR, say so.

## 11. 2026-10-08: owner decisions executed

Owner decisions received: (1) global audience default, niche/character determines audience by logic; (2) Drive copy approved; (3) first renders approved with no cap, to measure a real render cost; (4) Cinema Studio 4.0 control-id retrieval approved; (5) niche path N3/N1/N2 accepted, explanation of the N's requested.

| Action | Result |
|---|---|
| Audience policy | Recorded in both `project.json` files and bible `inspector-v1` v3 (`audience`: global default, visual-first, English captions) |
| Reference stills (Nano Banana Pro, 2k) | 2 character-sheet variants (jobs `6dd8c02f` variant 0, `ee6ec308` variant 1), living-room still (`baf3b039`), kitchen still (`cfdcc98d`); **8 credits charged**; registry status `generated_pending_owner_approval`. Jobs report serving model `nano_banana_2` while the ledger says "Nano Banana Pro": logged, unresolved |
| First render | C-B1 U1 as planned by the adapter: Seedance 2.0 Mini, 12 s, 9:16, 720p, silent, refs variant 0 + living-room still. **12 credits charged = quote.** Pixels not viewable from this container; owner inspects via the Higgsfield widget / result URL |
| Real cost picture | Measured: 2 credits per 2k still; 12 credits per 12 s Mini 720p silent clip. Quoted, unmeasured: Seedance 2.5 16 s = 48 (480p draft) / 112 (720p) / 192 (1080p); Cinema Studio 4.0 16 s = 112; owner's own CS 4.0 ledger 2026-10-06 shows 112-154 per job. A 16-post pilot at one Mini take per post is ~200 credits; at Seedance 2.5 1080p with one retake it is ~6,000 |
| Resolution question | Answered in `docs/RESOLUTION-POLICY.md`: platforms want a 1080x1920 H.264 upload with HD on; Seedance/Veo-class tools are native 720p/1080p; creators describe generate-then-upscale; **no account's source resolution is observable from its posts**, so "what the top accounts render at" is inference. Policy: drafts 480p/720p, masters 1080p (finalize or one upscale), export 1080x1920 |
| Cinema Studio 4.0 ids | Two read-only attempts (`models_explore`, `apps_search`, `get_preset_instructions`): no MCP surface lists the camera/lens/light/pacing ids. Remains **gap**; owner can copy ids from the web UI, otherwise lens/lighting stay prompt text |
| Drive mirror | Folder `1s9H5G2_kvZcu0M01h01RKg8cETm-DXAA` (14 files). `RESEARCH-INDEX.md` / `PROJECT-FILE-CATALOG.csv` untouched; a one-line registration is proposed, not applied |

Balance: 981.16 -> 961.16 credits across the session (20 spent, all owner-approved).

Open for the owner: pick character variant 0 or 1 (or regenerate); judge the test render against the checklist in `renders/0455d48d...json`; say whether to run the NB 2.1 comparison (2 credits) and a Seedance 2.5 render of F-B5 (48 draft / 192 at 1080p); country/entity for payouts and disclosure.
