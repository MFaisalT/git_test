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
