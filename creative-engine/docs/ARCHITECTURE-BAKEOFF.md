# Architecture comparison (matched-task bake-off, 2026-10-07 UTC)

## Setup (predeclared; see eval/rubric.md, frozen before any output)

- Briefs (identical across architectures): B1 silent 12 s gag, B2 spoken 20 s episode, B3 15 s sponsored episode with a commercial constraint. Bible: `inspector-v1`.
- Candidates assessed: standalone prompting (A), skill-assisted single agent (B), scripted multi-stage workflow with validators (C = the engine), specialist multi-agent (not run: depth is capped at 1 in this runtime and nothing in the task needed role specialists beyond stages), hybrid (adopted after results, see Decision).
- Matched resources: every generation worker ran `model=sonnet`, default effort (medium), via the Agent tool; no web; same bible. A = one rigid template call, no bible reasoning fields, no demos. B = one call with full bible + distilled craft rules, premises→hook→script in one pass, no validator loop. C = four staged calls (premises, hooks, script+storyboard, QA) with typed contracts, retrieved demos (k=2), deterministic validators and ≤2 repairs.
- Blind judge: `opus` (different model from generators), one call per brief, plans labelled X/Y/Z in a seeded shuffle sealed in `mapping.json` before judging; judge forbidden from reading mapping or project folders.
- Served-model evidence: requested models recorded; actual serving metadata is **not independently observable** through the Agent tool (see docs/MODEL-EVIDENCE.md).

## Results

### Blind quality (weighted rubric total, 1–5; recomputed from judge scores)

| Brief | A fixed template | B skill single-agent | C engine | Judge ranking |
|---|---|---|---|---|
| B1 silent gag | 2.72 | 3.93 | **4.03** | C > B > A |
| B2 spoken | 2.52 | **4.03** | 3.73 | B > C > A |
| B3 commercial | 2.80 | **4.45** | 4.18 | B > C > A |
| **Mean** | 2.68 | **4.14** | 3.98 | |

Pass thresholds (character intent, premise-specific payoff, complete direction, commercial fit): A failed character intent on all three and complete direction on all three; B passed all 12; C passed 11/12 — the judge marked C-B3 commercial fit false because it "omits the platform tool", but C-B3's `export.disclosure_plan` does name the Instagram paid-partnership label (verified by `engine validate`); the judge never saw it because the judge-assembly script passed only script/scenes/continuity, not `export`. **This is a confound against C on dimension 8.**

### Deterministic structure (engine validators run on all nine outputs)

| Brief | A | B | C |
|---|---|---|---|
| B1 | 0 errors | 0 errors | 0 errors |
| B2 | 10 errors (DIALOGUE_SHAPE) | 12 errors (DIALOGUE_SHAPE) | 0 errors |
| B3 | 7 errors (DIALOGUE_SHAPE, TOO_MANY_CUTS) | 10 errors (DIALOGUE_SHAPE) | 0 errors |

A and B emitted scene dialogue as plain strings on the spoken briefs; their templates showed `"dialogue": []` inside scenes without the item shape, whereas C's contract spelled it out. Partly a template-authoring confound, partly the point: without a contract + validator loop, outputs are not machine-checkable. Only C produced a complete packet (tool mapping, rights, approval state, provenance, repetition check).

### Anti-template observations from the judge

- B1: B and A shared a "nudge the table 1 cm, then her own object drags it back" skeleton; C's cable-tie self-own was distinct.
- B3: **B and C converged on the same turn** (six cables, box holds six, the seventh is her own chest-lamp lead). Same model + same bible + same brief → the model's favourite idea recurs across architectures. The engine's history-based repetition check catches this *across episodes*; nothing catches it across parallel runs of one brief except a human reviewer. Recorded as a known limit.
- A twice broke the fixed silhouette (bob/trench coat/torch), i.e. a baseline without the bible drifts identity.

### Cost and latency (worker tokens as reported by the Agent tool; wall-clock per call)

| Arch | Calls per packet | Worker tokens per packet | Wall-clock per packet |
|---|---|---|---|
| A | 1 | ~67K | 35–39 s |
| B | 1 | 72–76K | 58–93 s |
| C | 4 (+0 repairs on 3/3) | ~293K | 130–157 s |
| Judge (opus) | 1 per brief | 83–85K | 40–47 s |

Tokens are the harness's `subagent_tokens` figure (includes the worker's own context), not billed API tokens; USD cost not exposed. Fable 5.1 was used only for orchestration.

## Decision

1. **A (fixed template) is rejected**: fails identity and complete-direction thresholds on every brief; drifts the bible.
2. **B vs C are not distinguishable on blind quality at n=3** (mean 4.14 vs 3.98; C won one brief; C was handicapped on one dimension by the judge-assembly omission). B is ~4× cheaper per packet.
3. **Chosen: C with B's craft rules folded in (hybrid).** Reasons that are not about the judge score: C is the only candidate that (a) passes deterministic gates, (b) exposes inspectable alternatives (5 premises, 6 hooks, rejection reasons) that the lab's evidence-before-ideas policy requires, (c) carries provenance, rights, approval and tool mapping in the packet, and (d) can run the repetition check against history. The one measurable gap (B's explicit craft rules) was closed by adding the same block to `prompts/script_storyboard.md` (tuning log entry 2) before the freeze.
4. Model/effort: `sonnet` at default effort was adequate for all stages (0 repair passes on 3/3). No reason to escalate to opus/fable for generation; judge stays on a different model.
5. Not built (noted as option): a `--fast` single-call draft mode modelled on B for cheap ideation when a full packet is not needed.

## Limits of this comparison

Three briefs, one bible, one judge call per brief, one generation per architecture: this suggests a choice, it does not establish superiority. Judge scores are a single opus reading of anonymised text; they cannot measure audience response. The B/C convergence on B3 shows same-model same-brief runs can agree on the "best" idea — diversity across episodes, not within a brief, is what the engine's history check enforces. Outputs: `eval/bakeoff_runs/` (A/B requests and responses, sealed mappings, judge responses, `structural.json`, `results.json`, `worker_usage.tsv`, `tuning_log.txt`) and `projects/bakeoff/episodes/*/` (C packets, storyboards, adapter plans, stage requests/responses).
