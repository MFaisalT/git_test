# Hand-object interaction: research and the staging rules now in the engine (2026-10-08)

## Why this matters

The influencer will review, unbox and try on products. Interaction cannot be avoided, so it has to be staged so current video models render it. The owner's observations on the Uncle Verdict renders: in the Seedance 2.5 draft, when he touched the clock arm at the end, it moved unnaturally; in the Mini render, when he touched the arm, another arm appeared from the centre of the clock, reaching his pointing finger.

## What the evidence says

**Research (peer-reviewed and preprints).** Hand-object contact and hand structure are still the weakest region of video diffusion models. CoInteract (2026) targets e-commerce and advertising and names the two failures we saw: structural instability of hands and implausible contact such as hand-object interpenetration. Its fix conditions generation on a person reference, a product reference and explicit interaction geometry. Other work (SCAR 2025, SViMo 2025, HVG-3D 2026, Re-HOLD CVPR 2025) conditions on contact maps, layouts, 3D structure or keyframes. Physics surveys (PISA 2025, NewtonRewards 2025, VideoREPA 2025, LikePhys 2025) agree that objects float, drift and collide wrongly, and that this improves with model scale but is not solved. None of these controls are exposed on Higgsfield; the available equivalents are reference images and keyframe stills.

**Practitioner sources (vendor and blog grade).** Hands warp, fuse with the product or grow fingers. Common fixes: two or three product reference angles, explicit grip wording, a still keyframe as an anchor, and region edits in post for small defects. Kling 3.0 is often named for product-handling b-roll and Veo 3.1 for talking hooks; these rankings are unverified.

**The platform's own production recipe (strongest source).** Higgsfield's bundled `ugc-video` workflow (unboxing, try-on, review, tutorial) was read in full. It names the failure modes and the staging that avoids them:

| Failure mode | Staging rule |
|---|---|
| Phantom third arm | At most two hands act, each named; the free hand is parked somewhere specific; an unheld object beside busy hands also spawns a third hand, so every object is held or resting, explicitly |
| Both states of an object rendered (our extra clock arm) | Every state change is a shown action, cause before effect; fiddly mechanics happen across a hard cut: state A, cut, the next shot opens already in state B |
| Motion loops | One interaction per cut; no "again", "twice", "repeatedly", "back and forth" |
| Product multiplying or morphing | Exactly one instance; front label side only; never rotated or spun; angle changes only by cuts |
| Duplicated limbs and bodies | No mirrors or reflections |
| Stiff, puppet-like presenters | Every cut opens mid-action; small body micro-beats, one movement at a time |
| Wrong weight | Heavy items: both hands and visible effort; light: one relaxed hand; tiny: thumb and index |
| Try-on artefacts | Dressing is never shown (hard cut to already wearing it); fabric moves only from the body (turn, breath, step); no hands touching the garment in close-ups |

