<!-- requested_model: sonnet; effort: medium; tag: qa_review-0 -->

# Stage 4 - Creative QA (subjective; kept separate from deterministic gates)

Your responsibility: review the packet below against the predeclared rubric and report scores with one sentence of evidence each. You are not rewriting it. Deterministic validation has already run; do not re-check timing arithmetic.

## Rubric (weights): originality .15, hook .15, coherence .15, identity .10, audiovisual completeness .15, feasibility .10, grounding .08, commercial fit .12. Anchors: 1 fail, 3 adequate, 5 excellent.

## Packet
{
  "packet": {
    "brief": {
      "brief_id": "B1_silent_gag",
      "title": "Silent 12-second gag: the one-centimetre-short charger cable",
      "project": "bakeoff",
      "bible_ref": "inspector-v1",
      "format": "silent_gag",
      "platform": "instagram_reels",
      "duration_target_s": 12,
      "language": "none (visual; optional 1 caption line)",
      "objective": "Make a stranger send it to the friend whose tiny habits cause group chaos.",
      "constraints": [
        "No dialogue. Ambience and foley only.",
        "Single location: a living-room side table and wall socket.",
        "One cut maximum inside any single generated clip.",
        "Loop-friendly ending (last pose approximates first)."
      ],
      "commercial": null,
      "negative_constraints": [
        "Do not copy any researched creator's look, catchphrase or footage.",
        "No readable brand text in frame."
      ]
    },
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "H1 puts both the one-centimetre gap and the cable tie in frame one, so the muted viewer is already ahead of the Inspector, which is the bible rule in its purest form and sets up the relapse loop. The trade-off against the runner-up (P5/H5) is that the drawer hook is the more instantly sendable to a specific friend, but its payoff lands later and its camera-notices-first beat is weaker, so P1/H1 is the stronger fit for a 12-second silent loop."
    },
    "premises": [
      {
        "id": "P1",
        "logline": "The Inspector measures, tags and condemns a charger cable that falls exactly one centimetre short, while a neat cable tie she wrapped round its middle sits in plain sight the whole time.",
        "audience_emotion": "Fond recognition with a half-second of dread: the viewer spots the tie before she does and waits for her to find it.",
        "character_desire": "To prove the cable is defective so the fault can be filed somewhere other than her.",
        "obstacle": "The cable cannot reach the socket from the side table, and her procedure (tape measure, orange evidence tag) keeps confirming the gap without explaining it.",
        "escalation": "Static eye-level frame. Beat 1: phone held at the cable end, short by a visible sliver. Beat 2: she lays the cable along the table and measures it. Beat 3: she tags it with safety-orange tape and tries again from a crouch. Each failed attempt tugs the cable a little taut, so the tie bunching the middle stays centre frame.",
        "surprise": "She takes the cable end and slowly runs her fingers along it. Her hand stops at the tie, with the spare tie on her lanyard clearly matching it. A beat of warm disappointment. She cuts it, the cable reaches, the phone plugs in with a satisfied click.",
        "payoff": "She is the culprit: her own habit of tidy-wrapping every cable ate the missing centimetre. After the fix she looks at the loose, slightly messy cable, produces a fresh tie from a flap pocket and wraps it tight again. The cable is short again; she steps back into the opening pose. The camera noticed the tie in frame one.",
        "structure": "Single locked-off take. Procedure, then a fair-play reveal that is visible from the first second, then a compulsive relapse that loops back to the opening pose and a short cable.",
        "why_send_it": "A viewer sends it to the friend who 'tidies' everything into a worse state, such as the one who coils the group chat's shared charger so tightly nobody can use it, with the implied message 'this is you, and you do it with love.' The loop invites a second watch to catch the tie that was there at second 0.",
        "commercial_fit": "None. No brand or product is shown; the cable and phone are generic and unbranded.",
        "rejected_because": ""
      },
      {
        "id": "P2",
        "logline": "To spare a nearly dead phone, the Inspector refuses to move the table and holds the plug at full stretch, becoming a rigid, trembling human bridge across the one-centimetre gap.",
        "audience_emotion": "Escalating tension and giggling disbelief at deadpan endurance, ending in a held breath.",
        "character_desire": "To keep the investigation untouched and the evidence in place, even at personal cost.",
        "obstacle": "The cable will not reach, and she will not move any element of the scene because that would contaminate it.",
        "escalation": "She extends her arm fully and plugs in. A tiny tremor starts. Her lamp swings on its strap. Her lanyard clipboard slowly hooks the side-table lamp's cord and drags the lamp toward the table edge, millimetre by millimetre, while her face stays composed.",
        "surprise": "The lamp tips over the edge and she catches it with her free foot without breaking her rigid pose.",
        "payoff": "The Inspector caused the second fault by hooking her own lanyard on the lamp cord. She returns the lamp to the table and stands in the same stretched pose, but the clipboard is already hooking the cord again. Loop.",
        "structure": "Endurance gag. A single sustained physical pose that builds to a near-disaster and a tiny recovery, with a loop by relapse.",
        "why_send_it": "A viewer sends it to the friend who will physically suffer rather than do the obvious, tiny thing, such as the one who stands for an hour holding a phone at an angle instead of moving the table.",
        "commercial_fit": "None.",
        "rejected_because": "The pose is hard for generation models to hold without limb drift, and the cause of the lamp's movement is harder to read at a glance than the other premises."
      },
      {
        "id": "P3",
        "logline": "Shot top-down like a micro-scale investigation, the Inspector's gloved hands measure the short cable while the phone creeps one centimetre further away every time she leans in.",
        "audience_emotion": "Pleasure in a rhythmic, escalating pattern, plus the small thrill of seeing what she cannot.",
        "character_desire": "To get an accurate, uncontested measurement of the shortfall.",
        "obstacle": "The shortfall keeps changing, because the thing she is measuring keeps moving.",
        "escalation": "Three repeating beats: she places the tape, leans in with the clipboard and lamp strap, and the table jolts; the phone slides one centimetre. She re-squares everything, repeats, and the phone slides further each round.",
        "surprise": "On the third round the phone slides off the cable entirely, then the cable slowly slides after it, and her lanyard is revealed as the thing dragging both.",
        "payoff": "Her own measuring technique creates and widens the gap. She nods in satisfaction at the 'confirmed' gap, which is now ten centimetres. Final frame returns the phone to its starting position, ready for beat one again.",
        "structure": "Rhythmic triple-beat Sisyphean cycle, shot as top-down insert detail with only hands and sleeves visible.",
        "why_send_it": "A viewer sends it to the friend whose 'just checking' always makes the situation worse, such as the one who re-checks a shared plan until it falls apart.",
        "commercial_fit": "None.",
        "rejected_because": "Hands-only framing loses the Inspector's face and warm-disappointment expression, which are the core identity anchors."
      },
      {
        "id": "P4",
        "logline": "A silent stealth swap: the Inspector tiptoes to steal a longer cable from a sleeping housemate's phone and leaves her own short one behind, until a blanket-wrapped hand quietly passes the short cable back.",
        "audience_emotion": "Sneaky glee and warmth between two people who never speak.",
        "character_desire": "To fix her charging problem without waking the housemate.",
        "obstacle": "The housemate's sleeping phone charges on the long cable; every foley sound threatens to wake them.",
        "escalation": "Exaggerated foley for each tiptoe, the clipboard clack she muffles with a sleeve, a hand sliding the plug out in slow motion, the housemate's foot twitching in the sofa corner of frame.",
        "surprise": "The swap works, and the housemate's blanketed hand reaches out, takes the cable from her without opening an eye and puts the short one back in her palm.",
        "payoff": "The housemate's phone now sits one centimetre short, and she is the next offender: she holds the short cable again, standing in the original pose.",
        "structure": "Two-hander relay. Her heist is answered by a passed fault, ending in a handoff that loops her back to the start.",
        "why_send_it": "A viewer sends it to the housemate or partner who 'borrows' the good charger and returns a worse one.",
        "commercial_fit": "None.",
        "rejected_because": "It needs a second performer in a sleeping pose and depends on a subtle off-camera handoff that is harder to keep legible in 12 seconds."
      },
      {
        "id": "P5",
        "logline": "Defeated by the short cable, the Inspector opens the side-table drawer for a spare and reveals dozens of identical cables, each a centimetre short and each carrying her own orange evidence tag.",
        "audience_emotion": "Delighted 'oh no, that is my drawer' recognition.",
        "character_desire": "To find one cable that finally works and close the case.",
        "obstacle": "Every cable she tries from the drawer fails in the same way.",
        "escalation": "She pulls cable after cable, tags each with a flick of orange tape and lays it on the table in a perfectly straight row, tapping the clipboard once before the last attempt.",
        "surprise": "The camera reveals the drawer is packed with identical tagged cables, so she has been repeating this investigation for years.",
        "payoff": "She is the culprit: she keeps buying the same wrong length. She tags the newest cable, slides it into the drawer next to the others, closes it with an exaggerated click and returns to the opening pose. Loop.",
        "structure": "Cold-open problem, then a pattern reveal in the drawer and a ritual filing that loops.",
        "why_send_it": "A viewer sends it to the friend with the drawer of useless chargers, with the message 'we need to talk about the drawer.'",
        "commercial_fit": "None. Cables are unbranded and tags carry no readable text.",
        "rejected_because": "Strong and relatable, but the reveal is a static pile-up, so the camera noticing before her is weaker than in P1."
      }
    ],
    "script": {
      "title": "One Centimetre Short",
      "synopsis": "In a single locked-off take, the Inspector measures, tags and condemns a phone charger cable that stops one centimetre short of the wall socket, while a neat white cable tie she wrapped herself sits in plain view mid-cable. She finally runs her fingers along the cable, finds the tie, matches it to the spare on her lanyard, cuts it, and the phone plugs in. Then she compulsively wraps a fresh tie round the loose cable, and the cable is short again as she resumes the opening pose.",
      "beats": [
        {
          "beat": "Frame one: the Inspector holds the plug a visible sliver from the socket with the white cable tie cinched dead centre on the cable; she pushes, the cable goes taut and the tie quivers.",
          "function": "hook"
        },
        {
          "beat": "She lays the cable along the table, measures it with a tape, and reads the number with grave composure; the tie sits centre frame throughout.",
          "function": "setup"
        },
        {
          "beat": "She wraps a strip of safety-orange tape round the cable end as an evidence tag, retries from a crouch, and each failed pull tugs the cable and shakes the tie.",
          "function": "escalation"
        },
        {
          "beat": "She runs two fingers along the cable, stops at the tie, glances at the matching spare on her lanyard, and her face settles into warm disappointment.",
          "function": "turn"
        },
        {
          "beat": "She cuts the tie, the cable reaches, the plug seats with a satisfied click; then she produces a fresh tie from a flap pocket and cinches it tight again.",
          "function": "payoff"
        },
        {
          "beat": "She steps back into the opening pose holding the plug one centimetre short of the socket, tie dead centre. Loop.",
          "function": "button"
        }
      ],
      "dialogue": [],
      "caption_text": "Case closed. (Again.)",
      "cta": "Send it to the friend who ties everything up too tight.",
      "disclosure_line": "AI-generated video; fictional character; no product endorsement."
    },
    "scenes": [
      {
        "scene_id": "S1",
        "start_s": 0,
        "end_s": 3,
        "location": "Living-room side table and wall socket, a modern lived-in living room with a skirting-board socket just above table height.",
        "action": "The Inspector stands square to the side table holding the phone in her left hand and the charger plug in her right, plug raised beside the wall socket with a clear sliver of air between them. A neat white cable tie is cinched round the middle of the cable, dead centre of frame. She pushes the plug toward the socket, the cable goes taut and stops, the plug stays one centimetre short, and the tied bunch in the middle quivers.",
        "performance": "She carries out a formal alignment procedure: eyes locked on the gap, shoulders square, pushing with small precise forward pulses as if testing a load-bearing joint.",
        "microexpression": "Straight dark brows lower a fraction and her mouth tightens one millimetre when the cable stops taut.",
        "dialogue": [],
        "camera": {
          "shot": "medium shot, eye level, slightly too formal and centred",
          "lens": "26mm-equivalent phone main camera",
          "movement": "locked off, no movement",
          "rig": "phone propped on a stack of books on the sofa arm, 2 m from the table"
        },
        "lighting": "Soft key from a window camera-left; warm bounce from the cream wall and wood table fills the shadow side of her face; a soft contact shadow sits under the cable where it touches the table edge and under her jacket flaps.",
        "environment": "A tidy living room with a pale cream wall, a small walnut side table, a single wall socket with a plain white faceplate and no visible text, and soft late-afternoon light.",
        "sound": {
          "ambience": "quiet room tone with faint distant traffic hum and a low fridge buzz from another room",
          "foley": [
            "soft plastic scrape as the plug pushes toward the socket",
            "taut cable creak",
            "tiny rattle of the cable tie"
          ],
          "music": "none",
          "voice": "none"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "phone",
          "charger cable",
          "white cable tie on cable",
          "wall socket",
          "side table",
          "inspection lamp",
          "clipboard",
          "spare cable tie on lanyard"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S2",
        "start_s": 3,
        "end_s": 6,
        "location": "Same living-room side table and wall socket.",
        "action": "She lays the phone down, stretches the cable straight along the table edge beside a pocket tape measure, and reads the number with the lamp on her chest lighting the tape. She notes the reading on the clipboard with a short pen stroke. The white cable tie stays centre frame in the middle of the stretched cable. She then gives the clipboard a slow two-finger tap as her verdict.",
        "performance": "She runs a measuring procedure with total gravity: tape pinned with her thumb, eyes level with the markings, a tiny nod after each reading as if filing a report.",
        "microexpression": "A slow single blink and a barely perceptible lift of one brow at the measurement.",
        "dialogue": [],
        "camera": {
          "shot": "medium close shot, eye level, framing table and her torso",
          "lens": "26mm-equivalent phone main camera",
          "movement": "locked off with one tiny settle-wobble at the start",
          "rig": "same propped phone"
        },
        "lighting": "Window key from camera-left; the chest lamp adds a small bright pool on the tape with a faint orange-warm bounce from the table wood; crisp contact shadow under the cable and tape measure.",
        "environment": "The same room; the wall socket stays visible at the frame edge with the cable end resting a thumb's width short of it; the cream wall glows warm at the edges.",
        "sound": {
          "ambience": "same quiet room tone and fridge buzz",
          "foley": [
            "metallic tape-measure extend and lock click",
            "pen scratch on clipboard",
            "slow double tap on clipboard"
          ],
          "music": "none",
          "voice": "none"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "phone",
          "charger cable",
          "white cable tie on cable",
          "wall socket",
          "side table",
          "inspection lamp",
          "clipboard",
          "tape measure",
          "pen",
          "spare cable tie on lanyard"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S3",
        "start_s": 6,
        "end_s": 9,
        "location": "Same living-room side table and wall socket.",
        "action": "She tears a strip of safety-orange tape and wraps it round the cable end as an evidence tag, then crouches to retry the plug from socket height. The cable pulls taut, the tie shakes, and the plug stays short. She stands, slowly runs two fingers along the cable, and her hand stops at the white tie. Her eyes drop to the matching spare tie on her lanyard, then back to the one on the cable.",
        "performance": "She commits to a methodical re-test, crouching with the plug at arm's length and checking the gap by eye, then follows the cable with her fingertips like a technician tracing a fault.",
        "microexpression": "Eyes widen a hair, then the face softens into warm disappointment as her glasses slide a little lower on her nose.",
        "dialogue": [],
        "camera": {
          "shot": "medium shot, eye level, slightly tighter on hands and cable at the end",
          "lens": "26mm-equivalent phone main camera",
          "movement": "locked off with a slow digital push-in of about 5 percent",
          "rig": "same propped phone"
        },
        "lighting": "Window key from camera-left; the chest lamp throws a small pool onto the cable and tie; warm wood bounce lights her fingers; clear contact shadows from the cable on the table and the tape strip on the cable.",
        "environment": "The same living room; the orange-tagged cable end and white tie are the two colour accents on the pale table; the socket is just visible at the frame edge.",
        "sound": {
          "ambience": "same quiet room tone and fridge buzz",
          "foley": [
            "sharp tape tear",
            "tape press squeak on cable",
            "knee creak and fabric rustle as she crouches",
            "fingertips sliding along the cable",
            "tiny tie click as her hand meets it"
          ],
          "music": "none",
          "voice": "none"
        },
        "captions": "",
        "transition_out": "continuous",
        "props_from_frame_one": [
          "charger cable",
          "white cable tie on cable",
          "wall socket",
          "side table",
          "inspection lamp",
          "clipboard",
          "safety-orange tape",
          "phone",
          "spare cable tie on lanyard"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      },
      {
        "scene_id": "S4",
        "start_s": 9,
        "end_s": 12,
        "location": "Same living-room side table and wall socket.",
        "action": "She snips the white tie with a small pair of scissors from a flap pocket; the cable relaxes, reaches the socket, and the plug seats with a click while the phone lights. She looks at the loose, slightly messy cable, produces a fresh white cable tie from a flap pocket and cinches it tight round the middle again, pulling the plug a centimetre out of the socket. She unplugs, steps back and returns to the opening pose, plug raised beside the socket, one centimetre short, tie dead centre.",
        "performance": "She restores order with absolute focus, squaring the cable into a neat bundle and cinching the tie with a single decisive pull, wholly unaware of what it undoes.",
        "microexpression": "A satisfied exhale through the nose as the tie tightens; neutral composure returns for the final pose.",
        "dialogue": [],
        "camera": {
          "shot": "medium shot, eye level, matching the opening frame",
          "lens": "26mm-equivalent phone main camera",
          "movement": "locked off, settling back to the opening framing",
          "rig": "same propped phone"
        },
        "lighting": "Window key from camera-left; a faint cool-white bounce from the lit phone screen on the table; warm wood bounce on her hands; contact shadow under the re-tied bunch on the table edge.",
        "environment": "The same living room, neat again, with the orange tape tag on the cable end and the socket plate unmarked.",
        "sound": {
          "ambience": "same quiet room tone and fridge buzz",
          "foley": [
            "scissor snip",
            "satisfying plug-in click",
            "soft phone charging chime tone",
            "zip-tie ratchet cinch",
            "plug scrape out of socket"
          ],
          "music": "none",
          "voice": "none"
        },
        "captions": "Case closed. (Again.)",
        "transition_out": "loop",
        "props_from_frame_one": [
          "phone",
          "charger cable",
          "white cable tie on cable",
          "wall socket",
          "side table",
          "inspection lamp",
          "clipboard",
          "small scissors",
          "fresh cable tie",
          "spare cable tie on lanyard"
        ],
        "cuts_inside_clip": 0,
        "generation_unit": "U1"
      }
    ],
    "continuity": {
      "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger.",
      "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun; plain dark trousers and flat shoes.",
      "props": [
        "phone",
        "charger cable",
        "white cable tie on cable",
        "spare cable tie on lanyard",
        "fresh cable tie",
        "wall socket",
        "side table",
        "inspection lamp",
        "clipboard",
        "pen",
        "tape measure",
        "safety-orange tape",
        "small scissors"
      ],
      "notes": "The cable tie is cinched at the cable midpoint in every scene until S4 and must stay centre frame and legible; the gap between plug and socket is one centimetre in S1 and again at the end. The two-finger clipboard tap is used once (S2). Unbranded cable, phone and socket; no readable text or app UI. The last pose matches the first pose for the loop."
    },
    "growth_hypotheses": [
      {
        "hypothesis": "A viewer who spots the cable tie in the first second and waits for the Inspector to find it will rewatch to confirm the loop and send it to a friend who ties everything too tight.",
        "metric": "shares per view and replays per view on Reels",
        "falsifier": "Shares per view fall below the account baseline, or replays per view are no higher than for non-looping clips."
      },
      {
        "hypothesis": "Showing both the one-centimetre gap and the tie in frame one holds viewers past 3 seconds with the sound off.",
        "metric": "3-second hold rate on muted autoplay",
        "falsifier": "3-second hold rate is not above the account median."
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
