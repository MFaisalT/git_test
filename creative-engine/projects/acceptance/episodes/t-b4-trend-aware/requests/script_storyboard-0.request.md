<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{
  "brief_id": "B4_trend_aware",
  "title": "Trend-aware 18-second episode: the Inspector opens a case on a single sock that keeps reappearing in the hallway; use the current trend radar to choose format and hook",
  "project": "acceptance",
  "bible_ref": "inspector-v1",
  "format": "spoken_episode",
  "platform": "youtube_shorts",
  "duration_target_s": 18,
  "language": "English, short lines",
  "objective": "Demonstrate that fresh trend entries change format/hook choices (cite trend_id) while the identity and rule stay fixed; adapt mechanisms, never copy protected assets.",
  "constraints": [
    "Location: hallway with coat hooks, daytime.",
    "One on-camera speaker; no off-camera voices.",
    "No cables, chargers, sockets, tape or cones (used in earlier episodes).",
    "If a serialised/episodic mechanism is adopted from the radar, the episode must still stand alone."
  ],
  "commercial": null,
  "negative_constraints": [
    "Do not copy any researched creator's look, catchphrase or footage.",
    "No readable brand text in frame."
  ]
}
## Bible
{
  "bible_id": "inspector-v1",
  "version": 1,
  "show_title": "Inspector of Tiny Problems (working title; name/IP uncleared)",
  "logline": "A composed inspector treats trivial household faults as major infrastructure investigations, and always ends up committing the same fault herself.",
  "character": {
    "name": "The Inspector (unnamed on screen)",
    "age_range": "35-45",
    "silhouette": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun.",
    "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger.",
    "desire": "To restore order to a world that keeps producing one-centimetre problems.",
    "flaw": "She is the main source of the faults she investigates.",
    "rule": "Every investigation ends with the Inspector exposed as the culprit or the next offender; the camera notices before she does.",
    "performance_register": "Stillness and procedure; comedy comes from disproportion, never from mugging.",
    "voice": "Measured, bureaucratic cadence; short declarative lines; never raises her voice.",
    "signature_gesture": "A slow two-finger tap on the clipboard before delivering a verdict (rationed: once per episode)."
  },
  "world": {
    "recurring_locations": [
      "living room side table",
      "shared kitchen",
      "hallway with coat hooks"
    ],
    "visual_language": "Clean modern phone look, eye-level, slightly too formal framing for the triviality; procedural colour accents (aubergine, safety-orange tape).",
    "sound_language": "Diegetic foley exaggerated one notch (clicks, tape, clipboard); no music by default; optional licensed sting only in edit."
  },
  "do_not": [
    "No bob/moustache/white-tunic combination or any researched creator's identity.",
    "No deprivation/luxury contrast as the joke.",
    "No firsthand product endorsements."
  ],
  "evolution_policy": "Costume and locations may vary per episode; silhouette, rule, register and signature gesture are fixed until a versioned bible bump with a stated reason.",
  "provenance": {
    "created": "2026-10-07",
    "basis": "comedy-report.md hypothesis 1, sharpened per independent-audit.md C2",
    "status": "hypothesis, untested",
    "saved_at": "2026-10-07T23:17:47Z"
  }
}
## Selected premise and hook
{
  "premises": {
    "premises": [
      {
        "id": "P1",
        "logline": "Cold open on a single grey sock lying on the hallway floor under a formal case title card; the Inspector files a flat missing-persons-style report on it, and the sock she keeps 'finding' is the one clinging to the back of her own jacket.",
        "audience_emotion": "Amused recognition and a small rush of superiority, because the viewer spots the culprit before she does.",
        "character_desire": "To close Case 11 and return the sock to a lost-property hook so the hallway is in order.",
        "obstacle": "Every time she places the sock on its hook and steps away, it is back on the floor; she assumes interference.",
        "escalation": "Three placements in 18 seconds: floor, then hook, then boxed on the shoe shelf. Each time she turns away and the sock is back, her verdicts get more formal ('Repeat offender. Repeat.'). Each turn of her back shows a little more of the sock's grey toe at the nape of her jacket.",
        "surprise": "The camera drifts behind her on the third turn and the sock is statically clinging to the back of the aubergine jacket, riding with her. She places it, turns, and the clinging sock drops again.",
        "payoff": "Single slow two-finger clipboard tap, then 'The suspect is on my back. The suspect is me.' She peels it off, hangs it on the hook, and as she steps back it clings to her jacket again. The rule lands: she is the culprit and the camera knew first.",
        "structure": "Cold open on object, then a rule-of-three loop that ends on a visual reveal, finishing on a repeat of the opening pose; the sock reappears at the end.",
        "why_send_it": "You send this to the flatmate whose laundry is always somewhere it should not be: 'it's following you, not me.' The 2-second title-card hook is built for a quick share.",
        "commercial_fit": "None (commercial null). Trend use: T-20261007-05 adapted as a silent close shot of the micro-fault with a formal case title card in the first 2 seconds and no spoken setup; T-20261007-02 adapted as the Inspector's own fault hinted in the back of frame before she notices. Both adapt mechanism only; no creator look, line or footage.",
        "rejected_because": ""
      },
      {
        "id": "P2",
        "logline": "Seated on the hallway bench beneath the coat hooks, the Inspector adjusts an imaginary evidence lapel mic and gives grave testimony about the sock that keeps reappearing, until her own statement convicts her.",
        "audience_emotion": "Dry delight at over-seriousness collapsing into a small, human confession.",
        "character_desire": "To have her sworn account of the sock accepted as the official record.",
        "obstacle": "Her own testimony keeps contradicting itself: each fact she states about where the sock was last seen turns out to be a place she was standing.",
        "escalation": "Statement 1: the sock was on the floor by the hooks. Statement 2: it was on the bench beside her. Statement 3: it was warm. Each fact narrows toward her; she pauses a beat longer each time but delivers each line with more certainty.",
        "surprise": "On 'last seen with its pair,' she glances down and finds the matching sock on her own left foot, with the other foot bare in a shoe. She has been wearing one sock for days and re-finding the other.",
        "payoff": "Slow two-finger clipboard tap, then 'Withdrawn. The witness is also the suspect.' She unclips the imaginary mic with great ceremony and slides her bare foot back into the shoe. Rule delivered: she is the culprit and the camera, tilting to her feet a half second early, noticed first.",
        "structure": "Direct-address testimony monologue with a slow confession reversal; one locked mid shot, with a single late tilt-down as the reveal.",
        "why_send_it": "You send this to the colleague who tells long, solemn stories about trivial things: 'this is you giving evidence about the stapler.' It works as a self-aware, low-stakes share.",
        "commercial_fit": "None (commercial null). Trend use: T-20261007-04 adapted only as the imaginary lapel-mic and 'sworn testimony' staging with new wording (no meme phrase, no documentary title); T-20261007-03 adapted as formal incident language applied to a trivial act. Rights do_not_copy honoured: mechanism only.",
        "rejected_because": "Strongest as a monologue, but it relies on a single speaking beat and reuses the sit-and-address layout of the earlier side-table episode, so the visual language is less fresh than P1."
      },
      {
        "id": "P3",
        "logline": "Case file number 4, stand-alone: the Inspector reviews three numbered sightings of one sock on three different coat hooks, each announced by a day card, and concludes the sightings are all hers.",
        "audience_emotion": "Comfortable ritual and anticipation: viewers settle into the pattern, then enjoy its snap.",
        "character_desire": "To establish a clean, numbered chain of evidence for the case file.",
        "obstacle": "The chain refuses to hold: sighting 1 and sighting 3 are the same hook, and the sock never travels on its own.",
        "escalation": "Sighting 1: sock on the far left hook. Sighting 2: on the middle hook. Sighting 3: on the near hook. Her walk to each hook is the same count of steps, and her verdicts compress: 'Sighting one. Sighting two. Sighting three.' The routine speeds up.",
        "surprise": "Sighting 3 shows her hanging her own bag on a hook. She hangs the sock with it, because it was in her pocket flap; the three 'sightings' are her three trips through the hallway that morning, replayed side by side.",
        "payoff": "She stops, taps the clipboard once, and says 'All three sightings are mine.' She closes the case, hangs the sock on the end hook, and walks off; the final card reads 'Next case', yet the episode is complete. Rule delivered: she is the culprit and the camera showed her carrying it in shot one.",
        "structure": "Numbered case-file series entry with a rule-of-three, then a pattern-break, and a soft series tag at the end; the episode stands alone.",
        "why_send_it": "You send this to the friend who loves a recurring bit and would want to follow the Inspector's case files; 'case 4' makes it easy to say 'start from case 1'.",
        "commercial_fit": "None (commercial null). Trend use: T-20261007-01 adapted by packaging as a numbered case in an episodic container; the episode must stand alone without prior cases, so the numbering is a tag, not a dependency. Free to adapt; no protected assets.",
        "rejected_because": "Series packaging adds value only if the platform feature and numbering are used; as a premise it repeats the rule-of-three loop shape of P1 with less visual surprise."
      },
      {
        "id": "P4",
        "logline": "In a slow walking-and-reading shot down the hallway, the Inspector delivers a formal incident bulletin on the sock ('last seen near the hooks, lightly worn'), and the description of the culprit's pocket flap matches her own jacket.",
        "audience_emotion": "Mock-solemn tension building into a pleased, knowing laugh at the self-incrimination.",
        "character_desire": "To issue an accurate public bulletin so the sock can be recovered.",
        "obstacle": "Each detail in the bulletin is a physical description of something on her: a flap pocket, a slight lean, a bun.",
        "escalation": "The walk takes her past three hooks. Each step, a crisper detail: 'Four-pocket outerwear. Low profile. Glasses.' The camera follows at a measured pace, noticing her reflection in the glass door panel.",
        "surprise": "The final detail is 'identifying mark: a sock in the left pocket flap', and the sock's toe is visible, poking out, in the last wide frame.",
        "payoff": "Two-finger clipboard tap, then 'Bulletin withdrawn. The suspect is the issuer.' She tucks the toe back in, resumes the walk, and the sock slides out again behind her. Rule delivered: she is the culprit and the camera noticed first.",
        "structure": "Moving tracking walk and read, with a descriptive list that builds to a self-match; one continuous shot.",
        "why_send_it": "You send this to the sibling who narrates everyone's habits in a police-report voice, as a gentle tease.",
        "commercial_fit": "None (commercial null). Trend use: T-20261007-03 adapted as formal incident language applied to a trivial act, in the Inspector's own composed voice, without any running, call-out wording or creator identity. Rights do_not_copy honoured: mechanism only.",
        "rejected_because": "The self-match reveal is the same pocket-clue idea as P1 delivered with less contrast, and a continuous tracking shot is harder to hold cleanly in 18 seconds."
      },
      {
        "id": "P5",
        "logline": "A quiet sting: the Inspector sets down a decoy sock on a coat hook, retreats out of frame, and the camera holds on the decoy alone for a long stillness while the sound of a patient observer fills the hallway.",
        "audience_emotion": "Suspense turned absurd: the viewer waits with her, and the wait becomes the joke.",
        "character_desire": "To catch the sock in the act of moving without being seen.",
        "obstacle": "Surveillance requires leaving the scene, but she is the only person who ever enters it.",
        "escalation": "The stillness stretches: a faint clipboard click from off-frame, a shoe shuffle, a held breath. The sock does not move. She re-enters twice to check, each time adjusting it slightly, which is the movement she is trying to catch.",
        "surprise": "On her final check, she sets her real sock beside the decoy: the second sock comes out of her jacket as she reaches for the hook. She has introduced the extra sock herself.",
        "payoff": "She taps the clipboard slowly once and says 'Two socks. One scene. Both mine.' Rule delivered: she is the culprit and the unattended camera was watching all along.",
        "structure": "Observer stillness with a deferred reveal: long held frame, short re-entries, then a quick hand-over of the second sock; ends on an open-loop final held frame.",
        "why_send_it": "You send this to the friend who can never leave things alone to 'see what happens'; the held frame is the whole mood.",
        "commercial_fit": "None (commercial null). No radar entry is used for the main device; T-20261007-02 is used only lightly (the extra sock visible in her pocket flap in frame one). Free to adapt; no copied assets.",
        "rejected_because": "The suspense mood is nice, but it echoes the earlier stakeout episode's held-frame stillness and the extra-sock reveal is the weakest of the five."
      }
    ],
    "ranking": [
      "P1",
      "P2",
      "P3",
      "P4",
      "P5"
    ],
    "ranking_rationale": "P1 is strongest: it has an immediate visual hook that works in the first two seconds without speech, a clean escalation, and a camera-first reveal that carries the bible rule in a single legible image. P2 follows for its distinct performance mode (direct testimony) and clear confession reversal, while P3 and P4 are coherent but lean on repeating the rule-of-three or pocket-clue ideas. P5 is last because its stillness echoes an earlier episode and its reveal is the least surprising. All five end with the Inspector as culprit, and the trend entries used are cited only as adapted mechanisms."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Silent tight close shot of one grey sock lying on a hallway floor beside the foot of a coat-hook rail, daytime light; a plain white formal title card across the lower third reads 'CASE 11: THE SOCK' (no brand text); in the extreme top edge of frame a sliver of aubergine jacket hem is visible.",
        "first_line_or_action": "No spoken setup. Held 1.5 seconds on the sock, then the Inspector's shoe and clipboard enter; her slow two-finger-ready hand lowers to the sock as the card clears. First spoken line at about 2.5s: 'Case eleven. One sock. Missing from its hook.'",
        "mechanism": "visible_problem",
        "score": 9,
        "rationale": "Adapts T-20261007-05 (silent specific-frame micro-fault plus formal case card inside 2 seconds) so the problem reads muted in one second, and the aubergine hem sliver adapts T-20261007-02 to promise the camera-notices-first rule."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Medium shot, Inspector facing camera in the hallway, a grey sock plainly clinging to the back of her aubergine jacket shoulder is NOT visible; instead the sock is hanging on the coat hook beside her in sharp focus, and a caption card reads 'Repeat offender.'",
        "first_line_or_action": "She points the inspection lamp at the hooked sock and says: 'Repeat offender. Third time this week.'",
        "mechanism": "escalating_ritual",
        "score": 6,
        "rationale": "The line sets a ritual-escalation expectation and a clear object, but the frame is more staged than a close micro-fault and the 'repeat' framing is weaker muted and less specific than the case-title close shot."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Over-the-shoulder rear view of the Inspector walking down the hallway toward a lone sock on the floor ahead, the grey toe of a second sock faintly visible at the nape of her jacket collar, a case title card in the corner.",
        "first_line_or_action": "She stops, lowers the lamp to the floor sock and says flatly, without turning: 'Someone has been here before me.'",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "Adapts T-20261007-02 by planting the nape sock in frame one so viewers spot the culprit first and the line 'someone has been here before me' ironically promises the rule, though the nape detail is small on a phone screen and costs some first-frame legibility."
      },
      {
        "id": "H4",
        "premise_id": "P2",
        "first_frame": "Locked mid shot of the Inspector seated on the hallway bench under the coat hooks, one hand raised to clip an invisible mic to her lapel, the clipboard on her knee, a grey sock lying on the floor at her feet.",
        "first_line_or_action": "She adjusts the imaginary lapel mic with great ceremony, looks into camera and says: 'For the record. The sock was not here yesterday.'",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "Adapts T-20261007-04 staging only (imaginary lapel mic, grave testimony, new wording with no meme phrase), and the muted frame already reads as mock-solemn with the sock visible at her feet, though the seated mid shot is less fresh than a close micro-fault."
      },
      {
        "id": "H5",
        "premise_id": "P2",
        "first_frame": "Tight close shot of the Inspector's face with small round glasses slipping down the nose, mouth about to speak, hallway coat hooks soft in the background; a plain card reads 'SWORN STATEMENT'.",
        "first_line_or_action": "She taps the lapel twice, then says in her measured cadence: 'Statement one. I have never lost a sock.'",
        "mechanism": "curiosity_gap",
        "score": 7,
        "rationale": "A categorical claim ('never lost a sock') invites the viewer to wait for the contradiction and adapts T-20261007-03 formal incident language, but the face-only frame shows no sock so the problem is less legible muted."
      },
      {
        "id": "H6",
        "premise_id": "P2",
        "first_frame": "Wide-ish locked shot of the Inspector seated on the bench, one foot in a shoe and one foot visibly bare on the hallway floor, a single grey sock lying on the bench beside her; she is composed and looking at the camera.",
        "first_line_or_action": "Without moving, she says: 'The witness will state where the sock was last seen.' Her bare foot flexes once.",
        "mechanism": "recognition",
        "score": 7,
        "rationale": "The bare foot plants the confession in frame one in the T-20261007-02 foreshadowing style and rewards rewatch, but giving the twist away this early reduces the reveal's surprise and the bare foot is easily missed on a phone."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "H1 is the only variant whose problem (one sock, one formal case card) is legible in the first frame with the sound off, which applies the specific-frame, silent-open mechanism from T-20261007-05, while the hem sliver quietly plants the bible rule via T-20261007-02 so the camera notices before she does. It also stays a standalone episode. The runner-up, P2's H4, has a stronger performance beat and a distinct staging from T-20261007-04, but it reuses the earlier sit-and-address layout, needs her speech to land, and gives a less immediate visual hook, so it trades first-second legibility for character voice."
    }
  }
}

