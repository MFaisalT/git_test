# Voice design stage (custom, iconic, locked)

Owner rules (2026-10-08):
- Each character's voice is a custom voice designed from the character, never a stock preset, and it is locked for every production.
- The rejected attempts "all sound like computer voices": Seed Audio cued from the character image, with only speed and pitch changes.

This stage is run by a voice-casting specialist agent. The lead runs the generations and QA. The owner picks. Then the voice is cloned and locked (see docs/VOICE-LOCK.md).

## Inputs
- The character bible: character.*, voice note, performance_register, do_not.
- The episode lines and their time slots.

## The specialist delivers
1. **A voice identity sheet.** Timbre, register, age texture, pace (slowness lives in the gaps, not in stretched words), rhythm, breath, signature habits that viewers can imitate, and what the voice never does.
2. **A locked direction block** of at most 128 characters for Qwen, plus a long form. It travels with every future line, because a clone copies timbre better than delivery.
3. **Performance scripts** for each engine.
4. **A 35-45 s in-character casting monologue** that covers the character's verbal format. It is both the audition and the clone source.
5. **A test matrix of about 6 candidates.** Each candidate tests one hypothesis.

## Engine rules (research, 2026-10-08; sources in docs/VOICE-LOCK.md)

### Seed Audio
- Do not slow it down with speech_rate or lower its pitch with pitch_rate. Uniform time-stretch and formant shift sound robotic.
- Put the slowness into punctuation and pauses instead.

### ElevenLabs v4 (`elevenlabs_v4`)
- Input format: `dialogue: [{voice_type, voice_id, text}]`.
- Set stability to 0.2-0.4 for comedic or emotional delivery and similarity to about 0.8.
- Use one or two inline tags per line, placed right before the words they change: `[inhales]`, `[exhales]`, `[softly]`, `[quietly]`, `[sighs]`.
- Control pacing with punctuation first: an ellipsis gives weight, commas give breath. Never use SSML.
- Use 250+ characters of connected text. Short single lines are less consistent.
- Takes cost about 0.23 credits.

### Qwen Audio TTS (`qwen_audio_tts`)
- The `instruction` is capped at 128 characters.
- Order it as persona → timbre → pace → emotion → context.
- Only some presets support Qwen. Verified on 2026-10-08: Arthur, Alistair and Gideon. Others return "Voice preset is not available".

### General
- Write lines for speech: contractions, fragments, and at most one natural hesitation.
- After generation, add a phone-realism pass in the edit: room tone at about -55 dB and a slight 2-4 kHz cut.

## QA before the owner listens (Higgsfield sandbox)
- A Whisper transcript must match the script. This catches tags read aloud and misheard words.
- Median F0 and the p10-p90 range: a narrow range means monotone.
- Pause lengths between phrases: identical pauses sound machine-like.
- Report all three alongside each take.

## Clone and lock
1. Use the owner-picked monologue take, 35 s-3 min of clean speech.
2. Run `create_voice_from_confirmed_audio` to get an element voice_id.
3. Re-test the clone on the episode line and on one new line.
4. Lock it in the bible: `voice_type element`, `provenance designed_from_character`, `reference_audio`, and the direction block.
