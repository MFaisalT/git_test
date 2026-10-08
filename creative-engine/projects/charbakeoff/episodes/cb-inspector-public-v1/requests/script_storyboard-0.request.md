<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

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
## Bible
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
## Selected premise and hook
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
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Locked-off eye-level frame at a bus stop: the Inspector in aubergine utility jacket stands centre-left beside an unreadable timetable board, lamp lit on her chest, clipboard on lanyard, one small paper ticket stub on the pavement four centimetres from a bin, blurred passers-by streaming through.",
        "first_line_or_action": "She does one slow two-finger tap on the clipboard and says to the passing blurred crowd: 'Finding one. A stub. Four centimetres from the bin.'",
        "mechanism": "visible_problem",
        "score": 8,
        "rationale": "Silhouette, lamp and a tiny concrete fault are all readable in frame one, the tap promises the procedure, and the tidy pavement sets up the later trail, though the rule payoff is only implied."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Same locked bus-stop frame, but a ribbon of identical ticket stubs is already faintly visible running along the pavement behind her toward the bench, while she stands facing the bin and the lamp glows on her chest.",
        "first_line_or_action": "She lifts the lamp, points it at a single stub by the bin, and says flatly, 'Somebody did this.'",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "Opening on the trail behind her plants the camera-notices-first rule and rewards a second look, but the one-second read of the single stub is slightly diluted by the extra detail."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Close-ish eye-level on the Inspector at the bus stop with clipboard raised and lamp on, glasses slightly down her nose, a blur of passers-by crossing between her and the lens, one stub on the pavement at her shoes.",
        "first_line_or_action": "As a blurred stranger walks straight through frame without a glance, she says louder, to nobody, 'I will repeat the finding.'",
        "mechanism": "escalating_ritual",
        "score": 7,
        "rationale": "The ignored-in-public energy of the bible is legible at once and the raised volume is funny muted via captions, but the fault itself is less specific in this tighter frame."
      },
      {
        "id": "H4",
        "premise_id": "P2",
        "first_frame": "Wide shot down a self-checkout lane: the Inspector in aubergine jacket and chest lamp faces one unbranded machine with a red indicator flashing, four closed flap pockets visible on her jacket, blurred shoppers passing behind.",
        "first_line_or_action": "She sweeps the lamp across the red light, clicks it off with an exaggerated click, and the camera begins a slow push-in.",
        "mechanism": "curiosity_gap",
        "score": 7,
        "rationale": "Red light plus the starting push-in create an immediate question of what the camera is moving toward, but pocket bulges are not yet legible at phone scale so the specificity is moderate."
      },
      {
        "id": "H5",
        "premise_id": "P2",
        "first_frame": "Wide self-checkout frame with the Inspector at centre, one jacket flap pocket visibly bulging with a round green shape (an unbranded apple) while she studies the flashing red indicator.",
        "first_line_or_action": "She gives one slow two-finger tap on the clipboard and nods firmly at the machine as if issuing a ruling.",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "A bulging pocket against a stern procedural pose shows the contradiction in the first frame and the tap lands the gesture, though it spends the signature gesture early and relies on small-scale fabric detail."
      },
      {
        "id": "H6",
        "premise_id": "P2",
        "first_frame": "Wide shot of the self-checkout lane at eye level, the machine's red light pulsing in the foreground, the Inspector's lamp and aubergine jacket small but clear mid-frame, shoppers blurred through the background.",
        "first_line_or_action": "Slow push-in begins as she lifts the lamp at the machine; no speech, only the lamp click and the machine's repeated beep.",
        "mechanism": "curiosity_gap",
        "score": 6,
        "rationale": "The silent push-in reads fine muted and teases the reveal, but the first frame explains the least about who she is and what she did."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "P1 with H1 gives the clearest cold introduction: silhouette, lamp, signature tap and a specific tiny fault all read in one locked frame, and the (static, on_camera_dialogue) pair is new relative to the empty recent list. The trade-off against the P2 runner-up is that P2's push-in is a stronger visual device but depends on pocket fabric reading at phone scale and has no voice, so P1 is the safer bake-off baseline."
    }
  },
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
}

## Production format to realise (declared by the selected premise; the validator checks it)
{
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
