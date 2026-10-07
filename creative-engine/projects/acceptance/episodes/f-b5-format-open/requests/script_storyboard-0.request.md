<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{
  "brief_id": "B5_format_open",
  "title": "Format left fully open: the Inspector investigates a kitchen timer that keeps ringing with nothing in the oven",
  "project": "acceptance",
  "bible_ref": "inspector-v1",
  "format": "other",
  "platform": "instagram_reels",
  "duration_target_s": 16,
  "language": "English or none - the engine decides with the audio mode",
  "objective": "Demonstrate production-format choice: the engine must pick shot architecture, audio mode and continuity reuse (same voice/location or new) that differ from the recent episodes and justify them.",
  "constraints": [
    "Location: the bible's shared kitchen, daytime.",
    "No cables, sockets, tape, cones, socks, coat hooks or fridge alarms (used in earlier episodes).",
    "Anything else (single take vs multi-scene, silent vs spoken, camera style) is the engine's call."
  ],
  "production_format": {},
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
        "logline": "One unbroken glide through the shared kitchen follows a ringing timer from the empty oven to the Inspector's own fourth flap pocket, which the camera has been quietly shaking in frame since the first second.",
        "audience_emotion": "Dry, rising amusement that tips into the pleasure of being a step ahead of the investigator.",
        "character_desire": "To locate the source of an unauthorised ring and close the case before the next ring.",
        "obstacle": "Every location she checks (oven cavity, dial, counter) is empty, and the ring keeps moving with her so it never resolves where she looks.",
        "escalation": "She opens the oven, then crouches to the dial, then presses her ear to the cupboard; each stop she moves, and the ring is always one step 'behind' her, getting louder as she circles back to the counter.",
        "surprise": "The ring tracks her, not the room: the camera drifts from the oven to her chest and the lowest flap pocket is visibly buzzing against the jacket, a small wind-up timer inside, jiggling in time with the bell.",
        "payoff": "She lifts the flap, takes out the timer, and the ring dies. Beat of warm disappointment. Single slow two-finger tap on the clipboard. She winds the timer a quarter turn 'to test it', slips it back into the pocket and walks out; it begins to ring again as she exits. Bible rule delivered: she is the culprit and the camera noticed first.",
        "structure": "Procedural chase that ends in a reversal of the search direction: the camera leads the viewer to the answer before the character.",
        "why_send_it": "Send it to the friend who always says 'what is that noise' while the noise is in their own bag or pocket.",
        "commercial_fit": "None; no product. Trend T-20261007-05 used lightly: the opening frame states the micro-fault visually with no spoken setup.",
        "rejected_because": "",
        "production_format": {
          "shot_architecture": "single_take_moving_camera",
          "audio_mode": "silent_ambience",
          "camera_style": "Phone at eye level on a slow motivated glide: starts wide on the empty oven and counter, tracks laterally with her, then drifts in and down to her flap pocket; no cuts, gentle breathing-level drift, one tiny settle at the start.",
          "continuity_reuse": {
            "voice": "none",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [
            "T-20261007-05"
          ],
          "rationale": "The reveal is physical and spatial (the ring migrates), so one continuous move makes the viewer travel with the sound and land on the pocket; a silent mode makes the exaggerated bell foley the entire joke and differs from the recent locked-off, spoken and cut-heavy episodes. Same kitchen and costume keep the bible identity; no voice is used."
        }
      },
      {
        "id": "P2",
        "logline": "A locked frame on the empty oven jump-cuts through a long afternoon of observation while the Inspector's dry case-log narration insists the timer rings spontaneously, and each cut quietly shows her pressing start on it before she walks away.",
        "audience_emotion": "Deadpan patience turning into delighted recognition of a self-deceiving routine.",
        "character_desire": "To establish a reliable ring pattern so the fault can be formally classified.",
        "obstacle": "The timer rings at irregular times and never when she is looking at the dial.",
        "escalation": "Log entries get more severe (anomaly, recurrence, pattern, escalation) while the light shifts slightly between cuts and a mug, an orange peel and a pile of notes accumulate on the counter.",
        "surprise": "Each cut, mid-action, her thumb taps the oven timer's start button as a ritual 'resetting for observation' while the narration says she has touched nothing.",
        "payoff": "Final cut: she sees the log summary, the voice-over pauses, and she slowly taps the clipboard with two fingers; the narration says 'Cause: observation.' She presses start once more, steps out of frame, and the empty oven's timer counts down. Rule delivered: she is the culprit and the camera saw each press first.",
        "structure": "Time-lapse accumulation with an ironic voice-over contradicting the image, resolved in a single confession line.",
        "why_send_it": "Send it to the person who 'definitely did not touch it' and then touches it every ten minutes.",
        "commercial_fit": "None. Trend T-20261007-01 used by numbering it Case 12 so it can sit in a case-file series.",
        "rejected_because": "Ranked below P1, P3 and P4 because the repeated press-and-leave beat is a gentler hook and narration tells part of the joke that P1 and P3 show.",
        "production_format": {
          "shot_architecture": "jump_cut_timelapse",
          "audio_mode": "voiceover_narration",
          "camera_style": "Locked-off propped phone at eye level, formal symmetrical framing on the oven and counter, 4 hard jump cuts on an identical frame; only the light, counter clutter and her position change.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [
            "T-20261007-01"
          ],
          "rationale": "Time passing is the comedy of a stakeout, and an ironic voice-over recorded separately lets her measured bureaucratic cadence contradict the picture without mouth sync. It reuses the bible voice and kitchen deliberately so the show feels consistent, while the structure (log entries) differs from the recent hook-and-gag skeletons."
        }
      },
      {
        "id": "P3",
        "logline": "Filming her own bodycam-style evidence walk-through of the kitchen, the Inspector declares the ringing 'unsourced' while every sweep of her phone passes a small pan of boiling water with an egg on the hob.",
        "audience_emotion": "Nosy, shouting-at-the-screen amusement.",
        "character_desire": "To record a clean, admissible walk-through proving the oven is empty.",
        "obstacle": "The ringing continues in every angle she films, and the oven, grill and shelves are all empty.",
        "escalation": "Each sweep she films tighter and more formally: oven window, oven shelf, dial, counter; the bubbling pan creeps closer to centre of every pass and the reflection in the oven glass shows steam climbing.",
        "surprise": "The source is a timer she set for an egg on the hob; the oven was never the point. The camera has her walking past it three times and she films the pan as 'unrelated'.",
        "payoff": "She says 'Item four: a pan. Unrelated.' then the timer next to the pan rings its final ring; she lowers the phone, taps the clipboard with two fingers, and in the last frame she lifts the egg out, turns and writes 'Oven: empty' while the phone catches her own reflection. Rule delivered: she is the culprit (the egg is hers), the camera saw it first.",
        "structure": "First-person evidence log where the cameraperson is the culprit; the reveal comes from the edge of the frame.",
        "why_send_it": "Send it to the flatmate who is convinced the problem is in the other room.",
        "commercial_fit": "None.",
        "rejected_because": "Ranked below P1 and above P4 because the culprit reveal is a side object rather than something on her person, which is a little less iconic for the show rule.",
        "production_format": {
          "shot_architecture": "pov_handheld",
          "audio_mode": "on_camera_dialogue",
          "camera_style": "Character-held phone, selfie-then-reverse: she turns it from her face to the oven, shelves and counter; angle changes come from her wrist; short formal sentences to lens, steady procedural pace.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "A character-held phone is the natural 'evidence footage' format and puts the culprit behind the lens, which is a new relationship to the viewer, while on-camera speech suits her short declarative lines in 16 seconds. Same voice, kitchen and jacket keep identity; the format is new for the show."
        }
      },
      {
        "id": "P4",
        "logline": "Under a formal title card, a closed oven rings with muffled bells; the Inspector opens it, finds the timer inside, 'arrests' it, and ends by shutting it back in the oven where she placed it, so the clip loops into its own opening.",
        "audience_emotion": "Quiet, ceremonial absurdity that rewards a rewatch.",
        "character_desire": "To contain the ringing and attach a proper label to it.",
        "obstacle": "The ringing is muffled and seems to come from inside a closed oven that she insists is empty.",
        "escalation": "Card, then ring, then door opens, then she holds the timer up like a captured suspect, then she sets it on the counter where it rings louder, then she decides to 'contain' it.",
        "surprise": "The on-screen text, which updates in post at each beat, ends with 'Placed by: the Inspector', and her putting the timer back is exactly what the opening frame showed.",
        "payoff": "She closes the oven door on the timer, two-finger clipboard tap, and steps out; the final frame matches the first (closed oven, muffled ring, empty counter), so autoplay restarts the case. Rule delivered: she is the culprit, shown by text and framing.",
        "structure": "Closed loop with text beats: title card, findings and a confession line as captions.",
        "why_send_it": "Send it to the person who hides an annoying thing in the oven and then asks who did it.",
        "commercial_fit": "None. Trend T-20261007-05 used: silent open on the micro-fault with a formal case title card in the first 2 seconds, no spoken setup.",
        "rejected_because": "Ranked below P1 and P3 because the loop reuses the earlier hallway-hook feel and has less physical escalation.",
        "production_format": {
          "shot_architecture": "loop",
          "audio_mode": "text_over_broll",
          "camera_style": "Locked-off medium on the oven front at eye level with symmetrical framing; one clean mid-clip close insert is not used; end frame is identical to frame one for seamless repeat.",
          "continuity_reuse": {
            "voice": "none",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [
            "T-20261007-05"
          ],
          "rationale": "A seamless loop makes the paradox (she is the one who put it there) literal, and text-over-b-roll lets the joke read on mute in reels autoplay with no speech to write. It drops the voice altogether, deliberately varying from the dialogue-heavy recent episodes while keeping location and costume."
        }
      },
      {
        "id": "P5",
        "logline": "In three hard-cut scenes, the Inspector discovers the ringing timer exists to remind her to check another timer, and in answer to a flatmate off-camera she sets a third one to remind her to check this one.",
        "audience_emotion": "Escalating bureaucratic absurdity with a satisfied groan at the end.",
        "character_desire": "To find which timer is the origin of the chain and shut it down.",
        "obstacle": "Every timer she silences proves to be a reminder for another, and the oven remains empty.",
        "escalation": "Scene 1 she examines the empty oven; scene 2 she finds a small egg-timer with a sticky label that says 'check other timer' (no readable brand); scene 3 she finds the other timer is set for four minutes.",
        "surprise": "The off-camera flatmate asks 'What is that one for?' and she answers calmly, 'To remind me to check the other one.'",
        "payoff": "She sets a fresh timer to remind herself to check the pair, two-finger clipboard tap, and the camera holds on three timers lined up. Rule delivered: she is the culprit and the next offender; the chain is hers.",
        "structure": "Three-beat recursive chain with a dialogue punchline.",
        "why_send_it": "Send it to the colleague who sets reminders to read reminders.",
        "commercial_fit": "None.",
        "rejected_because": "Ranked lowest because the recursion joke is wordier and leans on dialogue and a set-up label, which risk being slow in 16 seconds.",
        "production_format": {
          "shot_architecture": "multi_scene_cut",
          "audio_mode": "off_camera_dialogue",
          "camera_style": "Three formal, slightly too tidy set-ups cut hard: wide on the oven, medium over the counter, close on three timers; eye level, locked off; the flatmate is a close-mic voice from behind the camera.",
          "continuity_reuse": {
            "voice": "new",
            "location": "same",
            "costume": "new"
          },
          "trend_refs": [],
          "rationale": "A recursive chain needs discrete scenes to count steps, so hard cuts serve it, and a second off-camera voice tests whether the Inspector holds up when someone else talks, which is why the voice is new. Costume changes to a lighter shirt under the jacket as a small allowed evolution while the silhouette stays fixed."
        }
      }
    ],
    "ranking": [
      "P1",
      "P3",
      "P4",
      "P2",
      "P5"
    ],
    "ranking_rationale": "P1 is the cleanest expression of the bible rule: the camera notices the buzzing pocket before she does, the one-take glide carries the chase visually, and silence makes the foley the joke. P3 keeps the same rule with a different relationship (the viewer holds the camera she holds) and a spoken register, and P4 is the most rewatchable but least escalating. P2 and P5 are sound but rely more on narration or dialogue to land."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Wide, eye-level, formally symmetrical shot of the shared kitchen in daylight: a clean empty oven with its glass door open and bare shelves, empty counter, a small caption card 'CASE 12: UNAUTHORISED RING' in the lower third. The Inspector stands at the edge of frame, still, side-on, in the aubergine jacket, lamp on chest strap.",
        "first_line_or_action": "Silent. A tiny visible ring-shake pulses the lowest flap pocket of her jacket in time with a bell animation on the oven dial, while she stares at the empty oven; she then walks left and the camera starts its glide with her.",
        "mechanism": "visible_problem",
        "score": 7,
        "rationale": "The empty oven and the vibrating pocket are legible muted and specific, but the pocket jiggle at the frame edge is slightly easy to miss in one second, which holds back the legibility score."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Opening on an empty oven interior in tight frame with a small wind-up bell timer ring visible as a vibrating blur at the bottom edge of the shot (the Inspector's lowest flap pocket is slightly in shot, reading as the 'wrong' object), with a fast subtitle-free visual of sound waves from the oven mouth.",
        "first_line_or_action": "She crouches into frame and peers into the oven mouth with her lamp, hand raised to hold the oven door; the lowest pocket buzzes visibly against her hip in the foreground, and the camera begins to drift back.",
        "mechanism": "status_contradiction",
        "score": 6,
        "rationale": "It states the paradox (she investigates the oven while the pocket in foreground is shaking) but the foreground-lamp-and-oven composition is busy and the first frame competes for attention."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Static-looking wide on the empty oven and bare counter, formal framing with the formal case title card 'CASE 12' in the top corner and an animated bell icon pulsing; nobody is in shot yet.",
        "first_line_or_action": "Silent. The bell icon pulses and the Inspector steps into frame from the right, lamp on, stops, and her lowest flap pocket is already trembling; the camera starts to glide with her toward the oven.",
        "mechanism": "curiosity_gap",
        "score": 6,
        "rationale": "The title card plus empty oven follows the trend of a silent, specific opening, but with no person in the first frame the one-second read is 'something is wrong with this oven', which is less specific than a visible tell."
      },
      {
        "id": "H4",
        "premise_id": "P3",
        "first_frame": "Selfie-angle phone shot of the Inspector's face close to the lens in the shared kitchen, small round glasses slipping, lamp glowing at her chest; behind her shoulder a small pan with an egg bubbles on the hob, slightly out of focus, with steam rising.",
        "first_line_or_action": "She says, to lens: 'Item one. The oven. Empty.' and reverses the phone toward the oven door, still with the pan visible at the edge of the frame as she turns.",
        "mechanism": "callout",
        "score": 7,
        "rationale": "The bubbling pan behind her makes the culprit visible in frame one, which is strong for send-ability to the flatmate who looks in the wrong room, but it relies on the spoken line and is weaker when muted."
      },
      {
        "id": "H5",
        "premise_id": "P3",
        "first_frame": "Phone held against the oven door glass: an empty oven interior in close-up, with the faint reflection of a bubbling pan and the Inspector's glasses and lamp visible in the glass.",
        "first_line_or_action": "A formal timestamp overlay 'EVIDENCE 01' appears and she says 'Oven shelf. Empty.' in a flat voice while the reflected steam climbs behind her head.",
        "mechanism": "visible_problem",
        "score": 5,
        "rationale": "The reflected pan is a clever tell for rewatchers, but at one second the reflection is hard to read and the frame mostly looks like a plain empty oven."
      },
      {
        "id": "H6",
        "premise_id": "P3",
        "first_frame": "A shaky character-held phone view sweeping fast across the kitchen, pausing on the Inspector's gloved hand pointing at the oven while a small timer beside a boiling pan sits at the lower corner of the frame.",
        "first_line_or_action": "Her hand taps the clipboard (rationed signature gesture) too early and she says 'Admissible.' while the camera sweeps past the pan.",
        "mechanism": "escalating_ritual",
        "score": 5,
        "rationale": "The early signature gesture spends the rationed tap and weakens the final payoff, and the sweep is a muddier first frame than the selfie variants."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "P1 with H1 gives the clearest muted, one-second read: an empty oven plus a trembling pocket sets the bible rule up so the camera notices before she does. Its production-format pair (single_take_moving_camera, silent_ambience) differs from the recent episodes' locked-off/spoken/cut-heavy pairs and from P3's (pov_handheld, on_camera_dialogue) that leans on speech, so it best demonstrates the format choice. The trade-off against the runner-up H4 (P3) is that H4 has a more immediate culprit reveal in frame one but is weaker muted and keeps a spoken register closer to recent episodes."
    }
  },
  "production_format": {
    "shot_architecture": "single_take_moving_camera",
    "audio_mode": "silent_ambience",
    "camera_style": "Phone at eye level on a slow motivated glide: starts wide on the empty oven and counter, tracks laterally with her, then drifts in and down to her flap pocket; no cuts, gentle breathing-level drift, one tiny settle at the start.",
    "continuity_reuse": {
      "voice": "none",
      "location": "same",
      "costume": "same"
    },
    "trend_refs": [
      "T-20261007-05"
    ],
    "rationale": "The reveal is physical and spatial (the ring migrates), so one continuous move makes the viewer travel with the sound and land on the pocket; a silent mode makes the exaggerated bell foley the entire joke and differs from the recent locked-off, spoken and cut-heavy episodes. Same kitchen and costume keep the bible identity; no voice is used."
  }
}

