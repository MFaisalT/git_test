<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

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
    "Advertiser facts available: 'holds up to six cables', nothing else — do not invent features."
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
        "logline": "In the hallway, the Inspector lays out a six-cable tangle as a police line-up and boxes the suspects in a plain organiser; the count comes out at seven, and the seventh cable runs straight into her own chest lamp.",
        "audience_emotion": "Dry, escalating anticipation, then the pleasure of seeing it coming a beat before she does.",
        "character_desire": "To close the Cable Incident cleanly with every suspect accounted for and filed.",
        "obstacle": "Her tally never reconciles: the box takes up to six and a seventh cable will not go in, however formally she re-counts.",
        "escalation": "Orange tape cordons the floor. Each cable is read its 'rights' and dropped in with a clipboard tick. Cable six lands. The seventh will not go in and she re-counts with more ceremony each time, while the lamp strap tugs at her chest.",
        "surprise": "The unaccounted seventh cable is her own lamp's charging lead, plugged into the wall socket behind her. She has been dragging the tangle across the hallway every time she steps back.",
        "payoff": "Camera pulls wide on the lead taut from her chest to the wall. Two-finger clipboard tap (the one allowed per episode). 'Six fit. One is mine.' She unplugs herself; the box closes with six inside. Bible rule delivered: the Inspector is the culprit and the camera saw it first.",
        "structure": "Procedural line-up and count that does not reconcile; cause-and-effect reveal via a wide pull-back; single static hallway setup.",
        "why_send_it": "Send it to the flatmate who 'organises' the hallway and still trips on their own charger: it is the tidy-person-is-the-mess joke in 15 seconds.",
        "commercial_fit": "The box's single verified fact (holds up to six cables) is the comic mechanism: the six-cable limit is what makes the seventh visible. No durability, price, award or result claims; the Inspector never says she used, tested or benefited from the box and only counts cables into it. Disclosure plan: platform paid-partnership label turned on, plus caption line 'Paid partnership with fictional-cable-box-co. The Inspector is a fictional character and has not used this product.' Spoken words (about 17): 'Suspects: six. The box holds six. Count: seven.' / 'Six fit. One is mine.' No brand text visible on box.",
        "rejected_because": ""
      },
      {
        "id": "P2",
        "logline": "On the living room side table the Inspector finds the six cables already boxed and tidy, hunts for the fault for ten silent seconds, and cannot bear its absence.",
        "audience_emotion": "Uneasy, gently absurd tension: an investigator with nothing to investigate.",
        "character_desire": "To find the fault, because an inspection that finds nothing is an offence in itself.",
        "obstacle": "Everything is in order: six cables in, lid closed, nothing to cite.",
        "escalation": "Lamp passes over the box, tape measure, clipboard ticks, glasses nudged down; her silence stretches while the unbroken order becomes the problem.",
        "surprise": "She quietly takes her own phone charger from a flap pocket and plugs it in, creating the first fault in the scene.",
        "payoff": "A single trailing cable now hangs over the table edge. She nods in satisfaction and starts to write the citation; the camera holds on the cable. She is the culprit again, and the final pose matches the opening pose for a loop.",
        "structure": "Inverted structure: begins in the resolved state, then she creates the fault; near-silent single locked-off take that loops.",
        "why_send_it": "Send it to a partner who rearranges a perfectly good shelf the moment you finish arranging it.",
        "commercial_fit": "The box is the cause of the problem disappearing, and its six-cable capacity is shown as full order that she cannot tolerate. Only the verified fact appears; no claim of results, durability or price, and no first-person use claims. Disclosure plan: platform paid-partnership tool plus on-screen end caption and a spoken closing line 'Paid partnership. Fictional character.' Spoken words about 6 plus caption.",
        "rejected_because": "the product is more backdrop than mechanism, so it ranks below the premises where the six-cable limit drives the joke"
      },
      {
        "id": "P3",
        "logline": "In the shared kitchen the Inspector convenes a one-minute hearing with a housemate (voice and hand only) to decide whose cables clog the counter; her verdict names the housemate, until a name tag on the evidence says otherwise.",
        "audience_emotion": "Bickering domestic warmth, escalating to schadenfreude.",
        "character_desire": "A ruling that assigns blame to someone else.",
        "obstacle": "The housemate refuses to confess and keeps pointing at the cable tags.",
        "escalation": "Rapid back-and-forth: accusation, denial, evidence slid across the counter, each cable dropped into the box as it is ruled on, up to six.",
        "surprise": "The last cable's orange-tape tag is in her own handwriting with her own clipboard initials.",
        "payoff": "She stares at the tag. The housemate's hand slides the box lid shut. Deadpan: 'Case dismissed. Against me.' Rule delivered: she is the offender.",
        "structure": "Two-hander courtroom cross-examination, dialogue-led, ending on a verdict reversal.",
        "why_send_it": "Send it to a housemate you have a running 'whose cable is this' dispute with.",
        "commercial_fit": "The box's six slots are the court's evidence limit, and the verified six-cable fact is the only claim. No testimonials, results or invented features; the housemate is a hand and voice only. Disclosure plan: platform paid-partnership tool and caption line stating the character is fictional and has not used the product. Spoken words about 22.",
        "rejected_because": "dialogue-heavy and the closest to a standard accusation-reversal that the other premises make fresher"
      },
      {
        "id": "P4",
        "logline": "At the hallway coat hooks the Inspector runs a fire drill for cables, with a stopwatch and a muster-point box, and the roll call comes up one short.",
        "audience_emotion": "Brisk, playful momentum.",
        "character_desire": "A perfect evacuation: six out, six in, on time.",
        "obstacle": "Only five cables reach the muster box and the clock keeps running.",
        "escalation": "Fast cuts: whistle, cables hurried off the hooks, stopwatch, a roll call called louder in tone yet never in volume, a second sweep of the hallway.",
        "surprise": "The missing sixth cable has been in her own flap pocket all along, its plug poking out.",
        "payoff": "Camera holds on the plug. She looks down, taps the clipboard once, and posts the sixth cable in. 'Drill complete. Late. Me.' She is the fault.",
        "structure": "Montage-style timed drill with countdown and roll call; fast cutting in contrast to the still premises.",
        "why_send_it": "Send it to the colleague who runs 'efficiency drills' and is always the last one out.",
        "commercial_fit": "The box is the muster point, and its six-cable capacity defines the roll call. No other product claim; she does not claim any use. Disclosure plan: platform paid-partnership label and caption disclosure that the character is fictional. Spoken words about 14.",
        "rejected_because": "the pocket reveal is a smaller surprise and the fast-cut style strains the show's stillness register"
      },
      {
        "id": "P5",
        "logline": "At the side table the Inspector reconstructs the 'tangle incident' in mime with tape outlines, and her own reconstruction proves she caused it.",
        "audience_emotion": "Quiet delight at ritual overcommitment, then recognition.",
        "character_desire": "A faithful reconstruction of how six cables became one knot.",
        "obstacle": "The reconstruction only makes sense if one actor's movement is added to it, and that actor is the investigator.",
        "escalation": "Overhead flat-lay: she chalks (tapes) the knot, walks her hands through the 'suspect's movements' in slow motion, narrating each step in flat procedure, each repeating a gesture that exactly matches her own reach.",
        "surprise": "The mime's final gesture, a hand sweeping a sleeve across the table, exactly matches the one she makes to sweep her papers aside in the opening frame.",
        "payoff": "She freezes mid-sweep; the six cables go into the box one by one with her clipboard tick; 'Culprit identified.' She does not look up. Rule delivered: she is the culprit and the camera knew first.",
        "structure": "Reconstruction and reveal using a flashback-in-place; overhead flat-lay ASMR visual language.",
        "why_send_it": "Send it to a true-crime-obsessed friend who re-enacts how everyone else broke something.",
        "commercial_fit": "The box is where the evidence ends up and the six-cable capacity is the only claim; no results or testing claims by the character. Disclosure plan: platform paid-partnership tool plus caption line 'Paid partnership. Fictional character, has not used this product.' Spoken words about 12.",
        "rejected_because": "the overhead reconstruction is stylish but the product is the tidy-up at the end, not the engine of the joke"
      }
    ],
    "ranking": [
      "P1",
      "P5",
      "P2",
      "P4",
      "P3"
    ],
    "ranking_rationale": "P1 makes the product's single verified fact (six cables) the engine of the joke, and the culprit reveal (her own lamp lead) is visible before she notices, which is the bible rule at full strength in a clear 15-second shape. P5 and P2 are strong but use the box more as a prop; P4 and P3 are readable but lean on weaker reveals or heavier dialogue. The premises differ in structure, location, relationship, pacing, visual language and ending type."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Eye-level, formal framing of a hallway floor: six cables fanned out in a neat police line-up under orange tape, a plain unbranded organiser box open beside them, the Inspector's aubergine-jacketed shins and lamp strap just in frame.",
        "first_line_or_action": "She clicks the lamp on, sweeps it down the row of cables one by one, and says flatly: 'Suspects: six.'",
        "mechanism": "visible_problem",
        "score": 8,
        "rationale": "The cordoned cable line-up reads muted in one second as a absurdly formal tidy-up, and the 'six' sets up the count that will not reconcile, though the problem is implied rather than yet visible."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Tight on the Inspector's gloved fingers dropping the sixth cable into the open box, lid hovering; a seventh cable end is visibly lying on the floor beside it, trailing off-frame behind her.",
        "first_line_or_action": "She counts aloud with a slow finger-point: 'Count: seven.' Her brow lifts a fraction.",
        "mechanism": "curiosity_gap",
        "score": 8,
        "rationale": "Opening on the mismatch (a full box and one cable left over, its source off-frame) gives a precise, specific problem and a question the viewer wants answered, but spends the line that carries the count on frame one."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Wide locked-off hallway shot, Inspector centre with clipboard, orange tape cordoning a pile of tangled cables; a thin cable is faintly visible running from her chest strap behind her toward the wall socket, unremarked.",
        "first_line_or_action": "She taps nothing yet, raises the clipboard and states: 'Cable Incident. Six suspects. The box holds six.'",
        "mechanism": "status_contradiction",
        "score": 9,
        "rationale": "The composed official in a crime-scene cordon over a trivial tangle is legible instantly, the plain 'box holds six' line states the only verified fact as the rule of the case, and the half-hidden lead plants the camera-knows-first promise for re-watchers."
      },
      {
        "id": "H4",
        "premise_id": "P5",
        "first_frame": "Overhead flat-lay of a side table: a knot of six cables outlined in safety-orange tape like a chalk body outline, the unbranded box standing empty at the edge, the Inspector's hands poised above with a tiny clipboard.",
        "first_line_or_action": "Her two hands lower and trace the tape outline in slow motion while she murmurs: 'Reconstruction. Step one.'",
        "mechanism": "escalating_ritual",
        "score": 7,
        "rationale": "The taped outline around a cable knot is a striking and specific image that works muted, but the problem (what exactly went wrong) is less obvious in frame one than in the line-up premise."
      },
      {
        "id": "H5",
        "premise_id": "P5",
        "first_frame": "Overhead flat-lay, side table, the Inspector's sleeve mid-sweep across a pile of loose papers, with six cables lying in a tangle beside the open box, arm blur slightly cut off at frame edge.",
        "first_line_or_action": "Papers fly aside; she pauses, then says without looking down: 'Someone has made a mess.'",
        "mechanism": "recognition",
        "score": 7,
        "rationale": "A sweeping arm that creates the mess is instantly recognisable and plants the sleeve gesture that the payoff echoes, yet the opening line over-tells the irony and the product is barely present."
      },
      {
        "id": "H6",
        "premise_id": "P5",
        "first_frame": "Overhead flat-lay: six numbered orange-tape flags planted on a side table beside one big cable knot, the plain box at the corner, and a lone hand-shaped tape outline where no hand has been placed yet.",
        "first_line_or_action": "She lowers her own hand into the empty tape outline and says: 'Suspect's position.'",
        "mechanism": "callout",
        "score": 7,
        "rationale": "Placing her own hand into the suspect outline is a clean visual joke that foreshadows the rule, though the six-cable limit is not yet doing any work and the setup takes longer than one second to parse."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H3",
      "rationale": "H3 gives the clearest muted read (formal cordoned cable line-up in the hallway), states the single verified fact only as the case's rule, and quietly plants the lead from her chest strap to the wall so the camera notices before she does, which delivers the bible rule on rewatch. The runner-up H2 has a sharper puzzle but reveals the seventh cable too early and removes the escalating count, while P5's best hook (H4) is more stylish but leaves the box as backdrop rather than the engine of the joke."
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


- Dialogue lines fit their scene at <=2.8 words/s. Write for the ear: short lines, no thesis sentences.


- Commercial: product solves or escalates the story problem; include disclosure_line and a disclosure_plan entry; use only verified facts [
  "holds up to six cables"
]; never imply the character used or benefited from it. Forbidden topics: [
  "durability",
  "price",
  "awards",
  "any user result"
].


## Demonstrations
### Demonstration D3_commercial_mechanism (sponsored_episode)
Input brief: A 15-second sponsored episode for a different show (a ceremonial fixer who performs rituals to solve tiny problems). Advertiser: a generic desk lamp. Verified fact: 'three brightness levels'. No other claims allowed.
Accepted output (excerpt): {"premise": "The fixer stages a sunrise ceremony to light a single lost earring under a desk; the lamp's third brightness level ends the ceremony early, and he is visibly disappointed that the problem was that easy.", "disclosure_line": "Paid partnership. The Fixer is a fictional character and has not used this product.", "script_excerpt": [{"speaker": "Fixer", "line": "Level three. ...Anticlimactic.", "on_camera": true}], "commercial_fit_note": "Product is the comic mechanism (it ends the ritual); only the verified fact is used; the character's disappointment is the joke, not a testimonial."}
Why it was accepted: Accepted because the product resolves the story problem, the one verified fact is the only claim, the disclosure is in the plan and spoken/captioned, and the fictional character makes no firsthand-experience claim.
Rejected alternative: A version with 'I've used this lamp every night for a month' was rejected as a false testimonial by a fictional character.

### Demonstration D1_silent_gag (silent_gag)
Input brief: A silent 12-second gag for a different show (a night-shift museum guard who salutes every object before moving it). Problem: one framed photo hangs crooked.
Accepted output (excerpt): {"scenes_excerpt": [{"scene_id": "S1", "start_s": 0, "end_s": 3.5, "action": "Guard enters frame-right already mid-salute to a crooked frame; torch beam lands on the tilt first, his face second.", "performance": "Invested task: assess the tilt like a structural fault; eyes travel the frame edge, not the camera.", "microexpression": "Single slow blink when the beam reaches the corner.", "camera": {"shot": "medium, eye level", "lens": "35mm feel, mild phone wide", "movement": "static propped phone with one settle-wobble", "rig": "phone propped on a radiator"}, "lighting": "Torch is the key from frame-right; cool corridor fill from a far window; warm bounce off the oak floor; hard contact shadow under the frame.", "sound": {"ambience": "empty corridor hum, distant HVAC", "foley": ["torch click", "two boot steps", "fabric creak of the salute"], "music": "none"}, "transition_out": "continuous"}, {"scene_id": "S3", "start_s": 9.0, "end_s": 12.0, "action": "He straightens the frame with two fingers, salutes it, steps back; the frame behind HIM is now crooked. He does not notice. Final pose matches frame one.", "microexpression": "Satisfied exhale through the nose.", "sound": {"ambience": "same hum", "foley": ["frame tick against wall", "single boot step"], "music": "none"}, "transition_out": "loop"}], "dialogue": [], "payoff": "The fix displaces the fault to where he cannot see it; the camera sees it first."}
Why it was accepted: Accepted because the gag is legible with no words: the problem is visible in frame one, the payoff is a visible displacement, the final pose loops, every scene has camera, lighting with bounce and contact shadows, ambience and foley, and no dialogue was invented for a silent brief.
Rejected alternative: A version where the guard mutters 'not on my watch' was rejected: it added speech to a silent brief and told the joke instead of showing it.


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
