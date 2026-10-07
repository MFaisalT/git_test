<!-- requested_model: sonnet; effort: medium; tag: hooks-0 -->

# Stage 2 - Scored hook variants

Your responsibility: for the top two premises, write three hook variants each (six total) and score them. A hook is the first frame plus the first line or action; it must work muted and read in about one second.

## Brief
{
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
    "saved_at": "2026-10-07T23:06:37Z"
  }
}
## Prior stage output
{
  "premises": {
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
    "ranking": [
      "P1",
      "P5",
      "P3",
      "P4",
      "P2"
    ],
    "ranking_rationale": "P1 best satisfies the bible rule: the cause is visible in frame one, the camera notices before she does, and her relapse makes the loop the punchline. P5 is the most shareable, with a clean reveal and a strong send target, but its payoff lands later and is less rewatchable. P3, P4 and P2 are distinct in visual language, relationship and performance mode but each carries a production or legibility risk for a 12-second single-clip silent gag."
  }
}

Mechanisms allowed: curiosity_gap, recognition, visible_problem, status_contradiction, escalating_ritual, callout, other.
Scoring (0-10): legibility in first frame (0-3), specificity of the problem (0-3), promise of the bible's rule/payoff (0-2), send-ability to a specific person (0-2). Report the score and a one-sentence rationale per hook.

No spoken words. first_line_or_action must be an action.



## Output contract (JSON only)
{
  "hook_variants": [ {"id": "H1", "premise_id": "P?", "first_frame": "", "first_line_or_action": "", "mechanism": "", "score": 0, "rationale": ""}, ... 6 items ],
  "selected": {"premise_id": "P?", "hook_id": "H?", "rationale": "why this premise+hook pair, in 2-3 sentences; mention the trade-off against the runner-up"}
}
