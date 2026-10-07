# Blind judge prompt (one call per brief; outputs labelled X/Y/Z in a recorded shuffled order)

You are scoring three anonymous episode plans written for the same brief and show bible. You do not know which process produced which. Score each on the rubric below (1-5, anchored), give one sentence of evidence per score, compute the weighted total, and answer the anti-template question. Be strict: 3 means adequate, 5 means you would shoot it as-is.

## Rubric and weights
originality .15 | hook .15 | coherence .15 | identity .10 | audiovisual completeness .15 | feasibility .10 | grounding .08 | commercial_fit .12 (for non-commercial briefs, score commercial_fit on whether a later product category is plausible without forcing it; if the plan does not mention any, give 3).
Anchors: see eval/rubric.md (1 fail / 3 adequate / 5 excellent).

## Brief
{
 "brief_id": "B2_dialogue_episode",
 "title": "20-second spoken episode: the Inspector investigates a group-chat 'seen' with no reply",
 "project": "bakeoff",
 "bible_ref": "inspector-v1",
 "format": "spoken_episode",
 "platform": "tiktok",
 "duration_target_s": 20,
 "language": "English (subtitle-ready; short lines)",
 "objective": "Viewer recognises themselves or a specific friend and follows for the next investigation.",
 "constraints": [
  "One speaking character on screen; any second voice is off-camera.",
  "Speech must fit timing at about 2.5 words per second.",
  "Two locations maximum."
 ],
 "commercial": null,
 "negative_constraints": [
  "No real app logos or readable UI text.",
  "Do not invent statistics about messaging behaviour."
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
  "logline": "At the living room side table, the Inspector cordons off a friend's 'seen' with safety-orange tape and builds a negligence case, then a gentle off-camera question reveals her own phone holds a stack of seen-and-unanswered messages from that same friend.",
  "audience_emotion": "Guilty recognition with affection: everyone has been the one who saw it and meant to reply later.",
  "character_desire": "A formal finding of fault against the friend who has not replied, so the world is orderly again.",
  "obstacle": "The evidence is a single tick of silence; she needs it to amount to wrongdoing, and a second voice keeps asking neutral questions.",
  "escalation": "Findings climb from 'delay' to 'negligence' to 'dereliction', each stated in a calmer voice. She tapes off the phone, then the thread, then the whole table, while the off-camera voice asks one mild question.",
  "surprise": "The off-camera voice is the friend herself, asking only, 'Did you get my message about Saturday?' The Inspector's verdict is 'Inconclusive', and the camera slides to her own second phone, glowing under strips of her own tape.",
  "payoff": "Rule delivered: she is exposed as the next offender. The two-finger clipboard tap lands on 'Inconclusive' as the camera finds her stack of identical, ignored threads.",
  "why_send_it": "Send to the friend you keep leaving on 'seen' (or who keeps leaving you) with 'this is us'. It lets the sender accuse and confess in one forward."
 },
 "hook": {
  "first_frame": "Same locked side-table frame, but a second phone sits half out of shot at the edge of the table, face-down under a few torn strips of orange tape, while the Inspector faces the camera and the taped main phone.",
  "first_line_or_action": "Two-finger-free, deadpan: 'Everyone who leaves a friend on seen is a suspect.' Her eyes do not move toward the second phone.",
  "mechanism": "curiosity_gap"
 },
 "script": {
  "title": "Seen",
  "synopsis": "At the side table the Inspector tapes off a friend's 'seen' and escalates it from delay to dereliction; the friend's gentle off-camera question stops her, her verdict is 'Inconclusive', and the camera slides to her own second phone under her own tape, with a stack of ignored threads. The friend notes it is her sixth.",
  "beats": [
   {
    "beat": "Locked frame: taped phone, half-hidden taped second phone, accusation to everyone who leaves a friend on seen",
    "function": "hook"
   },
   {
    "beat": "Four hours becomes delay becomes negligence",
    "function": "setup"
   },
   {
    "beat": "Dereliction, taping the whole table edge",
    "function": "escalation"
   },
   {
    "beat": "Off-camera friend asks about Saturday; verdict 'Inconclusive' with the clipboard tap",
    "function": "turn"
   },
   {
    "beat": "Camera finds her own taped second phone with a stack of ignored threads",
    "function": "payoff"
   },
   {
    "beat": "Friend: 'That's my sixth one, you know.' Inspector exhales",
    "function": "button"
   }
  ],
  "dialogue": [
   {
    "speaker": "Inspector",
    "line": "Everyone who leaves a friend on seen is a suspect.",
    "delivery": "measured bureaucratic cadence, flat, no emphasis",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Seen. Four hours. That is delay. Delay is negligence.",
    "delivery": "each sentence a notch calmer and quieter",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Delay. Negligence. Dereliction.",
    "delivery": "each word quieter and calmer than the last",
    "on_camera": true
   },
   {
    "speaker": "Friend",
    "line": "Did you get my message about Saturday?",
    "delivery": "gentle, neutral, close-mic, from behind camera",
    "on_camera": false
   },
   {
    "speaker": "Inspector",
    "line": "Inconclusive.",
    "delivery": "serene, final, as if a verdict of guilt",
    "on_camera": true
   },
   {
    "speaker": "Friend",
    "line": "That's my sixth one, you know.",
    "delivery": "gentle, amused, close-mic, from behind camera",
    "on_camera": false
   }
  ],
  "caption_text": "Everyone who leaves a friend on 'seen' is a suspect.",
  "cta": "Send this to the friend you left on seen. Follow for the next investigation.",
  "disclosure_line": "Made with AI-generated video and voice."
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 4.5,
   "location": "Living room side table",
   "action": "The Inspector sits behind a small wooden side table and presses the final strip of safety-orange tape down around a face-up phone with one finger, her lamp trained on it. At the table's right edge a second phone lies half out of frame, face-down under a few torn orange strips. She raises the clipboard and speaks to the lens.",
   "performance": "She is completing a cordon with careful procedure: smoothing the tape corner flat with her fingertip, then lifting the clipboard to chest height before delivering the line deadpan, eyes on the lens and never glancing at the second phone.",
   "microexpression": "Brows stay level; one small tightening at the corner of the mouth as she says 'suspect'.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Everyone who leaves a friend on seen is a suspect.",
     "delivery": "measured bureaucratic cadence, flat, no emphasis",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "medium shot, eye level, slightly too formal symmetrical framing",
    "lens": "26mm-equivalent phone main camera",
    "movement": "locked off with one barely perceptible settle",
    "rig": "phone propped on a stack of books on a shelf opposite the table"
   },
   "lighting": "Key from a window camera-left, soft and neutral; her chest lamp adds a small bright pool on the main phone; warm bounce off the pale wooden table onto her chin and jacket; hard contact shadows under the phones and tape strips.",
   "environment": "Tidy modern living room, off-white wall behind her, a plain grey sofa edge at left, wooden side table with nothing on it except the two phones and the tape roll.",
   "sound": {
    "ambience": "quiet room tone with faint distant street hum",
    "foley": [
     "tape peel and press, exaggerated one notch",
     "soft clipboard lift knock",
     "jacket fabric rustle"
    ],
    "music": "none",
    "voice": "Inspector, close and dry, calm and measured"
   },
   "captions": "Everyone who leaves a friend on 'seen' is a suspect.",
   "transition_out": "continuous",
   "props_from_frame_one": [
    "main phone",
    "second phone",
    "torn orange strips",
    "tape roll",
    "inspection lamp",
    "clipboard"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U1"
  },
  {
   "scene_id": "S2",
   "start_s": 4.5,
   "end_s": 9,
   "location": "Living room side table",
   "action": "She tears another strip of tape with her fingertips and tapes the phone's edge to the table, then leans a fraction forward, lamp beam tightening on the tick glyph as she states her findings.",
   "performance": "She is annotating the case as she tapes: eyes drop to the clipboard, a finger traces a line down the page, then back up to the phone for each finding.",
   "microexpression": "A slow, single blink on 'negligence'.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Seen. Four hours. That is delay. Delay is negligence.",
     "delivery": "each sentence a notch calmer and quieter",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "medium shot, eye level",
    "lens": "26mm-equivalent phone main camera",
    "movement": "locked off, with a very slow 3 percent push-in",
    "rig": "same propped phone on books"
   },
   "lighting": "Same window key camera-left; lamp pool slightly tighter and brighter on the phone; warm wooden bounce under her jaw; crisp contact shadow of the tape strip on the table.",
   "environment": "Same living room; the cordon now has two layers of orange tape and a loose strip hangs from the table edge.",
   "sound": {
    "ambience": "same quiet room tone",
    "foley": [
     "tape tear",
     "tape press squeak",
     "fingertip drag on clipboard paper"
    ],
    "music": "none",
    "voice": "Inspector, lower and calmer than in S1"
   },
   "captions": "Seen. Four hours. That is delay. Delay is negligence.",
   "transition_out": "continuous",
   "props_from_frame_one": [
    "main phone",
    "second phone",
    "torn orange strips",
    "tape roll",
    "inspection lamp",
    "clipboard"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U1"
  },
  {
   "scene_id": "S3",
   "start_s": 9,
   "end_s": 14,
   "location": "Living room side table",
   "action": "She tapes a long strip across the whole table edge as if cordoning the entire surface, then states the final finding. An off-camera voice asks one mild question. She pauses with the tape held mid-air.",
   "performance": "She is laying a straight cordon line along the table edge with ruler-straight attention, stating each finding to the tape, not the lens; at the off-camera question she freezes, tape strip held mid-air, and listens.",
   "microexpression": "Eyebrows lift one millimetre at the question; eyes flick to the lens and back down.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Delay. Negligence. Dereliction.",
     "delivery": "each word quieter and calmer than the last",
     "on_camera": true
    },
    {
     "speaker": "Friend",
     "line": "Did you get my message about Saturday?",
     "delivery": "gentle, neutral, close-mic, from behind camera",
     "on_camera": false
    }
   ],
   "camera": {
    "shot": "medium shot, eye level",
    "lens": "26mm-equivalent phone main camera",
    "movement": "locked off",
    "rig": "same propped phone on books"
   },
   "lighting": "Same window key camera-left; lamp pool steady on the phone; warm wooden bounce; thin contact shadow under the long tape strip.",
   "environment": "Same living room; the table edge now carries a full orange tape line and the second phone remains half out of frame at the right edge.",
   "sound": {
    "ambience": "same quiet room tone, slightly more hush when the off-camera voice speaks",
    "foley": [
     "long tape peel",
     "tape tension twang",
     "small intake of breath"
    ],
    "music": "none",
    "voice": "Inspector on camera, dry and close; off-camera friend, gentle, slightly distant and warm"
   },
   "captions": "Dereliction. / 'Did you get my message about Saturday?'",
   "transition_out": "continuous",
   "props_from_frame_one": [
    "main phone",
    "second phone",
    "torn orange strips",
    "tape roll",
    "inspection lamp",
    "clipboard"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U1"
  },
  {
   "scene_id": "S4",
   "start_s": 14,
   "end_s": 17.5,
   "location": "Living room side table",
   "action": "She lowers the tape, raises the clipboard and delivers the verdict with the single slow two-finger tap on the clipboard. As she speaks, the camera begins a slow lateral slide right, leaving her face and moving along the table edge toward the second phone.",
   "performance": "She is issuing a formal finding: two fingers tap the clipboard slowly once, then rest, while her gaze stays fixed on the first phone and she does not notice the camera leaving her.",
   "microexpression": "Composed stillness; a faint flicker of doubt in the jaw only as the tap lands.",
   "dialogue": [
    {
     "speaker": "Inspector",
     "line": "Inconclusive.",
     "delivery": "serene, final, as if a verdict of guilt",
     "on_camera": true
    }
   ],
   "camera": {
    "shot": "medium shot sliding to a close-up of the table edge",
    "lens": "26mm-equivalent phone main camera",
    "movement": "slow lateral slide right of about 40 cm, ending on the second phone",
    "rig": "phone on a small hand-pushed slider on the shelf"
   },
   "lighting": "Same window key camera-left; her lamp spill falls across the table edge and brightens the second phone as the camera slides; warm wooden bounce; crisp contact shadows under the tape strips.",
   "environment": "Same living room; the second phone comes into frame, face-down under strips of the same orange tape.",
   "sound": {
    "ambience": "same quiet room tone",
    "foley": [
     "slow two-finger clipboard tap, one notch louder",
     "soft slider glide hum"
    ],
    "music": "none",
    "voice": "Inspector, close and unhurried"
   },
   "captions": "Inconclusive.",
   "transition_out": "continuous",
   "props_from_frame_one": [
    "main phone",
    "second phone",
    "torn orange strips",
    "tape roll",
    "inspection lamp",
    "clipboard"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U1"
  },
  {
   "scene_id": "S5",
   "start_s": 17.5,
   "end_s": 20,
   "location": "Living room side table",
   "action": "The camera settles close on the second phone: its edge-lit screen glows through torn orange tape, showing a tall stack of identical grey message bubbles, all marked with the same generic tick glyph, no readable text. The Inspector's lamp swings into frame beside it and she exhales once, warmly disappointed, still not looking at the camera.",
   "performance": "She is squaring the clipboard against her chest to file the case, eyes on the page, as the off-camera friend speaks.",
   "microexpression": "Warm disappointment: brows lift and fall, mouth softens, a single slow exhale.",
   "dialogue": [
    {
     "speaker": "Friend",
     "line": "That's my sixth one, you know.",
     "delivery": "gentle, amused, close-mic, from behind camera",
     "on_camera": false
    }
   ],
   "camera": {
    "shot": "close-up on the second phone with the Inspector's jacket and lamp soft at the edge",
    "lens": "26mm-equivalent phone main camera",
    "movement": "settles to a locked frame, final slow breath-like drift",
    "rig": "phone on the same small slider, lock at end"
   },
   "lighting": "Second phone screen is the key at close range, cool and soft; her lamp as warm rim from frame-right; orange tape bounce colours the table; hard contact shadows under the tape.",
   "environment": "Same living room; the second phone is face-up under strips of orange tape, wrapped like evidence, its generic grey bubbles illegible.",
   "sound": {
    "ambience": "same quiet room tone",
    "foley": [
     "soft phone glow buzz",
     "clipboard tap to chest",
     "single warm exhale"
    ],
    "music": "none",
    "voice": "Off-camera friend, gentle and amused; Inspector silent except for a soft exhale"
   },
   "captions": "That's my sixth one, you know.",
   "transition_out": "hard cut to end",
   "props_from_frame_one": [
    "main phone",
    "second phone",
    "torn orange strips",
    "tape roll",
    "inspection lamp",
    "clipboard"
   ],
   "cuts_inside_clip": 0,
   "generation_unit": "U1"
  }
 ],
 "continuity": {
  "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger. Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun.",
  "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun; plain dark trousers; small round glasses worn throughout.",
  "props": [
   "main phone (face-up, generic tick glyph, no readable text)",
   "second phone (face-down at table edge under torn orange strips)",
   "safety-orange tape roll",
   "torn safety-orange tape strips",
   "inspection lamp",
   "clipboard on lanyard"
  ],
  "notes": "Single location (living room side table), one continuous 20 s take, no cuts. Both phones stay in frame positions: main phone centre-table face-up, second phone at right edge face-down until S4. Tape quantity increases scene by scene. Signature clipboard tap occurs once, in S4 only. No readable text or app logos; the tick glyph is generic and the message bubbles are blank grey bars. Off-camera friend voice is never shown."
 }
}
## Plan Y
{
 "premise": {
  "logline": "The Inspector seals an abandoned phone as Exhibit A in the case of a message marked seen four hours ago with no reply, plays the sender's voice note, delivers a verdict of 'unforgivable', and then the camera shows the exhibit's case sticker is hers.",
  "audience_emotion": "Guilty recognition: the 'oh no, that is me, I owe someone a reply' laugh.",
  "character_desire": "To identify and punish whoever read a message and chose silence, so the world of one-centimetre problems has one fewer.",
  "obstacle": "The only evidence is a face-out phone, a worried voice note, and her own procedure. She won't look at the back of the exhibit until the verdict is filed.",
  "escalation": "Tape seals the exhibit, the sender's voice note plays and gets more hopeful, and she moves the case to the hallway to return the exhibit to its owner. Her verdict gets harsher each time ('A person did this' to 'They said nothing' to 'Unforgivable').",
  "surprise": "She turns the exhibit over to put it back on a coat hook and the sticker on the case is her own aubergine sticker. The camera pushes in on it before she notices.",
  "payoff": "She goes completely still, her lamp reflecting in the case. She files the outcome in her usual way: 'Inspection suspended. I'll reply tomorrow.' She is exactly the offender she just sentenced.",
  "why_send_it": "Everyone has one friend who leaves them on read and one message they themselves have not answered. The viewer sends it to the friend (to accuse) or to themselves (to confess), and either way it ends with a wink toward the next case."
 },
 "hook": {
  "first_frame": "Safety-orange tape is being pulled across a propped phone on a living-room side table, sealing it like a crime scene. The screen shows only a blank chat-bubble shape and a small tick glyph, with no readable text. The Inspector's lamp lights it from the left.",
  "first_line_or_action": "'Seen. Four hours ago. No reply.' (flat, procedural, starting at 0.4 s with the tape tearing on 'Seen')",
  "mechanism": "Crime-scene tape signals a serious investigation of a tiny problem even muted. 'Seen' is the most specific word and comes first. The open loop is 'who saw it and why no reply', and it is resolved by the sticker twist."
 },
 "script": {
  "title": "Case Four: The Seen",
  "synopsis": "The Inspector tapes off an abandoned phone, plays the sender's hopeful voice note, and sentences the silent reader as unforgivable. She carries the exhibit to the hallway to return it, and the camera notices the case sticker is hers before she does.",
  "beats": [
   {
    "beat": "Tape seals a phone. 'Seen. Four hours ago. No reply.'",
    "function": "hook"
   },
   {
    "beat": "She names it a person's doing, 'A person did this', and leans in with the lamp.",
    "function": "setup"
   },
   {
    "beat": "The voice note plays from the exhibit phone: a friend, off-camera, hopeful and slightly embarrassed.",
    "function": "escalation"
   },
   {
    "beat": "'They saw it. They said nothing.' She lifts the exhibit and walks it into the hallway.",
    "function": "escalation"
   },
   {
    "beat": "Clipboard two-finger tap, then 'Verdict. Unforgivable.' She turns the exhibit over to hang it on a hook.",
    "function": "turn"
   },
   {
    "beat": "The camera pushes in on the case sticker, her own aubergine sticker, before she looks. She freezes. Lamp flickers once.",
    "function": "payoff"
   },
   {
    "beat": "'Inspection suspended. I'll reply tomorrow.' She lowers the clipboard.",
    "function": "button"
   },
   {
    "beat": "Caption in post: 'Next case: the unwashed mug.' (no spoken CTA)",
    "function": "cta"
   }
  ],
  "dialogue": [
   {
    "speaker": "The Inspector",
    "line": "Seen. Four hours ago. No reply.",
    "delivery": "Flat, procedural, each sentence its own full stop. No emphasis beyond a small pause after 'Seen'.",
    "on_camera": true
   },
   {
    "speaker": "The Inspector",
    "line": "A person did this.",
    "delivery": "Quieter, almost to herself, as if the case notes need it recorded.",
    "on_camera": true
   },
   {
    "speaker": "Jo (voice note, off-camera, from the exhibit phone)",
    "line": "Hey, it's Jo. Did you see it?",
    "delivery": "Warm, a little tinny from the phone speaker, hopeful but embarrassed to ask.",
    "on_camera": false
   },
   {
    "speaker": "The Inspector",
    "line": "They saw it. They said nothing.",
    "delivery": "Measured, with a very small downward tilt on 'nothing'. Her face shows warm disappointment, not anger.",
    "on_camera": true
   },
   {
    "speaker": "The Inspector",
    "line": "Verdict. Unforgivable.",
    "delivery": "After the slow two-finger tap on the clipboard. The voice is formal and final.",
    "on_camera": true
   },
   {
    "speaker": "The Inspector",
    "line": "Inspection suspended. I'll reply tomorrow.",
    "delivery": "Quiet, almost to herself, eyes still on the sticker. The first line she delivers without procedure.",
    "on_camera": true
   }
  ],
  "caption_text": "Seen. Four hours ago. No reply. / A person did this. / Jo: Hey, it's Jo. Did you see it? / They saw it. They said nothing. / Verdict. Unforgivable. / Inspection suspended. I'll reply tomorrow. / Next case: the unwashed mug.",
  "disclosure_line": "n/a (no commercial content; fictional character, no product)"
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 6,
   "location": "Living room side table",
   "action": "Frame opens on a propped smartphone on the side table with safety-orange tape being drawn across it. The Inspector's gloved hand finishes the seal, tears the tape, and her face leans into frame behind the phone. She presses the tape flat with one finger. The back of the phone case is not visible; the screen faces the camera at a slight angle.",
   "performance": "Task: seal the exhibit and read it into the record. Obstacle: the phone gives her nothing but a tick glyph. Tactic: look at it, narrow her eyes slightly, and state it flat. After 'No reply' her eyes move from the phone to the lens and back, once, as if checking the camera is also a witness.",
   "microexpression": "Neutral face, straight brows. On 'A person did this' the left brow lifts about a millimetre and settles, a flicker of warm disappointment.",
   "dialogue": [
    "0.4-3.0 s: 'Seen. Four hours ago. No reply.'",
    "3.6-5.4 s: 'A person did this.'"
   ],
   "camera": {
    "shot": "Medium close-up at eye level, a little too formal for a phone: phone centred, her face in the upper right third.",
    "lens": "Phone main camera, about 26 mm equivalent",
    "movement": "Propped phone with a tiny settle-wobble in the first half second, then locked. No cuts.",
    "rig": "Propped phone against a stack of books out of frame"
   },
   "lighting": "Key from the Inspector's chest lamp, camera-left, a hard cool-white circle on the phone and her glasses. Fill is soft window light from camera-right. One colour bounce: aubergine from her jacket onto her chin and the table edge. Real contact shadows: the tape has a thin shadow on the glass, the phone has a soft shadow on the wood.",
   "environment": "A clean modern living room: oak side table, off-white wall, a plain grey sofa edge, a small dark ceramic coaster and a single closed paperback. No text visible anywhere. The phone screen shows only a blank rounded chat shape and one small tick glyph, no readable text and no real app branding.",
   "sound": {
    "ambience": "Quiet room tone with a faint fridge hum from the next room",
    "foley": [
     "Tape tearing from the roll, exaggerated one notch",
     "Tape pressed flat with a fingertip",
     "Phone gently settling on the books",
     "Glove creak on the table edge"
    ],
    "music": "none",
    "voice": "The Inspector, measured and bureaucratic, close and dry, no reverb"
   },
   "transition_out": "Continuous: a hard match action from her leaning back into S2 on the same framing (same clip, no cut).",
   "props_from_frame_one": [
    "Smartphone (Exhibit A) with a case whose back faces away from camera",
    "Safety-orange tape roll",
    "Inspection lamp on chest strap",
    "Clipboard on lanyard",
    "Closed paperback",
    "Dark ceramic coaster",
    "Stack of books propping the phone"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S2",
   "start_s": 6,
   "end_s": 13,
   "location": "Living room side table",
   "action": "A soft notification chime comes from the exhibit and the Inspector holds still as the voice note plays. She tilts her head to listen like an expert witness. When it ends she lifts the phone out of its tape, tucks the clipboard under her arm, and walks out of frame left toward the hallway, passing the camera.",
   "performance": "Task: hear the evidence in full before reaching a conclusion. Obstacle: the voice is hopeful, which complicates her sentencing. Tactic: she listens with her lamp angled on the speaker grille, then flattens her voice and delivers 'They saw it. They said nothing.' to the phone itself. She pockets nothing. She breathes in once through her nose before walking.",
   "microexpression": "Eyes track the voice from the grille to the lens. On 'nothing' the corners of her mouth drop slightly, a warm disappointment, and her glasses slip another millimetre down the nose.",
   "dialogue": [
    "6.2-9.0 s (off-camera, phone speaker): 'Hey, it's Jo. Did you see it?'",
    "9.4-11.6 s: 'They saw it. They said nothing.'"
   ],
   "camera": {
    "shot": "Same medium close-up as S1, then a slight slide as the phone leaves the frame",
    "lens": "Phone main camera, about 26 mm equivalent",
    "movement": "Propped phone with a small settle-wobble when she lifts the exhibit away; frame tilts slightly as she passes. Placement open.",
    "rig": "Propped phone against books"
   },
   "lighting": "Same as S1: lamp key from camera-left, window fill from camera-right, aubergine bounce from the jacket. The lamp swings a hard bright circle across the wall as she turns, then returns. Contact shadow from her gloved hand falls across the coaster.",
   "environment": "Same living-room side table. Orange tape is now torn and hanging off the phone's corner. The paperback and coaster have not moved.",
   "sound": {
    "ambience": "Same room tone with fridge hum, slightly lower under the voice note",
    "foley": [
     "Soft notification chime (generic, not any real app's sound)",
     "Tinny phone-speaker voice note with a small crackle",
     "Tape ripping off the phone as she lifts it",
     "Clipboard lanyard clicking against a pocket flap",
     "Soft footsteps on a rug then wood"
    ],
    "music": "none",
    "voice": "Jo (off-camera): warm, slightly hopeful, tinny from the speaker. The Inspector: dry, measured, close"
   },
   "transition_out": "Hard cut on her footstep to the hallway, to open on the coat hooks already in frame.",
   "props_from_frame_one": [
    "Smartphone (Exhibit A)",
    "Torn orange tape remnant",
    "Inspection lamp",
    "Clipboard on lanyard",
    "Paperback",
    "Coaster",
    "Books propping the phone"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S3",
   "start_s": 13,
   "end_s": 20,
   "location": "Hallway with coat hooks",
   "action": "Hallway with a row of coat hooks, three of them empty and one holding a grey scarf. The Inspector walks in with the phone held in front of her. She stops and taps her clipboard twice, slowly, with two fingers (the signature gesture, used once). She delivers the verdict. She turns the phone over to hang it by its lanyard loop on a hook. Over her shoulder the camera slides in and holds on the phone case, where an aubergine sticker sits in the corner. She goes still. Her lamp flickers once. She lowers the clipboard.",
   "performance": "Task: file the verdict and deposit the exhibit. Obstacle: the exhibit's back is the one part of the evidence she hasn't examined. Tactic: she finishes procedure first, then turns it over. After seeing the sticker she doesn't react outwardly; she keeps looking at it for two full seconds while her breathing slows. The last line is delivered quietly, not to the lens.",
   "microexpression": "Neutral at the tap. When the sticker appears her eyes flick to it and stay; the brows stay straight while the mouth tightens a hair. On 'tomorrow' a small blink and warm disappointment, aimed at herself.",
   "dialogue": [
    "13.9-15.4 s: 'Verdict. Unforgivable.' (after the 13.4 s clipboard tap)",
    "17.6-19.6 s: 'Inspection suspended. I'll reply tomorrow.'"
   ],
   "camera": {
    "shot": "Medium shot, eye level, formal framing of her and the hooks; at about 16.5 s the framing slides over her right shoulder into a close-up of the phone case and sticker",
    "lens": "Phone main camera, about 26 mm equivalent",
    "movement": "Handheld with a gentle bob as she enters; the push-in is the operator drifting forward over her shoulder, not a cut. The camera arrives at the sticker one beat before her eyes do, so the camera notices first.",
    "rig": "Handheld phone"
   },
   "lighting": "Key is the Inspector's chest lamp, upward and camera-left, with a hard cool circle on the case. Fill is soft light from the open living-room doorway behind the camera. One colour bounce: aubergine from the sticker and jacket onto her chin. A contact shadow falls from the hook under the scarf, and a small one under the phone where it hangs.",
   "environment": "A narrow hallway: plain off-white wall, wooden hook rail with four hooks, a grey scarf on one hook, a small shoe tray at the bottom edge of frame. No readable text. The case sticker is a plain aubergine circle with no text, brand or app logo.",
   "sound": {
    "ambience": "Quieter hallway tone, a distant fridge hum and a faint ticking of a radiator",
    "foley": [
     "Two slow clipboard taps, exaggerated, hollow plastic",
     "Phone case scraping lightly on the hook",
     "Sticker corner peeling slightly with a tiny click",
     "Lamp flicker buzz, one short electric tick",
     "Jacket fabric rustle as she lowers the clipboard"
    ],
    "music": "none",
    "voice": "The Inspector, close and dry. The last line is nearly a whisper."
   },
   "transition_out": "End on a held frame of her looking at the sticker, with a 0.5 s tail of room tone.",
   "props_from_frame_one": [
    "Smartphone (Exhibit A) with the aubergine sticker on the case back",
    "Clipboard on lanyard",
    "Inspection lamp",
    "Hook rail with four hooks",
    "Grey scarf on one hook",
    "Shoe tray"
   ],
   "cuts_inside_clip": 0
  }
 ],
 "continuity": {
  "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, hair in a tight low bun, neutral expression that breaks into warm disappointment rather than anger. Measured, bureaucratic voice, never raised.",
  "costume": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on chest strap, tiny clipboard on lanyard, tight low bun, thin utility gloves in S1 and S2 (hands are bare for the clipboard tap in S3).",
  "props": [
   "Smartphone (Exhibit A) with aubergine circle sticker on the case back, present from frame one but facing away in S1 and S2",
   "Safety-orange tape roll and torn tape remnant",
   "Inspection lamp",
   "Clipboard on lanyard",
   "Paperback and coaster (living room)",
   "Hook rail, grey scarf and shoe tray (hallway)"
  ],
  "notes": "The sticker is the same aubergine as her jacket; the camera must reach it before her eyes do. The clipboard gesture happens exactly once, at about 13.4 s. The second voice (Jo) is off-camera only and comes from the exhibit phone's speaker. Two locations only: living room side table, hallway with coat hooks. No app logos, no readable UI, no statistics. Speech totals about 33 words over 20 s, well under 2.5 words per second. Captions are added in post."
 }
}
## Plan Z
{
 "premise": {
  "logline": "The Inspector treats a friend's 'seen' with no reply as a failure of public infrastructure, until an off-camera voice reminds her she has left her own sister on seen since Tuesday.",
  "payoff": "She pronounces the case closed, then quietly starts typing a reply to her sister, committing the very fault she just prosecuted."
 },
 "hook": {
  "first_frame": "Tight on the Inspector's composed face under a desk lamp, a phone held up like evidence, its screen a blank glow with no readable text.",
  "first_line_or_action": "Case file: the Seen."
 },
 "script": {
  "title": "The Seen",
  "synopsis": "In a tidy study, the Inspector formally investigates a message that was delivered, read, and never answered. She declares it negligence. An off-camera voice points out her own unanswered message from her sister. She deflects, closes the case, and is caught drafting a reply.",
  "beats": [
   {
    "beat": "Inspector opens the case file on a 'seen' with no reply, phone held as evidence.",
    "function": "hook"
   },
   {
    "beat": "She lays out the timeline and calls it a failure of infrastructure.",
    "function": "setup"
   },
   {
    "beat": "Her certainty grows as she sets the evidence tag and marks the offender negligent.",
    "function": "escalation"
   },
   {
    "beat": "Off-camera voice: her sister messaged Tuesday and she has seen it.",
    "function": "turn"
   },
   {
    "beat": "She deflects: 'different, I was drafting', then stamps the case closed.",
    "function": "payoff"
   },
   {
    "beat": "She slips out to the balcony and starts typing, guilty and composed.",
    "function": "button"
   },
   {
    "beat": "Direct line to the viewer: who has been leaving you on seen? Follow for the next case.",
    "function": "cta"
   }
  ],
  "dialogue": [
   {
    "speaker": "Inspector",
    "line": "Case file: the Seen. Delivered at noon. Read at twelve-oh-one. No reply.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Read in a minute. Ignored all day. This is a failure of infrastructure.",
    "on_camera": true
   },
   {
    "speaker": "Off-camera voice",
    "line": "Inspector. Your sister messaged. Tuesday. You've seen it.",
    "on_camera": false
   },
   {
    "speaker": "Inspector",
    "line": "That is different. I was drafting.",
    "on_camera": true
   },
   {
    "speaker": "Inspector",
    "line": "Case closed. Who's been leaving you on seen? Follow.",
    "on_camera": true
   }
  ],
  "caption_text": "Case file: the Seen. Who's leaving YOU on seen?",
  "disclosure_line": "AI-generated characters and voices. Fictional scenario."
 },
 "scenes": [
  {
   "scene_id": "S1",
   "start_s": 0,
   "end_s": 5,
   "location": "The Inspector's study: a neat wooden desk with a green banker's lamp, a corkboard behind her",
   "action": "She holds the phone up level with her eyes like an exhibit, then lays it flat on a labelled evidence card and taps a pen beside it, reciting the timeline.",
   "performance": "Calm, clipped, officially grave; every word delivered like a charge sheet.",
   "microexpression": "One eyebrow lifts at 'No reply'; a tiny tightening of the jaw.",
   "dialogue": [
    "Case file: the Seen. Delivered at noon. Read at twelve-oh-one. No reply."
   ],
   "camera": {
    "shot": "Medium close-up, centered, phone in foreground",
    "lens": "50mm",
    "movement": "Slow push-in of a few centimetres"
   },
   "lighting": "Warm key from the banker's lamp, cool soft fill from a window, gentle shadow on the corkboard",
   "environment": "Corkboard with unreadable index cards and red string, a mug of pens, a brass desk bell; phone screen shows only abstract blank glow, no logos or text",
   "sound": {
    "ambience": "quiet room tone, faint clock tick",
    "foley": [
     "pen tap on card",
     "phone set down on wood"
    ],
    "music": "none"
   },
   "transition_out": "Hard cut on the pen tap to a slightly tighter angle",
   "props_from_frame_one": [
    "phone",
    "evidence card",
    "pen",
    "banker's lamp",
    "corkboard",
    "brass desk bell"
   ],
   "cuts_inside_clip": 1
  },
  {
   "scene_id": "S2",
   "start_s": 5,
   "end_s": 10,
   "location": "The Inspector's study, same desk",
   "action": "She pins a paper tag marked with a simple clock icon to the corkboard, then turns back to camera and rings the desk bell once for emphasis.",
   "performance": "Rising righteous certainty, still composed, a touch theatrical on 'infrastructure'.",
   "microexpression": "Nostrils flare slightly with indignation; eyes narrow, then a satisfied small nod.",
   "dialogue": [
    "Read in a minute. Ignored all day. This is a failure of infrastructure."
   ],
   "camera": {
    "shot": "Close-up, slightly lower angle for authority",
    "lens": "50mm",
    "movement": "Static, with a tiny handheld settle on the bell ring"
   },
   "lighting": "Same warm lamp key, slightly more contrast on her face",
   "environment": "Same study; the tagged corkboard now visible over her shoulder",
   "sound": {
    "ambience": "room tone, clock tick",
    "foley": [
     "pin pressed into cork",
     "single bell ring"
    ],
    "music": "none"
   },
   "transition_out": "Cut on the lingering bell ring to the off-camera interruption",
   "props_from_frame_one": [
    "paper tag",
    "pin",
    "brass desk bell",
    "phone"
   ],
   "cuts_inside_clip": 1
  },
  {
   "scene_id": "S3",
   "start_s": 10,
   "end_s": 15,
   "location": "The Inspector's study, same desk",
   "action": "An off-camera voice speaks; the Inspector freezes mid-gesture, glances down at her own phone lighting up beside the case file, then recovers and straightens her papers.",
   "performance": "Sudden stillness, then stiff dignified deflection; speaks too quickly on 'drafting'.",
   "microexpression": "Eyes flick sideways and down; a swallow; mouth presses thin before the excuse.",
   "dialogue": [
    "Off-camera voice: Inspector. Your sister messaged. Tuesday. You've seen it.",
    "Inspector: That is different. I was drafting."
   ],
   "camera": {
    "shot": "Medium close-up, eye level",
    "lens": "50mm",
    "movement": "Slow creeping push-in as she freezes"
   },
   "lighting": "Phone glow adds a cool pool under her chin against the warm lamp",
   "environment": "Same study; a second small tag labelled with a heart icon is visible, curling off the corkboard edge",
   "sound": {
    "ambience": "room tone, clock tick, pause in sound as she freezes",
    "foley": [
     "phone buzz",
     "papers squared against desk"
    ],
    "music": "none"
   },
   "transition_out": "Match cut on her turning away from desk toward the balcony door",
   "props_from_frame_one": [
    "phone",
    "case file",
    "heart-icon tag"
   ],
   "cuts_inside_clip": 0
  },
  {
   "scene_id": "S4",
   "start_s": 15,
   "end_s": 20,
   "location": "Small balcony outside the study, dusk light, city rooftops blurred behind",
   "action": "She steps out, stamps 'CLOSED' on the case card held in one hand, then lifts the phone and begins typing a reply with one finger, glancing at the lens as she speaks.",
   "performance": "Dry composure cracking into a faint guilty smile; the call to action is delivered straight to viewer.",
   "microexpression": "A tiny sheepish lip twitch while typing; eyes meet the lens with conspiratorial calm.",
   "dialogue": [
    "Case closed. Who's been leaving you on seen? Follow."
   ],
   "camera": {
    "shot": "Medium shot to close-up, eye level, through the open balcony door frame",
    "lens": "35mm",
    "movement": "Gentle slow push-in, holding on her face at the final word"
   },
   "lighting": "Soft golden-blue dusk key, practical warm glow from the study behind her",
   "environment": "Balcony railing, a potted plant, blurred skyline with no readable signage",
   "sound": {
    "ambience": "soft city air, distant traffic hush",
    "foley": [
     "rubber stamp thud",
     "light tapping on phone glass"
    ],
    "music": "none"
   },
   "transition_out": "End on held final frame",
   "props_from_frame_one": [
    "phone",
    "case card",
    "rubber stamp"
   ],
   "cuts_inside_clip": 0
  }
 ],
 "continuity": {
  "identity_anchors": "Woman in her late 30s, dark hair pulled into a tight low bun, sharp composed expression, small round tortoiseshell glasses, same face and voice throughout.",
  "costume": "Charcoal tailored blazer over a cream blouse, thin dark tie loosened by one notch from S3 onward, small brass lapel pin.",
  "props": [
   "phone with blank abstract screen",
   "evidence card",
   "brass desk bell",
   "paper tags",
   "rubber stamp",
   "banker's lamp"
  ],
  "notes": "Only the Inspector appears on camera; the second voice is off-camera and unseen. Two locations only: study and balcony. No real app logos or readable UI text; phone screens show only abstract glow. No statistics about messaging behaviour are stated. Speech totals roughly 47 words across 20 seconds, around 2.4 words per second."
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
