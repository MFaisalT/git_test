<!-- requested_model: sonnet; effort: medium; tag: qa_review-0 -->

# Stage 4 - Creative QA (subjective; kept separate from deterministic gates)

Your responsibility: review the packet below against the predeclared rubric and report scores with one sentence of evidence each. You are not rewriting it. Deterministic validation has already run; do not re-check timing arithmetic.

## Rubric (weights): originality .15, hook .15, coherence .15, identity .10, audiovisual completeness .15, feasibility .10, grounding .08, commercial fit .12. Anchors: 1 fail, 3 adequate, 5 excellent.

## Packet
{
  "packet": {
    "brief": {
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
      "commercial": null,
      "negative_constraints": [
        "Do not copy any researched creator's look, catchphrase or footage.",
        "No readable brand text in frame.",
        "No real people or recognisable locations."
      ]
    },
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "P1 with H1 gives the clearest cold introduction: silhouette, lamp, signature tap and a specific tiny fault all read in one locked frame, and the (static, on_camera_dialogue) pair is new relative to the empty recent list. The trade-off against the P2 runner-up is that P2's push-in is a stronger visual device but depends on pocket fabric reading at phone scale and has no voice, so P1 is the safer bake-off baseline."
    },
    "premises": [
      {
        "id": "P1",
        "logline": "At a bus stop the Inspector calmly cites a stranger-free fault, one stray ticket stub four centimetres from the bin, then walks off to file it trailing a paper stream from her own flap pockets.",
        "audience_emotion": "Dry delight of recognition, then a small shock of laughter when the camera lingers on the trail.",
        "character_desire": "Restore order: get the stub into the bin and the finding on record.",
        "obstacle": "The city keeps walking through frame and ignores her; the stub is a centimetre beyond easy reach in a formal pose.",
        "escalation": "Verdict volume rises one notch after each blurred passer-by crosses without reacting; she bins the stub with ceremony and logs it.",
        "surprise": "As she turns to leave, a ribbon of identical ticket stubs is shown spilling from her pockets across the pavement behind her, a trail running back to the bench where she began.",
        "payoff": "Rule lands visibly: the camera notices before she does, she is exposed as the culprit of the very fault she cited, and she exits satisfied, unaware.",
        "structure": "Locked-off setup, procedure, verdict, reveal. 0-3s: she stands centre-left by the timetable board (unreadable), lamp on chest, passers-by blur through; 3-6s: two-finger tap once, verdict line; 6-9s: she bins the stub and writes; 9-12s: she walks out of frame-right leaving the trail in clear view, one beat held on the trail.",
        "why_send_it": "Anyone who has a friend who corrects everyone else's habits while trailing their own mess; sent with 'this is you'.",
        "commercial_fit": "None; brief has no commercial and the premise carries no product or brand.",
        "rejected_because": "",
        "production_format": {
          "shot_architecture": "single_take_static",
          "audio_mode": "on_camera_dialogue",
          "camera_style": "Locked-off phone at eye level, slightly too formal framing, aubergine against grey street; the reveal needs no camera move because the trail enters frame behind her.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Static frame makes the silhouette and the trail reveal legible muted; short spoken lines (about 20 words, under 2 words per second) add the bureaucratic voice. Speech is optional: the gag reads on captions alone."
        }
      },
      {
        "id": "P2",
        "logline": "At a self-checkout lane a slow push-in follows the Inspector auditing the machine's beeping, while her four flap pockets reveal unscanned produce she is walking out with.",
        "audience_emotion": "Rising dread-laugh as the camera creeps in on something she has not noticed.",
        "character_desire": "Get the lane to behave and have the unexpected-item fault formally resolved.",
        "obstacle": "The machine keeps flashing its red indicator and nobody nearby reacts; she must stay composed and procedural.",
        "escalation": "Push-in starts wide on the lane; each time she lifts the lamp at the machine, the framing tightens and one more pocket bulge becomes visible: an apple, a lemon, a bread roll, a pepper (all unbranded).",
        "surprise": "She taps the clipboard, nods at the green light and exits, and the final close frame shows all four pockets full.",
        "payoff": "Rule lands visibly: the verdict she pronounced on the machine becomes her own offence, and the camera noticed first via the push-in.",
        "structure": "Push-in structure: one continuous move converts a wide procedural scene into an incriminating close-up; escalation is the lens, not dialogue. 0-4s wide, 4-8s lamp sweep and tap, 8-12s tight on pockets as she walks away.",
        "why_send_it": "Anyone who has ever absent-mindedly walked out of a shop holding something; sent to a partner with 'we are her'.",
        "commercial_fit": "None; brief has no commercial and the premise carries no product or brand.",
        "rejected_because": "Strong but silent-only and the reveal depends on pocket fabric reading at phone scale; held as runner-up.",
        "production_format": {
          "shot_architecture": "single_take_moving_camera",
          "audio_mode": "silent_ambience",
          "camera_style": "Slow motivated push-in on a handheld-feel phone from lane end, steady, ending tight on the chest-level pockets.",
          "continuity_reuse": {
            "voice": "none",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Moving camera is the joke engine; no voice needed so it reads in a muted feed; foley (lamp click, clipboard tap) carries the character. New location shows the Inspector travels."
        }
      },
      {
        "id": "P3",
        "logline": "On a cafe terrace a companion-held phone follows the Inspector as her dictated field report declares the terrace faultless while the handheld lingers on the rings her own cup leaves on every table she passes.",
        "audience_emotion": "Warm exasperation at a character who sincerely certifies her own mess.",
        "character_desire": "Issue a clean certificate for the terrace.",
        "obstacle": "Her report and the evidence disagree; she cannot see the evidence because she is looking at the next table.",
        "escalation": "Voiceover reports one clause per table ('Table one: compliant. Table two: compliant.') while each table shows a fresh cup ring behind her; the handheld creeps closer.",
        "surprise": "The cup in her hand is the same one and it is dripping; the voiceover's last word is 'immaculate' over the stained table.",
        "payoff": "Rule lands: the report certifies the terrace while the image convicts her; she is exposed as the next offender without noticing.",
        "structure": "Report versus evidence: narration states one thing, picture another, handheld follow takes the viewer's side. Accumulative rhythm of three tables then a final turn.",
        "why_send_it": "Anyone who knows a colleague who signs off their own sloppy work; send as 'your meeting minutes'.",
        "commercial_fit": "None; brief has no commercial and the premise carries no product or brand.",
        "rejected_because": "Voice-over contradiction is clever but the mouth is not synced so the Inspector is less physically present in the first look.",
        "production_format": {
          "shot_architecture": "pov_handheld",
          "audio_mode": "voiceover_narration",
          "camera_style": "Companion-held phone, eye level, following one step behind; angle changes come from the holder drifting toward tables and the cup, not cuts.",
          "continuity_reuse": {
            "voice": "same",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Handheld gives a different visual language; voice-over lets the bureaucratic cadence be reused without lip-sync risk; companion holder stays off screen so no second performer."
        }
      },
      {
        "id": "P4",
        "logline": "A bus-stop sign leans; the Inspector straightens it and ends in exactly her opening pose leaning on it, so the loop shows it leaning again.",
        "audience_emotion": "Smug satisfaction curdling into the pleasure of a perfect loop.",
        "character_desire": "Make the sign pole exactly vertical.",
        "obstacle": "The pole's lean returns every time she steps back to admire it.",
        "escalation": "Frame one: she is already mid-tilt posture beside the pole, clipboard raised, lamp on. Each of three attempts at straightening looks successful, then her elbow rests on it and it drifts back. Caption stamps appear in post: 'Verdict: leaning.'",
        "surprise": "The last frame is identical to the first, with her blamed pose restored; she does not notice she is the cause.",
        "payoff": "Rule lands at loop point: she is the culprit and the sign is the same as before, so the viewer's second watch reveals the elbow.",
        "structure": "Loop: frame one equals frame last; the first watch shows the pole fixed, the second shows the cause. Pacing is tidy and mechanical.",
        "why_send_it": "Anyone who loves seamless loops; sent with 'watch it twice'.",
        "commercial_fit": "None; brief has no commercial and the premise carries no product or brand.",
        "rejected_because": "Loop is novel but the cause is subtle and the character's voice is absent, so it explains least about her energy.",
        "production_format": {
          "shot_architecture": "loop",
          "audio_mode": "text_over_broll",
          "camera_style": "Locked-off phone at eye level; end pose matches opening pose exactly so autoplay repeats seamlessly; one caption in post.",
          "continuity_reuse": {
            "voice": "none",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Loop and caption-only differ from the others and test whether the rule reads with no speech at all; location reused deliberately to isolate the premise variable."
        }
      },
      {
        "id": "P5",
        "logline": "At self-checkout the Inspector argues with the machine's flat recorded voice, and an insert on the scale shows the unexpected item is her own lamp.",
        "audience_emotion": "Pleasure in an immovable bureaucrat meeting an equally immovable machine.",
        "character_desire": "Win a procedural argument with the machine.",
        "obstacle": "The machine repeats one line and cannot be persuaded; the scale will not settle.",
        "escalation": "Each exchange gets more formal: she cites the item as 'unclaimed', the machine repeats 'unexpected item in the bagging area', she raises her tone one notch.",
        "surprise": "Cut to the scale insert: it holds her own lamp, detached from the chest strap, which she has put down without noticing.",
        "payoff": "Rule lands but conflicts with the lamp being centrally on her silhouette; the cut-to-insert uses the only cut in the budget.",
        "structure": "Duel, insert, exit: machine and Inspector trade lines, insert reveals the cause, she exits.",
        "why_send_it": "Anyone who has argued with a self-checkout; sent with 'my last shop'.",
        "commercial_fit": "None; brief has no commercial and the premise carries no product or brand.",
        "rejected_because": "The lamp is a core silhouette item and removing it risks the character's look; the machine voice also replaces strangers' reactions rather than the world ignoring her.",
        "production_format": {
          "shot_architecture": "split_or_insert",
          "audio_mode": "off_camera_dialogue",
          "camera_style": "Wide locked-off phone with one insert close-up of the scale in edit; machine voice is a generic recorded line off camera.",
          "continuity_reuse": {
            "voice": "new",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Insert uses the one allowed cut; the machine voice is the second voice and not a stranger."
        }
      }
    ],
    "script": {
      "title": "Finding One",
      "synopsis": "At a bus stop the Inspector formally cites a single ticket stub four centimetres from the bin while the city ignores her, bins it with ceremony, and walks away trailing a ribbon of identical stubs from her own pockets.",
      "beats": [
        {
          "beat": "Locked frame shows silhouette, lamp and the stub; one two-finger tap",
          "function": "hook"
        },
        {
          "beat": "She states the finding to indifferent passers-by",
          "function": "setup"
        },
        {
          "beat": "Louder verdict, bins and logs the stub",
          "function": "escalation"
        },
        {
          "beat": "Ribbon of stubs spills from her pockets as she exits",
          "function": "turn"
        },
        {
          "beat": "Held beat on the trail she does not see",
          "function": "payoff"
        }
      ],
      "dialogue": [
        {
          "speaker": "Inspector",
          "line": "Finding one.",
          "delivery": "measured, bureaucratic",
          "on_camera": true
        },
        {
          "speaker": "Inspector",
          "line": "A stub. Four centimetres from the bin.",
          "delivery": "short declarative, slightly louder",
          "on_camera": true
        },
        {
          "speaker": "Inspector",
          "line": "Litter. Noted. Filed.",
          "delivery": "verdict volume up one notch",
          "on_camera": true
        }
      ],
      "caption_text": "Finding one. A stub. Four centimetres from the bin. Litter. Noted. Filed.",
      "cta": "",
      "disclosure_line": "AI-generated character and footage."
    },
    "scenes": [
      {
        "scene_id": "S1",
        "start_s": 0,
        "end_s": 3,
        "location": "Bus stop with a timetable board (recurring bible location)",
        "action": "Frame one: the Inspector stands centre-left beside the blank timetable board, lamp lit on her chest, facing a single ticket stub on the pavement four centimetres from the steel bin. A blurred passer-by crosses behind. After one beat she gives one slow two-finger tap on the clipboard, then speaks.",
        "performance": "Invested task: formally open a finding; goal is to get the stub on record, obstacle is the crowd walking through frame, tactic is stillness and procedure. Eyes stay on the stub, then lift to the passing blur.",
        "microexpression": "Brows level; a faint settle of the glasses down the nose as she looks at the stub.",
        "dialogue": [
          {
            "speaker": "Inspector",
            "line": "Finding one.",
            "delivery": "measured, bureaucratic, normal volume, aimed at passers-by",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "medium-wide, eye level, slightly too formal framing, Inspector centre-left",
          "lens": "28mm-equivalent phone main camera, mild wide",
          "movement": "Locked-off propped phone with a single small settle-wobble in the first half second, then still",
          "rig": "phone propped on a low wall at eye level"
        },
        "lighting": "Soft overcast daylight key from camera-left above; cool grey fill from the sky; faint warm bounce off the sandstone pavement into the jacket underside; soft contact shadows under shoes and bin. Light stays constant for the whole clip.",
        "environment": "Generic grey street bus stop, unreadable blank timetable board, steel bin, wooden bench behind her; blurred generic passers-by cross at mid-distance, never in focus and never reacting to her.",
        "sound": {
          "ambience": "real street ambience: distant traffic, footsteps, soft wind",
          "foley": [
            "slow two-finger clipboard tap, exaggerated one notch",
            "lamp hum-click as it settles",
            "footsteps passing"
          ],
          "music": "none",
          "voice": "on-camera, close-in room tone, flat bureaucratic cadence"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "tiny clipboard on lanyard",
          "bright circular inspection lamp on chest strap",
          "small paper ticket stub (the cited fault)",
          "street bin",
          "bus stop timetable board (unreadable, no text)",
          "bus stop bench"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S2",
        "start_s": 3,
        "end_s": 6,
        "location": "Bus stop with a timetable board (recurring bible location)",
        "action": "She raises the lamp and sweeps it onto the stub. A second blurred stranger crosses frame without a glance. She states the finding to them.",
        "performance": "Invested task: pin the fault down for the record; obstacle is that nobody answers, tactic is to enunciate every word and measure the gap with two fingers held up.",
        "microexpression": "Warm disappointment starts at the corners of her mouth, not anger.",
        "dialogue": [
          {
            "speaker": "Inspector",
            "line": "A stub. Four centimetres from the bin.",
            "delivery": "short declarative lines, slightly louder than the first",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "medium-wide, eye level, slightly too formal framing, Inspector centre-left",
          "lens": "28mm-equivalent phone main camera, mild wide",
          "movement": "Locked-off, no move",
          "rig": "phone propped on a low wall at eye level"
        },
        "lighting": "Soft overcast daylight key from camera-left above; cool grey fill from the sky; faint warm bounce off the sandstone pavement into the jacket underside; soft contact shadows under shoes and bin. Light stays constant for the whole clip.",
        "environment": "Generic grey street bus stop, unreadable blank timetable board, steel bin, wooden bench behind her; blurred generic passers-by cross at mid-distance, never in focus and never reacting to her.",
        "sound": {
          "ambience": "real street ambience: distant traffic, footsteps, soft wind",
          "foley": [
            "lamp click on",
            "paper rustle of the stub in the breeze",
            "clipboard knock on lanyard"
          ],
          "music": "none",
          "voice": "on-camera, a notch louder"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "tiny clipboard on lanyard",
          "bright circular inspection lamp on chest strap",
          "small paper ticket stub (the cited fault)",
          "street bin",
          "bus stop timetable board (unreadable, no text)",
          "bus stop bench"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S3",
        "start_s": 6,
        "end_s": 9,
        "location": "Bus stop with a timetable board (recurring bible location)",
        "action": "A third blurred passer-by walks through frame ignoring her. Louder, she gives the verdict, picks up the stub, bins it with ceremony and writes on the clipboard with a pen. Behind her, unseen by her, a first ticket stub slips from a flap pocket.",
        "performance": "Invested task: carry out the sentence precisely; obstacle is the stub needing a formal reach, tactic is a stiff, correct posture while she bins and logs.",
        "microexpression": "Brief satisfied press of the lips as the stub drops into the bin.",
        "dialogue": [
          {
            "speaker": "Inspector",
            "line": "Litter. Noted. Filed.",
            "delivery": "verdict volume up one notch, crisp",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "medium-wide, eye level, slightly too formal framing, Inspector centre-left",
          "lens": "28mm-equivalent phone main camera, mild wide",
          "movement": "Locked-off, no move",
          "rig": "phone propped on a low wall at eye level"
        },
        "lighting": "Soft overcast daylight key from camera-left above; cool grey fill from the sky; faint warm bounce off the sandstone pavement into the jacket underside; soft contact shadows under shoes and bin. Light stays constant for the whole clip.",
        "environment": "Generic grey street bus stop, unreadable blank timetable board, steel bin, wooden bench behind her; blurred generic passers-by cross at mid-distance, never in focus and never reacting to her.",
        "sound": {
          "ambience": "real street ambience: distant traffic, footsteps, soft wind",
          "foley": [
            "stub drops into the bin with a hollow tick",
            "pen scratch on the clipboard",
            "lamp click off",
            "pocket flap slap"
          ],
          "music": "none",
          "voice": "on-camera, verdict volume"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "tiny clipboard on lanyard",
          "bright circular inspection lamp on chest strap",
          "small paper ticket stub (the cited fault)",
          "street bin",
          "bus stop timetable board (unreadable, no text)",
          "bus stop bench"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S4",
        "start_s": 9,
        "end_s": 12,
        "location": "Bus stop with a timetable board (recurring bible location)",
        "action": "She turns and walks out of frame-right satisfied. Behind her a ribbon of identical ticket stubs spills from her flap pockets and runs along the pavement back to the bench. The frame holds one beat on the trail after she leaves, then ends.",
        "performance": "Invested task: leave the scene correct and orderly; she never looks down. The camera notices the trail before she does.",
        "microexpression": "Calm, content half-nod; no glance back.",
        "dialogue": [],
        "camera": {
          "shot": "medium-wide, eye level, frame holds on the trail after she exits frame-right",
          "lens": "28mm-equivalent phone main camera, mild wide",
          "movement": "Locked-off, no move; hold on the empty frame with the trail",
          "rig": "phone propped on a low wall at eye level"
        },
        "lighting": "Soft overcast daylight key from camera-left above; cool grey fill from the sky; faint warm bounce off the sandstone pavement into the jacket underside; soft contact shadows under shoes and bin. Light stays constant for the whole clip.",
        "environment": "Generic grey street bus stop, unreadable blank timetable board, steel bin, wooden bench behind her; blurred generic passers-by cross at mid-distance, never in focus and never reacting to her.",
        "sound": {
          "ambience": "real street ambience: distant traffic, footsteps, soft wind",
          "foley": [
            "two flat shoe steps receding",
            "stubs fluttering and ticking on pavement",
            "distant traffic swells"
          ],
          "music": "none",
          "voice": "none"
        },
        "captions": "Verdict: litter. (She is the litter.)",
        "transition_out": "end of clip",
        "props_from_frame_one": [
          "tiny clipboard on lanyard",
          "bright circular inspection lamp on chest strap",
          "street bin",
          "bus stop bench",
          "bus stop timetable board (unreadable, no text)",
          "ribbon of identical paper ticket stubs spilling from her flap pockets"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      }
    ],
    "continuity": {
      "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger.",
      "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun; plain charcoal trousers, flat black work shoes. Same costume for the whole episode.",
      "props": [
        "tiny clipboard on lanyard",
        "bright circular inspection lamp on chest strap",
        "small paper ticket stub (the cited fault)",
        "street bin",
        "pen",
        "ribbon of identical paper ticket stubs spilling from her flap pockets",
        "bus stop bench",
        "bus stop timetable board (unreadable, no text)"
      ],
      "notes": "Rule: the Inspector is exposed as the culprit of the fault she cited; the camera notices first via the trail. Signature two-finger clipboard tap used exactly once, in S1. Strangers are blurred generic extras who never react and are never the joke. No readable text anywhere, including timetable board and stubs. Hair: dark hair in a tight low bun with a matte finish."
    },
    "growth_hypotheses": [
      {
        "hypothesis": "The trail reveal at 9-12 s lands the rule muted and prompts the share 'this is you'.",
        "metric": "share rate and completion rate",
        "falsifier": "completion under 60% or fewer than 1 share per 100 views"
      },
      {
        "hypothesis": "Escalating verdict volume to ignoring strangers reads as the character's energy without mugging.",
        "metric": "comment mentions of her being ignored or of the trail",
        "falsifier": "comments do not reference the trail or the ignoring"
      }
    ]
  }
}

## Output contract (JSON only)
{
  "scores": {"originality": 0, "hook": 0, "coherence": 0, "identity": 0, "audiovisual": 0, "feasibility": 0, "grounding": 0, "commercial_fit": 0},
  "evidence": {"originality": "", "hook": "", "coherence": "", "identity": "", "audiovisual": "", "feasibility": "", "grounding": "", "commercial_fit": ""},
  "weighted_total": 0.0,
  "pass_thresholds": {"character_intent": true, "premise_specific_payoff": true, "complete_direction": true, "commercial_fit": true},
  "summary": "two sentences",
  "top_fix": "the single most valuable change, or 'none'"
}
