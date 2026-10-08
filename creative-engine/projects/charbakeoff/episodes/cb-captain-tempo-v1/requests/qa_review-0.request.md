<!-- requested_model: sonnet; effort: medium; tag: qa_review-0 -->

# Stage 4 - Creative QA (subjective; kept separate from deterministic gates)

Your responsibility: review the packet below against the predeclared rubric and report scores with one sentence of evidence each. You are not rewriting it. Deterministic validation has already run; do not re-check timing arithmetic.

## Rubric (weights): originality .15, hook .15, coherence .15, identity .10, audiovisual completeness .15, feasibility .10, grounding .08, commercial fit .12. Anchors: 1 fail, 3 adequate, 5 excellent.

## Packet
{
  "packet": {
    "brief": {
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
      "rationale": "P1 with H1 shows the full silhouette, public setting, conducting body language and a countdown promise in the first frame, so energy, rule and silhouette are legible muted, and its single-take moving-camera plus on-camera-dialogue pair is not in the recent list (empty) and fits one draft_mini unit with zero cuts. The trade-off against the runner-up (P3 with H4) is that P3 is more intimate and tests close-range identity anchors, but it loses her full-body silhouette and the Tempo Stomp and risks readable bakery text, so P1 is the safer cold introduction."
    },
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
    "script": {
      "title": "Captain Tempo Counts the Crossing",
      "synopsis": "At a busy junction Captain Tempo counts down THREE, TWO, ONE, AND with her whole body; the signal flips on its own timer; she erupts into the Tempo Stomp as if she caused it; a commuter walks through her celebration without a glance and the camera lingers one beat too long.",
      "beats": [
        {
          "beat": "Wide low shot: towering teal-and-gold woman, arms raised like a conductor, red figure glowing; downbeat on THREE",
          "function": "hook"
        },
        {
          "beat": "Conducting arms and bounce build; the countdown is the rule stated aloud",
          "function": "setup"
        },
        {
          "beat": "Whistle blast on TWO, roar of ONE, push-in tightens",
          "function": "escalation"
        },
        {
          "beat": "AND: the signal flips on its own timer; Tempo Stomp",
          "function": "payoff"
        },
        {
          "beat": "Commuter walks through her frozen victory; camera lingers one beat too long",
          "function": "button"
        }
      ],
      "dialogue": [
        {
          "speaker": "Captain Tempo",
          "line": "THREE!",
          "delivery": "hoarse booming downbeat",
          "on_camera": true
        },
        {
          "speaker": "Captain Tempo",
          "line": "TWO!",
          "delivery": "louder, whistle after",
          "on_camera": true
        },
        {
          "speaker": "Captain Tempo",
          "line": "ONE!",
          "delivery": "roaring, breathless",
          "on_camera": true
        },
        {
          "speaker": "Captain Tempo",
          "line": "AND!",
          "delivery": "explosive, held",
          "on_camera": true
        }
      ],
      "caption_text": "She counted. The light changed. Obviously she did that.",
      "cta": "",
      "disclosure_line": "AI-generated character and footage; original character."
    },
    "scenes": [
      {
        "scene_id": "S1",
        "start_s": 0,
        "end_s": 3,
        "location": "Pedestrian crossing at a busy junction, grey city street, kerb on the near side of the road, signal pole behind her",
        "action": "Wide, slightly low across the road: Captain Tempo stands at the kerb towering over a blurred grey stream of pedestrians, both arms raised like a conductor about to cue an orchestra, red standing figure glowing on the signal behind her. Her raised arms slam down on the beat as she bellows THREE and the handheld camera starts its slow push-in.",
        "performance": "Invested task: set the downbeat for the entire crossing; she stares down the blurred crowd, hunting for any sign they are following her tempo, and sharpens her baton arms when they ignore it.",
        "microexpression": "Eyebrows shoot up on the downbeat, then lock into a stern conductor's frown.",
        "dialogue": [
          {
            "speaker": "Captain Tempo",
            "line": "THREE!",
            "delivery": "hoarse booming shout on the downbeat, rhythmic",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "wide, slightly low angle, full body head to trainers",
          "lens": "phone main camera feel, wide (about 24mm equivalent)",
          "movement": "slow handheld push-in begins, gentle bob, camera noticing her before she notices it",
          "rig": "handheld phone, operator walking slowly forward from across the road"
        },
        "lighting": "Overcast daylight key from high camera-left, soft; fill from the open grey sky; warm gold bounce off her tracksuit stripe onto her jaw and forearms and teal bounce onto the pavement beside her; soft contact shadows under her trainers and each pedestrian. Light stays constant, no clouds breaking.",
        "environment": "Busy junction, grey tarmac and kerb, a stream of generic pedestrians as soft blurred shapes with no faces readable, distant traffic out of focus, no readable signs, logos or text.",
        "sound": {
          "ambience": "real junction traffic, footsteps and crowd murmur, idling engines",
          "foley": [
            "metronome tick on the waistband",
            "tracksuit fabric swish as arms drop",
            "trainer scuff on kerb",
            "whistle cord swinging"
          ],
          "music": "none",
          "voice": "Captain Tempo, on camera, hoarse booming count"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "referee whistle on red cord",
          "small handheld metronome clipped to waistband",
          "white sweatband",
          "pedestrian signal head showing red standing figure then green walking figure (pictograms only, no text)",
          "blurred generic pedestrians (extras)"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S2",
        "start_s": 3,
        "end_s": 6,
        "location": "Pedestrian crossing at a busy junction, grey city street, kerb on the near side of the road, signal pole behind her",
        "action": "Push-in continues. Her arms conduct harder, left hand chopping time, right hand circling; legs bounce on the spot. On TWO she clamps the whistle in her teeth and blasts it, then spits it out into a roar of ONE, knees bending, torso leaning toward camera as the lens closes in.",
        "performance": "Invested task: wind the whole street up to a single instant; she drives each number into the crowd with her entire body and checks the red figure over her shoulder with a flick of the eyes between counts.",
        "microexpression": "Eyes widen on the whistle blast, cheeks puff, a quick sideways glance at the signal.",
        "dialogue": [
          {
            "speaker": "Captain Tempo",
            "line": "TWO!",
            "delivery": "louder, whistle blast right after",
            "on_camera": true
          },
          {
            "speaker": "Captain Tempo",
            "line": "ONE!",
            "delivery": "roaring, breathless, almost a bark",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "wide, low angle, tightening to knees-up as the push-in closes",
          "lens": "phone main camera feel, wide (about 24mm equivalent)",
          "movement": "continuing slow low-angle handheld push-in, bob grows slightly with her bounce",
          "rig": "handheld phone, operator walking slowly forward from across the road"
        },
        "lighting": "Overcast daylight key from high camera-left, soft; fill from the open grey sky; warm gold bounce off her tracksuit stripe onto her jaw and forearms and teal bounce onto the pavement beside her; soft contact shadows under her trainers and each pedestrian. Light stays constant, no clouds breaking.",
        "environment": "Busy junction, grey tarmac and kerb, a stream of generic pedestrians as soft blurred shapes with no faces readable, distant traffic out of focus, no readable signs, logos or text.",
        "sound": {
          "ambience": "real junction traffic, footsteps and crowd murmur, idling engines",
          "foley": [
            "sharp referee whistle blast",
            "metronome rattling with her bounce",
            "trainer slaps on pavement",
            "tracksuit swish"
          ],
          "music": "none",
          "voice": "Captain Tempo, on camera, shouts TWO then ONE"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "referee whistle on red cord",
          "small handheld metronome clipped to waistband",
          "white sweatband",
          "pedestrian signal head showing red standing figure then green walking figure (pictograms only, no text)",
          "blurred generic pedestrians (extras)"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S3",
        "start_s": 6,
        "end_s": 9,
        "location": "Pedestrian crossing at a busy junction, grey city street, kerb on the near side of the road, signal pole behind her",
        "action": "On AND she freezes, arms raised, and the signal behind her flips from red standing figure to green walking figure exactly on its own timer. She detonates the Tempo Stomp: two stomps of her white trainers, a hip swing, one whistle blast, both fists thrust to the sky. The blurred crowd begins crossing without looking at her.",
        "performance": "Invested task: claim the change of light as her own work; she holds the instant of the flip with total certainty, then spends every limb on the celebration to sell that she caused it.",
        "microexpression": "Gap-toothed grin explodes wide, eyebrows lifting skyward with the fists.",
        "dialogue": [
          {
            "speaker": "Captain Tempo",
            "line": "AND!",
            "delivery": "one explosive shout, held, joyful",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "wide, low angle, full body, towering silhouette against grey sky",
          "lens": "phone main camera feel, wide (about 24mm equivalent)",
          "movement": "low-angle handheld push-in slows to a settle as she peaks, one small wobble on the stomp impact",
          "rig": "handheld phone, operator walking slowly forward from across the road"
        },
        "lighting": "Overcast daylight key from high camera-left, soft; fill from the open grey sky; warm gold bounce off her tracksuit stripe onto her jaw and forearms and teal bounce onto the pavement beside her; soft contact shadows under her trainers and each pedestrian. Light stays constant, no clouds breaking.",
        "environment": "Busy junction, grey tarmac and kerb, a stream of generic pedestrians as soft blurred shapes with no faces readable, distant traffic out of focus, no readable signs, logos or text.",
        "sound": {
          "ambience": "real junction traffic, footsteps and crowd murmur, idling engines",
          "foley": [
            "two heavy trainer stomps",
            "tracksuit swish on hip swing",
            "whistle blast",
            "metronome clack",
            "green-signal beep tone, generic and unlabelled"
          ],
          "music": "none",
          "voice": "Captain Tempo, on camera, shouts AND"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "referee whistle on red cord",
          "small handheld metronome clipped to waistband",
          "white sweatband",
          "pedestrian signal head showing red standing figure then green walking figure (pictograms only, no text)",
          "blurred generic pedestrians (extras)"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S4",
        "start_s": 9,
        "end_s": 12,
        "location": "Pedestrian crossing at a busy junction, grey city street, kerb on the near side of the road, signal pole behind her",
        "action": "Fists still in the air, Captain Tempo holds her frozen victory pose, beaming, whistle in her teeth. A single blurred commuter in a dark coat walks calmly through the frame between her raised fists and the camera, hair-width from her, never looking over. The camera lingers one beat too long on her unblinking triumphant face, then rests, still held.",
        "performance": "Invested task: soak up the applause nobody is giving; she scans the crowd for acknowledgement, finds none, and refuses to drop the pose.",
        "microexpression": "Proud grin holds, one eyebrow twitches up as the commuter passes, eyes stay locked on camera.",
        "dialogue": [],
        "camera": {
          "shot": "wide settling to medium-wide, low angle, full figure held",
          "lens": "phone main camera feel, wide (about 24mm equivalent)",
          "movement": "camera settles into a final held framing with a small handheld breathe, no cut",
          "rig": "handheld phone, operator walking slowly forward from across the road"
        },
        "lighting": "Overcast daylight key from high camera-left, soft; fill from the open grey sky; warm gold bounce off her tracksuit stripe onto her jaw and forearms and teal bounce onto the pavement beside her; soft contact shadows under her trainers and each pedestrian. Light stays constant, no clouds breaking.",
        "environment": "Busy junction, grey tarmac and kerb, a stream of generic pedestrians as soft blurred shapes with no faces readable, distant traffic out of focus, no readable signs, logos or text.",
        "sound": {
          "ambience": "real junction traffic, footsteps and crowd murmur, idling engines",
          "foley": [
            "commuter footsteps passing",
            "fabric brush of the passing coat",
            "distant traffic",
            "one last metronome tick"
          ],
          "music": "none",
          "voice": "No speech; crowd murmur and traffic only"
        },
        "captions": "",
        "transition_out": "end of clip, hold on frozen pose",
        "props_from_frame_one": [
          "referee whistle on red cord",
          "small handheld metronome clipped to waistband",
          "white sweatband",
          "pedestrian signal head showing red standing figure then green walking figure (pictograms only, no text)",
          "blurred generic pedestrians (extras)"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      }
    ],
    "continuity": {
      "identity_anchors": "Lean weathered face, deep laugh lines, bright wide-set grey eyes, short silver hair cropped close at the sides and spiky on top, very mobile eyebrows, a wide gap-toothed grin.",
      "costume": "Glossy teal and gold tracksuit zipped to the chin, white sweatband, a referee whistle on a red cord, chunky white trainers, a small handheld metronome clipped to the waistband; glossy teal tracksuit trousers with a gold side stripe. Same outfit throughout the episode.",
      "props": [
        "referee whistle on red cord",
        "small handheld metronome clipped to waistband",
        "white sweatband",
        "pedestrian signal head showing red standing figure then green walking figure (pictograms only, no text)",
        "blurred generic pedestrians (extras)"
      ],
      "notes": "Single continuous take, one generation unit U1 of 12 s, zero cuts. Light constant overcast. Signal pictograms only, no text. Strangers are blurred generic extras and never the joke; the passing commuter is a neutral background figure. The Tempo Stomp is original and used once: two stomps, hip swing, whistle blast, both fists to the sky."
    },
    "growth_hypotheses": [
      {
        "hypothesis": "A muted viewer reads the rule (count, event, celebration, indifference) from the silhouette and body language alone and watches to the held end.",
        "metric": "3-second hold rate and average watch percentage",
        "falsifier": "Under 60 percent hold at 3 s or under 50 percent average watch percentage"
      },
      {
        "hypothesis": "The held beat after a commuter ignores the Stomp drives shares to the friend who thinks they control the light.",
        "metric": "shares per 1000 views",
        "falsifier": "Share rate no higher than the comparison bake-off characters"
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
