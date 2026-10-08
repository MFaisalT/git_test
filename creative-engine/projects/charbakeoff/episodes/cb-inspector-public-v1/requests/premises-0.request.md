<!-- requested_model: sonnet; effort: medium; tag: premises-0 -->

# Stage 1 - Divergent premises

You are the episode developer for a recurring short-form character show. Your responsibility in this stage: produce five genuinely divergent premises for one episode that obey the show bible, then rank them. You are not writing the script yet.

## Brief
{
  "brief_id": "CB1_intro_inspector-public-v1",
  "title": "Character bake-off intro: 12-second first public appearance of inspector-public-v1",
  "project": "charbakeoff",
  "bible_ref": "inspector-public-v1",
  "format": "other",
  "platform": "tiktok",
  "duration_target_s": 12,
  "language": "English or none - the engine decides with the audio mode",
  "objective": "Introduce the character to a cold viewer in 12 seconds in a public setting so that the character's energy, rule and silhouette are legible muted; make the viewer want to see the next one. This is a bake-off: the same brief runs for three characters and the owner compares the rendered tests.",
  "constraints": [
    "Public setting from the bible's recurring locations; generic blurred passers-by allowed, never the joke.",
    "Render tier: draft_mini (one 12 s Seedance 2.0 Mini unit, <=15 s, one generation unit, at most one cut) - this is a cost-capped test render.",
    "The bible rule must land inside 12 seconds; the signature gesture may be used once.",
    "Any dance or move is original and fully described; no trending dance or sound."
  ],
  "production_format": {},
  "commercial": null,
  "render_tier": "draft_mini",
  "negative_constraints": [
    "Do not copy any researched creator's look, catchphrase or footage.",
    "No readable brand text in frame.",
    "No real people or recognisable locations."
  ]
}

## Show/character bible (fixed identity; evolution only where the bible allows)
{
  "bible_id": "inspector-public-v1",
  "version": 1,
  "show_title": "Inspector of Tiny Problems: Field Unit (working title; name/IP uncleared)",
  "logline": "The same composed Inspector takes her clipboard into public spaces, delivering formal verdicts on strangers' tiny faults to a city that does not react, and always ends up committing the fault herself.",
  "character": {
    "name": "The Inspector (unnamed on screen)",
    "age_range": "35-45",
    "sex_presentation": "woman",
    "silhouette": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun.",
    "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger.",
    "hair": "dark hair in a tight low bun with a matte finish",
    "lower_body": "plain charcoal trousers, flat black work shoes",
    "desire": "To restore public order one centimetre at a time.",
    "flaw": "She is the main source of the faults she investigates.",
    "rule": "Every investigation ends with the Inspector exposed as the culprit or the next offender; the camera notices before she does. In public, strangers never react to her, which makes her verdicts louder.",
    "performance_register": "Stillness and procedure in a moving world: she announces findings to passers-by at normal volume while they walk through frame; comedy from disproportion and from being ignored, never from mugging.",
    "voice": "Measured, bureaucratic cadence; short declarative lines spoken to strangers who do not answer.",
    "signature_gesture": "A slow two-finger tap on the clipboard before delivering a verdict (rationed: once per episode)."
  },
  "world": {
    "recurring_locations": [
      "bus stop with a timetable board",
      "supermarket self-checkout lane",
      "pavement cafe terrace"
    ],
    "visual_language": "Clean modern phone look, eye-level, slightly too formal framing in busy public space; passers-by blurred and generic; aubergine against grey street.",
    "sound_language": "Street ambience real and present; her foley exaggerated one notch (clipboard, lamp click); no music by default."
  },
  "do_not": [
    "No bob/moustache/white-tunic combination or any researched creator's identity, catchphrase, costume or footage.",
    "No real people, no real brands, no religion, no politics, no mocking of strangers' bodies, accents, disabilities or faith; strangers in frame are generic extras who never become the joke.",
    "No trending dance or sound that is not cleared; any dance is an original move described in the storyboard.",
    "No firsthand product endorsements."
  ],
  "evolution_policy": "Locations may vary; silhouette, rule, register and gesture fixed until a versioned bump.",
  "provenance": {
    "created": "2026-10-08",
    "basis": "owner feedback 2026-10-08: the Inspector is too quiet and indoors versus the reference list; hypothesis A keeps the rule and moves her into public space",
    "status": "hypothesis, untested",
    "saved_at": "2026-10-08T05:53:57Z",
    "bump_reason": "character bake-off hypothesis"
  },
  "audience": {
    "target": "global; visual comedy of recognition; subtitle-ready; no region-specific references",
    "language_default": "visual-first; English when spoken"
  }
}