Their physical formats also generate keyframe **boards** first (a strip of 4 or 8 stills, one per beat, each naming every hand's role), clean them, inspect them, and only then animate on Seedance 2.5 with the board as a sequence and timing reference.

## What the engine now does

- `engine/interaction.py` warns on: on-screen state change of a mechanism, loop wording, mirrors, a manipulated object with no named hand, a single named hand with the other unparked, a heavy object lifted one-handed.
- New scene field `state_change_by_cut`: the scene opens already in the end state after a hard cut.
- The storyboard prompt carries the hand-object contract above, including try-on rules.
- The render prompt adds a hand rule line and the platform's negative list (no third arm, no extra hands, no duplicated limbs, no extra fingers, no deformed hands, exactly one of each prop, no mirrors, no slow motion). Per-beat camera moves are restored and never trimmed. Hard cuts are written as "Hard cut to."
- Uncle Verdict's ending is restaged: the paddle at 2, hard cut, the paddle already at 1 in his hand, "Final." Caption: "He rates everything. He is always wrong." Captain Tempo says "GO!" instead of "AND", with the caption "She thinks she controls the traffic lights."

## Test renders (2026-10-08)

| Clip | Model | Job |
|---|---|---|
| Uncle Verdict v3, dial change across a cut | Seedance 2.0 Mini 720p | `04e8ad70` |
| Uncle Verdict v3 | Seedance 2.5 480p draft | `197118cc` |
| Captain Tempo v3, camera per beat, GO | Seedance 2.0 Mini 720p | `c3087214` |

## Not yet built

- **Keyframe boards** are built for a single shown interaction (see "Shown interaction, keyframed" below). Multi-beat boards (a 4 or 8 still strip for a full unboxing) are not built yet. This session cannot view images, so the owner inspects boards in the widget before any video is generated from them.
- **Product references**: one product instance, front label, two or three angles uploaded by the owner for real products.
- Whether Kling 3.0 or Seedance 2.5 handles product handling better is untested here; it needs a same-prompt comparison with a real product.

## Sources

Research: [CoInteract](https://consensus.app/papers/details/b1b0cedd07065d9a81d8158c548ded56/), [SCAR open-world HOI video](https://consensus.app/papers/details/80c1880a17b0560f91c1a26791c9ed6f/), [SViMo](https://consensus.app/papers/details/3981875386c95409ab4e4dff9484d680/), [HVG-3D](https://consensus.app/papers/details/56f94370730f52289f0259e07e86cb3b/), [Re-HOLD](https://consensus.app/papers/details/796eaa5c813f5cee9d4c37c189bf9d8b/), [PISA](https://consensus.app/papers/details/b608a62af6f853e79c5d0743601480b5/), [NewtonRewards](https://consensus.app/papers/details/eabfcff739ed502186b2cfce3f77ceb7/), [VideoREPA](https://consensus.app/papers/details/a7899f40af5751848259ffd61db833d2/), [LikePhys](https://consensus.app/papers/details/add5b20071b25b3bad308a011125d49c/), [iDiT-HOI](https://arxiv.org/pdf/2506.12847), [SparseCtrl-HOI](https://arxiv.org/pdf/2607.05994). Practitioner: [Medium UGC prompt](https://mateostarcevicfilipovic.medium.com/the-one-prompt-that-makes-ai-ugc-ads-stop-looking-plastic-copy-it-below-55b0a4fccdc3), [Morphic Seedance guide](https://morphic.com/resources/how-to/seedance-2-guide), [Flyne Kling vs Seedance](https://flyne.ai/blog/detail/Kling-3-0-vs-Seedance-2-0-Which-AI-Video-Model-Fits-Your-Creative-Workflow-on-Flyne-AI-91bf4c1ccf95/), [Kling try-on guide](https://app.klingai.com/global/quickstart/ai-virtual-try-on-guide). Platform: Higgsfield `ugc-video` workflow bundle (boards.md, ugc-unboxing-board.md, ugc-unboxing-clip.md, ugc-try-clip.md).

## Result of the staging test (owner inspection, 2026-10-08)

Owner frames from Uncle Verdict v3. Seedance 2.5 draft: the cut-staged change worked (2, hard cut, 1 already in his hand; no extra arm); grip on the paddle and palm on the umbrella held; rain and the passing umbrella landed. Defects: the paddle rendered as a clock face with duplicated numerals, and a ring appeared. Seedance 2.0 Mini: the paddle showed 2 and 1 at once (both states again, despite the cut staging), invented text around the rim, a clip-on microphone and a second umbrella handle appeared, a passer-by vanished mid-shot with a small jump, and "Final" was said twice.

Causes and fixes:
- **Clock face:** our bug. The compact prompt dropped the props list, so the model only saw "paddle" and "dial". Fixed: a props line with each prop's exact design, never trimmed.
- **Duplicated numerals and invented text:** small text is a known failure; the platform's rule is big print only. The scoring prop should show one large numeral and nothing else.
- **Ring, microphone:** the identity line now forbids accessories not in the reference.
- **Repeated last word:** lines are now written "says once" and the sound line ends "each exactly once, then silence".
- **Mini:** routed away from any unit with dialogue or handled props, even on the cheap test tier; Mini stays for silent, hands-free clips only. Seedance 2.5 draft (36 credits per 12 s) becomes the test tier for interaction.

## Five-model comparison on one identical prompt (2026-10-08)

The owner asked for this so the comparison is fair: every clip below used the same current Uncle Verdict prompt, the same reference still (`cb1f3458`), 12 s, 9:16, with audio on. The earlier Mini and 2.5 clips used older prompts, so Mini and 2.5 were re-rendered for this test.

| # | Model | Res | Credits (charged) | Job |
|---|---|---|---|---|
| 1 | Seedance 2.0 Mini | 720p | 12 | `fab09815-da4b-4b40-be21-90c6c75c88c6` |
| 2 | Kling O3 (std, image reference) | 720p | 15 | `30625b53-9856-40f2-9247-376b4f63866a` |
| 3 | Seedance 2.0 fast | 720p | 30 | `f39a8cfd-0029-4ec8-b93f-b7f3d6dedbd4` |
| 4 | Seedance 2.5 draft | 480p | 36 | `e4fd3681-5de5-4cdb-a66d-57d42d9208fc` |
| 5 | Cinema Studio 4.0 (no control ids set) | 480p | 36 | `1e996219-8648-4325-95ef-4795cf3854da` |

Every charge matched its quote. The session cannot view pixels, so the verdict belongs to the owner. Checklist:
- Paddle at 2, then a hard cut to the paddle at 1, with no morph on screen.
- Hands: two at most, with no extra hand or arm growing from the prop.
- Exactly one umbrella and one paddle; no added ring, watch or mic.
- Passers-by don't vanish and the frame doesn't jump.
- "Final." is said once.
- Camera feel.

**Owner verdict:** Cinema Studio 4.0 best, Seedance 2.5 second. The engine now routes identity-critical units up to 15 s to Cinema Studio 4.0, with Seedance 2.5 as the fallback.

**Defect in the Cinema Studio clip (owner frames):** the paddle rendered as a clock face with random numerals (23, 40, 51, -6, 55...) around a large "2", and no pointer arm. The prompt only said "large wooden scoring paddle with a 0-10 dial". The prop was underspecified.

## Shown interaction, keyframed (implemented 2026-10-08)

The owner's direction: his hand should interact with the paddle. The research above said how; this is the implementation. The earlier "always hide it behind a cut" rule was avoidance, not the fix.

**What the research and platform recipe prescribe, and what the engine now does:**

| Prescription | Engine |
|---|---|
| Exact object design, plus a product reference image | Bible `props[]` with `design` text and `reference_asset`. The render prompt replaces the short prop name with the exact design and ties it to its `@image` slot. The reference goes into `image_references` after the character. |
| One interaction per shot | `scene.interaction` makes the scene its own generation unit, never merged. `INTERACTION_SHARED_UNIT` is an error. |
| Name the hand, the contact point and the other hand | `interaction` requires actor_hand, contact, object, part, from_state, to_state, motion and support_hand (`INTERACTION_SPEC_INCOMPLETE`, error). The prompt gets one deterministic sentence built from them. |
| Keyframe anchors, inspected before animating | `interaction.keyframes.start/end` become `start_image` / `end_image`. Missing keyframes are an error (`INTERACTION_KEYFRAMES_MISSING`). Keyframes not yet approved by the owner are a warning not to animate yet. The first manual step in the plan is the board. |
| Slow, continuous move with a held end beat | At least 3 s (`INTERACTION_TOO_SHORT`). The prompt says "one slow continuous move and stops". |

Incidental state changes can still go across a hard cut (`state_change_by_cut`). A shown interaction is the default when the moment is the point: reviews, unboxing, the signature gesture.

**Uncle Verdict v4 restage:**
- U1, 0-8 s: the verdict, then the rain.
- Hard cut.
- U2, 8-12 s: medium close-up. The paddle is held up by the left hand. The right index fingertip pushes the pointer from 2 to 1, then he says "Final."

The bible is v3 and carries the paddle design: a light oak board, a white semicircular gauge, numerals 0-10 in order along the arc, and one black pointer on a brass pin.

| Asset | Model | Job | Credits |
|---|---|---|---|
| Paddle reference still | gpt_image_2_5 high | `4c094812-ad7e-44df-a34a-48287565877c` | 1.5 |
| U2 start keyframe (pointer at 2, fingertip on the tip) | gpt_image_2_5 high, refs: character + paddle | `70f2656d-22ca-422a-9bde-0d87667de225` | 1.5 |
| U2 end keyframe (edit of the start frame: pointer at 1) | gpt_image_2_5 high, refs: start frame + paddle | `7ec903a7-e304-43af-af3c-f7d9896e7c82` | 1.5 |

Next step: the owner inspects the three stills, checking the numerals 0-10 in order, one pointer, two hands with five fingers, the fingertip on the pointer tip and the same face. Only then is U2 animated on Cinema Studio 4.0 at 480p (4 s, about 12 credits), with Seedance 2.5 draft as a second take.

### Image-model correction and the one-time NB 2 test (2026-10-08)

The owner pointed out that the first board was made on `gpt_image_2_5` (Flare variant), while the engine recommends Nano Banana Pro. That was an ad-hoc pick. The engine now routes prop references and keyframes through `route_image_asset("prop_reference" | "keyframe")`, which returns NB Pro, and the adapter's keyframe step names it.

All three chains ran the same three prompts: paddle, start frame, end frame. Each chain used only its own outputs as references; the character reference `cb1f3458` is shared. All images are 2k.

| Step | NB Pro (recommended) | NB 2 (one-time test) | GPT Image 2.5 (first board, comparison only) |
|---|---|---|---|
| Paddle | `3a640e87-c426-48ff-bb01-b679ce36b0ed` | `178cebe1-d735-4ab7-b8bb-b40859ab75e0` | `4c094812` |
| Start frame (pointer at 2) | `e38bd7f1-3fca-4d58-8f64-03ad49a46a3d` | `057d8420-bc13-4413-a13b-eebbfef7e5bd` | `70f2656d` |
| End frame (pointer at 1) | `7a0020db-9398-4a5f-9320-12e2772e4cc2` | `9511f27f-26e5-4da2-ac4e-2afc24f74fe6` | `7ec903a7` |
| Credits | 3 x 2 | 3 x 2 | 3 x 1.5 |

Backend naming: jobs submitted as `nano_banana_pro` report `nano_banana_2`, and jobs submitted as `nano_banana_2` report `nano_banana_flash`. The engine records the requested id and the reported id side by side.

The owner picks the chain. The winner's job ids replace the keyframes in Uncle Verdict's S3 interaction and the paddle's `reference_asset`. Animation follows only after that pick.

### First keyframed interaction renders (2026-10-08)

The owner picked the NB Pro board. Unit U2 (4 s) was animated with the same prompt and the same four media on both models. The completed jobs report the media roles start_image `e38bd7f1`, end_image `7a0020db` and references `cb1f3458` (character) and `3a640e87` (paddle). The roles survived, even though the submit echo listed all four as reference_images.

| Model | Job | Res | Charged |
|---|---|---|---|
| Cinema Studio 4.0 | `77ecb61d-da10-4d4c-87c5-534891a30fc1` | 480p | 12 |
| Seedance 2.5 draft | `6ec44d5b-551c-4d2f-bfba-94dbbe7f60c6` | 480p | 12 |

The owner judges these. Checklist:
- Does the fingertip stay on the pointer tip and push it, rather than the pointer moving by itself?
- Does the pointer rotate on the pin, with no second pointer?
- Do the numerals stay 0-10?
- Does the left hand hold still?
- Is "Final." said once, after the move?

**Owner verdict on the keyframed push:** Cinema Studio 4.0 (`77ecb61d`) is "more realistic than the other by far". Interaction units stay on Cinema Studio 4.0, with Seedance 2.5 as a fallback only. U1 (0-8 s, the verdict and the rain) was then rendered on Cinema Studio 4.0 at 480p as job `a60ce385-edde-4b12-89ff-71719dca8362` (quoted 24 credits), to pair with U2 for a full 12 s review. Before this render, S1's beat was changed to state "pointer at 2" so it matches U2's start frame.

### Owner review of the full Cinema Studio pair, and the UGC restage (2026-10-08)

**Owner feedback:**
- The pointer moved from about 4 to 1, not from 2.
- The camera has no creative micro-movement.
- The camera transition to a close-up before "Final." is missing.
- "Final." is never said.
- "It needs more artistic UGC style direction."

**Causes:**
- The bible said "locked-off phone", and every shot inherited it.
- The compact prompt cut per-beat camera direction at the first comma.
- "Final." shared the 4 s interaction shot with the hand move, so the move used up the time.
- The shot never stated where the pointer starts.

**Engine fixes:**
- `engine/camera.py` warns on `CAMERA_DEAD` (locked camera with no micro-movement) and `CAMERA_PUNCHLINE_FLAT` (the last line is not delivered in a closer framing).
- Per-beat camera direction is no longer truncated.
- An interaction must open its unit, and continuous scenes may follow it in the same shot. A line spoken during the move raises `INTERACTION_LINE_CROWDED`.
- The interaction sentence states the opening position and forbids any travel outside from -> to.
- The storyboard prompt now carries the camera and punchline rules.

**Uncle Verdict v5:**
- The bible (v5) now uses handheld UGC visual language.
- U1, 0-6 s: the verdict with a handheld creep-in, then the rain with a tilt and a reframe to the passing umbrella.
- Hard cut.
- U2, 6-12 s, one continuous handheld shot:
  - 6-9 s: the fingertip pushes the pointer from 2 to 1 (keyframed).
  - 9-12 s: the camera pushes in to a tight close-up, he lifts his eyes and says "Final.", then silence.
- U2 keyframes:
  - Start: `e38bd7f1` (approved).
  - End: new close-up `e30afec1-bd94-40bd-bd45-862032157fd3` (NB Pro, 2 credits), pending owner inspection.

Rendering stays blocked until the owner picks Uncle's voice (voice lock).

### Locked plate: closer framings are crops, never regenerations (2026-10-08)

**Defect (owner frame):** the regenerated close-up end frame `e30afec1` showed the gauge as 0 1 1 2 3, with the "1" doubled.

**Inspection:** this session could see the frames for the first time, via the Higgsfield sandbox (it fetches the generated images and returns them as images). The approved frames are correct:
- `e38bd7f1`: the pointer is near 2, and the dial reads 0-10 in order.
- `7a0020db`: the pointer is on 1.

Only the regenerated close-up is wrong.

**Cause:** an image model redraws the whole frame for a new framing. Text and small props are re-synthesized, not copied, and text rendering is a known weak point ([unite.ai](https://www.unite.ai/why-your-ai-images-come-with-errors-and-how-to-improve-them), [HN: underdrawings for accurate text and numbers](https://hn.nuxt.dev/item/47977990)). The standard way to fake a push-in is to crop and scale one correct master frame ([LRTimelapse forum](https://forum.lrtimelapse.com/thread-5453.html)). No source tests this on AI video models, so the engine treats it as a rule to verify on our own footage.

**Fix (the owner's "locked environment"):**
- The U2 end frame is now a pixel-exact crop of the approved `7a0020db`: box (583, 357, 706, 1255), about a 2.2x push-in.
- It was made in the sandbox with PIL and uploaded as media `4611a013-46d6-4b07-9a83-f71dfc2f1c09`.
- The face, paddle, numerals and pointer are identical to the approved frame.
- Schema: `keyframes.end_derivation {method: crop|edit|generate, source, box}`.
- The engine warns `KEYFRAME_FRAMING_REGENERATED` when a closer end frame is regenerated.
- The adapter's keyframe step says crops are made in the sandbox.

### U2 ending with the locked voice (2026-10-08)

**Job `31072c5c` (CS4, 480p, 18 credits).** Frames checked in the sandbox:
- **Camera:** the punch-in to a close-up is visible between 3.6 s and 4.5 s.
- **Line:** "Final." is said once, at 4.3-5.0 s.
- **Voice:** it held the lock (correlation 0.962).
- **Defect:** the pointer swung from about 2 up to 5, the wrong way, and ended on 5. CS4 took its framing from the end frame but not the pointer state.

**Fix:**
- New interaction field `direction` for rotating parts. For this shot: "counter-clockwise, one notch (about 18 degrees), toward the 0 end; the tip moves down and to the left, never up toward 5".
- The end state is restated in the end-frame sentence.

**Retake:** `18a32f05`.

**Episode draft:** U1 `17fe9dae` and U2 `31072c5c` were joined in the sandbox into a 12.1 s file and uploaded as media `b972af6c-e822-4c89-b606-af5c541ae4d8`.

**Retake `18a32f05` (18 credits): pass.**
- **Pointer:** starts near 2, rotates counter-clockwise, and is on 1 by 3.0 s. The `direction` wording fixed it.
- **Camera:** punch-in from 3.0 to 4.2 s.
- **Line:** "Final." is said once, at 3.4-4.8 s, in the close-up.
- **Voice:** held the lock (correlation 0.969).
- **Minor:** the pointer is out of frame in the close-up.

**Full episode, take 2:** U1 `17fe9dae` + U2 `18a32f05`, 12.2 s, media `4231584f-8ce6-44d7-9326-c438064aff77`.

**Still open in U1:** the rain and the passing umbrella are missing, because the speech filled the slot. The fix is to start the rain under the line.

### First cold-viewer check (2026-10-08, episode `648c2168`, locked-voice "Final.")

A fresh reviewer with no brief or context went through three rounds: 2 s muted, the whole clip muted, then with the transcript.
- **Engine score (`engine/cold_viewer.py`):** verdict "pass" (muted coverage 0.5, with speech 0.75).
- **Stop scrolling:** weakly yes, because of the costume and prop. Nothing happens in the first 2 s.
- **Muted read:** "rain, he never opens the umbrella, lowers the needle". It misread the dial as his mood.
- **With the words:** it got the joke exactly. "The joke is on him, the snob who would rather get wet than admit the umbrella works." Comment: "Sir, the tiny roof was for YOU."

**Problems it named:**
1. The dial looks like a different prop in the close-up because the "0" is missing. Cause: his fingertip covers the 0 in the approved source frame. A wider crop does not help. Staging rule for next time: keep the hand clear of the scale's end numerals.
2. "Final." alone lands flat, and you have to read the needle to get the punchline. Candidate line: "One. Final." (owner's call).
3. About 5 s with no speech in the middle (5.5-10.3 s). The v7 restage puts the rain under the line. A dial-click foley on the move would fill the push; the bible already asks for an "exaggerated dial click".
4. "Correct answer" confused a cold viewer ("correct answer to what?"). It is part of the bible's fixed verdict format, so changing it is the owner's call.
5. The spliced "Final." sounds quieter and drier than the opening line. The level was matched to the model's quiet word, so it needs a louder mix and matching room reverb.