## Rules
- Scenes tile [0, duration_target_s] exactly: first start_s = 0, each start_s = previous end_s, last end_s = target.
- Each scene: location, action, performance (an invested task, not an emotion adjective), microexpression, camera {shot, lens, movement, rig}, lighting (key direction + colour bounce + contact shadows), environment, sound {ambience, foley[], music, voice}, transition_out, props_from_frame_one, cuts_inside_clip (0 or 1), generation_unit (which clip this belongs to; clips are 4-30 s).
- One on-camera speaker per scene at most; a second voice is off-camera.
- Signature gesture at most once. The bible's rule must cause the payoff.
- Continuity: restate identity anchors verbatim from the bible; list every moving prop; costume per episode.
- No readable brand text, logos or real-app UI. No researched creator's identity markers.


- Dialogue lines fit their scene at <=2.8 words/s. Write for the ear: short lines, no thesis sentences.



## Craft rules (distilled from the content-engine and ugc-influencer-video skills; added after the 2026-10-07 bake-off)
- Hook earns the next second: the most specific word or image first; no warm-up.
- Camera alive, never "tripod": propped phone with one settle-wobble, handheld bob, or placement-open; angle changes come from the character, not cuts.
- Performance = an invested task (goal, obstacle, tactic) with eye-work as action; emotion adjectives are not direction.
- Lighting names key direction, fill, one colour bounce from a named surface and contact shadows; add a light-stability line if the light must not change.
- Audio names ambience plus 3-5 diegetic foley per scene; music none by default.
- The payoff must re-read the opening; the camera notices before the character does.


