# Character bake-off (2026-10-08)

## Why

The owner's reference list is loud, physical, public and polarising. The Inspector (`inspector-v1`) is quiet, indoors and procedural. She came from the lab's comedy report, which rewarded a behaviour rule and single-room producibility, not reach. Nothing in the evidence ledger shows a quiet deadpan character cold-starting. The owner asked whether she could trend; the honest answer was "not as designed", and the owner said yes to a three-way character test.

## The three hypotheses (all original; none copies a researched creator)

| | A `inspector-public-v1` | B `captain-tempo-v1` | C `uncle-verdict-v1` |
|---|---|---|---|
| One line | Same Inspector, taken into public space; strangers never react, she is always the culprit | Wiry booming 60-year-old in a teal-and-gold tracksuit who counts the city down and celebrates events that would have happened anyway | Serene 55-year-old in a mustard suit who rates everyday things with total confidence and total wrongness, and doubles down when proven wrong on camera |
| What it bets on | the self-own rule plus "being ignored in public" | loud, physical, public, an original victory move, world's indifference | argument in the comments about taste only (objects, food, habits), never people |
| Register | stillness in a moving world | big, breathless, joyful | seated calm; loudness is in the opinion |
| Signature | two-finger clipboard tap | the Tempo Stomp (original move) | one-finger dial turn, paddle to lens |
| Platform/legal exposure | low | low (no real people, no cleared-dance dependency) | low by design: do_not forbids opinions about people, groups, beliefs, bodies |

Full bibles: `eval/bibles/{inspector-public-v1,captain-tempo-v1,uncle-verdict-v1}.json`. Shared brief: `eval/briefs/CB1_intro_*.json` (12 s public introduction, `render_tier: draft_mini`).

## What the engine produced (real broker workflow, sonnet workers, 0 repairs)

| | A | B | C |
|---|---|---|---|
| Premise selected | bus-stop litter finding; she bins one stub while a ribbon of stubs spills from her own pockets | pedestrian crossing: THREE, TWO, ONE, AND; the light changes on its own timer; Tempo Stomp; a commuter walks through her pose | "Umbrella. Two out of ten. Correct answer: a tiny roof for nobody." Rain starts; a stranger's umbrella passes dry; he turns the dial down to 1: "Final." |
| Format | single_take_static / on_camera_dialogue | single_take_moving_camera / on_camera_dialogue | single_take_static / on_camera_dialogue |
| Creative QA (sonnet) | 3.63 | 3.53 | 3.55 |
| QA's main doubt | familiar hypocrisy gag; tiny props may not render on Mini | face-level identity in a wide shot; dense choreography for one cheap unit | gentle joke; lip-sync and a readable "1" at risk |
| Deterministic gates | PASS, 0 errors | PASS, 0 errors | PASS, 0 errors |
| Route (budget tier) | seedance_2_0_mini 12 s 720p audio, 12 credits | same | same |

Engine changes the bake-off forced (all tested, 97 tests): bible-driven character sheet prompt (sex presentation, hair, lower body), `render_tier: draft_mini` carried into the packet so budget routing applies, adapter media placeholders from the bible registry instead of hard-coded Inspector ids, and a registry rule that an asset with no registry entry cannot be declared owned (a worker had declared a non-existent voice "owned").

## Spend

| Item | Credits |
|---|---|
| Captain Tempo sheet (Nano Banana Pro 2k) | 2 |
| Uncle Verdict sheet | 2 |
| Inspector sheet | 0 (reused variant 0) |
| Three Mini test renders, 12 s, 720p, with audio | 3 x 12 = 36 (measured in the ledger, equal to the quote) |

Render job ids: A `1b95e045-cd7c-4f1e-adf3-04aea5c85203`, B `f8a1f505-369d-47a2-8bc7-8a151f5f5a98`, C `3777de49-7e13-4bbf-9b5b-ea71b63dd8f5`. Records: `projects/charbakeoff/episodes/cb-*/renders/`.

## How to judge (owner; the session cannot view pixels)

1. Watch all three muted first. Which one makes you stop in the first second, and which rule is legible without sound?
2. Then with sound. Does the voice add or distract?
3. Identity: does the face hold against the sheet for 12 s? (Mini is the cheap tier; a winner gets a Seedance 2.5 take.)
4. Energy: which one would you argue about or send to someone? That is the trend test, not the craft test.
5. Say which character wins, or which two to iterate, and what to change. A hybrid (e.g. Uncle Verdict's wrong takes delivered with Captain Tempo's body) is a legitimate answer; it becomes a new bible version with a stated reason.

## What this does not establish

Three 12 s Mini renders are not audience data. They tell you which character you believe in enough to pilot; the pilot (docs/LAUNCH-EXPERIMENT.md) measures the rest.