## Production format to realise (declared by the selected premise; the validator checks it)
{
  "shot_architecture": "single_take_moving_camera",
  "audio_mode": "silent_ambience",
  "camera_style": "Phone at eye level on a slow motivated glide: starts wide on the empty oven and counter, tracks laterally with her, then drifts in and down to her flap pocket; no cuts, gentle breathing-level drift, one tiny settle at the start.",
  "continuity_reuse": {
    "voice": "none",
    "location": "same",
    "costume": "same"
  },
  "trend_refs": [
    "T-20261007-05"
  ],
  "rationale": "The reveal is physical and spatial (the ring migrates), so one continuous move makes the viewer travel with the sound and land on the pocket; a silent mode makes the exaggerated bell foley the entire joke and differs from the recent locked-off, spoken and cut-heavy episodes. Same kitchen and costume keep the bible identity; no voice is used."
}
Realisation rules: single-take architectures = no cuts and one generation unit (<=30 s) with the camera move written into every scene's camera.movement; multi_scene_cut = hard cuts between scenes, each scene its own unit; jump_cut_timelapse = >=3 jump cuts, same framing, visible accumulation; loop = last transition_out says "loop"; silent_ambience / text_over_broll = empty dialogue (text_over needs caption_text); voiceover_narration = speaker "VO" lines with on_camera false; off_camera_dialogue = at least one on_camera:false line; music_driven = name the licensed/owned cue in sound.music and declare a music asset; continuity_reuse voice/location "same" = declare the voice / location_still assets from the bible's approved_assets by asset_id.

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
