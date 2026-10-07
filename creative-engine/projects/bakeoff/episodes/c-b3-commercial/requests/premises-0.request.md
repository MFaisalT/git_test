<!-- requested_model: sonnet; effort: medium; tag: premises-0 -->

# Stage 1 - Divergent premises

You are the episode developer for a recurring short-form character show. Your responsibility in this stage: produce five genuinely divergent premises for one episode that obey the show bible, then rank them. You are not writing the script yet.

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

## Show/character bible (fixed identity; evolution only where the bible allows)
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



## Reasoning targets (reason about these; report conclusions, not private deliberation)
For each premise state: audience emotion, character desire, obstacle, escalation, surprise, payoff, narrative structure, and why a specific viewer would send it to a specific person.
Diverge across at least four of: narrative structure, conflict type, relationship, location, stakes, performance mode, visual language, pacing, ending type. Setting swaps inside one skeleton do not count as divergence.



Commercial constraint: the product must be the mechanism that resolves or escalates the story problem. Use ONLY these verified advertiser facts: [
  "holds up to six cables"
]. Forbidden claim topics: [
  "durability",
  "price",
  "awards",
  "any user result"
]. The fictional character may never claim firsthand use, testing or results.


## Demonstrations (observable outputs + justification; follow the quality, not the content)
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


## Output contract (JSON only, no prose outside the object)
{
  "premises": [ {"id": "P1", "logline": "", "audience_emotion": "", "character_desire": "", "obstacle": "", "escalation": "", "surprise": "", "payoff": "", "structure": "", "why_send_it": "", "commercial_fit": "", "rejected_because": ""} , ... 5 items ],
  "ranking": ["P?", "P?", "P?", "P?", "P?"],
  "ranking_rationale": "2-4 sentences on quality and coherence, not on count of combinations"
}
Fill rejected_because for the four non-top premises (one clause each). Before answering, check: five premises, each with all fields, divergence along >=4 axes, bible rule present in the top premise's payoff.
