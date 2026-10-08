"""Voice lock: one character, one voice, forever (owner rule, 2026-10-08).

Owner: "Make a strict hard rule that any given character does not change voice id between generations or scenes ever on all
future productions." Cause: Uncle Verdict's two Cinema Studio units (a60ce385, 77ecb61d) were rendered without an audio
reference, so the video model invented a different voice per clip.

The lock, in the bible's approved_assets.voice:
  voice_id, voice_type ('preset' | 'element'), name  - the Higgsfield voice (list_voices)
  reference_audio                                    - job/media id of a speech clip generated in that voice (seed_audio),
                                                       passed as audio_references to every spoken video render
  status: 'locked'

Enforcement:
  - save_bible refuses any version that changes or drops a locked voice_id (VoiceLockError). A new voice means a new character.
  - validate_all: spoken packets need a locked voice (VOICE_LOCK_MISSING, error).
  - plan(): spoken units carry the locked reference audio as audio_references, never a placeholder; without a lock the unit is
    marked render_blocked.
  - render records: every spoken render of a bible must record the same voice_id (render_voice_findings).
  - Voices built from creative assets the owner excluded from this project are refused (VOICE_FORBIDDEN).
"""
from __future__ import annotations

SPOKEN_MODES = ("on_camera_dialogue", "off_camera_dialogue", "voiceover_narration")
FORBIDDEN_VOICE_NAMES = ("elias",)  # owner constraint: never read, import, reuse or imitate Elias's creative assets


class VoiceLockError(ValueError):
    pass


# Owner 2026-10-08: "Always produce a custom iconic voice based on the character and make sure it's locked with every production."
# So a lock must be a custom voice (voice_type 'element', cloned into the account) designed from the character, never a stock preset
# another creator could also be using. Pipeline: seed_audio with the character sheet as image_references (voice designed from the
# character) -> owner picks a take -> create_voice_from_confirmed_audio clones it into an element voice -> a clean sample in that
# element voice becomes reference_audio -> status 'locked'.
CUSTOM_PROVENANCE = ("designed_from_character", "owned_recording_with_consent")


def voice_lock(bible: dict | None) -> dict | None:
    """The locked voice entry, or None. Locked = has voice_id, voice_type, reference_audio and status 'locked'."""
    v = ((bible or {}).get("approved_assets") or {}).get("voice") or {}
    if v.get("voice_id") and v.get("voice_type") and v.get("reference_audio") and v.get("status") == "locked":
        return v
    return None


def assert_voice_unchanged(old: dict | None, new: dict) -> None:
    """Raise when a new bible version would change or drop a voice that an earlier version locked."""
    prev = voice_lock(old)
    if not prev:
        return
    cur = ((new.get("approved_assets") or {}).get("voice") or {})
    for k in ("voice_id", "voice_type", "reference_audio"):
        if cur.get(k) != prev.get(k):
            raise VoiceLockError(f"{new.get('bible_id')}: voice is locked ({prev.get('name')} {prev.get('voice_id')}); {k} cannot change "
                                 f"from {prev.get(k)!r} to {cur.get(k)!r}. A different voice means a different character (new bible_id).")
    if cur.get("status") != "locked":
        raise VoiceLockError(f"{new.get('bible_id')}: voice lock cannot be removed (status {cur.get('status')!r})")


def packet_speaks(packet: dict) -> bool:
    am = ((packet.get("production_format") or {}).get("audio_mode")) or ""
    if am in ("silent_ambience", "text_over_broll", "music_driven"):
        return False
    return am in SPOKEN_MODES or any(s.get("dialogue") for s in packet.get("scenes", []) or [])


def voice_findings(packet: dict, bible: dict | None) -> list[dict]:
    out = []
    v = ((bible or {}).get("approved_assets") or {}).get("voice") or {}
    if any(n in str(v.get("name", "")).lower() for n in FORBIDDEN_VOICE_NAMES):
        out.append({"code": "VOICE_FORBIDDEN", "severity": "error", "path": "bible.approved_assets.voice",
                    "message": f"voice '{v.get('name')}' comes from creative assets excluded from this project; pick another voice"})
    if v.get("status") == "locked" and (v.get("voice_type") != "element" or v.get("provenance") not in CUSTOM_PROVENANCE):
        out.append({"code": "VOICE_NOT_CUSTOM", "severity": "error", "path": "bible.approved_assets.voice",
                    "message": "the locked voice must be a custom voice designed from the character (voice_type 'element', provenance "
                               f"{' or '.join(CUSTOM_PROVENANCE)}), never a stock preset"})
    if packet_speaks(packet) and not voice_lock(bible):
        out.append({"code": "VOICE_LOCK_MISSING", "severity": "error", "path": "bible.approved_assets.voice",
                    "message": "spoken episode but the character has no locked voice (voice_id + reference_audio, status 'locked'); "
                               "without it every render invents a new voice. Lock one voice in the bible before any render."})
    return out


def render_voice_findings(records: list[dict], bible: dict | None) -> list[dict]:
    """Every spoken render of this bible must carry the locked voice_id."""
    lock = voice_lock(bible)
    out = []
    for r in records:
        if not r.get("spoken", True) or int(r.get("bible_version") or 0) < int((bible or {}).get("voice_locked_from_version") or 0):
            continue
        vid = r.get("voice_id")
        if not lock:
            continue
        if vid != lock["voice_id"]:
            out.append({"code": "VOICE_DRIFT", "severity": "error", "path": f"renders.{r.get('job_id')}",
                        "message": f"render {r.get('job_id')} used voice {vid!r}; the character's locked voice is {lock['voice_id']!r}"})
    return out


def voice_prompt_line(bible: dict | None) -> str:
    lock = voice_lock(bible)
    if not lock:
        return ""
    return "Voice: every spoken word is in exactly the voice of @audio1 (same timbre, pitch, accent, pace); never a different voice."


def project_voice_findings(bibles: list[dict]) -> list[dict]:
    """Two characters never share a voice."""
    seen, out = {}, []
    for b in bibles:
        lock = voice_lock(b)
        if not lock:
            continue
        other = seen.get(lock["voice_id"])
        if other and other != b.get("bible_id"):
            out.append({"code": "VOICE_SHARED", "severity": "error", "path": f"bibles.{b.get('bible_id')}",
                        "message": f"{b.get('bible_id')} and {other} share voice {lock['voice_id']}; every character has its own voice"})
        seen.setdefault(lock["voice_id"], b.get("bible_id"))
    return out
