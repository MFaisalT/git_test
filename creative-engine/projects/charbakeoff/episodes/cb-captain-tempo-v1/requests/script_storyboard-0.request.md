<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{
  "brief_id": "CB1_intro_captain-tempo-v1",
  "title": "Character bake-off intro: 12-second first public appearance of captain-tempo-v1",
  "project": "charbakeoff",
  "bible_ref": "captain-tempo-v1",
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
  "bible_id": "captain-tempo-v1",
  "version": 1,
  "show_title": "Captain Tempo (working title; name/IP uncleared)",
  "logline": "A wiry, booming 60-year-old woman in a shiny tracksuit conducts the public like an orchestra, counts strangers through crossings, lifts and queues, and breaks into a victory dance whenever anything she counted happens, which it always would have anyway.",
  "character": {
    "name": "Captain Tempo",
    "age_range": "58-65",
    "sex_presentation": "woman",
    "silhouette": "Glossy teal and gold tracksuit zipped to the chin, white sweatband, a referee whistle on a red cord, chunky white trainers, a small handheld metronome clipped to the waistband.",
    "identity_anchors": "Lean weathered face, deep laugh lines, bright wide-set grey eyes, short silver hair cropped close at the sides and spiky on top, very mobile eyebrows, a wide gap-toothed grin.",
    "hair": "short silver hair cropped close at the sides and spiky on top, matte",
    "lower_body": "glossy teal tracksuit trousers with a gold side stripe, chunky white trainers",
    "desire": "To make the whole city move in time.",
    "flaw": "She takes credit for every event she counted toward, even though none of it needed her.",
    "rule": "She counts something down out loud and with her whole body; it happens on its own schedule; she celebrates with an original victory move as if she caused it; a passer-by walks through her celebration without noticing. The camera lingers one beat too long on the celebration.",
    "performance_register": "Big, physical, loud, breathless, joyful; arms conduct, legs bounce, the whistle blows; the comedy is total commitment to a pointless job plus the world's indifference.",
    "voice": "Booming, rhythmic, counting in a hoarse shout: 'THREE... TWO... ONE... AND!' Short bursts, never sentences longer than six words.",
    "signature_gesture": "The Tempo Stomp: two stomps, a hip swing, a whistle blast, both fists to the sky (original move; once per episode)."
  },
  "world": {
    "recurring_locations": [
      "pedestrian crossing at a busy junction",
      "glass lift lobby of a shopping centre",
      "bakery queue on a high street"
    ],
    "visual_language": "Handheld phone, wide, slightly low angle so she towers; saturated teal and gold against grey city; strangers as a blurred, indifferent stream.",
    "sound_language": "Real traffic and crowd; her whistle and counting dominate; one original percussive sting in edit only if licensed."
  },
  "do_not": [
    "No bob/moustache/white-tunic combination or any researched creator's identity, catchphrase, costume or footage.",
    "No real people, no real brands, no religion, no politics, no mocking of strangers' bodies, accents, disabilities or faith; strangers in frame are generic extras who never become the joke.",
    "No trending dance or sound that is not cleared; any dance is an original move described in the storyboard.",
    "No firsthand product endorsements."
  ],
  "evolution_policy": "Locations and the thing she counts vary every episode; silhouette, rule, register and the Tempo Stomp are fixed until a versioned bump.",
  "provenance": {
    "created": "2026-10-08",
    "basis": "owner feedback 2026-10-08: reference accounts are loud, physical, public and dance; hypothesis B is an original loud public character with an original move",
    "status": "hypothesis, untested",
    "saved_at": "2026-10-08T05:53:57Z",
    "bump_reason": "character bake-off hypothesis"
  },
  "audience": {
    "target": "global; physical comedy reads muted; counting is universal; no region-specific references",
    "language_default": "visual-first; English numbers when spoken"
  }
}
## Selected premise and hook
{
  "premises": {
    "premises": [
      {
        "id": "P1",
        "logline": "At a busy junction Captain Tempo conducts the red-man countdown for a blurred stream of pedestrians, shouts THREE, TWO, ONE, AND, the signal flips exactly when it was always going to, she detonates the Tempo Stomp, and a commuter walks straight through her fist-pump without a glance while the camera holds one beat too long.",
        "audience_emotion": "Delighted disbelief, then warm laughter at pure misplaced confidence.",
        "character_desire": "To make the whole city move in time, starting with this crossing.",
        "obstacle": "The signal runs on its own timer and the crowd is indifferent to her.",
        "escalation": "Low-angle push-in as the count drops from a whisper-shout to a roar; arms conduct harder each number; the whistle joins on TWO.",
        "surprise": "The Stomp lands, and a passer-by calmly walks through the middle of her celebration, hair-width from her raised fists, never looking over.",
        "payoff": "Bible rule in full: she counts down aloud with her whole body, the light changes on its own schedule, she celebrates with the original Tempo Stomp (two stomps, hip swing, whistle blast, both fists to the sky) as if she caused it, a passer-by walks through it unnoticing, and the camera lingers one beat too long on her frozen victory pose.",
        "structure": "Setup-countdown-release-deflation: one continuous build to a single beat, then a held anticlimax.",
        "why_send_it": "Anyone who has ever stood at a crossing and felt personally responsible for the light sends it to the friend who 'always makes the green come'.",
        "commercial_fit": "None; no product, no brands.",
        "rejected_because": "",
        "production_format": {
          "shot_architecture": "single_take_moving_camera",
          "audio_mode": "on_camera_dialogue",
          "camera_style": "Handheld phone, wide, slow low-angle push-in from across the road toward her; the camera is the crowd's indifferent witness, settling on a held beat after the Stomp.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Clearest single-take introduction of energy, rule and silhouette; a push-in sells her towering scale, one unit and zero cuts fit draft_mini, and shouted numbers are universal when muted. It is the bible's canonical location so the rule is unambiguous."
        }
      },
      {
        "id": "P2",
        "logline": "In a glass shopping-centre lift lobby, Captain Tempo silently conducts the lift down from the top floor with finger counts and whistle blasts; it arrives, she celebrates, the doors open on nobody, she steps in and the clip ends on the exact opening frame so it replays as if the lift had just been summoned again.",
        "audience_emotion": "Hypnotic, absurd satisfaction; a calm loop-laugh.",
        "character_desire": "To bring the lift down on the beat.",
        "obstacle": "Floors descend at lift speed; she cannot hurry them and will not stop conducting.",
        "escalation": "Floor indicator lights tick down while her gestures grow from baton-small to full-arm sweeps; the whistle punctuates each floor.",
        "surprise": "The doors open and the lift is empty and has plainly been coming all along; the final frame silently mirrors frame one, restarting the whole gag.",
        "payoff": "Visible displacement: she credits herself for an arrival that was always going to happen, then the loop resets her to the same hopeful pose. The Tempo Stomp fires once on arrival while a blurred shopper crosses behind the glass without turning.",
        "structure": "Loop: ending frame equals opening frame so the countdown reads as endless.",
        "why_send_it": "Loop-watchers send it to a colleague who also 'calls' the lift by pressing the button three extra times.",
        "commercial_fit": "None; keep signage out of frame.",
        "rejected_because": "loop gimmick dilutes the spoken counting that carries the bible voice; lift floor display is small to read muted",
        "production_format": {
          "shot_architecture": "loop",
          "audio_mode": "silent_ambience",
          "camera_style": "Locked-off phone at a slight low angle in front of the glass lift; she fills the left third, floor lights and moving lift cage give the frame its clock.",
          "continuity_reuse": {
            "voice": "new",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Tests a quieter register than P1: the count lives in fingers, whistle foley and the lift lights, so legibility muted is proven; a loop ending suits autoplay. The location is new to show range, the costume unchanged because the silhouette is fixed."
        }
      },
      {
        "id": "P3",
        "logline": "Captain Tempo, filming herself at arm's length in a bakery queue, counts down the number display to her turn; a deadpan voice off camera keeps confirming each number; when her number lands she celebrates, and the baker serves the next blurred customer behind her without a glance.",
        "audience_emotion": "Affectionate, intimate amusement, as if she is a loud friend vlogging a tiny triumph.",
        "character_desire": "To get her loaf on the beat she herself called.",
        "obstacle": "The queue moves at its own pace and the numbers advance by someone else's rhythm.",
        "escalation": "Her selfie view tilts as she bounces on her toes; each tick brings her closer to the lens until her eyebrows fill the frame.",
        "surprise": "Her number turns out to be called while she is mid-Stomp, so the Stomp becomes the answer to a question nobody asked; the off-camera voice flatly says 'Your loaf.'",
        "payoff": "Bible rule in full: she counts the queue down aloud, it resolves on its own schedule, she celebrates with the Tempo Stomp as if she caused it, and a customer walks through her celebration unnoticing while the phone lingers one beat too long.",
        "structure": "Vlog-style countdown to a mundane payoff, closed by a second voice puncturing it.",
        "why_send_it": "People send it to a sibling who narrates the queue like a sport.",
        "commercial_fit": "None; no real products or brand names.",
        "rejected_because": "phone-in-hand framing loses her full-body silhouette and the Stomp; bakery interior risks readable text",
        "production_format": {
          "shot_architecture": "pov_handheld",
          "audio_mode": "off_camera_dialogue",
          "camera_style": "Phone held by Captain Tempo at arm's length, wobbling with her bounce, then dropping to waist height for the Stomp so her whole teal-and-gold figure is visible.",
          "continuity_reuse": {
            "voice": "new",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Shows the character from her own point of view, which proves the identity anchors hold when she is close to the lens; the off-camera voice allows a second, flat comic rhythm while keeping one on-camera speaker."
        }
      },
      {
        "id": "P4",
        "logline": "At a crossing, a clipped metronome on Captain Tempo's waistband ticks in sync with a bus she is counting in; one insert close-up of the metronome shows its arm stop dead the instant the bus arrives, and she turns to face camera and Stomps as if she stopped it.",
        "audience_emotion": "Playful curiosity, then a small rush of rhythm-satisfaction.",
        "character_desire": "To bring the bus in on tempo.",
        "obstacle": "A bus does not obey a metronome; it arrives when it arrives.",
        "escalation": "Wide shot: her conducting widens as the bus nears in the background; a single cut to the metronome close-up shows its swing slowing and her thumb nudging it.",
        "surprise": "The metronome's stop and the bus's arrival land together only because she nudged the arm, so she is both cause and fraud.",
        "payoff": "A cheap lie rewarded: the bus arrives on its own, the Tempo Stomp lands, a blurred commuter boards without noticing, and the final shot lingers one beat too long.",
        "structure": "Wide-insert-wide: main action, one cutaway detail that reframes it, then a return to the celebration.",
        "why_send_it": "For the friend who 'times' their arrival to match the bus and takes the credit.",
        "commercial_fit": "None; no readable bus or route text.",
        "rejected_because": "the single insert spends the entire cut budget on a prop gag; the Stomp competes with the insert for the clip's beats",
        "production_format": {
          "shot_architecture": "split_or_insert",
          "audio_mode": "text_over_broll",
          "camera_style": "Wide locked-off phone with a slight low angle, plus one macro insert of the waist metronome assembled in edit; the single hard cut is the only edit.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "A one-cut architecture that fits draft_mini; text-only audio tests whether the idea reads on mute, with a post-added counter (3, 2, 1) since there is no speech."
        }
      },
      {
        "id": "P5",
        "logline": "In the lift lobby Captain Tempo counts a lift down from five, but it arrives on THREE; undaunted, she restarts and counts it back up to a celebration, claiming a victory she visibly miscounted, while the blurred crowd steps around her.",
        "audience_emotion": "Gleeful confusion, lovable pomposity.",
        "character_desire": "To be the reason the lift came when she said it would.",
        "obstacle": "The lift is early, which ruins her count and threatens her authority.",
        "escalation": "The count races to reconcile the lift's early arrival; her volume rises through the restart; the whistle blasts twice in disbelief.",
        "surprise": "She does not admit the miss: she runs the count back up to meet the lift and Stomps anyway, bending reality to her tempo.",
        "payoff": "Failure reframed as victory: the Tempo Stomp lands over a doors-already-open lift, and the camera holds a beat too long on her glowing, wrong, perfectly happy face.",
        "structure": "Reversal: expectation set, expectation broken, character bends the world's schedule to her own story.",
        "why_send_it": "For the friend who never admits being wrong and claims credit anyway.",
        "commercial_fit": "None; keep lift panels and signs unreadable.",
        "rejected_because": "the miscount undercuts the bible rule that it always happens on its own schedule, and muting it is slightly harder to read",
        "production_format": {
          "shot_architecture": "single_take_static",
          "audio_mode": "on_camera_dialogue",
          "camera_style": "Locked-off phone, wide, slightly low angle on a tripod-height prop in front of the glass lift so she fills the frame with the lift doors behind her.",
          "continuity_reuse": {
            "voice": "same",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "A static single take is the cheapest render and a deliberate contrast to P1's moving camera; a new location shows range while the same voice keeps the counting hook recognisable."
        }
      }
    ],
    "ranking": [
      "P1",
      "P3",
      "P5",
      "P2",
      "P4"
    ],
    "ranking_rationale": "P1 delivers the full bible rule in the cleanest single-take frame and reads muted at once, making it the best fit for a cold viewer. P3 offers a different intimacy and voice without losing the rule, while P5 adds a character-driven reversal; P2 and P4 are stronger as format experiments than as introductions."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Handheld phone, wide and slightly low across a busy junction: Captain Tempo in glossy teal and gold tracksuit, white sweatband, red-cord whistle, chunky white trainers, stands at the kerb towering over a blurred grey stream of pedestrians, both arms raised like a conductor about to cue the orchestra, the red standing-man signal glowing behind her (no readable text).",
        "first_line_or_action": "Her raised arms slam down on the beat as she bellows 'THREE!' and the camera starts its slow push-in.",
        "mechanism": "escalating_ritual",
        "score": 9,
        "rationale": "Silhouette, scale, public setting and the conducting posture read in one second muted, and the downbeat promises a countdown with a payoff; it is the cleanest send-to-the-friend-who-thinks-they-control-the-light hook."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Extreme low-angle close frame on the small metronome clipped to her glossy teal waistband, its arm ticking left and right in sharp focus, the red crossing signal and blurred legs of passers-by soft behind it.",
        "first_line_or_action": "Without a cut the phone tilts up the tracksuit zip to her gap-toothed grin as she whistle-blasts once and shouts 'TWO!'.",
        "mechanism": "curiosity_gap",
        "score": 7,
        "rationale": "The ticking prop is a vivid, specific tease and the tilt-up reveals the character, but the first frame alone does not show her silhouette or the crossing clearly enough to hit full legibility."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Wide low-angle shot from the far kerb: Captain Tempo stands with her back half to camera, facing the blurred crowd gathered at the crossing the way a conductor faces an orchestra, fists clenched at chest height, whistle in her teeth, saturated teal and gold against grey tarmac.",
        "first_line_or_action": "She blasts the whistle and flings her arms wide in a huge cue; the stream of pedestrians simply keeps walking, unaffected, as she hisses 'AND...' under her breath.",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "A tiny woman commanding an indifferent crowd shows the bible's core contradiction instantly and reads muted, though the setup arrives slightly before the countdown so the rule is promised a beat later than in H1."
      },
      {
        "id": "H4",
        "premise_id": "P3",
        "first_frame": "Selfie-view at arm's length, wobbling: Captain Tempo's lean weathered face, wide grey eyes and raised silver-spiky hair fill the frame, her eyebrows arched mid-bounce, a blurred bakery queue and an unlabelled glowing number display behind her shoulder.",
        "first_line_or_action": "She jabs a finger at the number display behind her and stage-whispers 'FOUR...' with huge eyebrow work straight to lens.",
        "mechanism": "visible_problem",
        "score": 8,
        "rationale": "The face, eyebrows and a very legible small problem (waiting for your number) read muted and feel intimate, though the full silhouette is not yet visible, which costs a point on legibility."
      },
      {
        "id": "H5",
        "premise_id": "P3",
        "first_frame": "Selfie-view at arm's length: Captain Tempo, mid-sentence, leans toward the lens and points her whole arm directly at the viewer, the blurred bakery queue behind, her sweatband and whistle cord visible at the frame edge.",
        "first_line_or_action": "She mouths and hisses 'YOU. Hold my place. THREE...' then swings the phone round to the queue and begins counting down with a finger.",
        "mechanism": "callout",
        "score": 7,
        "rationale": "Directly addressing the viewer makes it highly sendable and the countdown starts at once, but the command is spoken so it reads weaker muted and the pointing gesture is generic rather than specific to her."
      },
      {
        "id": "H6",
        "premise_id": "P3",
        "first_frame": "Phone dropped to waist height so her whole teal-and-gold figure bounces on tiptoe in the foreground, arms half raised, chunky white trainers visible, the blurred bakery queue shuffling forward behind her.",
        "first_line_or_action": "A flat off-camera voice says 'Forty-one.' and she answers by throwing both arms up and shouting 'COMING IN ON THE BEAT!'.",
        "mechanism": "recognition",
        "score": 6,
        "rationale": "The full silhouette is strong and anyone who narrates a queue will recognise the mood, but the deadpan voice is audio-dependent and the rule does not appear in the first second."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "P1 with H1 shows the full silhouette, public setting, conducting body language and a countdown promise in the first frame, so energy, rule and silhouette are legible muted, and its single-take moving-camera plus on-camera-dialogue pair is not in the recent list (empty) and fits one draft_mini unit with zero cuts. The trade-off against the runner-up (P3 with H4) is that P3 is more intimate and tests close-range identity anchors, but it loses her full-body silhouette and the Tempo Stomp and risks readable bakery text, so P1 is the safer cold introduction."
    }
  },
  "production_format": {
    "shot_architecture": "single_take_moving_camera",
    "audio_mode": "on_camera_dialogue",
    "camera_style": "Handheld phone, wide, slow low-angle push-in from across the road toward her; the camera is the crowd's indifferent witness, settling on a held beat after the Stomp.",
    "continuity_reuse": {
      "voice": "same",
      "location": "same",
      "costume": "same"
    },
    "trend_refs": [],
    "rationale": "Clearest single-take introduction of energy, rule and silhouette; a push-in sells her towering scale, one unit and zero cuts fit draft_mini, and shouted numbers are universal when muted. It is the bible's canonical location so the rule is unambiguous."
  }
}

## Production format to realise (declared by the selected premise; the validator checks it)
{
  "shot_architecture": "single_take_moving_camera",
  "audio_mode": "on_camera_dialogue",
  "camera_style": "Handheld phone, wide, slow low-angle push-in from across the road toward her; the camera is the crowd's indifferent witness, settling on a held beat after the Stomp.",
  "continuity_reuse": {
    "voice": "same",
    "location": "same",
    "costume": "same"
  },
  "trend_refs": [],
  "rationale": "Clearest single-take introduction of energy, rule and silhouette; a push-in sells her towering scale, one unit and zero cuts fit draft_mini, and shouted numbers are universal when muted. It is the bible's canonical location so the rule is unambiguous."
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
