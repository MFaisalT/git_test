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
