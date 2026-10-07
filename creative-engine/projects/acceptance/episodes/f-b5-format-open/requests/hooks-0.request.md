<!-- requested_model: sonnet; effort: medium; tag: hooks-0 -->

# Stage 2 - Scored hook variants

Your responsibility: for the top two premises, write three hook variants each (six total) and score them. A hook is the first frame plus the first line or action; it must work muted and read in about one second.

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
## Bible (identity anchors and rule)
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
## Prior stage output
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
  }
}


## Current trend radar (dated; adapt mechanisms, never copy protected assets)
Dated entries. Use them to choose and tailor topics, hooks, pacing and vocabulary. ADAPT the mechanism; never copy a protected sound, choreography or identity. Cite trend_id in the premise's commercial_fit or why_send_it when used.
- [T-20261007-01] platform_feature: YouTube serialized Shorts (episodic Shorts) (youtube_shorts; captured 2026-10-07, 1d old; evidence aggregator; rights free_to_adapt). Why: Announced at Made On YouTube on 2026-09-23 and rolling out globally, it gives recurring-character series a native episodic container. Adapt: Package each Inspector case as a numbered episode so the recurring 'she commits the same fault herself' reveal pays off across a case-file series.
- [T-20261007-05] hook_pattern: Specific-frame hook with immediate visual contrast or confession (tiktok, instagram_reels; captured 2026-10-07, 1d old; evidence aggregator; rights free_to_adapt). Why: A vendor analysis says specific framing, visual contrast and confession openers beat generic openers, and that most high-click videos hook within the first 3 seconds (attributed there to TikTok for Business, not verified here). Adapt: Open on a close shot of the micro-fault with the Inspector's formal case title card in the first 2 seconds, silent, with no spoken setup.


Mechanisms allowed: curiosity_gap, recognition, visible_problem, status_contradiction, escalating_ritual, callout, other.
Scoring (0-10): legibility in first frame (0-3), specificity of the problem (0-3), promise of the bible's rule/payoff (0-2), send-ability to a specific person (0-2). Report the score and a one-sentence rationale per hook.



## Output contract (JSON only)
{
  "hook_variants": [ {"id": "H1", "premise_id": "P?", "first_frame": "", "first_line_or_action": "", "mechanism": "", "score": 0, "rationale": ""}, ... 6 items ],
  "selected": {"premise_id": "P?", "hook_id": "H?", "rationale": "why this premise+hook pair, in 2-3 sentences; mention the trade-off against the runner-up"}
}
