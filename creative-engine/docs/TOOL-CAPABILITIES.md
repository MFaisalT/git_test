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
