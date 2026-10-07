# Predeclared creative rubric, weights and pass thresholds

Frozen 2026-10-07 before any architecture-comparison or acceptance output was generated.
Scores are 1–5 anchored. Blind scoring: the judge sees anonymised packets (A/B/C labels shuffled per brief) and never sees which architecture produced them.

## Dimensions and weights (sum = 1.00)

| # | Dimension | Weight | 1 (fail) | 3 (adequate) | 5 (excellent) |
|---|---|---|---|---|---|
| 1 | Originality (premise + payoff not a stock skit; not a setting-swap of another packet) | 0.15 | Generic "character does X in Y" with obvious payoff | A recognisable twist on a familiar structure | Premise, obstacle and payoff all surprising yet inevitable in hindsight |
| 2 | Hook strength (first ≤1.5 s readable as image + first line; curiosity gap or recognition) | 0.15 | Opens on neutral establishing shot / warm-up | Clear problem visible by second 2 | Problem *and* character stance legible in the first frame; works muted |
| 3 | Story coherence (desire → obstacle → escalation → surprise → payoff; payoff resolves the specific premise) | 0.15 | Beats missing or payoff unrelated to setup | All beats present, some generic | Each beat causally forces the next; payoff re-reads the opening |
| 4 | Identity consistency (bible traits drive the choices; identity preserved, evolution justified) | 0.10 | Character interchangeable | Traits mentioned but not load-bearing | Character's rule causes the plot and the ending |
| 5 | Complete audiovisual direction (per scene: timing, action, performance/micro-expression, camera/lens/movement, lighting, environment, sound; captions/transitions where needed) | 0.15 | Dialogue-only or missing camera/audio | All fields present, some vague | Every field concrete and shootable; silent gag has no invented dialogue |
| 6 | Feasibility (fits verified tool controls: ≤30 s/clip, ≤1 cut per generation, prop-persistence rules, manual steps named; retake risks flagged) | 0.10 | Needs crowds, fine hand-object work, multi-speaker shots, unverified controls | Mostly feasible, risks unflagged | Explicitly designed around known failure modes, manual steps separated |
| 7 | Factual grounding (claims about audience/platform/tool are sourced or marked hypothesis; no invented metrics; no firsthand product claims by a fictional character) | 0.08 | Invents metrics or endorsements | Mostly hedged | Every external claim labelled fact / inference / hypothesis |
| 8 | Commercial fit (where the brief has a commercial constraint: product solves a story problem, disclosure present, no false testimonial; else: a plausible later category named without forcing it) | 0.12 | Ad-read or fabricated experience | Product present, somewhat bolted on | Product is the comic/story mechanism; disclosure and rights in the plan |

Efficiency (reported, not weighted into quality): wall-clock latency, number of model calls, measured tokens when exposed by the runtime; otherwise "not independently observable".

## Minimum pass thresholds (all must hold for a packet to be "planning-ready")

- Character intent: dimension 4 ≥ 3 **and** the bible's `rule` or `desire` is named as the cause of at least one scene action.
- Premise-specific escalation/payoff: dimension 3 ≥ 3 **and** the payoff cannot be transplanted to another packet in the same batch without rewriting.
- Distinct hooks/plots/visual language: across the three packets of a batch, no two share the same hook mechanism, the same payoff type, or the same shot list skeleton (judge answers a yes/no "anti-template" question with one sentence of evidence).
- Complete audiovisual direction: dimension 5 ≥ 3 and deterministic validators pass (no missing camera/audio per scene).
- Commercial fit: dimension 8 ≥ 3 when a commercial constraint exists; disclosure and "no firsthand experience claim" present in the packet.
- Weighted total ≥ 3.2 / 5.

## Anti-template test (applied at final acceptance)

Materially different or constraint-perturbed briefs must change: narrative structure, the scene actions, the performance notes, camera plan, sound design and the payoff. If two packets differ only by setting/keywords inside one skeleton, the batch fails regardless of individual scores.

## What this rubric cannot do

Structural validation and judge scores cannot establish creativity in the market, virality or profit. The repetition checker is evidence for a human reviewer, not proof of originality. A tiny comparison (3 briefs × 3 architectures) suggests a choice; it does not prove universal superiority.
