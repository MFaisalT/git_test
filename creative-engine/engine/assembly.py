"""Assembly and captions stage (S8), built on Higgsfield's first-party `video-montage` workflow (read 2026-10-08:
SKILL.md, references/ugc-captions.md, references/caption-clearance.md). Its scripts are preinstalled in the Higgsfield
sandbox under ${HF_WORKFLOWS}/video-montage/scripts/.

What we take from it, verbatim in spirit:
- Assembly: probe every source; keep order, resolution, aspect and timing; hard cuts by default, no transitions unasked;
  concat demuxer with stream copy when codecs match, otherwise normalise only what the output needs; verify duration,
  streams, first/last frames and every join. An exit code is not proof.
- Captions are OFF by default for UGC and opt-in (Subtitles, Hook or Both). Timing comes from the finished video's actual
  speech; the authored script is the reference for wording. Placement is subject-aware: protect face (mouth, chin), hands,
  props/labels; keep top 10%, bottom 17% and side margins clear; burn with the guarded renderer; inspect the encoded result.
  Budget: two region maps and two render attempts per clean source; never shrink boxes to force a pass.
- Reserve the upload slot before the producing sandbox command and PUT in that same command; confirm after HTTP 200.

Our additions:
- Locked-voice line replacement (owner 2026-10-08: "Final." came back in a different voice and vibe). A line from the locked
  voice (generated inside a longer in-character take, then trimmed with word timestamps) replaces the model-voiced word: the
  original voice is ducked under the window and room tone is refilled so the ambience does not drop out.
- Uploads go only to the owner's own Higgsfield media storage for review; publishing and external sharing stay owner-gated.
"""
from __future__ import annotations

from dataclasses import dataclass, field

WF = "${HF_WORKFLOWS}/video-montage/scripts"


@dataclass
class LineReplacement:
    episode_start_s: float          # where the model-voiced word starts in the assembled episode (from Whisper word timing)
    episode_end_s: float
    take_url: str                   # locked-voice take
    take_word_start_s: float        # the word inside the take (from Whisper word timing)
    take_word_end_s: float
    duck_to: float = 0.05


@dataclass
class AssemblyPlan:
    unit_urls: list[str]
    out_name: str = "final.mp4"
    replacements: list[LineReplacement] = field(default_factory=list)
    captions: str = "off"           # off | subtitles | hook | both (opt-in, owner decides)
    hook_text: str = ""
    script_lines: list[str] = field(default_factory=list)


def concat_commands(plan: AssemblyPlan) -> list[str]:
    cmds = [f"curl -sf -o u{i}.mp4 '{u}'" for i, u in enumerate(plan.unit_urls)]
    cmds += [f"ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,sample_rate -of csv=p=0 u{i}.mp4" for i in range(len(plan.unit_urls))]
    n = len(plan.unit_urls)
    ins = " ".join(f"-i u{i}.mp4" for i in range(n))
    v = "".join(f"[{i}:v]setsar=1,fps=24[v{i}];[{i}:a]aresample=48000[a{i}];" for i in range(n))
    cat = "".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[v][a]"
    cmds.append(f'ffmpeg -loglevel error -y {ins} -filter_complex "{v}{cat}" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -pix_fmt yuv420p '
                f'-c:a aac -b:a 160k -movflags +faststart clean.mp4')
    return cmds


def verify_commands(name: str, unit_durations: list[float]) -> list[str]:
    """Duration, streams and a frame either side of every join (the montage workflow's 'verify every join')."""
    cmds = [f"ffprobe -v error -show_entries format=duration:stream=codec_type -of csv=p=0 {name}"]
    t = 0.0
    for i, d in enumerate(unit_durations[:-1]):
        t += d
        cmds.append(f"ffmpeg -loglevel error -y -ss {max(0.0, t - 0.08):.2f} -i {name} -frames:v 1 join{i}_before.jpg")
        cmds.append(f"ffmpeg -loglevel error -y -ss {t + 0.04:.2f} -i {name} -frames:v 1 join{i}_after.jpg")
    return cmds


