# Blind judge prompt (one call per brief; outputs labelled X/Y/Z in a recorded shuffled order)

You are scoring three anonymous episode plans written for the same brief and show bible. You do not know which process produced which. Score each on the rubric below (1-5, anchored), give one sentence of evidence per score, compute the weighted total, and answer the anti-template question. Be strict: 3 means adequate, 5 means you would shoot it as-is.

## Rubric and weights
originality .15 | hook .15 | coherence .15 | identity .10 | audiovisual completeness .15 | feasibility .10 | grounding .08 | commercial_fit .12 (for non-commercial briefs, score commercial_fit on whether a later product category is plausible without forcing it; if the plan does not mention any, give 3).
Anchors: see eval/rubric.md (1 fail / 3 adequate / 5 excellent).

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
  "status": "hypothesis, untested"
 }
}

## Plan X
{
 "premise": {
  "logline": "The Inspector measures, tags and condemns a charger cable that falls exactly one centimetre short, while a neat cable tie she wrapped round its middle sits in plain sight the whole time.",
  "audience_emotion": "Fond recognition with a half-second of dread: the viewer spots the tie before she does and waits for her to find it.",
  "character_desire": "To prove the cable is defective so the fault can be filed somewhere other than her.",
  "obstacle": "The cable cannot reach the socket from the side table, and her procedure (tape measure, orange evidence tag) keeps confirming the gap without explaining it.",
  "escalation": "Static eye-level frame. Beat 1: phone held at the cable end, short by a visible sliver. Beat 2: she lays the cable along the table and measures it. Beat 3: she tags it with safety-orange tape and tries again from a crouch. Each failed attempt tugs the cable a little taut, so the tie bunching the middle stays centre frame.",
  "surprise": "She takes the cable end and slowly runs her fingers along it. Her hand stops at the tie, with the spare tie on her lanyard clearly matching it. A beat of warm disappointment. She cuts it, the cable reaches, the phone plugs in with a satisfied click.",
  "payoff": "She is the culprit: her own habit of tidy-wrapping every cable ate the missing centimetre. After the fix she looks at the loose, slightly messy cable, produces a fresh tie from a flap pocket and wraps it tight again. The cable is short again; she steps back into the opening pose. The camera noticed the tie in frame one.",
  "why_send_it": "A viewer sends it to the friend who 'tidies' everything into a worse state, such as the one who coils the group chat's shared charger so tightly nobody can use it, with the implied message 'this is you, and you do it with love.' The loop invites a second watch to catch the tie that was there at second 0."
 },
 "hook": {
  "first_frame": "Eye-level, locked-off, slightly too formal: the Inspector in aubergine jacket stands square to the side table, phone in one hand, charger plug in the other, held up beside the wall socket with a clearly visible sliver of air between plug and socket. A neat white cable tie is cinched round the middle of the cable, dead centre of frame.",
  "first_line_or_action": "She pushes the plug toward the socket, the cable goes taut and stops, and the plug stays one centimetre short; the tied bunch in the middle of the cable quivers.",
  "mechanism": "visible_problem"
 },
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
 }
}
## Plan Y
{
 "premise": {
  "logline": "The charger plug hovers exactly one centimetre short of the wall socket. The Inspector investigates with total gravity, fixes it by nudging the side table, then her own clipboard lanyard snags the table and pulls it back to the exact same gap.",
  "audience_emotion": "Recognition and pleasure at a tiny, familiar household frustration, followed by the satisfaction of watching the fixer undo her own fix.",
  "character_desire": "To restore order: get the plug into the socket so the phone can charge.",
  "obstacle": "A cable one centimetre too short, tautly holding the plug in mid-air, and a heavy side table.",
  "escalation": "Observe, measure, mark the gap with safety-orange tape, rule it a fault, then physically correct it with a careful 1 cm shove.",
  "surprise": "The fix works and she is pleased, but her clipboard swings on its lanyard, hooks the table's drawer pull, and drags the table back as she steps away, popping the plug out again.",
  "payoff": "The frame ends where it began: cable taut, plug floating 1 cm from the socket, orange tape mark still on the floor. The camera noticed; she did not.",
  "why_send_it": "Everyone has a friend who solves a tiny problem and instantly recreates it with a tiny habit (dragging furniture, leaving a bag strap on something). It is the perfect 'this is you' share, and the loop makes people watch it twice to catch the snag."
 },
 "hook": {
  "first_frame": "Macro on a charger plug hovering exactly 1 cm from a wall socket, cable bar-taut to a phone on a side table, a small orange tape flag on the cable.",
  "first_line_or_action": "A circular inspection lamp beam swings in and locks onto the 1 cm gap; a faint electrical-quiet room hum, one tiny sway of the plug.",
  "mechanism": "The whole problem is visible in the first frame with no explanation; the lamp beam announces the Inspector and creates an open loop (will it reach?)."
 },
 "script": {
  "title": "One Centimetre Short",
  "synopsis": "A plug floats 1 cm from the socket. The Inspector investigates, marks the gap, and nudges the side table to fix it. Phone charges. She turns to leave, her clipboard lanyard hooks the drawer pull and drags the table back. The plug pops out. Same frame as the opening.",
  "beats": [
   {
    "beat": "Macro: plug hovers 1 cm from socket, cable taut, lamp beam arrives and holds on the gap.",
    "function": "hook"
   },
   {
    "beat": "Pull out: Inspector, kneeling, takes a tiny ruler to the gap, nods, sticks a strip of orange tape on the floor at the table foot as a position mark.",
    "function": "setup"
   },
   {
    "beat": "She slowly taps the clipboard with two fingers, writes a single tick, then braces and pushes the table exactly 1 cm to the wall; the plug seats with a heavy click and the phone lights green.",
    "function": "escalation"
   },
   {
    "beat": "She rises, satisfied; the clipboard on its lanyard swings out behind her and hooks the drawer pull.",
    "function": "turn"
   },
   {
    "beat": "As she steps away the table slides back 1 cm, the plug pops out and swings; she leaves frame unaware; the camera holds on the gap.",
    "function": "payoff"
   },
   {
    "beat": "Hold on the floating plug and the orange tape mark, the phone screen dimming; matches frame 0 for a seamless loop.",
    "function": "button"
   }
  ],
  "dialogue": [],
  "caption_text": "1 cm. Case closed.",
  "disclosure_line": ""
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 3,
   "location": "Living room, side table and wall socket (low skirting-board corner)",
   "action": "Macro on a white charger plug hovering 1 cm from a wall socket, cable pulled bar-taut from a phone on a small wooden side table. A small orange tape flag is stuck on the cable. A circular lamp beam sweeps in from the right and locks on the gap. The plug sways once and settles. Camera slow-pulls back to reveal the Inspector kneeling, lamp on her chest strap, looking at the gap over small round glasses.",
   "performance": "The Inspector's goal is to confirm the fault exactly; her tactic is stillness and measured observation. She lowers her head until the lamp beam is level with the gap, holds it, and slowly lifts a tiny ruler into frame. Eye-work: eyes go to the plug, to the socket, back to the plug, never mugging.",
   "microexpression": "Straight dark brows lower a few millimetres in concentration; a slight pursing of the lips; glasses slip a hair down the nose.",
   "dialogue": [],
   "camera": {
    "shot": "Macro on the plug, pulling out to a medium-close two-subject frame, formal and slightly too centred",
    "lens": "Phone main lens, macro-feel start moving to 26mm equivalent",
    "movement": "Slow pull-back (about 20 cm of travel) with a gentle propped-phone settle-wobble at the end",
    "rig": "Propped phone on a floor-level book stack, slight settle on touch"
   },
   "lighting": "Key: warm window light from camera-left at about 45 degrees, soft; fill: low ambient room bounce; colour bounce: aubergine from the jacket onto the white skirting and the pale cable; the inspection lamp adds a hard small circle of cool white on the plug and socket; true contact shadow of the plug on the wall plate and of the table foot on the floor.",
   "environment": "Plain pale-grey living-room wall, white skirting board, wooden side table with one small drawer, grey carpet, a wall socket with a standard flat white plate (no logos), a phone on the table with a blank dark case. Quiet evening.",
   "sound": {
    "ambience": "Quiet living-room room tone, faint fridge hum from the next room",
    "foley": [
     "Soft tick of the cable tensing",
     "Tiny plastic sway of the plug",
     "Click of the inspection lamp switching on",
     "Fabric rustle of the jacket as she lowers"
    ],
    "music": "none",
    "voice": "none"
   },
   "transition_out": "Hard cut to a tighter medium shot (new clip) at the moment she lifts the ruler.",
   "props_from_frame_one": [
    "Charger cable and plug (white, no logos)",
    "Phone on side table (dark case, screen dim)",
    "Wooden side table with small drawer and round pull",
    "Wall socket with plain plate",
    "Orange tape flag on cable",
    "Strip of orange tape roll in jacket pocket",
    "Tiny ruler",
    "Clipboard on lanyard",
    "Chest-strap inspection lamp"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S2",
   "start_s": 3,
   "end_s": 8,
   "location": "Living room, side table and wall socket",
   "action": "Medium shot, eye-level. The Inspector holds the ruler against the gap, nods once, peels a strip of orange tape from her pocket and presses it on the carpet at the table foot as a position mark. She lifts the clipboard, gives the slow two-finger tap (the one signature gesture), makes one deliberate tick. She then sets both hands on the side table edge, braces, and shoves it exactly 1 cm toward the wall. The plug slides home with a heavy click and the phone lights with a soft green glow.",
   "performance": "Goal: close the gap precisely. Obstacle: a heavy table and a taut cable. Tactic: measure, mark, then a single controlled shove. She does it with procedural calm; the pleasure at the click shows only in her shoulders dropping a notch and a small exhale.",
   "microexpression": "Neutral to a faint warm satisfaction at the corner of the mouth as the phone lights; eyes flick to the screen glow and back to the plug.",
   "dialogue": [],
   "camera": {
    "shot": "Medium shot, eye-level, centred and formal with side table and socket in the right third",
    "lens": "26mm equivalent main lens",
    "movement": "Gentle handheld bob with a small push-in toward the plug as it seats",
    "rig": "Handheld phone, light settle-wobble"
   },
   "lighting": "Key: warm window light camera-left, soft; fill: low room bounce; colour bounce: aubergine from the jacket on the pale wall and skirting, safety-orange glint from the tape strip on the carpet; green glow from the phone screen lights her chin and the table top; contact shadow of the table foot sliding on the carpet and a shadow under the plug as it seats.",
   "environment": "Same room and positions as S1. Carpet nap shows a faint trail where the table slides 1 cm.",
   "sound": {
    "ambience": "Quiet room tone, faint fridge hum",
    "foley": [
     "Sharp rip of the tape strip",
     "Two soft taps of fingers on clipboard",
     "Pen tick on paper",
     "Low drag of table feet on carpet",
     "Heavy satisfying plug click"
    ],
    "music": "none",
    "voice": "none"
   },
   "transition_out": "Hard cut to a wide shot (new clip) on the green phone chime moment.",
   "props_from_frame_one": [
    "Charger cable and plug",
    "Phone on side table",
    "Wooden side table with small drawer and round pull",
    "Wall socket with plain plate",
    "Orange tape flag on cable",
    "Orange tape roll in pocket",
    "Tiny ruler",
    "Clipboard on lanyard with pen on a string",
    "Chest-strap inspection lamp"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S3",
   "start_s": 8,
   "end_s": 12,
   "location": "Living room, side table and wall socket",
   "action": "Wide, formal and level. The Inspector straightens, hangs the ruler in a pocket, gives a small satisfied nod, and turns to leave. Her clipboard swings out on its lanyard and hooks the drawer pull. As she steps away, the table drags back 1 cm, the plug pops from the socket and swings on the taut cable, the phone glow dies. She exits frame unaware. Camera holds on the plug floating 1 cm from the socket, orange tape mark now visible on the carpet beside the table foot, matching the opening frame.",
   "performance": "Goal: leave with the job done. She is entirely absorbed in her exit, posture upright and procedural, never glancing back; the camera notices what she does not.",
   "microexpression": "Calm, faintly pleased lips as she turns; no reaction because she never sees it.",
   "dialogue": [],
   "camera": {
    "shot": "Wide, eye-level, symmetrical and too formal for the triviality; ends on a tightening push-in to the plug and socket",
    "lens": "24mm equivalent main lens",
    "movement": "Propped-phone settle-wobble, then a slow push-in on the gap in the last 2 seconds",
    "rig": "Propped phone on the floor-level book stack, same position as S1"
   },
   "lighting": "Key: warm window light camera-left, soft; fill: low room bounce; colour bounce: aubergine jacket on the white skirting as she exits; the phone's green glow cuts out so the table top returns to the neutral warm light; contact shadows sharpen on the plug as it swings and settles.",
   "environment": "Same room, same props. By the end the table is back exactly 1 cm from the wall, as in the opening frame.",
   "sound": {
    "ambience": "Quiet room tone, faint fridge hum",
    "foley": [
     "Soft clipboard knock against the drawer pull",
     "Low drag of table feet on carpet",
     "Plug pop as it unseats",
     "Phone power-down chirp (non-musical, no UI)",
     "Receding footsteps on carpet"
    ],
    "music": "none",
    "voice": "none"
   },
   "transition_out": "Loops directly back to the S1 opening frame (plug hovering 1 cm from socket, cable taut, orange flag on cable).",
   "props_from_frame_one": [
    "Charger cable and plug",
    "Phone on side table",
    "Wooden side table with small drawer and round pull",
    "Wall socket with plain plate",
    "Orange tape flag on cable",
    "Orange tape mark on carpet",
    "Tiny ruler in pocket",
    "Clipboard on lanyard",
    "Chest-strap inspection lamp"
   ],
   "cuts_inside_clip": 0
  }
 ],
 "continuity": {
  "identity_anchors": "Oval face, straight dark brows, small round glasses slightly down the nose, hair in a tight low bun, neutral expression breaking into warm disappointment or faint satisfaction, never mugging.",
  "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun.",
  "props": [
   "White charger cable and plug (no logos)",
   "Phone with a dark blank case",
   "Wooden side table with one small drawer and round pull",
   "Wall socket with plain plate",
   "Orange tape flag on cable",
   "Orange tape roll in jacket pocket",
   "Tiny ruler",
   "Clipboard on lanyard with pen on a string",
   "Chest-strap inspection lamp"
  ],
  "notes": "Silent brief: no dialogue, ambience and foley only. Single location. Zero cuts inside each generated clip; the two cuts between clips are the S1-S2 and S2-S3 boundaries. The signature two-finger clipboard tap is used once, in S2. The lanyard and clipboard are the established causal object: it is on the lanyard from frame one and is the cause of the reset. The last frame (plug floating 1 cm from socket, table back at its start position) approximates the first for a clean loop. No readable brand text or UI in frame; the phone glow is a plain green light, not a screen interface."
 }
}
## Plan Z
{
 "premise": {
  "logline": "A composed inspector investigates a phone charger cable that stops exactly one centimetre short of the socket, fixes it with a solemn table-nudge and a stamp of approval, then commits the identical fault with her own cable.",
  "payoff": "The moment she stamps 'resolved', her own inspector's torch on a cable that is also one centimetre short drags the table back and yanks the phone out. She ends in the same stare-down pose she began with."
 },
 "hook": {
  "first_frame": "Extreme close-up, low angle: a phone dangling off a side-table edge by a fully taut white cable. The plug tip hovers visibly one centimetre from the wall socket, and a ruler-straight shadow runs across the gap.",
  "first_line_or_action": "The cable gives a tiny twang and the phone swings a few degrees, as if the cable is straining toward the socket and failing."
 },
 "script": {
  "title": "One Centimetre Short",
  "synopsis": "The Inspector crouches at a side table where a phone hangs from a taut charger cable that falls a centimetre short of the wall socket. She inspects the gap with grave professionalism: a tiny tape measure, a nod, a clipboard note. She nudges the table a centimetre closer, the plug clicks in, the charging light glows, and she stamps the report with a satisfied thud. She then plugs in her own inspector's torch on its own cable, and that cable is also one centimetre short. The tension drags the table back, the phone's plug pops out, and she is left in the same crouch and stare as the opening frame.",
  "beats": [
   {
    "beat": "Taut cable, plug hovering a centimetre from the socket. Cable twangs. The Inspector's eyes slide into frame, level with the gap.",
    "function": "hook"
   },
   {
    "beat": "She pulls out a tiny tape measure, measures the gap, gives one grave nod, and writes a single line on her clipboard.",
    "function": "setup"
   },
   {
    "beat": "She presses two fingers to the table edge and nudges it exactly one centimetre. The plug slides in and clicks, and a small charging glow lights her face.",
    "function": "escalation"
   },
   {
    "beat": "She stamps the report with a heavy, satisfied thud and holds it up to the lamp, serene.",
    "function": "turn"
   },
   {
    "beat": "She plugs her own inspector's torch into the second socket slot. Its cable is also one centimetre short, taut, and the table slides back and the phone plug pops out.",
    "function": "payoff"
   },
   {
    "beat": "She is back in the opening crouch, eyes level with the gap, unblinking. The cable twangs.",
    "function": "button"
   }
  ],
  "dialogue": [],
  "caption_text": "Inspection pending.",
  "disclosure_line": "AI-generated video."
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 4,
   "location": "Living-room side table and wall socket, evening, one fixed corner.",
   "action": "Phone hangs off the table edge by a taut white cable with its plug hovering one centimetre from the wall socket. The cable twangs. The Inspector slides into frame, crouching, eyes level with the gap. She unrolls a tiny tape measure across the gap, nods once, and writes one line on her clipboard.",
   "performance": "Deadpan gravity, as if inspecting a bridge. Movements are small, deliberate and unhurried. No glances at camera.",
   "microexpression": "A slow single blink and a tightening at the jaw as the tape reads one centimetre. A faint eyebrow lift of professional disappointment.",
   "dialogue": [],
   "camera": {
    "shot": "Low-angle macro close-up widening to a medium close-up of the crouching Inspector",
    "lens": "35mm equivalent with shallow depth of field",
    "movement": "Locked off, with a very slow push-in of about 5 percent"
   },
   "lighting": "Warm tungsten table lamp from camera left, soft cool window spill from the right, a crisp shadow line across the gap.",
   "environment": "Cream wall, plain two-pin wall socket, wooden side table with a lamp, a small ceramic mug and a stack of two books. No readable text or logos anywhere.",
   "sound": {
    "ambience": "Quiet living-room room tone with a faint fridge hum from another room",
    "foley": [
     "Cable twang",
     "Tape measure rasp and snap",
     "Pen scratch on clipboard"
    ],
    "music": "none"
   },
   "transition_out": "Hard cut on the pen's final tick.",
   "props_from_frame_one": [
    "Phone",
    "White charger cable",
    "Wall socket",
    "Side table",
    "Table lamp",
    "Tape measure",
    "Clipboard"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S2",
   "start_s": 4,
   "end_s": 8,
   "location": "Same side table and wall socket, same camera corner.",
   "action": "The Inspector presses two fingers to the table edge and nudges the table exactly one centimetre toward the wall. The plug slides in and clicks, and the phone lights with a soft charging glow. She takes a rubber stamp from her pocket and stamps the clipboard report with a thud, then holds it up to the lamp.",
   "performance": "Quiet triumph held in check. A single measured exhale, shoulders settling, the posture of a job done properly.",
   "microexpression": "The corner of her mouth moves a fraction of a millimetre, a micro-smile, immediately suppressed.",
   "dialogue": [],
   "camera": {
    "shot": "Medium close-up two-shot of the table edge, her hands and the socket",
    "lens": "35mm equivalent",
    "movement": "Locked off, with a tiny rack of focus from the plug to the stamped report"
   },
   "lighting": "Same warm tungsten lamp, now with a small cool-green glow from the phone on her cheek.",
   "environment": "Unchanged, except the table now sits one centimetre closer to the wall and the cable hangs relaxed with a gentle loop.",
   "sound": {
    "ambience": "Quiet room tone with fridge hum",
    "foley": [
     "Table leg scrape on wooden floor",
     "Plug click",
     "Soft phone charge chime",
     "Heavy rubber stamp thud"
    ],
    "music": "none"
   },
   "transition_out": "Hard cut on the stamp thud's tail.",
   "props_from_frame_one": [
    "Phone",
    "White charger cable",
    "Rubber stamp",
    "Clipboard"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S3",
   "start_s": 8,
   "end_s": 12,
   "location": "Same side table and wall socket, same camera corner.",
   "action": "She plugs her own inspector's torch into the second socket slot. Its black cable is also one centimetre short and pulls taut. The table slides a centimetre back, the phone's plug pops out of the socket, and the phone swings. She ends crouched exactly as in the opening frame, eyes level with the gap, unblinking, the cable giving a small twang.",
   "performance": "Total composure that slowly freezes into stillness. She does not react, only stares, treating her own fault as a new case.",
   "microexpression": "Eyes widen a fraction and then narrow into a flat professional stare; one slow blink.",
   "dialogue": [],
   "camera": {
    "shot": "Medium close-up matching the S1 closing frame, easing to the S1 opening macro low angle",
    "lens": "35mm equivalent",
    "movement": "Locked off, with a slow push-in matching the opening push so the last frame approximates the first"
   },
   "lighting": "Same warm tungsten lamp with the phone's glow now gone, matching the opening light.",
   "environment": "Table back at its original distance from the wall, phone dangling off the edge by a taut cable, torch cable also taut. Same objects as the opening frame.",
   "sound": {
    "ambience": "Quiet room tone with fridge hum",
    "foley": [
     "Torch cable snap taut",
     "Table leg scrape backward",
     "Plug pop",
     "Phone dangle swing",
     "Cable twang"
    ],
    "music": "none"
   },
   "transition_out": "Seamless loop: the final pose and twang match the first frame of S1.",
   "props_from_frame_one": [
    "Phone",
    "White charger cable",
    "Black torch cable",
    "Inspector's torch",
    "Wall socket",
    "Side table"
   ],
   "cuts_inside_clip": 0
  }
 ],
 "continuity": {
  "identity_anchors": "The Inspector: a composed woman in her 40s, hair pulled into a tight low bun, round tortoiseshell glasses, a neutral unreadable expression, small precise hands.",
  "costume": "Beige trench-style inspector's coat with a plain unbranded lanyard badge (no readable text), a pen in the breast pocket, slim dark trousers.",
  "props": [
   "Phone",
   "White charger cable",
   "Black torch cable",
   "Inspector's torch",
   "Tape measure",
   "Clipboard",
   "Rubber stamp",
   "Wall socket",
   "Wooden side table",
   "Table lamp"
  ],
  "notes": "No readable brand text, labels or logos on any object. The cable gap is always one centimetre. The table must start and end in its original position so the end pose loops into the first frame. Each clip has zero internal cuts, and only hard cuts join S1 to S2 and S2 to S3. No dialogue anywhere."
 }
}

## Output (JSON only)
{
  "scores": {"X": {"originality": 0, "hook": 0, "coherence": 0, "identity": 0, "audiovisual": 0, "feasibility": 0, "grounding": 0, "commercial_fit": 0, "weighted_total": 0.0},
             "Y": {...}, "Z": {...}},
  "evidence": {"X": {"originality": "", "hook": "", "coherence": "", "identity": "", "audiovisual": "", "feasibility": "", "grounding": "", "commercial_fit": ""}, "Y": {...}, "Z": {...}},
  "thresholds": {"X": {"character_intent": true, "premise_specific_payoff": true, "complete_direction": true, "commercial_fit": true}, "Y": {...}, "Z": {...}},
  "ranking": ["", "", ""],
  "anti_template": {"any_two_share_skeleton": false, "evidence": ""},
  "notes": "two sentences"
}
