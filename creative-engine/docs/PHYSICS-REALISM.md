# Physics realism: causes, fix, and the prompt-versus-model test (2026-10-08)

## What the owner saw

All three bake-off renders lacked physical realism. Examples: Uncle Verdict's paddle floating in front of his belly with no hand on it; Captain Tempo's whistle hovering in a wide open grin, lips not closed on it, whistle sound with no blowing. Many smaller glitches in all three.

## Causes (ours first, then the model's)

| Cause | Evidence | Ours or the model's |
|---|---|---|
| Prompts of roughly 1,000 words, four scenes, each with 3-4 actions in 3 s | our own adapter output (`prompt_text_full` keeps the old version) | ours |
| Held props with no named hand or resting surface ("he lifts the paddle", then nothing says where it goes) | storyboard text; new `PHYSICS_NO_CONTACT` / `PHYSICS_HANDS_OVERLOAD` warnings fired on every scene | ours |
| A literal contradiction: "clamps the whistle in her teeth and blasts it... grin explodes wide... shouts AND" | Captain Tempo storyboard S2-S4; new `PHYSICS_MOUTH_CONFLICT` fired on S2 and S4 | ours |
| Nothing declared still, so undirected elements drift | public Seedance prompting guides say the model keeps things drifting unless told to hold still | ours |
| Cheapest model tier (Seedance 2.0 Mini) | vendor comparisons report Seedance 2.5 holds objects, liquids and faces better than 2.0, but one reports 2.5 drifts more on mechanical motion; none is independent | model, unverified |

Public guidance (vendor and blog grade, read 2026-10-08): keep prompts roughly 60-260 words with important visuals first; one main action beat per short clip; describe the chain cause, movement, contact, consequence with named contact points and weight; state what stays still; describe what to see rather than what to avoid. Sources: fal.ai, Luma, Runway, Picsart, Magnific prompting guides; Framia's 2.5 vs 2.0 comparison (vendor). Several primary pages were egress-blocked and were read via search snippets only.

## Fix applied (engine, tested: 100 tests)

1. `engine/physics.py`: warnings for mouth conflict, more than two held props per beat, held prop with no contact word, action density over one beat per 3 s on the draft tier, nothing declared still, missing beat. They run in `validate_all` and judge the text the render prompt actually sends.
2. New scene field `physical_beat`: one sentence, at most 40 words, naming who moves what, with which hand, the contact point, what holds still, and any world event the joke depends on.
3. Storyboard prompt module carries a physics contract (two hands, at most two held objects, mouth object means no speech or open grin, one action per 3 s, say what is still).
4. Adapter sends a compact physics-first prompt (~300-380 words: identity, setting, camera, a physics rule block, then one beat per time range with its dialogue). The old dense prompt is kept as `prompt_text_full` for reference.
5. Captain Tempo and Uncle Verdict storyboards repaired: the whistle is blown with sealed lips in its own beat and hangs on its cord whenever she speaks or grins; the paddle is always in his left hand or on his left thigh; the rain and the stranger's dry umbrella stay in the beat.

## The A/B test (same compact prompt, two models)

| Character | v1 (old dense prompt, Mini) | v2 prompt fix, Mini 720p | v2 prompt fix, Seedance 2.5 480p draft |
|---|---|---|---|
| B Captain Tempo | `f8a1f505` | `3134bcab` (12 credits) | `c49c63f8` (36 credits) |
| C Uncle Verdict | `3777de49` | `a07f073b` (12 credits) | `de466b9d` (36 credits) |

How to read it: v1 versus v2-Mini isolates the prompt; v2-Mini versus v2-2.5 isolates the model. If v2-Mini is clean enough, Mini stays the draft tier. If only 2.5 is clean, routing moves prop-handling units to Seedance 2.5 (draft at 480p, then finalize the approved take at 1080p). The session cannot view pixels, so the verdict is the owner's.

## Captain Tempo's point

The owner stopped on B but did not get the point. The intended joke: she counts the crossing down as if she controls the traffic light, the light changes on its own timer, she celebrates as if she caused it, and nobody notices her. If that is not legible in 12 s muted, the fix is in the edit and the next brief, not the renderer: a one-line caption in the first second ("She thinks she controls the traffic lights.") and a closer look at the signal on "AND".