## Demonstrations
### Demonstration D2_spoken_tool_honesty (spoken_episode)
Input brief: An 18-second spoken episode for a different show (a weather presenter who forecasts social awkwardness). The production tool's JSON support is unverified.
Accepted output (excerpt): {"dialogue_excerpt": [{"speaker": "Presenter", "line": "Light small talk this morning, clearing by the lift.", "on_camera": true, "delivery": "brisk broadcast cadence, eyes to lens then to the 'map'"}, {"speaker": "Colleague", "line": "You're in my lift.", "on_camera": false, "delivery": "flat, close-mic, from behind camera"}], "tool_mapping_excerpt": {"adapter": "higgsfield-mcp/generate_video", "units": [{"generation_unit": "U1", "model": "seedance_2_5", "controls": {"duration": 18, "aspect_ratio": "9:16", "resolution": "720p", "generate_audio": true}, "prompt_text": "TOP PRIORITY ... (free-text house-order prompt)", "manual_steps": ["burn caption in edit", "platform disclosure if sponsored"], "gaps": ["lip-sync quality not controllable; inspect", "no fps control"]}], "notes": "Internal episode JSON is kept for the engine; the tool receives only prompt_text plus the listed native controls. The JSON is NOT a native tool payload."}}
Why it was accepted: Accepted because speech fits the timing (about 2.4 words per second), the second voice is off-camera, and the tool mapping names the free-text prompt as the only creative payload with manual steps and explicit gaps, instead of claiming the internal JSON executes natively.
Rejected alternative: A version that labelled the internal episode JSON as a 'native Higgsfield JSON payload' was rejected: JSON support is unverified and the model catalogue exposes prompt as a string.

