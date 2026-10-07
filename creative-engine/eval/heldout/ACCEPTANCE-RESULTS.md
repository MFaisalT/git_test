# Final acceptance: anti-template test, held-out brief, and gate results (2026-10-07 UTC)

All packets below were produced by the engine's real Claude workflow (broker provider fulfilled by Agent-tool workers, `requested_model=sonnet`, served model not independently observable). None is rendered. Every packet is labelled **planning-ready; render unverified**.

## 1. The three deliverable packets (engine, project `bakeoff`)

| Packet | Brief | Hook mechanism | Narrative structure (from the packet) | Scenes / units | Repairs | Creative QA (engine's own sonnet review) | Deterministic gates |
|---|---|---|---|---|---|---|---|
| `C-B1_silent_gag` | 12 s silent gag | visible_problem | single locked-off take; procedure → fair-play reveal planted in frame one → compulsive relapse that loops | 4 / 1 (mini) | 0 | 3.90, all thresholds pass | PASS |
| `C-B2_dialogue_episode` | 20 s spoken, TikTok | curiosity_gap | procedural accusation in one locked frame, two-voice cross-examination (second voice off-camera) | 5 / 1 (seedance 2.5) | 0 | 3.75, pass | PASS (after prop-matching validator fix) |
| `C-B3_commercial` | 15 s sponsored | status_contradiction | line-up and count that will not reconcile; product capacity is the reveal mechanism; three-part disclosure | 4 / 1 (mini) | 0 | 3.98, pass | PASS |

Paths: `projects/bakeoff/episodes/<id>/{packet.json, storyboard.md, adapter_plan.json, requests/, responses/}`. Blind opus judge totals for the same three (from the bake-off): 4.03 / 3.73 / 4.18.

## 2. Anti-template test (constraint-perturbed brief, project `acceptance`)

`B1p_perturbed` keeps B1's fault (a cable one centimetre short) but changes format (silent → spoken 20 s), platform, location (living room → kitchen at 2 a.m.), light sources, adds an off-camera flatmate, a hard two-moving-prop limit and bans B1's payoff and earlier-episode devices.

| Dimension | `C-B1_silent_gag` | `P-B1p_perturbed` | Changed? |
|---|---|---|---|
| Narrative structure | procedure → planted reveal → relapse loop | ticking clock (fridge-door alarm) + light toggle, ends on an unresolved beep | yes |
| Scene actions | measure, tag, run fingers along cable, cut tie, re-tie | hold door, lamp-check plug, whisper finding to fridge, wedge door with milk carton, find own phone inside fridge | yes |
| Performance | formal alignment procedure, precise pushes | witness-statement verification under noise pressure, whispering | yes |
| Camera | locked-off medium, settle-wobble, digital push-in, loop | handheld push-ins and tilt-downs following her gaze, propped open | yes |
| Sound | room tone, foley of tape/plug/clipboard, no music | compressor hum, drip, accelerating alarm beeps as the escalation device, whispered lines | yes |
| Payoff | her own cable tie ate the centimetre; she re-ties it | she put the phone in the fridge "to cool it"; flatmate: "Why is your phone in the fridge?" — "Under review." | yes |
| Lexical overlap vs history (repetition check) | — | hook .09, premise .04, payoff .07, surprise .05, shots .12 (threshold .35) | no repetition flagged |

Verdict: passes the anti-template test — a constraint change produced different structure, actions, performance, camera, sound and payoff, not a setting swap. One bounded repair was needed (`PROP_UNDECLARED`: scene prop names not matching `continuity.props`), fixed by the worker on the first repair pass.

Weakness observed and recorded: the selected hook mechanism was `visible_problem` for B1, B1p and the held-out brief (B2 chose `curiosity_gap`, B3 `status_contradiction`). The hooks stage scores legibility heavily, so a frame-one visible fault keeps winning. This is a model/scoring bias to watch across episodes; the history fingerprints do not currently include the hook mechanism label. Proposed follow-up (not implemented, to keep the freeze honest): add `hook_mechanism` to history fingerprints and penalise a mechanism used in the last N episodes.

## 3. Held-out brief (independent author, unseen by generator and demos)

- Brief: `HELDOUT_hook_overload_two_part` — written by an independent opus worker that read only the reviewer instructions and the bible. Serial cliffhanger (Part 1 of 2), 28 s, three-prop hard limit, blue-hour lighting only (frosted door panel + chest lamp), one off-camera line max, cliffhanger in the last 4 s, signature tap rationed across both parts, no fine hand-object choreography.
- Run: `python3 -m engine run acceptance HELDOUT_hook_overload_two_part inspector-v1 --packet-id H-heldout --provider broker --model sonnet` → 4 real stages (premises 80K worker tokens/104 s; hooks 72K/29 s; storyboard 79K/46 s; QA 76K/19 s), 0 creative repairs.
- Result: `projects/acceptance/episodes/h-heldout/` — stakeout structure with jump-cut time lapse; heap grows between cuts; low reverse angle from inside the heap reveals her adding a coat; Part 1 ends unresolved, tap saved for Part 2; props = coat heap + coat on forearm (within limit); all five scenes blue-hour only; one off-camera line.
- Creative QA: 3.48 weighted, all four thresholds pass; top fix suggested by the reviewer stage: make the reveal more incriminating and give the Part 2 outline three concrete beats.
- Deterministic gates: **failed on first finalisation** on two engine defects, not creative defects: (a) `SCRIPT_BEATS` required a `payoff` beat even for a cliffhanger; (b) the adapter did not split generation units on "hard jump cut", planning one 28 s clip containing four cuts. Both were fixed as code bugs (format-aware beat rule; split on any cut; new `TOOL_UNIT_CUTS` gate; tests added), the creative output was left untouched, and the packet re-finalised to **planning-ready; render unverified** with five 4–6 s mini units. Logged in `eval/bakeoff_runs/tuning_log.txt` as post-freeze gate fixes.
- Provenance: `provider=broker`, `requested_model=sonnet`, `observed_model=not independently observable`, `trends_used=[]` (the held-out run predates the trend ledger; a retrofitted list was removed and the pipeline now records only what the generating stage actually saw).

## 4. Trend-aware run (project `acceptance`, `T-B4_trend_aware`)

Demonstrates the trend radar end to end: a real refresh (sonnet worker with web search, 7 searches) produced 5 dated entries and 11 declared coverage gaps; `engine trends ingest` accepted 5/5; the premises prompt carried the radar section and the worker cited all five trend ids. Result: `T-B4_trend_aware` is **planning-ready; render unverified** — 4 scenes in two mini units, 0 repairs, creative QA 3.63 with all thresholds passing, repetition check clean (max overlap .13). Provenance records `trends_used` = all five ids with snapshot age 0.98 days; QA surfaces three `TREND_RIGHTS` warnings because the worker marked the adapted formats `do_not_copy` (the engine adapted mechanisms — a specific-frame silent open and an early planted clue — not assets; a reviewer should confirm). The selected premise (a single grey sock filed as a missing-persons case; the sock she keeps "finding" is on her own jacket) cites T-20261007-05 and -02 explicitly in its rationale. Caveat: the ingested trends are aggregator/press grade; the demonstration proves the plumbing and the citation discipline, not that these five entries are what is truly viral today.

## 5. What this acceptance does and does not establish

Establishes: the engine turns new briefs — including one it had never seen — into complete, gate-passing, planning-ready packets with inspectable alternatives, provenance and tool mappings, and changes its creative decisions when constraints change. Does not establish: audience response, virality, profit, render quality, lip-sync, or identity stability in generated video; those require owner-approved rendering and the pilot measurements in docs/LAUNCH-EXPERIMENT.md.


## 6. Independent review and repairs (2026-10-07)

Reviewer: a separate opus worker that did not build the engine; instructions in `eval/heldout/INDEPENDENT-REVIEW-INSTRUCTIONS.md`; report verbatim in `eval/heldout/independent-review.json`; adversarial packets in `eval/heldout/adversarial/`.

**Verdict: accept-with-fixes** — 0 fatal, 13 material, 9 minor. Status labels and tool mapping held up (nothing claims rendered/published/viral/profitable; `prompt_text` honestly the only payload). Of 15 adversarial probes only 4 were caught before repairs.

Substantiated and repaired (engine code; tests added in `tests/test_review_fixes.py`; all six packets re-finalised and still pass):

| Finding | Repair |
|---|---|
| `rejected` packet could be approved; publish/spend skipped rights; negative cap accepted | approval only from planning-ready; publish requires rendered-verified; spend/render refuse unresolved rights; `credit_cap` must be > 0 (CLI + validator) |
| NaN timings passed | `TIMING_NOT_FINITE` / `TIMING_NOT_NUMERIC` |
| 80 words of dialogue in a 15 s script passed (only per-scene rate was checked) | `SPEECH_SCRIPT_TOO_LONG` on script-level words / duration |
| Speech written into action text of a silent gag passed | `SILENT_SPEECH_IN_ACTION` (speech verb + quoted span, double or single quotes) |
| Paraphrased testimonial ("Mine's been spotless for months") and testimonial in hook variants passed | regex pattern set over audience-facing text (script, scenes, hooks, premises) |
| Forbidden claims reworded ("built to last") passed | synonym table per topic; negation-aware sentence scan so "no claims about durability" is not a hit |
| Fixture packet relabelled `manual` became planning-ready | non-draft status now requires `provider ∈ {broker, claude_cli}` and ≥3 successful live stages in `stage_log` |
| Trend provenance false on `P-B1p_perturbed` (ingest happened between request and response) | `trends_used` persisted at first render of the premises request; P-B1p corrected to `[]` |
| Trend validation weak (`httpnotaurl`, `localhost`, future dates, duplicates, hostile text accepted) | URL parse with real host; future-date, duplicate-id, length and instruction-injection rejection |
| Freshness ignored `decay_horizon_days` and trend origin | per-entry horizon (capped at 14 d) measured from `origin_date` when given |
| `do_not_copy` still injected; `license_required` unpenalised; docs said "blocked" | `do_not_copy` excluded from prompts; `license_required` down-ranked; sound/dance `free_to_adapt` only with platform-official source; README reworded |
| Entry T-20261007-01 rested on a blocked source seen only in search | downgraded to `aggregator` / `access_level=index_only` in the ledger |
| Niche: N1 ranked first on sunk cost; N1/N2 not divergent | docs/NICHE-DECISION.md revised: N3 is the stronger business bet; N1 kept as learning engine for a stated reason; overlap acknowledged |
| Evidence: lab sources not on disk; Caine absent | docs/EVIDENCE-LEDGER.md §7 lists every cited Drive file id; Caine/Benjamin explicitly unresolved and uncounted |

Adversarial rerun after repairs: **10/10 saved probes caught** (A1, A1b, A2, A2b, A2c, A3, A4, A5, A6, A7). Approval-flow probes (rejected→approved; publish/spend with unresolved rights and cap −1) are covered by `tests/test_review_fixes.py::TestApprovalGates`.

**Creative diversity finding — accepted, not fully repaired.** The reviewer judged the three bake-off packets share a production template beyond identity: orange evidence tape, cable/socket faults, the chest lamp as the reveal device, an off-camera voice that exposes her, window-left key light. Two of those (cable/socket; tape as the Inspector's procedure) were induced by the briefs and bible; lamp-as-reveal and off-camera-exposure recur by model habit. Repairs: (a) the repetition check now carries a `devices` fingerprint (hook mechanism, props, lighting language, off-camera-voice use, surprise device) and a **recurring-motif report** — for `C-B3` it now lists `prop:tape`, `prop:lamp`, `prop:orange`, `prop:clipboard` at 3/3 and `prop:cable`, `prop:socket`, `prop:phone` at 2/3; (b) the lexical similarity itself stays below threshold (max .14), so **the trio is not automatically flagged; the reviewer's semantic judgement stands and is recorded here**. Honest consequence: the "three genuinely different packets" claim rests on the perturbation, held-out and trend-aware packets (all with different structures, devices and payoffs) more than on the bake-off trio; the bake-off trio is better described as three *formats* of one production template. A semantic (embedding-based) device check is the natural next step; it was not built to keep the post-freeze changes to gates and reporting.

Minor findings not acted on (recorded): affiliate economics assumption wording; internal-consistency slips in packets; dead adapter logic branch; fixture gate still partly self-declared (mitigated by the provenance rule, not eliminated).


## 7. Production-format variety and Higgsfield routing (added after the owner's two follow-up requirements)

**Requirement 1 - the engine must produce different kinds of video (single moving take, multi-scene edit, jump-cut, silent/spoken, same or new voice/location, trend-driven options).** Implemented as a tracked decision (`engine/formats.py`): every premise declares a `production_format`; the five premises must span >=3 shot architectures and >=2 audio modes; the selected pair must not repeat the last 4 episodes unless the brief fixes it; realisation gates check the storyboard matches the declaration; the recurring-motif report tracks format pairs.

Live demonstration `F-B5_format_open` (brief left every format field open; kitchen timer premise; cables/tape/socks/hooks/fridge banned):
- Premises came back as five different pairs: (single_take_moving_camera, silent_ambience), (jump_cut_timelapse, voiceover_narration), (pov_handheld, on_camera_dialogue), (loop, text_over_broll), (multi_scene_cut, off_camera_dialogue).
- Selected: **single_take_moving_camera + silent_ambience**, chosen by the engine with the rationale that the reveal is spatial (a ringing wind-up timer "migrates" from the empty oven to her own flap pocket, trembling in frame from second one), so one continuous glide carries the viewer to the sound, and that this differs from the locked-off, spoken, cut-heavy recent episodes; location reuse `same` (loc-kitchen-01), voice `none`, costume `same`; cites trend T-20261007-05.
- Storyboard: 4 scenes, 0-16 s, every scene `continuous` except a final `hold`, camera.movement written per scene (settle-wobble -> lateral glide -> drift in and down -> rise and ease back), empty dialogue, ambience + bell foley. Deterministic gates: **PASS, 0 errors, 0 warnings** on first attempt (the single-take realisation checks were active). Creative QA 3.78, all thresholds pass. Routed to one `seedance_2_5 omni_reference` unit, 16 s, `generate_audio=false`, quoted 112 credits (draft tier 48).
- Caveat exposed and fixed: the worker declared the kitchen still and character reference as `owned` although the bible registry lists them as not yet generated; the pipeline now cross-checks declared rights against `approved_assets` and downgrades to `unresolved` with an evidence row (bible bumped to v2 in both projects for the registry; no identity change).

Across the seven engine packets the selected pairs are now: static/silent (C-B1), static/off-camera (C-B2), static/on-camera (C-B3), handheld-ish/off-camera (P-B1p), jump-cut/off-camera (H-heldout), static/on-camera (T-B4), **moving-take/silent (F-B5)**. Pre-format packets carry no declaration (labelled "pre-format" in their storyboards); from now on every packet does.

**Requirement 2 - optimise production for Higgsfield (Nano Banana Pro / NB 2 to test / Seedance 2.5 / Cinema Studio).** The live catalogue was re-read and credit preflights taken (docs/TOOL-CAPABILITIES.md "Production routing"). Routing (`engine/routing.py`) now assigns every unit and reference asset a model with reason, status and quote: Nano Banana Pro for character sheet (slot recipe from the Higgsfield character-sheet workflow) and location stills (2 credits each at 2k), NB 2.1 switchable for the owner's test; Seedance 2.5 omni_reference for dialogue/voice-lock/>15 s with a 480p draft -> 1080p finalize optimisation (48 vs 112 credits at 16 s); Seedance 2.0 Mini for <=15 s silent/draft units (15 credits/15 s); Cinema Studio 4.0 recorded as the only model with native lens/lighting/pacing controls but marked **gap** until its control ids are retrieved; Cinema Studio 3.0 recommended only for character-off-frame shots (no identity references, 75 credits/15 s); Genjutsu for owned footage. Nothing has been generated; "recommended_untested" is stated wherever that is the truth.