def caption_commands(plan: AssemblyPlan, language: str = "en") -> list[str]:
    """The montage workflow's guarded caption sequence. Each '# REVIEW' step is a real visual inspection through
    sandbox_exec image_paths before the next command; none of them may be pre-filled."""
    if plan.captions == "off":
        return []
    return [
        "python3 -c \"import json;json.dump({'blocks':[{'vo_line':l} for l in %r]},open('script_manifest.json','w'))\"" % (plan.script_lines,),
        f"python3 {WF}/audio_to_captions.py clean.mp4 --mixed --language '{language}' --script script_manifest.json --srt caps.srt --json caps.json --max-words 5 --max-chars 32",
        f"python3 {WF}/caption_evidence.py prepare --video clean.mp4 --srt caps.srt --out-dir clean-evidence",
        "# REVIEW: open every clean-evidence/sheet-*.jpg; write protected_regions.json (face incl. mouth/chin, both hands, paddle gauge)",
        f"python3 {WF}/caption_regions.py prepare --video clean.mp4 --srt caps.srt --regions protected_regions.json --clean-evidence clean-evidence/evidence.json --out-dir region-evidence",
        "# REVIEW: open every region-evidence/sheet-*.jpg; fill region-review.json per sample from the unprotected view",
        f"python3 {WF}/caption_regions.py verify --video clean.mp4 --srt caps.srt --regions protected_regions.json --clean-evidence clean-evidence/evidence.json --evidence region-evidence/region-evidence.json --review region-review.json --receipt region-review-receipt.json",
        f"python3 {WF}/subtitle_paper_burn.py --in clean.mp4 --srt caps.srt --out final_subbed.mp4 --style bold --no-caps --font-key metropolis --fontsize-frac 0.02604 --stroke-frac 0.12 --profile safe --protected-regions protected_regions.json --region-review region-review-receipt.json",
        f"python3 {WF}/caption_evidence.py prepare --video final_subbed.mp4 --srt caps.srt --out-dir final-evidence",
        "# REVIEW: open every final-evidence/sheet-*.jpg; fill review.json (clear/text_ok per frame) from the pixels",
        f"python3 {WF}/caption_evidence.py verify --video final_subbed.mp4 --srt caps.srt --evidence final-evidence/evidence.json --review review.json --receipt final_subbed.mp4.caption-review.json",
    ]


def line_replacement_script(r: LineReplacement, src_wav: str = "clean.wav", take_wav: str = "take.wav", out_wav: str = "mixed.wav") -> str:
    """Python run in the sandbox: duck the model-voiced word, refill room tone, lay the locked-voice word at its onset."""
    return f'''import wave, numpy as np
def load(f):
    w=wave.open(f); sr=w.getframerate(); return np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float), sr
x,sr=load("{src_wav}"); t,_=load("{take_wav}")
on,off={r.episode_start_s},{r.episode_end_s}
w=t[int(({r.take_word_start_s}-0.06)*sr):int(({r.take_word_end_s}+0.15)*sr)].copy(); f=int(0.02*sr); w[:f]*=np.linspace(0,1,f); w[-f:]*=np.linspace(1,0,f)
g=np.sqrt((x[int(on*sr):int((on+0.45)*sr)]**2).mean())/max(np.sqrt((w**2).mean()),1); w*=g*0.95
i0,i1=int((on-0.10)*sr),int((off+0.15)*sr); r=int(0.05*sr); env=np.ones(len(x)); env[i0:i1]={r.duck_to}
env[i0-r:i0]=np.linspace(1,{r.duck_to},r); env[i1:i1+r]=np.linspace({r.duck_to},1,r); y=x*env
amb=x[int((off+0.3)*sr):int((off+0.3)*sr)+(i1-i0)]
if len(amb)==i1-i0: y[i0:i1]+=amb*0.9
s=int((on-0.06)*sr); y[s:s+len(w)]+=w
o=wave.open("{out_wav}","wb"); o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes(np.clip(y,-32767,32767).astype(np.int16).tobytes()); o.close()
'''