### Demonstration D1_silent_gag (silent_gag)
Input brief: A silent 12-second gag for a different show (a night-shift museum guard who salutes every object before moving it). Problem: one framed photo hangs crooked.
Accepted output (excerpt): {"scenes_excerpt": [{"scene_id": "S1", "start_s": 0, "end_s": 3.5, "action": "Guard enters frame-right already mid-salute to a crooked frame; torch beam lands on the tilt first, his face second.", "performance": "Invested task: assess the tilt like a structural fault; eyes travel the frame edge, not the camera.", "microexpression": "Single slow blink when the beam reaches the corner.", "camera": {"shot": "medium, eye level", "lens": "35mm feel, mild phone wide", "movement": "static propped phone with one settle-wobble", "rig": "phone propped on a radiator"}, "lighting": "Torch is the key from frame-right; cool corridor fill from a far window; warm bounce off the oak floor; hard contact shadow under the frame.", "sound": {"ambience": "empty corridor hum, distant HVAC", "foley": ["torch click", "two boot steps", "fabric creak of the salute"], "music": "none"}, "transition_out": "continuous"}, {"scene_id": "S3", "start_s": 9.0, "end_s": 12.0, "action": "He straightens the frame with two fingers, salutes it, steps back; the frame behind HIM is now crooked. He does not notice. Final pose matches frame one.", "microexpression": "Satisfied exhale through the nose.", "sound": {"ambience": "same hum", "foley": ["frame tick against wall", "single boot step"], "music": "none"}, "transition_out": "loop"}], "dialogue": [], "payoff": "The fix displaces the fault to where he cannot see it; the camera sees it first."}
Why it was accepted: Accepted because the gag is legible with no words: the problem is visible in frame one, the payoff is a visible displacement, the final pose loops, every scene has camera, lighting with bounce and contact shadows, ambience and foley, and no dialogue was invented for a silent brief.
Rejected alternative: A version where the guard mutters 'not on my watch' was rejected: it added speech to a silent brief and told the joke instead of showing it.


