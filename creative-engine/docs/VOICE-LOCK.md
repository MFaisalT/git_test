# Voice lock: one character, one voice, forever

**Owner rule (2026-10-08):** "Make a strict hard rule that any given character does not change voice id between generations or scenes ever on all future productions."

**Why:** Uncle Verdict's two Cinema Studio units (`a60ce385`, `77ecb61d`) came out with different voices. Neither render had an audio reference, so the video model invented a voice per clip. That is the default behaviour of every video model with native audio.

## The lock

Each character bible has `approved_assets.voice`:

| Field | Meaning |
|---|---|
| `voice_id`, `voice_type`, `name` | The Higgsfield voice (`list_voices`; preset or a cloned "element") |
| `reference_audio` | Job id of a speech clip generated in that voice (`seed_audio`). It is passed as `audio_references` to every spoken video render, and the prompt says "every spoken word is in exactly the voice of @audio1". |
| `status` | Must be `locked` |

## Enforcement (engine/voice.py, all tested)

- **Bible store:** `save_bible` refuses any new version that changes `voice_id`, `voice_type` or `reference_audio`, or that removes the lock (`VoiceLockError`). A different voice means a different character, with a new `bible_id`.
- **Validation:** a packet with any dialogue and no locked voice fails with `VOICE_LOCK_MISSING`.
- **Adapter:** spoken units carry the locked reference audio, never a placeholder. Without a lock, the unit is `render_blocked` and validation fails with `RENDER_BLOCKED`. A model that cannot take an audio reference is blocked too.
- **Render records:** every spoken render records its `voice_id`. `render_voice_findings` flags any render whose voice is not the locked one (`VOICE_DRIFT`).
- **Excluded assets:** voices built from the excluded creative assets (the "Elias" voices in the account) are refused (`VOICE_FORBIDDEN`).

## Status of existing characters

| Character | Voice | Render status |
|---|---|---|
| Uncle Verdict | Not locked: the owner is choosing from 8 preset samples of his actual line | Blocked (`U1`, `U2`) |
| Captain Tempo | Not locked | Spoken packets blocked |
| Inspector (public) | Not locked | Spoken packets blocked |

**Untested:** how faithfully Cinema Studio 4.0 and Seedance 2.5 clone a voice from `audio_references`. The first locked render will tell us. If the clone drifts, the fallback is to generate the lines in the locked voice with `seed_audio` and lay them in the edit (or lip-sync), with the video rendered silent.

## Uncle Verdict voice samples (2026-10-08)

Each sample is his line "Umbrella. Two out of ten. Correct answer: a tiny roof for nobody. Final." on `seed_audio`, at 0.5 credits each. The owner picks one. The chosen sample's job id becomes `reference_audio`, and the lock is then permanent.

| # | Voice | Age tag | voice_id | Sample job | Length |
|---|---|---|---|---|---|
| 1 | Grady | middle-aged | `e2a2d2e6-9ed2-59cd-82af-feaa27f8a678` | `c855fd6e` | 9.0 s |
| 2 | Holden | middle-aged | `3c9d6053-6334-592c-8997-4e325286af3f` | `03d2693e` | 6.5 s |
| 3 | Arthur | old | `30fc8796-ceb6-4a66-b3a7-4a145ef7f346` | `1491b64b` | 6.9 s |
| 4 | Desmond | middle-aged | `563f728c-e249-5a85-97ab-8461e8c09da6` | `c3c4a98d` | 7.3 s |
| 5 | Barrett | middle-aged | `d603a8cd-3fe1-55e0-9245-617a2589131e` | `edada10c` | 6.9 s |
| 6 | Harrison | young (platform tag; likely too young for a 55-year-old) | `573e5163-59b3-4926-aab1-951ef2985f81` | `a8adb3a6` | 6.9 s |
| 7 | Alistair | old | `d9d5c263-f84e-4752-97b5-3750fcc6fd2f` | `dc8cde3c` | 6.9 s |
| 8 | Gideon | middle-aged | `1ad38ba4-9cc4-4f2f-9fde-b0fefdf67ae5` | `f0e5b755` | 7.3 s |

The two "Elias" voices in the account were excluded.