## Production format (choose per premise; vary it)
Shot architectures:
- single_take_static: one continuous take, locked-off camera, no cuts (one generation unit)
- single_take_moving_camera: one continuous take with a motivated camera move (push-in, orbit, handheld follow, tilt reveal); no cuts
- multi_scene_cut: several scenes joined by hard cuts in edit; each scene is its own generation unit
- jump_cut_timelapse: same framing, 3+ jump cuts marking time passing; change accumulates between cuts
- pov_handheld: character-held or companion-held phone; angle changes come from the character, not cuts
- interview_offcamera: character answers an unseen interviewer; one on-camera speaker
- montage: rapid series of short shots over one audio bed (voice-over or music) building one idea
- loop: ending matches the opening frame so autoplay repeats seamlessly
- continuation_from_last_frame: part 2 picks up from the last frame of an earlier approved clip (reference clip required)
- split_or_insert: main shot plus one insert/close-up or a split frame assembled in edit
- motion_transfer_owned_footage: owned/licensed driving footage re-cast with the character via Genjutsu (rights required)
- other: a format proposed from the trend radar or the brief; must be described
Audio modes:
- silent_ambience: no speech; ambience + foley only; optional caption added in post
- voiceover_narration: character or narrator voice-over recorded separately; mouth not synced on camera
- on_camera_dialogue: character speaks to camera; one on-camera speaker
- off_camera_dialogue: a second voice off camera; character may reply on camera
- text_over_broll: no speech; the script becomes on-screen text added in post
- music_driven: licensed/owned music carries the rhythm; cuts or actions land on beats; little or no speech
Fixed by this brief (obey exactly; empty means open): {}
Recently used (shot_architecture, audio_mode) pairs - do NOT repeat a pair in the top-ranked premise unless the brief fixes it: []
Each premise must carry a `production_format` {shot_architecture, audio_mode, camera_style, continuity_reuse {voice, location, costume: same|new|none}, trend_refs[], rationale}. Across the five premises use at least three different shot architectures and at least two audio modes. The same character voice and location may be reused ("same") or changed ("new") deliberately; say why. Silent and spoken are both valid; a single moving-camera take and a multi-scene edit are both valid; pick what serves the premise and the variety of the show.

## Reasoning targets (reason about these; report conclusions, not private deliberation)
For each premise state: audience emotion, character desire, obstacle, escalation, surprise, payoff, narrative structure, and why a specific viewer would send it to a specific person.
Diverge across at least four of: narrative structure, conflict type, relationship, location, stakes, performance mode, visual language, pacing, ending type. Setting swaps inside one skeleton do not count as divergence.




