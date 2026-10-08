<!-- requested_model: sonnet; effort: medium; tag: hooks-0 -->

# Stage 2 - Scored hook variants

Your responsibility: for the top two premises, write three hook variants each (six total) and score them. A hook is the first frame plus the first line or action; it must work muted and read in about one second.

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
## Bible (identity anchors and rule)
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
## Prior stage output
{
  "premises": {
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
    "ranking": [
      "P1",
      "P2",
      "P4",
      "P3",
      "P5"
    ],
    "ranking_rationale": "P1 is the cleanest first introduction: one locked frame shows silhouette, the tap gesture, the spoken verdict and a visible trail payoff that lands the bible rule even muted. P2 is a close second with a stronger visual device but no voice. P4, P3 and P5 each trade clarity of character for a formal trick, so they trail."
  }
}



Production formats: each premise declares one. Recently used (shot_architecture, audio_mode) pairs: []. Fixed by the brief: {}. Prefer a selected premise whose pair is not in the recent list unless the brief fixes it; name the pair in the selection rationale.

Mechanisms allowed: curiosity_gap, recognition, visible_problem, status_contradiction, escalating_ritual, callout, other.
Scoring (0-10): legibility in first frame (0-3), specificity of the problem (0-3), promise of the bible's rule/payoff (0-2), send-ability to a specific person (0-2). Report the score and a one-sentence rationale per hook.



## Output contract (JSON only)
{
  "hook_variants": [ {"id": "H1", "premise_id": "P?", "first_frame": "", "first_line_or_action": "", "mechanism": "", "score": 0, "rationale": ""}, ... 6 items ],
  "selected": {"premise_id": "P?", "hook_id": "H?", "rationale": "why this premise+hook pair, in 2-3 sentences; mention the trade-off against the runner-up"}
}