## Output contract (JSON only)
{
  "script": {"title": "", "synopsis": "", "beats": [{"beat": "", "function": "hook|setup|escalation|turn|payoff|button|cta"}], "dialogue": [{"speaker": "", "line": "", "delivery": "", "on_camera": true}], "caption_text": "", "cta": "", "disclosure_line": ""},
  "scenes": [ {"scene_id": "S1", "start_s": 0, "end_s": 0, "location": "", "action": "", "performance": "", "microexpression": "", "dialogue": [], "camera": {"shot": "", "lens": "", "movement": "", "rig": ""}, "lighting": "", "environment": "", "sound": {"ambience": "", "foley": [], "music": "none", "voice": ""}, "captions": "", "transition_out": "", "props_from_frame_one": [], "cuts_inside_clip": 0, "generation_unit": "U1"} ],
  "continuity": {"identity_anchors": "", "costume": "", "props": [], "notes": ""},
  "asset_rights": [ {"asset": "", "kind": "character_reference|location_still|voice|music|driving_footage|product_image|font|other", "source": "", "rights_status": "owned|licensed|consented|unresolved|not_needed", "scope": ""} ],
  "export": {"aspect_ratio": "9:16", "resolution": "1080x1920", "fps": 30, "container": "mp4", "max_duration_s": 0, "edit_plan": [""], "disclosure_plan": [""]},
  "growth_hypotheses": [ {"hypothesis": "", "metric": "", "falsifier": ""} ],
  "evidence": [ {"claim": "", "kind": "fact|inference|hypothesis", "source": "", "confidence": "low|medium|high"} ]
}
Self-check before answering: timings tile exactly; every scene has camera.shot/lens/movement and sound.ambience; props used appear in continuity.props; speech rate; one cut max; silent means no dialogue.
