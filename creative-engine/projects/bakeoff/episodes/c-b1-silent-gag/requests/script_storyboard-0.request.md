<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

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
    "status": "hypothesis, untested",
    "saved_at": "2026-10-07T23:06:37Z"
  }
}
## Selected premise and hook
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
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Eye-level, locked-off, slightly too formal: the Inspector in aubergine jacket stands square to the side table, phone in one hand, charger plug in the other, held up beside the wall socket with a clearly visible sliver of air between plug and socket. A neat white cable tie is cinched round the middle of the cable, dead centre of frame.",
        "first_line_or_action": "She pushes the plug toward the socket, the cable goes taut and stops, and the plug stays one centimetre short; the tied bunch in the middle of the cable quivers.",
        "mechanism": "visible_problem",
        "score": 9,
        "rationale": "The gap and the cable tie are both readable muted in one second (the viewer holds the answer before she does), though send-ability to a specific friend only lands after the loop."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Slightly raised eye-level on the side table: the cable laid straight along the table edge beside a tape measure, the white cable tie bunching its middle, the plug end resting a thumb's width from the socket-side edge, the Inspector's lamp-lit hands poised over it.",
        "first_line_or_action": "She presses a strip of safety-orange tape onto the cable end with an exaggerated foley click, tagging it as evidence.",
        "mechanism": "escalating_ritual",
        "score": 8,
        "rationale": "The orange tag ritual is instantly on-brand and the tie is in frame, but the gap to the socket is less obvious in frame one than in H1."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Tight-ish two-shot of plug and socket with the Inspector's face behind them, glasses slipped down her nose, composed; the plug hovers a visible centimetre from the socket and the cable tie sits in the soft-focus middle of the lead.",
        "first_line_or_action": "She very slowly edges the plug forward, then lets it spring back and holds still, her expression flat as she regards the gap.",
        "mechanism": "curiosity_gap",
        "score": 7,
        "rationale": "Her deadpan face sells the disproportion and the rule, but the tighter framing pushes the tie toward the edge of legibility and the action reads as less specific."
      },
      {
        "id": "H4",
        "premise_id": "P5",
        "first_frame": "Eye-level on the side table: the Inspector looks down at an open drawer packed with identical coiled cables, each wearing a small safety-orange tag; one cable lies stretched toward the wall socket, a visible centimetre short.",
        "first_line_or_action": "She lifts a tagged cable out of the drawer, holds it up to the socket, finds it short, and tags it with a fresh strip of orange tape.",
        "mechanism": "recognition",
        "score": 8,
        "rationale": "The full drawer is instantly funny and sendable to the friend with the dead-charger drawer, but showing it up front spends the reveal and weakens the camera-notices-first rule."
      },
      {
        "id": "H5",
        "premise_id": "P5",
        "first_frame": "Top-of-table eye-level view: five identical orange-tagged cables laid in a perfectly straight row, every plug ending the same sliver short of the socket edge; the Inspector stands at the end of the row holding a sixth cable.",
        "first_line_or_action": "She sets the sixth cable down at the end of the row with a precise click and squares it to the others with two fingertips.",
        "mechanism": "escalating_ritual",
        "score": 8,
        "rationale": "The repeated row makes the pattern and the shortfall readable at once and invites the 'we need to talk about the drawer' send, but the culprit twist is only implied rather than promised."
      },
      {
        "id": "H6",
        "premise_id": "P5",
        "first_frame": "Static frame of the closed side-table drawer with the Inspector standing before it, clipboard held across her chest, a single cable lying short of the socket on the tabletop and an orange tag fluttering on it.",
        "first_line_or_action": "She slides the drawer open a few centimetres, and orange tags spill into view along its edge.",
        "mechanism": "curiosity_gap",
        "score": 6,
        "rationale": "It builds a good withheld-reveal, but the first frame carries little by itself and the problem is not clear until a second or two in."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "H1 puts both the one-centimetre gap and the cable tie in frame one, so the muted viewer is already ahead of the Inspector, which is the bible rule in its purest form and sets up the relapse loop. The trade-off against the runner-up (P5/H5) is that the drawer hook is the more instantly sendable to a specific friend, but its payoff lands later and its camera-notices-first beat is weaker, so P1/H1 is the stronger fit for a 12-second silent loop."
    }
  }
}

## Rules
- Scenes tile [0, duration_target_s] exactly: first start_s = 0, each start_s = previous end_s, last end_s = target.
- Each scene: location, action, performance (an invested task, not an emotion adjective), microexpression, camera {shot, lens, movement, rig}, lighting (key direction + colour bounce + contact shadows), environment, sound {ambience, foley[], music, voice}, transition_out, props_from_frame_one, cuts_inside_clip (0 or 1), generation_unit (which clip this belongs to; clips are 4-30 s).
- One on-camera speaker per scene at most; a second voice is off-camera.
- Signature gesture at most once. The bible's rule must cause the payoff.
- Continuity: restate identity anchors verbatim from the bible; list every moving prop; costume per episode.
- No readable brand text, logos or real-app UI. No researched creator's identity markers.

- Silent gag: dialogue arrays must be empty. Use timed action, facial performance, camera, ambience, a reveal, and a loop-friendly final pose.




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
