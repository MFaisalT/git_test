# Blind judge prompt (one call per brief; outputs labelled X/Y/Z in a recorded shuffled order)

You are scoring three anonymous episode plans written for the same brief and show bible. You do not know which process produced which. Score each on the rubric below (1-5, anchored), give one sentence of evidence per score, compute the weighted total, and answer the anti-template question. Be strict: 3 means adequate, 5 means you would shoot it as-is.

## Rubric and weights
originality .15 | hook .15 | coherence .15 | identity .10 | audiovisual completeness .15 | feasibility .10 | grounding .08 | commercial_fit .12 (for non-commercial briefs, score commercial_fit on whether a later product category is plausible without forcing it; if the plan does not mention any, give 3).
Anchors: see eval/rubric.md (1 fail / 3 adequate / 5 excellent).

## Brief
{
 "brief_id": "B3_commercial",
 "title": "15-second sponsored episode: a cable-management box (fictional advertiser) must be the comic mechanism",
 "project": "bakeoff",
 "bible_ref": "inspector-v1",
 "format": "sponsored_episode",
 "platform": "instagram_reels",
 "duration_target_s": 15,
 "language": "English, max 25 spoken words",
 "objective": "Entertain first; the product resolves the story problem without the character claiming personal experience.",
 "constraints": [
  "Product: a plain cable-organiser box (generic design, no brand text in frame).",
  "Paid-partnership disclosure must appear in the plan (platform tool + spoken or caption line).",
  "The fictional character must not claim to have used, tested or benefited from the product.",
  "Advertiser facts available: 'holds up to six cables', nothing else \u2014 do not invent features."
 ],
 "commercial": {
  "advertiser": "fictional-cable-box-co",
  "verified_facts": [
   "holds up to six cables"
  ],
  "forbidden_claims": [
   "durability",
   "price",
   "awards",
   "any user result"
  ]
 },
 "negative_constraints": [
  "No testimonial language.",
  "No readable brand marks."
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
  "logline": "The Inspector rounds up six suspect cables behind a side table into a six-cable box, then the lid will not close on a seventh: the charging lead of her own inspection lamp.",
  "audience_emotion": "Smug anticipation turning into delighted 'of course it's her'.",
  "character_desire": "To close the Cable Incident cleanly with every offending cable contained.",
  "obstacle": "The lid will not close; one cable too many remains, and she cannot find its source.",
  "escalation": "She tags each of six cables with safety-orange tape and counts them in; the lid still rises a centimetre, so she recounts and traces the extra lead with her lamp beam.",
  "surprise": "The camera drifts down her jacket and follows the lead to her own chest lamp and the wall socket; she is tethered to the scene.",
  "payoff": "The box holds the six and her own lead is the seventh offender; she names herself, unplugs her lamp and the lid closes.",
  "why_send_it": "A clean, silent-readable gag: product limit (holds up to six) is the only fact used and it directly causes the reveal. The rule is honoured and no one claims to have used the box."
 },
 "hook": {
  "first_frame": "Tight low-angle on six tangled cables behind a living room side table, an empty open grey cable box beside them, a bright circular lamp beam cutting across the knot.",
  "first_line_or_action": "'Cable incident. Six suspects.' while a strip of safety-orange tape is torn off with an exaggerated rip.",
  "mechanism": "Specific noun first (cable), a clear count to track (six), tactile tape sound; readable muted from the knot, beam and open box."
 },
 "script": {
  "title": "Seventh Offender",
  "synopsis": "The Inspector tags six suspect cables and sorts them into a cable box that holds up to six. The lid will not close. A seventh lead runs down from her own chest lamp to the wall. She names the culprit: herself.",
  "beats": [
   {
    "beat": "Lamp beam finds a knot of six cables; tape rips; she declares an incident and six suspects.",
    "function": "hook"
   },
   {
    "beat": "She tags each cable with orange tape and counts them into the open box.",
    "function": "setup"
   },
   {
    "beat": "Six cables are in, contained; she presses the lid but it lifts a centimetre.",
    "function": "escalation"
   },
   {
    "beat": "She hunts the extra lead with her beam; the camera drifts down her jacket to her own lamp lead plugged into the wall.",
    "function": "turn"
   },
   {
    "beat": "She unplugs her lamp and the lid clicks shut; she taps her clipboard and names the offender.",
    "function": "payoff"
   },
   {
    "beat": "A deadpan disclosure after the verdict.",
    "function": "button"
   }
  ],
  "dialogue": [
   {
    "speaker": "Inspector",
    "line": "Cable incident. Six suspects.",
    "delivery": "Flat, procedural, no rise at the end.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "One. Two. Three. Four. Five. Six.",
    "delivery": "Evenly spaced, one word per cable placed in the box.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Six contained. One extra. Source unknown.",
    "delivery": "Level, a half-beat of puzzlement in the last two words.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Source identified.",
    "delivery": "Quiet, warm disappointment after the gesture.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Paid partnership.",
    "delivery": "Dry clerical aside, like reading a form field.",
    "on_camera": true
   }
  ],
  "caption_text": "Cable incident, closed. The box holds up to six cables. Paid partnership with fictional-cable-box-co. #ad",
  "disclosure_line": "Platform paid-partnership label enabled on the post; spoken line 'Paid partnership.' in S5; caption states 'Paid partnership with fictional-cable-box-co. #ad'."
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 3,
   "location": "living room side table",
   "action": "Lamp beam sweeps over a knot of six cables behind the side table, next to an open empty grey box. The Inspector steps into frame lower third, clipboard up, and rips a strip of safety-orange tape off a roll.",
   "performance": "Goal: open the case. Obstacle: the knot. Tactic: officially label it. She reads the knot with level eyes and tears tape without looking at it.",
   "microexpression": "Straight brows, neutral mouth, round glasses slightly down the nose; a tiny narrowing of the eyes at the knot.",
   "dialogue": [
    "Cable incident. Six suspects."
   ],
   "camera": {
    "shot": "Low close on knot, rising to medium on the Inspector",
    "lens": "35mm equivalent phone main lens",
    "movement": "Propped phone with a settle-wobble, a slow lift as she enters",
    "rig": "Phone propped on the side table edge"
   },
   "lighting": "Key: bright circular chest lamp, hard from camera-right-low; fill: soft window light camera-left; colour bounce: aubergine jacket on her face and warm beige wall; true contact shadows from cables on the table surface.",
   "environment": "Tidy modern living room, pale wall socket behind the table, small wall-mounted power strip, no readable text.",
   "sound": {
    "ambience": "quiet room tone, faint fridge hum from the next room",
    "foley": [
     "tape strip ripping loudly",
     "clipboard strap swing",
     "chest lamp soft click",
     "cable rustle as beam touches knot"
    ],
    "music": "none",
    "voice": "Inspector, measured, short declaratives"
   },
   "transition_out": "Continuous: she crouches toward the knot.",
   "props_from_frame_one": [
    "six cables (white, black, grey, flat white, braided black, thin white)",
    "open empty grey cable-organiser box with lid, no text",
    "orange tape roll",
    "clipboard on lanyard",
    "chest lamp with thin orange lead tucked under jacket hem",
    "side table",
    "wall socket and power strip"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S2",
   "start_s": 3,
   "end_s": 7,
   "location": "living room side table",
   "action": "She tags each cable with a small orange tape flag and lays it into the box one at a time, counting; the knot loosens as the count rises.",
   "performance": "Goal: log every suspect. Obstacle: cables slide back toward the knot. Tactic: tag, lift, place, move to the next.",
   "microexpression": "Eyes track each cable from the knot to the box; brief satisfaction around the fourth.",
   "dialogue": [
    "One. Two. Three. Four. Five. Six."
   ],
   "camera": {
    "shot": "Medium close over the box, looking down at an angle",
    "lens": "35mm equivalent",
    "movement": "Slight handheld bob following her hands",
    "rig": "Propped phone with settle-wobble, slow push-in"
   },
   "lighting": "Key: chest lamp from above-front; fill: window left; aubergine jacket bounce on her wrist; clear contact shadows under each cable and the box.",
   "environment": "Same table; box in the lower right; cable ends lead up to the power strip.",
   "sound": {
    "ambience": "room tone",
    "foley": [
     "tape flag press",
     "cable slide on wood",
     "dull plastic thunk as each cable goes into the box",
     "clipboard tap on lanyard"
    ],
    "music": "none",
    "voice": "Inspector counts, one word per placement, under 2.8 words per second"
   },
   "transition_out": "Continuous: she stands, lamp beam tilting up.",
   "props_from_frame_one": [
    "six cables",
    "open grey box",
    "orange tape roll",
    "clipboard",
    "chest lamp with lead",
    "side table",
    "power strip"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S3",
   "start_s": 7,
   "end_s": 10,
   "location": "living room side table",
   "action": "She presses the lid down over six cables; it rises a centimetre. She presses again, same result.",
   "performance": "Goal: close the case. Obstacle: the lid rises. Tactic: pressing with two flat fingers, more slowly each time.",
   "microexpression": "Brows draw together a millimetre; glasses slip a little lower.",
   "dialogue": [
    "Six contained. One extra. Source unknown."
   ],
   "camera": {
    "shot": "Medium, eye-level, formal",
    "lens": "35mm equivalent",
    "movement": "Settle-wobble, then a slow downward drift toward the base of her jacket",
    "rig": "Propped phone, no cut"
   },
   "lighting": "Key: chest lamp front; window fill; aubergine bounce on the box lid; contact shadow of the lid gap visible.",
   "environment": "Unchanged table; box now holds six cables and the knot is gone.",
   "sound": {
    "ambience": "room tone",
    "foley": [
     "lid press",
     "plastic lid creak as it lifts",
     "finger tap on lid",
     "lanyard swing"
    ],
    "music": "none",
    "voice": "Inspector, level, a half-beat pause before 'Source unknown'"
   },
   "transition_out": "Continuous: she bends to trace the extra cable with her beam.",
   "props_from_frame_one": [
    "six cables now in box",
    "grey box with lid",
    "orange tape roll",
    "clipboard",
    "chest lamp with lead",
    "side table",
    "power strip"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S4",
   "start_s": 10,
   "end_s": 13,
   "location": "living room side table",
   "action": "She sweeps her beam along the floor to find the extra lead; the camera drifts down her jacket, revealing the orange lead running from her own chest lamp, down her hem to the wall socket. She keeps tracing, unaware, then freezes.",
   "performance": "Goal: find the seventh cable. Obstacle: it keeps leading back to her. Tactic: follow the beam along the lead. The camera notices first; she notices last.",
   "microexpression": "Eyes follow the beam down, stop at her own jacket; brows lower in slow dawning; no mugging.",
   "dialogue": [],
   "camera": {
    "shot": "Medium to waist-height tilt-down",
    "lens": "35mm equivalent",
    "movement": "Slow tilt-down with handheld bob",
    "rig": "Phone propped then drifting on a gentle wobble"
   },
   "lighting": "Key: chest lamp raking across the lead; window fill; aubergine bounce and warm beige floor bounce; orange lead shows contact shadow on the floorboards.",
   "environment": "Floor and wall socket visible; her lamp lead is plugged into the same power strip.",
   "sound": {
    "ambience": "room tone",
    "foley": [
     "slow footsteps",
     "lead drag on floorboards",
     "plug tick in the socket",
     "clipboard swing"
    ],
    "music": "none",
    "voice": "none; silent beat"
   },
   "transition_out": "Continuous: she lifts her gaze and taps her clipboard.",
   "props_from_frame_one": [
    "six cables in box",
    "grey box",
    "orange tape roll",
    "clipboard",
    "chest lamp with orange lead plugged into power strip",
    "side table",
    "power strip"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S5",
   "start_s": 13,
   "end_s": 15,
   "location": "living room side table",
   "action": "She performs the signature slow two-finger tap on the clipboard, pulls the plug from her own lamp and the lid clicks shut.",
   "performance": "Goal: issue a verdict. Obstacle: she is the offender. Tactic: procedure. One slow tap, then she unplugs. The tap is the signature gesture, used only here.",
   "microexpression": "Warm disappointment: eyes soften, small downward corner of the mouth, no anger.",
   "dialogue": [
    "Source identified.",
    "Paid partnership."
   ],
   "camera": {
    "shot": "Medium, eye-level, formal",
    "lens": "35mm equivalent",
    "movement": "Settle-wobble to rest",
    "rig": "Propped phone"
   },
   "lighting": "Key: chest lamp front; window fill; aubergine bounce; the plug leaves a soft shadow on the wall.",
   "environment": "Closed box on the table, tidy; the Inspector standing, plug in her hand.",
   "sound": {
    "ambience": "room tone",
    "foley": [
     "slow two-finger clipboard tap",
     "plug pulled from socket",
     "lid click",
     "chest lamp dims with soft click"
    ],
    "music": "none",
    "voice": "Inspector, quiet, first line then a beat, then the disclosure line as a dry aside"
   },
   "transition_out": "End of clip; hold on a closed box and the Inspector's neutral face for the final beat.",
   "props_from_frame_one": [
    "grey box (now closed)",
    "orange tape roll",
    "clipboard",
    "chest lamp with lead",
    "side table",
    "power strip"
   ],
   "cuts_inside_clip": 0
  }
 ],
 "continuity": {
  "identity_anchors": "Oval face, straight dark brows, small round glasses slightly down the nose, hair in a tight low bun, neutral expression that breaks into warm disappointment.",
  "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard.",
  "props": [
   "six cables (distinct colours, no brand text)",
   "generic grey cable-organiser box with lid, no text",
   "orange tape roll and tape flags",
   "clipboard on lanyard",
   "chest lamp with thin orange lead",
   "side table",
   "wall socket and power strip"
  ],
  "notes": "One generated 15 s clip, zero hard cuts. Product facts used: holds up to six cables only. The Inspector never claims to have used or benefited from the product; she only sorts cables she is investigating, and her own lead is the culprit. No durability, price, award or result claims. The box shows no readable marks. Disclosure: platform paid-partnership tool on, spoken line in S5, caption line with #ad. Spoken word count: 4 + 6 + 6 + 2 + 2 = 20, under the 25 cap. Captions added in post. Signature gesture used once, in S5."
 }
}
## Plan Y
{
 "premise": {
  "logline": "The Inspector investigates a knot of six cables behind a TV console as a structural failure, files them in a plain box that holds up to six, then is hobbled by her own seventh cable.",
  "payoff": "The box visibly takes exactly six cables and the room goes calm. The Inspector's own seventh cable, trailing from her coat pocket, wraps her ankle and brings her down, so she commits the very fault she just condemned. The box's stated capacity is the joke's hinge, not a result claim."
 },
 "hook": {
  "first_frame": "Extreme close-up of a dense black knot of six cables behind a TV console, a torch beam sweeping across it, a gloved finger pointing at the centre of the knot.",
  "first_line_or_action": "Inspector, deadpan, torch on the knot: \"Six cables. One knot. Structural failure.\""
 },
 "script": {
  "title": "Capacity Finding",
  "synopsis": "The Inspector condemns a cable knot as a structural failure, sorts the six cables into a plain organiser box, and reads out its capacity. As she turns away satisfied, a seventh cable from her own coat pocket snags her ankle and ties her up.",
  "beats": [
   {
    "beat": "Torch beam finds the six-cable knot behind the console. She declares it a structural failure.",
    "function": "hook"
   },
   {
    "beat": "She kneels, clipboard on knee, and begins untangling with ceremonial precision. The knot resists.",
    "function": "setup"
   },
   {
    "beat": "She lifts the plain organiser box onto the floor and feeds the cables in one at a time. Six clean drops, six clean ticks on the clipboard.",
    "function": "escalation"
   },
   {
    "beat": "Lid closes. The floor is clear. She reads out the capacity as an official finding.",
    "function": "turn"
   },
   {
    "beat": "She stands and turns to leave. A seventh cable, her own torch charger trailing from her coat pocket, has looped around her ankle.",
    "function": "payoff"
   },
   {
    "beat": "She topples in slow, composed stillness, still holding the clipboard upright. One flat word from the floor.",
    "function": "button"
   },
   {
    "beat": "Held end card: the caption and platform partnership label stay on screen. No product claims beyond capacity.",
    "function": "cta"
   }
  ],
  "dialogue": [
   {
    "speaker": "Inspector",
    "line": "Six cables. One knot. Structural failure.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Finding: holds up to six cables.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Seventh. Noted.",
    "on_camera": true
   }
  ],
  "caption_text": "Some faults are structural. Some are personal. The box holds up to six cables. #ad #paidpartnership",
  "disclosure_line": "Paid partnership with fictional-cable-box-co. Enable Instagram's 'Paid partnership' label (branded content tool) before posting; also shown as the first line of the caption: 'Paid partnership with fictional-cable-box-co.'"
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 5,
   "location": "Living room, behind a low TV console, floor level",
   "action": "Torch beam sweeps over a dense knot of six black and white cables. The Inspector, crouched, points at the knot's centre and delivers her verdict. She sets the clipboard on her knee and starts to pry at the knot.",
   "performance": "Utterly composed, clipped delivery, treats the knot as a collapsed bridge.",
   "microexpression": "Single slow blink, jaw set, brow lowered a millimetre in grim confirmation.",
   "dialogue": [
    "Six cables. One knot. Structural failure."
   ],
   "camera": {
    "shot": "Extreme close-up pushing to medium close-up",
    "lens": "50mm macro-leaning",
    "movement": "Slow push-in following the torch beam"
   },
   "lighting": "Dark behind-furniture gloom with a hard white torch beam as key and a soft warm window spill from camera right",
   "environment": "Dusty floor, skirting board, a wall socket, TV console legs; no readable text or logos on any device",
   "sound": {
    "ambience": "Quiet room tone, faint fridge hum",
    "foley": [
     "torch click",
     "cable rustle",
     "clipboard tap"
    ],
    "music": "none"
   },
   "transition_out": "Hard cut on the first cable lifting free",
   "props_from_frame_one": [
    "tangled six-cable knot",
    "torch",
    "clipboard",
    "plain unbranded cable-organiser box just out of focus beside her knee",
    "her own torch charger cable looped unnoticed in coat pocket"
   ],
   "cuts_inside_clip": 1
  },
  {
   "scene_id": "S2",
   "start_s": 5,
   "end_s": 10,
   "location": "Same floor area, wider angle with the box centre frame",
   "action": "She lifts the plain organiser box into the light and feeds the cables in one by one, ticking the clipboard each time. Six drops, six ticks. The knot is gone. She closes the lid and taps it once.",
   "performance": "Ritual precision, the pace of a ceremony, no flicker of warmth.",
   "microexpression": "Tiny chin-lift of professional satisfaction when the sixth cable drops.",
   "dialogue": [
    "Finding: holds up to six cables."
   ],
   "camera": {
    "shot": "Medium shot, then insert on the box and lid",
    "lens": "35mm",
    "movement": "Locked off, quick insert cut on the lid closing"
   },
   "lighting": "Torch now set down as a practical, even warm room light, soft contrast",
   "environment": "Cleared floor, box in centre with no brand text or marks, TV glow off to one side showing blank screen",
   "sound": {
    "ambience": "Room tone, slightly warmer",
    "foley": [
     "six soft cable thuds",
     "pen ticks",
     "lid click",
     "knuckle tap on box"
    ],
    "music": "none"
   },
   "transition_out": "Cut on her rising to standing",
   "props_from_frame_one": [
    "plain organiser box with lid",
    "six cables",
    "clipboard",
    "pen"
   ],
   "cuts_inside_clip": 2
  },
  {
   "scene_id": "S3",
   "start_s": 10,
   "end_s": 15,
   "location": "Same room, wide of the cleared floor",
   "action": "She stands, turns to leave with the clipboard held high. A seventh cable from her coat pocket has looped around her ankle. She tips over slowly and stiffly onto the floor, clipboard still upright. From the floor she says her last line. The box sits tidy beside her. Hold on the end card with caption and partnership label.",
   "performance": "Stoic collapse, no panic, a flat bureaucratic acceptance of her own fault.",
   "microexpression": "Eyes drop to her ankle, one eyebrow rises a hair, mouth flat.",
   "dialogue": [
    "Seventh. Noted."
   ],
   "camera": {
    "shot": "Wide, low angle, then slight tilt down to her on the floor",
    "lens": "24mm",
    "movement": "Static, then a slow 5-degree tilt down"
   },
   "lighting": "Same warm soft room light, with the torch beam rolling across the floor from where it was dropped",
   "environment": "Clean floor with the closed unbranded box beside her, TV console above, window light",
   "sound": {
    "ambience": "Quiet room tone",
    "foley": [
     "cable snag zip",
     "slow thump of body on rug",
     "clipboard clack"
    ],
    "music": "none"
   },
   "transition_out": "Hold, then end card fade-out",
   "props_from_frame_one": [
    "seventh cable (her torch charger) trailing from coat pocket",
    "clipboard",
    "closed organiser box"
   ],
   "cuts_inside_clip": 1
  }
 ],
 "continuity": {
  "identity_anchors": "The Inspector: composed woman with a severe, neat bob, level gaze, buttoned trench-style coat with a visible deep right pocket, flat sensible shoes. She is never named on screen and never speaks in the first person.",
  "costume": "Dark buttoned coat, plain shirt, thin pale gloves (removed after S1), lanyard with a blank unreadable badge.",
  "props": [
   "clipboard and pen",
   "torch",
   "six cables",
   "plain generic cable-organiser box with lid, no text or logos",
   "seventh cable (her torch charger) in her right coat pocket from the first frame"
  ],
  "notes": "The seventh cable must be visible in her pocket from S1 so the S3 payoff is planted. She never claims to have used, tested or benefited from the box; her only product-related line is a capacity finding, matching the verified fact 'holds up to six cables'. No durability, price, award or user-result claims anywhere. No testimonial language. No readable brand marks on the box, devices or cables. Paid-partnership disclosure is delivered through the platform label plus the caption's first line. Spoken total: 8 + 5 + 2 = 15 words, within the 25-word limit."
 }
}
## Plan Z
{
 "premise": {
  "logline": "In the hallway, the Inspector lays out a six-cable tangle as a police line-up and boxes the suspects in a plain organiser; the count comes out at seven, and the seventh cable runs straight into her own chest lamp.",
  "audience_emotion": "Dry, escalating anticipation, then the pleasure of seeing it coming a beat before she does.",
  "character_desire": "To close the Cable Incident cleanly with every suspect accounted for and filed.",
  "obstacle": "Her tally never reconciles: the box takes up to six and a seventh cable will not go in, however formally she re-counts.",
  "escalation": "Orange tape cordons the floor. Each cable is read its 'rights' and dropped in with a clipboard tick. Cable six lands. The seventh will not go in and she re-counts with more ceremony each time, while the lamp strap tugs at her chest.",
  "surprise": "The unaccounted seventh cable is her own lamp's charging lead, plugged into the wall socket behind her. She has been dragging the tangle across the hallway every time she steps back.",
  "payoff": "Camera pulls wide on the lead taut from her chest to the wall. Two-finger clipboard tap (the one allowed per episode). 'Six fit. One is mine.' She unplugs herself; the box closes with six inside. Bible rule delivered: the Inspector is the culprit and the camera saw it first.",
  "why_send_it": "Send it to the flatmate who 'organises' the hallway and still trips on their own charger: it is the tidy-person-is-the-mess joke in 15 seconds."
 },
 "hook": {
  "first_frame": "Wide locked-off hallway shot, Inspector centre with clipboard, orange tape cordoning a pile of tangled cables; a thin cable is faintly visible running from her chest strap behind her toward the wall socket, unremarked.",
  "first_line_or_action": "She taps nothing yet, raises the clipboard and states: 'Cable Incident. Six suspects. The box holds six.'",
  "mechanism": "status_contradiction"
 },
 "script": {
  "title": "Cable Incident",
  "synopsis": "In her hallway the Inspector boxes six cables in an organiser that holds six; the count reads seven, and the seventh is her own lamp lead plugged into the wall behind her.",
  "beats": [
   {
    "beat": "Formal cordon and 'the box holds six'; faint lead visible behind her",
    "function": "hook"
   },
   {
    "beat": "Six cables boxed, one left on the floor",
    "function": "setup"
   },
   {
    "beat": "Recount with more ceremony, strap tugs",
    "function": "escalation"
   },
   {
    "beat": "Wide pull-back reveals taut lead to the wall",
    "function": "turn"
   },
   {
    "beat": "'Six fit. One is mine.' She unplugs herself",
    "function": "payoff"
   },
   {
    "beat": "Lid clicks shut on six; disclosure card",
    "function": "button"
   }
  ],
  "dialogue": [
   {
    "speaker": "Inspector",
    "line": "Cable Incident. Six suspects. The box holds six.",
    "delivery": "flat, measured",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Count: seven.",
    "delivery": "quiet, level",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Recount. Seven.",
    "delivery": "slower, formal",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Six fit. One is mine.",
    "delivery": "dry, deadpan",
    "on_camera": true
   }
  ],
  "caption_text": "Paid partnership with fictional-cable-box-co. The Inspector is a fictional character and has not used this product.",
  "cta": "",
  "disclosure_line": "Paid partnership with fictional-cable-box-co. The Inspector is a fictional character and has not used this product."
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 4,
   "location": "Hallway with coat hooks",
   "action": "Locked-off wide. The Inspector stands centre holding the clipboard level. She clicks the chest lamp on, sweeps its beam along the six cables in the tape cordon, then states the case. A thin lead is faintly visible from her chest strap back toward the wall socket, unremarked.",
   "performance": "Invested task: conducts a formal site briefing, eyes tracking each cable in the beam as if reading a charge sheet.",
   "microexpression": "Neutral, one slow blink as the beam reaches the sixth cable.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Cable Incident. Six suspects. The box holds six.",
     "delivery": "flat, measured, bureaucratic, each sentence separated by a short pause",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "wide, eye level, slightly formal symmetrical framing",
    "lens": "24mm-equivalent phone main camera",
    "movement": "static, locked off",
    "rig": "phone propped on a hallway shelf at chest height"
   },
   "lighting": "Key: soft daylight from a window frame-left at the hallway end; warm bounce off the oak floor; lamp beam adds a cool white highlight on the cables; soft contact shadows under the cables and the box.",
   "environment": "Narrow modern hallway, pale grey walls, three plain coat hooks with a beige coat, light oak floor, wall socket low on the left wall; orange tape square on the floor around six cables laid in a neat row beside the open box.",
   "sound": {
    "ambience": "quiet flat room tone, faint fridge hum from beyond",
    "foley": [
     "lamp click",
     "clipboard plastic tick",
     "one slow boot step on wood"
    ],
    "music": "none",
    "voice": "Inspector on camera, measured and dry"
   },
   "captions": "Paid partnership",
   "transition_out": "cut",
   "props_from_frame_one": [
    "plain unbranded cable-organiser box (no text)",
    "six loose cables (neutral colours, no logos)",
    "safety-orange tape cordon",
    "inspection lamp on chest strap",
    "tiny clipboard on lanyard",
    "lamp charging lead (seventh cable) running from chest strap to wall socket",
    "wall socket with plain faceplate"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U1"
  },
  {
   "scene_id": "S2",
   "start_s": 4,
   "end_s": 8,
   "location": "Hallway with coat hooks",
   "action": "Medium. She picks up each cable in turn, reads it a formal 'right' with a mouthed nod, drops it into the box with a clipboard tick. Cable six lands. A seventh cable end still lies on the floor. She steps back to count and the cordon tape drags a few centimetres with her.",
   "performance": "Invested task: processes each cable like a suspect, ticking the clipboard, then tallies with a pointing finger.",
   "microexpression": "Brow lifts a fraction on the count.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Count: seven.",
     "delivery": "quiet, level, a beat of puzzlement underneath",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "medium, eye level",
    "lens": "35mm-equivalent phone main camera",
    "movement": "static with a small settle-wobble on the cut",
    "rig": "phone propped on a hallway shelf at chest height"
   },
   "lighting": "Key: window light frame-left; warm oak-floor bounce; lamp spills a cool circle on the box lid; hard small contact shadow of the box on the floor.",
   "environment": "Narrow modern hallway, pale grey walls, three plain coat hooks with a beige coat, light oak floor, wall socket low on the left wall; orange tape square on the floor around six cables laid in a neat row beside the open box.",
   "sound": {
    "ambience": "same room tone",
    "foley": [
     "cable drop thuds into plastic box x6",
     "clipboard ticks",
     "tape peel creak"
    ],
    "music": "none",
    "voice": "Inspector on camera"
   },
   "captions": "",
   "transition_out": "continuous",
   "props_from_frame_one": [
    "plain unbranded cable-organiser box (no text)",
    "six loose cables (neutral colours, no logos)",
    "safety-orange tape cordon",
    "inspection lamp on chest strap",
    "tiny clipboard on lanyard",
    "lamp charging lead (seventh cable) running from chest strap to wall socket",
    "wall socket with plain faceplate"
   ],
   "cuts_inside_clip": 1,
   "generation_unit": "U1"
  },
  {
   "scene_id": "S3",
   "start_s": 8,
   "end_s": 11,
   "location": "Hallway with coat hooks",
   "action": "Close on her upper body. She repeats the count with more ceremony, pointing at each cable inside the box, then the one on the floor. The lead on her chest strap tugs taut and her lamp tilts slightly as she leans.",
   "performance": "Invested task: recounts with slower, more official gestures, committed to the procedure and not noticing the pull on her chest.",
   "microexpression": "Eyes narrow slightly behind the glasses; the lamp bobs.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Recount. Seven.",
     "delivery": "slower, more formal, same volume",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "medium close-up, eye level",
    "lens": "50mm-equivalent phone telephoto",
    "movement": "static, slight breathing drift",
    "rig": "phone propped on a hallway shelf"
   },
   "lighting": "Key: window light frame-left; warm floor bounce under the chin; lamp glint on her glasses; soft shadow of the clipboard on the jacket.",
   "environment": "Narrow modern hallway, pale grey walls, three plain coat hooks with a beige coat, light oak floor, wall socket low on the left wall; orange tape square on the floor around six cables laid in a neat row beside the open box.",
   "sound": {
    "ambience": "room tone, slightly tighter",
    "foley": [
     "finger tap on box lid",
     "strap creak",
     "lamp rattle"
    ],
    "music": "none",
    "voice": "Inspector on camera"
   },
   "captions": "",
   "transition_out": "cut",
   "props_from_frame_one": [
    "plain unbranded cable-organiser box (no text)",
    "six loose cables (neutral colours, no logos)",
    "safety-orange tape cordon",
    "inspection lamp on chest strap",
    "tiny clipboard on lanyard",
    "lamp charging lead (seventh cable) running from chest strap to wall socket",
    "wall socket with plain faceplate"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U2"
  },
  {
   "scene_id": "S4",
   "start_s": 11,
   "end_s": 15,
   "location": "Hallway with coat hooks",
   "action": "Camera pulls wide. The lead is visibly taut from her chest strap across the hallway to the wall socket behind her; the cordon and cables have been dragged along it. She looks down, performs her single slow two-finger tap on the clipboard, delivers the verdict, unplugs the lead from the socket, and closes the box lid on six cables.",
   "performance": "Invested task: issues her verdict with procedural calm, then completes the paperwork of unplugging herself.",
   "microexpression": "Warm disappointment: a slow exhale and eyes lowered to the lead.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Six fit. One is mine.",
     "delivery": "dry, deadpan, lowered slightly at the end",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "wide, eye level, ending on a held frame",
    "lens": "24mm-equivalent phone main camera",
    "movement": "smooth pull-back from medium to wide over 1.5 s, then static",
    "rig": "phone on a slow slider along the hallway floor rail"
   },
   "lighting": "Key: window light frame-left; warm oak bounce; lamp beam cool on the taut lead; thin shadow line of the lead on the floor.",
   "environment": "Narrow modern hallway, pale grey walls, three plain coat hooks with a beige coat, light oak floor, wall socket low on the left wall; orange tape square on the floor around six cables laid in a neat row beside the open box.",
   "sound": {
    "ambience": "room tone",
    "foley": [
     "two-finger clipboard tap",
     "plug pulling from socket",
     "box lid click"
    ],
    "music": "none",
    "voice": "Inspector on camera"
   },
   "captions": "",
   "transition_out": "end hold, end card with disclosure",
   "props_from_frame_one": [
    "plain unbranded cable-organiser box (no text)",
    "six loose cables (neutral colours, no logos)",
    "safety-orange tape cordon",
    "inspection lamp on chest strap",
    "tiny clipboard on lanyard",
    "lamp charging lead (seventh cable) running from chest strap to wall socket",
    "wall socket with plain faceplate"
   ],
   "cuts_inside_clip": 1,
   "generation_unit": "U2"
  }
 ],
 "continuity": {
  "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger.",
  "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun. (same costume throughout the episode).",
  "props": [
   "plain unbranded cable-organiser box (no text)",
   "six loose cables (neutral colours, no logos)",
   "safety-orange tape cordon",
   "inspection lamp on chest strap",
   "tiny clipboard on lanyard",
   "lamp charging lead (seventh cable) running from chest strap to wall socket",
   "wall socket with plain faceplate"
  ],
  "notes": "Silhouette, rule and register fixed per bible v1. Signature clipboard tap used once, in S4. The lead from chest strap to wall socket must be faintly visible in S1 and taut in S4. Box and cables carry no text or logos. Only claim: box holds up to six cables."
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
