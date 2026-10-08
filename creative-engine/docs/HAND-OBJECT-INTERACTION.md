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

- **Keyframe boards** for product formats (review, unboxing, try-on). The platform's recipe requires inspecting each board before animating it. This session cannot view images, so the owner would inspect boards in the widget before any video is generated from them.
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
