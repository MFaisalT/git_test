<!-- requested_model: sonnet; effort: medium; tag: qa_review-0 -->

# Stage 4 - Creative QA (subjective; kept separate from deterministic gates)

Your responsibility: review the packet below against the predeclared rubric and report scores with one sentence of evidence each. You are not rewriting it. Deterministic validation has already run; do not re-check timing arithmetic.

## Rubric (weights): originality .15, hook .15, coherence .15, identity .10, audiovisual completeness .15, feasibility .10, grounding .08, commercial fit .12. Anchors: 1 fail, 3 adequate, 5 excellent.

## Packet
{
  "packet": {
    "brief": {
      "brief_id": "CB1_intro_uncle-verdict-v1",
      "title": "Character bake-off intro: 12-second first public appearance of uncle-verdict-v1",
      "project": "charbakeoff",
      "bible_ref": "uncle-verdict-v1",
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
      "rationale": "H1 shows the full silhouette, the dial at 2, the umbrella and the rain edge in the first frame, so the rule and the coming contradiction read muted in about one second, and the on_camera_dialogue / single_take_static pair is not in the recent list. The trade-off against the runner-up (P4 with H4) is that the banana hook has a cleaner single prop but adds a second hand and a more handheld frame that dilutes the seated stillness."
    },
    "premises": [
      {
        "id": "P1",
        "logline": "Outside a corner shop, Uncle Verdict unfolds his chair and scores a closed umbrella 2 out of 10; rain arrives from the top edge, a dry stranger's umbrella drifts past, and he turns the dial down to 1.",
        "audience_emotion": "Delighted exasperation: the viewer sees the rain before he admits it and itches to argue in the comments.",
        "character_desire": "To be the final authority on umbrellas, today.",
        "obstacle": "The rain and the plainly useful umbrella in the background contradict him in frame.",
        "escalation": "Verdict at 2, first drops on the paddle, a generic passer-by's open umbrella slides through the frame edge, dial goes lower to 1.",
        "surprise": "He does not move, shelter or blink; the rain lands on his bald crown and the serenity does not change.",
        "payoff": "He turns the dial with one finger, holds the paddle to the lens, and says: 'Umbrella. Two out of ten. Correct answer: a tiny roof for nobody.' Rain pours, a dry umbrella passes, he lowers the dial to 1: 'Final.'",
        "structure": "Rule-complete single beat: claim, evidence enters, doubling down, hold on the face.",
        "why_send_it": "Sent to the friend who always argues about umbrellas with the message 'this is you'; the wrong take invites a reply.",
        "commercial_fit": "None needed; no brands. Umbrellas are a universal object and suit sponsor-safe categories later.",
        "rejected_because": "",
        "production_format": {
          "shot_architecture": "single_take_static",
          "audio_mode": "on_camera_dialogue",
          "camera_style": "Locked-off phone at seated eye level, centred portrait; rain and the passing umbrella enter from the frame edges.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "The cleanest cold-viewer introduction: static portrait shows silhouette, the verdict format and the rule within one generation unit, with the quiet delivery doing the work."
        }
      },
      {
        "id": "P2",
        "logline": "In a laundrette window seat, Uncle Verdict scores a warm folded towel zero out of ten while a slow push-in reveals the dryer door swinging open and fresh towels spilling over his loafers.",
        "audience_emotion": "Cosy absurdity with a slow-burn laugh at the pile building up.",
        "character_desire": "To rule that towels are a failure.",
        "obstacle": "Warm, clean, plainly excellent towels keep arriving in frame.",
        "escalation": "Towel handed down from the edge, door pops, pile reaches his shoe, the dial already at 0 has nowhere lower so he taps the paddle itself as if the dial were broken.",
        "surprise": "He treats the dial's floor as the world's fault.",
        "payoff": "Voice-over: 'Towel. Zero out of ten. Correct answer: a sad flat blanket.' He turns the dial the wrong way, holds up the paddle, 'Final.'",
        "structure": "Slow reveal; the camera finds the evidence while the voice stays certain.",
        "why_send_it": "Sent to the flatmate who folds towels wrong, with the caption 'rate this'.",
        "commercial_fit": "Laundry categories are generic; no brand text in frame.",
        "rejected_because": "the dial floor makes the rule's wrong-direction step weaker than P1",
        "production_format": {
          "shot_architecture": "single_take_moving_camera",
          "audio_mode": "voiceover_narration",
          "camera_style": "Slow motivated push-in from window height to his face, steam and dryer drum glow as practical light.",
          "continuity_reuse": {
            "voice": "same",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Moves the show to a second recurring location and voice-over so mouth sync is not a risk in a cheap render; the push-in motivates the reveal."
        }
      },
      {
        "id": "P3",
        "logline": "On a park bench row, Uncle Verdict rates a paper cup of tea 10 out of 10 in a main shot; one cutaway insert shows the tea is cold with a leaf floating in it, and he turns the dial up to 10 anyway.",
        "audience_emotion": "Smug disbelief; the insert lets the viewer feel superior to him.",
        "character_desire": "To crown tea the best thing on earth.",
        "obstacle": "The insert shows still, cold, leaf-dotted tea.",
        "escalation": "Verdict 8, cut to insert, back to the main shot with 10.",
        "surprise": "The insert shows what the camera knows and he does not.",
        "payoff": "Text: 'Tea. Eight out of ten. Correct answer: warm water in a hurry.' After the insert he turns the dial up and holds up the paddle: 'Final.'",
        "structure": "Main shot plus insert (the one allowed cut); evidence before the character sees it.",
        "why_send_it": "Sent to the tea-obsessed sibling with 'you in a nutshell'.",
        "commercial_fit": "Tea is a universal object; no brand shown.",
        "rejected_because": "the insert spends the one cut and the caption-only delivery makes the character less warm than a spoken take",
        "production_format": {
          "shot_architecture": "split_or_insert",
          "audio_mode": "text_over_broll",
          "camera_style": "Locked medium main shot plus a single macro insert of the cup.",
          "continuity_reuse": {
            "voice": "none",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Silent text option tests whether the character reads without any voice; the insert proves the evidence-before-him rule visually."
        }
      },
      {
        "id": "P4",
        "logline": "Outside the corner shop, an unseen friend behind the phone asks Uncle Verdict about a banana; he scores it 4 out of 10, a hand from frame edge holds up a perfect one, and he lowers the dial to 2.",
        "audience_emotion": "Warm, conversational comedy; the viewer feels like the third person in the chat.",
        "character_desire": "To be asked, and to answer with authority.",
        "obstacle": "The friend's spotless banana contradicts the score.",
        "escalation": "Question, verdict, banana offered, verdict lowered.",
        "surprise": "The off-camera voice stays kind and never mocks him.",
        "payoff": "Friend: 'And the banana?' Uncle: 'Banana. Four out of ten. Correct answer: a yellow apology.' The banana is perfect; he turns the dial down to 2, holds the paddle to the lens: 'Final.'",
        "structure": "Question-and-answer exchange with a visible object as evidence.",
        "why_send_it": "Sent to a family member who has strong food opinions.",
        "commercial_fit": "Fruit is generic; no brand text.",
        "rejected_because": "off-camera voice dilutes the solo seated stillness and adds a second voice to a 12 s clip",
        "production_format": {
          "shot_architecture": "interview_offcamera",
          "audio_mode": "off_camera_dialogue",
          "camera_style": "Handheld phone at seated eye level, held by the friend, with slight settle; the friend's hand enters from an edge.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Adds a relationship and a second voice to test whether the character holds a two-person beat in one cheap unit."
        }
      },
      {
        "id": "P5",
        "logline": "Silent loop in a laundrette window seat: a leaf blows past, Uncle Verdict dials a verdict on the leaf, and the clip ends on the same empty-chair pose it opened with.",
        "audience_emotion": "Hypnotic calm; the loop invites a second watch.",
        "character_desire": "To rate even a leaf.",
        "obstacle": "The leaf keeps coming back and he keeps reappraising it.",
        "escalation": "Dial moves one notch each pass until the loop closes.",
        "surprise": "The last frame equals the first, so the verdict starts again.",
        "payoff": "He turns the dial, holds the paddle to the lens in silence, and the frame returns to where it began.",
        "structure": "Loop with a repeated beat and no words.",
        "why_send_it": "Sent to a friend as a mood clip.",
        "commercial_fit": "None.",
        "rejected_because": "silence leaves the verdict format and the wrongness illegible to a cold viewer",
        "production_format": {
          "shot_architecture": "loop",
          "audio_mode": "silent_ambience",
          "camera_style": "Locked-off window-seat portrait; first and last frames identical.",
          "continuity_reuse": {
            "voice": "none",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "A silent loop tests the silhouette and the dial click alone, but the rule is hard to land without the spoken verdict."
        }
      }
    ],
    "script": {
      "title": "Umbrella. Final.",
      "synopsis": "Outside a corner shop Uncle Verdict rates a closed umbrella 2 out of 10; rain arrives and a dry stranger's umbrella drifts past; he lowers the dial to 1 and says Final.",
      "beats": [
        {
          "beat": "Mustard-suited man, paddle at 2, closed umbrella, rain edge visible",
          "function": "hook"
        },
        {
          "beat": "Verdict spoken: Umbrella, two out of ten, a tiny roof for nobody",
          "function": "setup"
        },
        {
          "beat": "Rain lands on paddle and bald crown; he stays serene",
          "function": "escalation"
        },
        {
          "beat": "Dry passer-by umbrella slides through the frame edge",
          "function": "turn"
        },
        {
          "beat": "Dial turned down to 1, paddle held to lens, Final.",
          "function": "payoff"
        },
        {
          "beat": "Held calm pose in the rain",
          "function": "button"
        }
      ],
      "dialogue": [
        {
          "speaker": "Uncle Verdict",
          "line": "Umbrella. Two out of ten. Correct answer: a tiny roof for nobody.",
          "delivery": "slow, warm, certain; never raises his voice; short pauses after each sentence",
          "on_camera": true
        },
        {
          "speaker": "Uncle Verdict",
          "line": "Final.",
          "delivery": "one soft, unhurried word, certain",
          "on_camera": true
        }
      ],
      "caption_text": "Umbrella. 2/10. ... Final.",
      "cta": "Argue with him in the comments: what should he rate next?",
      "disclosure_line": "Fictional character; AI-generated video."
    },
    "scenes": [
      {
        "scene_id": "S1",
        "start_s": 0,
        "end_s": 6,
        "location": "outside a corner shop on a pavement (generic, unrecognisable)",
        "action": "Locked portrait. Uncle Verdict sits on the white chair, paddle upright on his thigh with the dial at 2, closed umbrella across his knees, a thin grey rain edge at the top of frame. He lifts the paddle slightly so the 2 reads, and delivers the verdict.",
        "performance": "Invested task: present the verdict like a judge reading a ruling, eyes steady on the lens, finger resting on the dial.",
        "microexpression": "One slow blink on 'ten'; the half-smile does not change.",
        "dialogue": [
          {
            "speaker": "Uncle Verdict",
            "line": "Umbrella. Two out of ten. Correct answer: a tiny roof for nobody.",
            "delivery": "slow, warm, certain; never raises his voice; short pauses after each sentence",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "medium portrait, centred, seated eye level, 9:16",
          "lens": "phone main lens, about 26mm equivalent",
          "movement": "propped phone with one small settle-wobble in the first second, then locked",
          "rig": "phone propped on a low crate at seated eye level"
        },
        "lighting": "Soft overcast key from camera-left top (grey sky); weak fill from the pale shop wall at right; warm mustard bounce from his suit onto the white chair and the paddle; soft contact shadows under chair legs, loafers and the umbrella on his knees. Light stays flat and stable apart from rain darkening.",
        "environment": "Pavement outside a corner shop, grey wall and blank shutter behind, damp-free slabs at start, blurred generic passers-by far background, no readable text or brands.",
        "sound": {
          "ambience": "quiet street ambience, distant traffic, faint wind",
          "foley": [
            "wooden paddle tapping thigh",
            "suit fabric rustle",
            "umbrella canvas shift",
            "exaggerated dial click"
          ],
          "music": "none",
          "voice": "Uncle Verdict, slow warm confident, on camera, matches voice asset"
        },
        "captions": "Umbrella. 2/10.",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "white folding plastic garden chair",
          "large wooden scoring paddle with a 0-10 dial",
          "closed plain umbrella (no logo) across his knees",
          "passer-by's open plain dark umbrella (generic, no logo, passer-by only a blurred edge figure)",
          "rain (top edge, then falling)",
          "grey corner-shop wall with blank unreadable shutter"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S2",
        "start_s": 6,
        "end_s": 9,
        "location": "outside a corner shop on a pavement (generic, unrecognisable)",
        "action": "First drops land on the paddle wood and then on his bald crown. From the right frame edge a generic passer-by's open plain umbrella slides through, dry underneath. He does not move, shelter or blink.",
        "performance": "Invested task: hold his verdict against the weather, eyes fixed on the lens, refusing to glance at the sky.",
        "microexpression": "Drop runs down his forehead; the half-smile and heavy-lidded calm do not change.",
        "dialogue": [],
        "camera": {
          "shot": "medium portrait, centred, seated eye level, 9:16",
          "lens": "phone main lens, about 26mm equivalent",
          "movement": "propped phone, locked, no move",
          "rig": "phone propped on a low crate at seated eye level"
        },
        "lighting": "Soft overcast key from camera-left top (grey sky); weak fill from the pale shop wall at right; warm mustard bounce from his suit onto the white chair and the paddle; soft contact shadows under chair legs, loafers and the umbrella on his knees. Light stays flat and stable apart from rain darkening.",
        "environment": "Pavement outside a corner shop, grey wall and blank shutter behind, damp-free slabs at start, blurred generic passers-by far background, no readable text or brands.",
        "sound": {
          "ambience": "street ambience as light rain begins, patter on pavement",
          "foley": [
            "rain drops on wood",
            "drops on skin",
            "passing umbrella canopy whoosh",
            "soft footstep"
          ],
          "music": "none",
          "voice": "none"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "white folding plastic garden chair",
          "large wooden scoring paddle with a 0-10 dial",
          "closed plain umbrella (no logo) across his knees",
          "passer-by's open plain dark umbrella (generic, no logo, passer-by only a blurred edge figure)",
          "rain (top edge, then falling)",
          "grey corner-shop wall with blank unreadable shutter"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S3",
        "start_s": 9,
        "end_s": 12,
        "location": "outside a corner shop on a pavement (generic, unrecognisable)",
        "action": "He turns the dial with one finger from 2 down to 1 (exaggerated click), holds the paddle up to the lens showing 1, rain pouring, umbrella gone from frame, and says the final word. Holds the pose on the last frame.",
        "performance": "Invested task: correct the dial and present it with total certainty, finger steady, eyes on the lens.",
        "microexpression": "Slow blink after the word; rain on the crown, serenity unchanged.",
        "dialogue": [
          {
            "speaker": "Uncle Verdict",
            "line": "Final.",
            "delivery": "one soft, unhurried word, certain",
            "on_camera": true
          }
        ],
        "camera": {
          "shot": "medium portrait, centred, seated eye level, 9:16",
          "lens": "phone main lens, about 26mm equivalent",
          "movement": "propped phone, locked, paddle comes toward lens; no move",
          "rig": "phone propped on a low crate at seated eye level"
        },
        "lighting": "Soft overcast key from camera-left top (grey sky); weak fill from the pale shop wall at right; warm mustard bounce from his suit onto the white chair and the paddle; soft contact shadows under chair legs, loafers and the umbrella on his knees. Light stays flat and stable apart from rain darkening.",
        "environment": "Pavement outside a corner shop, grey wall and blank shutter behind, damp-free slabs at start, blurred generic passers-by far background, no readable text or brands.",
        "sound": {
          "ambience": "steady rain on pavement, distant traffic",
          "foley": [
            "exaggerated dial click",
            "rain on paddle",
            "suit rustle",
            "umbrella canvas drip"
          ],
          "music": "none",
          "voice": "Uncle Verdict, soft and certain"
        },
        "captions": "Final.",
        "transition_out": "end hold on the final frame",
        "props_from_frame_one": [
          "white folding plastic garden chair",
          "large wooden scoring paddle with a 0-10 dial",
          "closed plain umbrella (no logo) across his knees",
          "passer-by's open plain dark umbrella (generic, no logo, passer-by only a blurred edge figure)",
          "rain (top edge, then falling)",
          "grey corner-shop wall with blank unreadable shutter"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      }
    ],
    "continuity": {
      "identity_anchors": "Round soft face, heavy-lidded calm eyes, neat salt-and-pepper beard trimmed short, bald shining crown with a ring of grey hair, slow blink, serene half-smile that never changes.",
      "costume": "Mustard-yellow three-piece suit slightly too big, open collar, brown leather loafers with no socks, mustard trousers slightly too long; same costume all episode, no changes.",
      "props": [
        "white folding plastic garden chair",
        "large wooden scoring paddle with a 0-10 dial",
        "closed plain umbrella (no logo) across his knees",
        "passer-by's open plain dark umbrella (generic, no logo, passer-by only a blurred edge figure)",
        "rain (top edge, then falling)",
        "grey corner-shop wall with blank unreadable shutter"
      ],
      "notes": "Single continuous take, one generation unit U1, no cuts. Dial reads 2 until S3, then 1. Rain starts at the top edge in S1 and builds. Opinions are about objects only; the passer-by is a blurred generic extra, never the joke. Silhouette: mustard three-piece, white folding plastic chair, wooden paddle with 0-10 dial, brown loafers no socks."
    },
    "growth_hypotheses": [
      {
        "hypothesis": "A confident wrong take on a universal object makes viewers argue and share to a friend",
        "metric": "comments per 1k views and shares",
        "falsifier": "Comment rate below baseline with no arguments about umbrellas"
      },
      {
        "hypothesis": "The mustard silhouette reads muted within one second",
        "metric": "3-second hold rate on muted autoplay",
        "falsifier": "3-second hold below the account baseline"
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