## Demonstrations (observable outputs + justification; follow the quality, not the content)
### Demonstration D1_silent_gag (silent_gag)
Input brief: A silent 12-second gag for a different show (a night-shift museum guard who salutes every object before moving it). Problem: one framed photo hangs crooked.
Accepted output (excerpt): {"scenes_excerpt": [{"scene_id": "S1", "start_s": 0, "end_s": 3.5, "action": "Guard enters frame-right already mid-salute to a crooked frame; torch beam lands on the tilt first, his face second.", "performance": "Invested task: assess the tilt like a structural fault; eyes travel the frame edge, not the camera.", "microexpression": "Single slow blink when the beam reaches the corner.", "camera": {"shot": "medium, eye level", "lens": "35mm feel, mild phone wide", "movement": "static propped phone with one settle-wobble", "rig": "phone propped on a radiator"}, "lighting": "Torch is the key from frame-right; cool corridor fill from a far window; warm bounce off the oak floor; hard contact shadow under the frame.", "sound": {"ambience": "empty corridor hum, distant HVAC", "foley": ["torch click", "two boot steps", "fabric creak of the salute"], "music": "none"}, "transition_out": "continuous"}, {"scene_id": "S3", "start_s": 9.0, "end_s": 12.0, "action": "He straightens the frame with two fingers, salutes it, steps back; the frame behind HIM is now crooked. He does not notice. Final pose matches frame one.", "microexpression": "Satisfied exhale through the nose.", "sound": {"ambience": "same hum", "foley": ["frame tick against wall", "single boot step"], "music": "none"}, "transition_out": "loop"}], "dialogue": [], "payoff": "The fix displaces the fault to where he cannot see it; the camera sees it first."}
Why it was accepted: Accepted because the gag is legible with no words: the problem is visible in frame one, the payoff is a visible displacement, the final pose loops, every scene has camera, lighting with bounce and contact shadows, ambience and foley, and no dialogue was invented for a silent brief.
Rejected alternative: A version where the guard mutters 'not on my watch' was rejected: it added speech to a silent brief and told the joke instead of showing it.

### Demonstration D2_spoken_tool_honesty (spoken_episode)
Input brief: An 18-second spoken episode for a different show (a weather presenter who forecasts social awkwardness). The production tool's JSON support is unverified.
Accepted output (excerpt): {"dialogue_excerpt": [{"speaker": "Presenter", "line": "Light small talk this morning, clearing by the lift.", "on_camera": true, "delivery": "brisk broadcast cadence, eyes to lens then to the 'map'"}, {"speaker": "Colleague", "line": "You're in my lift.", "on_camera": false, "delivery": "flat, close-mic, from behind camera"}], "tool_mapping_excerpt": {"adapter": "higgsfield-mcp/generate_video", "units": [{"generation_unit": "U1", "model": "seedance_2_5", "controls": {"duration": 18, "aspect_ratio": "9:16", "resolution": "720p", "generate_audio": true}, "prompt_text": "TOP PRIORITY ... (free-text house-order prompt)", "manual_steps": ["burn caption in edit", "platform disclosure if sponsored"], "gaps": ["lip-sync quality not controllable; inspect", "no fps control"]}], "notes": "Internal episode JSON is kept for the engine; the tool receives only prompt_text plus the listed native controls. The JSON is NOT a native tool payload."}}
Why it was accepted: Accepted because speech fits the timing (about 2.4 words per second), the second voice is off-camera, and the tool mapping names the free-text prompt as the only creative payload with manual steps and explicit gaps, instead of claiming the internal JSON executes natively.
Rejected alternative: A version that labelled the internal episode JSON as a 'native Higgsfield JSON payload' was rejected: JSON support is unverified and the model catalogue exposes prompt as a string.


## Output contract (JSON only, no prose outside the object)
{
  "premises": [ {"id": "P1", "logline": "", "audience_emotion": "", "character_desire": "", "obstacle": "", "escalation": "", "surprise": "", "payoff": "", "structure": "", "why_send_it": "", "commercial_fit": "", "rejected_because": "",
                 "production_format": {"shot_architecture": "", "audio_mode": "", "camera_style": "", "continuity_reuse": {"voice": "same|new|none", "location": "same|new|none", "costume": "same|new|none"}, "trend_refs": [], "rationale": ""}} , ... 5 items ],
  "ranking": ["P?", "P?", "P?", "P?", "P?"],
  "ranking_rationale": "2-4 sentences on quality and coherence, not on count of combinations"
}
Fill rejected_because for the four non-top premises (one clause each). Before answering, check: five premises, each with all fields, divergence along >=4 axes, bible rule present in the top premise's payoff.
