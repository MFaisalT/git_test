# Verified tool capabilities and field mapping (read-only checks, 2026-10-07 UTC)

## Higgsfield (via MCP server in this session; no job submitted, no media imported)

`balance` → credits **981.16**, plan **ultra** (matches the lab's 20:28 UTC capture; still a point-in-time counter, not an entitlement).

`models_explore(get)`:

| Model | Duration | Aspect ratios | Resolution | Audio | Media roles | Notes |
|---|---|---|---|---|---|---|
| `seedance_2_5` | 4–30 s | auto, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 | 480p/720p/1080p | `generate_audio` bool | start_image, end_image, image_references, video_references, audio_references | modes t2v / omni_reference / video_edit / video_extension; draft→finalize |
| `seedance_2_0_mini` | 4–15 s | auto, 16:9, 9:16, 4:3, 3:4, 1:1, 21:9 | 480p/720p | `generate_audio` | same five roles | cheapest quoted (8 credits / 8 s / 720p on 2026-10-07; quote ≠ measured cost) |
| `kling3_0` | 3–15 s | 16:9, 9:16, 1:1 | std/pro/4k | `sound` on/off | start_image, end_image | "multi-shot, audio sync, motion transfer" per catalogue text; motion transfer input role not exposed in this listing |
| `hf_mult_motion_control` (Genjutsu) | ≤30 s (driving video) | — | 480p/720p/1080p | none | image_references + video_references | requires owned/licensed driving footage; 3 free uses remained at the 20:28 capture, shared across four Genjutsu ids |

`generate_video` params verified: `model`, `prompt` (free text), `duration`, `aspect_ratio`, `resolution`, `generate_audio`, `medias[{value: media_id|job_id, role}]`, `mode`, `bitrate_mode`, `genre`, `sound`, `count`, `get_cost` (preflight), `use_unlim`, `folder_id`.

**Verified negative:** there is no structured/JSON prompt input. The internal episode-packet JSON is an engine contract, **not a native Higgsfield payload**. A public search (2026-10-07) found only third-party Seedance prompt-format guides and the Higgsfield SDK page (flat `arguments` dict with a string `prompt`); no official JSON schema. The adapter therefore composes `prompt_text` and lists everything else as manual or gap.

## Field → control map (implemented in `engine/adapters.py`)

| Packet field | Mapping | Note |
|---|---|---|
| scene.action / performance / microexpression / camera.* / lighting / environment | prompt_text | No separate controls; lens is language only |
| scene.sound.ambience | native `generate_audio=true` + prompt_text | Exact SFX timing not controllable |
| scene.sound.music | manual | Licensed track added in edit; never rely on generated music for rights |
| scene.dialogue | prompt_text (+ optional `audio_references` for a pre-generated voice on Seedance) | Lip-sync quality unverified; inspect |
| captions / on-screen text | manual (edit) | Models render text unreliably |
| transitions between generation units | manual (edit) | ≤1 hard cut inside one clip, described in prompt |
| continuity.identity_anchors | native `image_references` + verbatim anchor text | Identity drift is a known failure; inspect |
| duration / aspect_ratio / resolution | native | Clamped to model range by adapter |
| export.fps / container | gap | Not controllable; verify on exported file |
| disclosure | manual | Platform branded-content tool + caption/spoken line |
| approval / credit cap | engine gate | `get_cost:true` preflight recorded before any submit; submit only after `render_approved` and `credit_cap` |

## Other owned tools

- ChatGPT subscription: not reachable from this container; the lab's authorised sidebar Project remains pending (capability blocker recorded in PROJECT-STATUS.md). Engine prompts are plain Markdown and can be pasted there manually; no claim that this was done.
- Platform official pages (TikTok newsroom/support, Google support, Instagram help) are egress-blocked from this container; the lab's 2026-10-07 captures in `commercial-report.md` are reused and labelled as such in `docs/NICHE-DECISION.md`.

## Dry-run contract

`python -m engine adapter <packet.json>` prints the plan. It never calls the tool. Rendering requires: owner approval (`engine approve --render --credit-cap N`), uploaded approved references (`media_upload`, owner action), a recorded `get_cost` preflight, then a human-initiated `generate_video`. After rendering, the packet may move to `rendered-verified` only with a complete `qa.render_inspection` (identity, continuity, timing, lip-sync/audio, artefacts, readability, music rights, tech specs, disclosure).


## Production routing (added 2026-10-07 after the owner's request to optimise for Higgsfield: Nano Banana Pro / NB 2 (to test) / Seedance 2.5 / Cinema Studio)

Catalogue re-read via `models_explore` (get/search/recommend) and credit preflights via `generate_video`/`generate_image` with `get_cost=true` (no jobs submitted). Implemented in `engine/routing.py`; applied by `engine/adapters.py` per generation unit and per reference asset.

### What the catalogue actually exposes

| Model id | Kind | Range / res | Identity refs? | Notable | Quote (9:16, 720p) |
|---|---|---|---|---|---|
| `nano_banana_pro` | image | 1k/2k/4k | image_references | "ultimate quality, text and diagrams"; unlim-capable | 2 credits (16:9, 2k) |
| `nano_banana_2_1` ("NB 2") | image | 1k/2k/4k | image + video refs, inpaint mask, thinking_level, seed | **the NB 2 the owner wants tested** - untested here | 2 credits (16:9, 2k) |
| `seedance_2_5` | video | 4-30 s, 480p/720p/1080p | image/video/audio refs | modes t2v / omni_reference / video_edit / video_extension; **480p draft -> finalize within 7 days** | 112 / 16 s; draft 48 / 16 s; 56 / 8 s |
| `seedance_2_0_mini` | video | 4-15 s, 480p/720p | image/video/audio refs | cheapest; genre hint | 15 / 15 s; 8 / 8 s |
| `cinematic_studio_video_4_0` (Cinema Studio 4.0) | video | 4-30 s, 480p-1080p | image/video/audio refs | **native** `camera_model_id`, `camera_lens_id`, `camera_aperture_id`, `light`/`light_id`/`light_custom`, `pacing_id`, `genre_id`, `era_id`, `color_palette` - all take creative-control ids from a catalogue this build has not retrieved | 112 / 16 s |
| `cinematic_studio_3_0` (Cinema Studio Video 3.0) | video | 4-15 s, up to 4k | **no** identity refs (image/start/end only) | premium look | 75 / 15 s |
| `cinematic_studio_video_v2` | video | 3-12 s | no identity refs | `multi_shots` + `multi_prompt`, `speedramp` | not quoted |
| `kling3_0` | video | 3-15 s | start/end only | multi-shot, audio sync | not quoted |
| `hf_mult_motion_control` | video | <=30 s driving clip | image + video refs | Genjutsu motion transfer | not quoted (3 free uses at the lab's capture) |

### Routing table

| Job | Model | Why | Status |
|---|---|---|---|
| Character reference sheet | nano_banana_pro (NB 2.1 to be tested) | 2k/4k, image refs, split-screen sheet recipe | verified controls / NB2.1 untested |
| Location stills (reused per location) | nano_banana_pro | 9:16 2k empty lived-in scene with planned key light | verified controls |
| Video <=15 s, silent or draft | seedance_2_0_mini | identity refs + audio, 15 credits/15 s quoted | verified controls |
| Video with dialogue / identity-critical, <=30 s | seedance_2_5 omni_reference (480p draft -> 1080p finalize) | image + audio refs (voice lock), native audio; 112 credits/16 s/720p, draft 48 | verified controls |
| Single take > 15 s | seedance_2_5 omni_reference | only identity-ref model besides Cinema 4.0 that reaches 30 s | verified controls |
| Premium cinematic look, character off-frame | cinematic_studio_3_0 | 4k, premium; no identity refs | recommended, untested |
| Native lens/lighting/pacing controls | cinematic_studio_video_4_0 | exposes camera_lens_id, light_custom, pacing_id... but needs control ids not retrieved | gap |
| Multi-shot inside one clip | cinematic_studio_video_v2 (multi_shots) or kling3_0 | native shot planning; no identity refs -> use for inserts only | recommended, untested |
| Owned footage re-cast | hf_mult_motion_control | Genjutsu; driving video + character refs | verified controls |
| Continuation (part 2) | seedance_2_5 video_extension | extends an approved clip | recommended, untested |

### Recommendation and honesty notes

- **Default production stack**: Nano Banana Pro for all reference stills (character sheet via the Higgsfield character-sheet slot recipe, location stills reused per location), Seedance 2.5 `omni_reference` for anything with dialogue, voice lock or >15 s, Seedance 2.0 Mini for <=15 s silent units and drafts. This keeps identity references in every video model used.
- **Draft-then-finalize** is the main cost optimisation the catalogue verifies: a 16 s Seedance 2.5 draft at 480p is quoted at 48 credits vs 112 at 720p; approve the take on the draft, finalize once at 1080p.
- **Cinema Studio**: 4.0 is the only model with native lens/lighting/pacing controls - exactly the fields the packet carries - but it needs control ids we have not retrieved, so it is marked **gap** and the adapter keeps lens/lighting as prompt text until a read-only listing of those ids is obtained. 3.0 lacks identity references, so it is only recommended for shots where the character is not in frame. Neither has been generated or inspected here.
- **NB 2 (nano_banana_2_1)**: exposed, same 2-credit quote, adds video references and inpainting; set `nb2_testing=True` in `asset_requests` to route reference stills to it for the owner's comparison test. Untested.
- Quotes are preflights, not measured completed-output costs; retake multipliers (2-4x) are untested assumptions. "Status" per unit distinguishes verified controls, recommended-untested and gap.

### 2026-10-08 addendum: first measured costs and the Cinema Studio 4.0 gap

- Owner-approved generations: `nano_banana_pro` 2k stills x4 = 8 credits (2 each, as quoted); `seedance_2_0_mini` 12 s / 720p / 9:16 / silent with two image refs (job ids used directly as `medias` values, which works) = 12 credits, as quoted. Jobs for the stills report `model: nano_banana_2` while the ledger display name is "Nano Banana Pro"; the discrepancy is logged, not resolved.
- Video submit behaviour: the first `generate_video` call was intercepted by a preset recommendation ("IN THE DARK"); resubmitting with `declined_preset_id` runs the literal prompt. The adapter notes this as a manual step.
- Cinema Studio 4.0 (`cinematic_studio_video_4_0`): `get_preset_instructions` has no cinema-studio entry and `models_explore` search returns only `cinematic_studio_video_v2` (genre / speedramp enums). The 4.0 control ids are not exposed through MCP; **gap confirmed**.
- Resolution policy for masters and exports: `docs/RESOLUTION-POLICY.md`.
