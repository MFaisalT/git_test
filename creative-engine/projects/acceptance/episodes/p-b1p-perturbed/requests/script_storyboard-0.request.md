<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{
  "brief_id": "B1p_perturbed",
  "title": "Anti-template perturbation of B1: same fault (a cable one centimetre short), but a spoken 20-second night-kitchen episode with an off-camera flatmate and a hard two-prop limit",
  "project": "acceptance",
  "bible_ref": "inspector-v1",
  "format": "spoken_episode",
  "platform": "tiktok",
  "duration_target_s": 20,
  "language": "English, short lines, subtitle-ready",
  "objective": "Show that changing constraints changes the narrative decisions, scene actions, performance, camera, sound and payoff, not just the setting words.",
  "constraints": [
    "Location: shared kitchen at 2 a.m., only the fridge light and the Inspector's chest lamp as sources.",
    "Exactly two props may move during the episode (declare them); everything else is set dressing.",
    "A flatmate speaks from off-camera (never seen); the Inspector is the only on-camera speaker.",
    "The payoff must NOT be a cable tie or a wrapped cable (that was the B1 payoff); the bible rule still applies.",
    "No cordon tape, no cones, no clipboard tick-counting (used in earlier episodes)."
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
    "saved_at": "2026-10-07T23:17:47Z"
  }
}
## Selected premise and hook
{
  "premises": {
    "premises": [
      {
        "id": "P1",
        "logline": "At 2 a.m. the Inspector pins her dying phone's cable on the kitchen counter, finds it exactly one centimetre short, and interrogates the dark while a flatmate answers from off-camera; the kettle she set down earlier is standing on the cable's slack.",
        "audience_emotion": "Dry, whispered amusement at over-formal procedure in a sleepy room; the small thrill of spotting the culprit before she does.",
        "character_desire": "To get a clean verdict on the short cable before the phone dies, without waking the house.",
        "obstacle": "The only light is the chest lamp and the fridge glow, so she must examine evidence by narrow beam; the flatmate keeps asking sleepy, literal questions.",
        "escalation": "She measures with a spread hand-span, rules out the socket, rules out the cable, then publicly 'clears' the kettle as a bystander because its steam-less base is in the beam the whole time.",
        "surprise": "The flatmate's lazy line 'Is that my kettle on your cable?' lands off-camera while the lamp beam slides to the kettle's foot pressing the lead flat.",
        "payoff": "Two props move: phone and kettle. She lifts the kettle, the cable gains its centimetre and the plug seats. Rule: she is the culprit, she set the kettle down for her 2 a.m. tea. After the click she mechanically sets the kettle back on the cable's slack, the plug eases out one centimetre, and the camera holds on it as she gives the single slow two-finger clipboard tap on 'Resolved.'",
        "structure": "Procedural interrogation with a single off-camera witness; locked-off, three-beat deadpan, closing on a repeat of the fault.",
        "why_send_it": "Send to a flatmate or partner who 'borrows' your counter space and leaves things on your charger lead: the tone is gentle blame with a built-in confession.",
        "commercial_fit": "None (no commercial in brief); kettle must carry no readable brand.",
        "rejected_because": "Her fault is again 'something she placed ate the centimetre', which is too close to the B1 cable-tie skeleton despite the new object."
      },
      {
        "id": "P2",
        "logline": "To read the dark kitchen she must keep the fridge door open, but her phone is on the middle shelf charging on a lead that only reaches the socket when the door is fully swung; each time the door drifts shut the plug eases out one centimetre and the fridge begins to beep.",
        "audience_emotion": "Escalating comic tension (a ticking clock in a tiny space) resolving in warm embarrassment.",
        "character_desire": "To keep the phone charging and the fridge open without making any noise that wakes the flatmate.",
        "obstacle": "The door swings back, the fridge door alarm rises, and the only way to see the socket is the fridge's own light.",
        "escalation": "Beep one at 3 seconds; she checks the cable with the lamp beam; beep faster; the plug slips out again; she whispers a formal finding to the fridge; the flatmate's voice from the dark asks what that noise is.",
        "surprise": "The investigation was never about the cable: the lamp beam rests on her own phone sitting inside the fridge between butter and a jar, where she put it herself 'to cool the overheating'.",
        "payoff": "Two props move: phone and a plain milk carton. She wedges the door open with the carton, the plug seats, the beeping peaks. Rule: she is the culprit (she put the phone in the fridge). The flatmate says, 'Why is your phone in the fridge?' She replies, 'Under review,' and delivers the two-finger clipboard tap as the beep continues over the final held frame.",
        "structure": "Ticking-clock single space, light-toggle (fridge light on/off alternates with chest lamp only), sound-driven escalation, ending on an unresolved beep.",
        "why_send_it": "Send to a night-owl friend who also keeps weird things in the fridge: the beep is a universally recognised 2 a.m. guilt sound.",
        "commercial_fit": "None; carton and jar are unbranded set dressing.",
        "rejected_because": ""
      },
      {
        "id": "P3",
        "logline": "In whispered audio-forensics, the Inspector asks the flatmate for the sound of every appliance in the kitchen, trying to prove who disturbed the extension lead; the flatmate's sleepy alibi turns out to include her.",
        "audience_emotion": "Cosy hush and the quiet delight of ASMR-like procedure.",
        "character_desire": "To identify the offender who nudged the socket block one centimetre away from the counter.",
        "obstacle": "The flatmate is half asleep, gives only literal replies, and cannot be seen to confirm anything.",
        "escalation": "Each answered noise (hum, click, tap) eliminates one appliance; she narrows her beam on the socket block as her voice drops lower.",
        "surprise": "The final noise the flatmate names is 'the drag when you stood up with your tea'.",
        "payoff": "Two props move: socket block and mug. Rule: she is the culprit; her chair dragged the block. She nudges it back by exactly one centimetre, and the cable now reaches. Her last whispered line lands as the flatmate softly says, 'Goodnight, Inspector.' She taps the clipboard twice and leaves the block exactly where it was before.",
        "structure": "Audio-led interrogation: black-box witness, whisper mode, minimal movement, ending on a blessing rather than a gag.",
        "why_send_it": "Send to the housemate who always answers your late-night nonsense with perfect patience.",
        "commercial_fit": "None.",
        "rejected_because": "Mostly audio with tiny visual action, which weakens the thumb-stopping first second and loops less cleanly."
      },
      {
        "id": "P4",
        "logline": "Cold open on the verdict: the Inspector announces 'Guilty' to the dark kitchen before any evidence, then spends twenty seconds proving it against the flatmate, until the evidence turns round.",
        "audience_emotion": "Anticipation of a reversal; satisfaction when the logic reroutes.",
        "character_desire": "To convict the flatmate of shortening her charger lead before she has shown her working.",
        "obstacle": "Her verdict is already out loud and each exhibit contradicts it a little more.",
        "escalation": "Three exhibits shown in the lamp beam, each less incriminating; the flatmate offers politely helpful corrections.",
        "surprise": "Exhibit three is a note in her own handwriting, 'borrow Sam's shorter cable', visible only as a scribbled shape.",
        "payoff": "Two props move: a charger lead and her phone. Rule: she is the culprit; the lead is her own swap. She swaps it back, the plug reaches, and her verdict changes to 'Guilty' again, spoken to herself.",
        "structure": "Verdict-first reverse logic with escalating counter-evidence and a self-convicting turnaround.",
        "why_send_it": "Send to a friend who always argues first and checks later.",
        "commercial_fit": "None.",
        "rejected_because": "The handwritten note is too readable-text dependent and the structure leans on a repeated 'Guilty' beat that is thin at 20 seconds."
      },
      {
        "id": "P5",
        "logline": "Before the flatmate's 5 a.m. shift, the Inspector quietly sets up the flatmate's dying phone on the counter, discovers the swapped-in lead is one centimetre short, and talks herself through the repair while the flatmate comforts her from the hallway.",
        "audience_emotion": "Tender, slightly absurd kindness; an 'aww' that survives the dryness.",
        "character_desire": "To have the flatmate's phone charged and waiting before they wake, without being thanked.",
        "obstacle": "She is working by chest lamp only, in whispers, and the flatmate keeps checking in from off-camera.",
        "escalation": "Tries the lead; tries a new angle; inspects the socket; the flatmate's replies edge from sleepy to touched.",
        "surprise": "The lead she picked is her own, taken from beside her bed, which is why it is short.",
        "payoff": "Two props move: the flatmate's phone and her own shorter lead. Rule: she is the next offender. She swaps back to the flatmate's own longer lead, which was in the drawer, and quietly gives the two-finger tap. The flatmate says, 'It reaches now. Thanks.' She stays stoic and shuts the drawer with the fridge light behind her.",
        "structure": "Act-of-service disguised as inspection, soft three-beat, emotional payoff over a gag.",
        "why_send_it": "Send to the person who does small kind things for you at silly hours.",
        "commercial_fit": "None.",
        "rejected_because": "The warmth overrides the disproportion that the show's comedy relies on, and the culprit reveal is quieter than the rest."
      }
    ],
    "ranking": [
      "P2",
      "P1",
      "P5",
      "P3",
      "P4"
    ],
    "ranking_rationale": "P2 changes the most: the fault becomes a physical ticking clock built from the two permitted light sources, the fridge's own alarm provides sound escalation, and the culprit is a behaviour (phone in the fridge) rather than a cable accessory, so it cannot be read as the B1 payoff. P1 is the cleanest and most readable but shares B1's 'she placed something that ate the centimetre' skeleton. P5 is emotionally strong yet dilutes the show's disproportion. P3 and P4 are interesting but thinner visually or textually at 20 seconds."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P2",
        "first_frame": "Locked-off, eye-level shot into an open fridge at 2 a.m.: the Inspector in the aubergine jacket is a dark silhouette behind the door, her chest lamp a hard white disc on the middle shelf, where a phone sits between a butter dish and a jar, its charge lead stretched taut to a wall socket.",
        "first_line_or_action": "The fridge door drifts shut by a hand's width; the plug eases out of the socket and a single beep sounds. She says, flat and whispered, 'Finding one: the door is lying.'",
        "mechanism": "visible_problem",
        "score": 8,
        "rationale": "A phone inside a fridge on a taut lead is legible in one frame with sound off and the beep gives a ready-made ticking clock, but the promise of her own guilt is only implied."
      },
      {
        "id": "H2",
        "premise_id": "P2",
        "first_frame": "Extreme close-up of a wall socket in the fridge's pale glow: a plug sits one centimetre proud of the socket face, the Inspector's lamp beam narrowing onto the gap like a spotlight.",
        "first_line_or_action": "Her two fingers push the plug home; the door swings gently shut, the fridge goes dark except for the lamp, and the plug eases back out by the same centimetre as the beep starts.",
        "mechanism": "escalating_ritual",
        "score": 7,
        "rationale": "The one-centimetre gap is the most specific problem and the push-and-slip loop reads muted, but the extreme close-up hides the fridge, so the strange part (phone in the fridge) is withheld past the first second."
      },
      {
        "id": "H3",
        "premise_id": "P2",
        "first_frame": "Wide, formal, slightly-too-centred frame of the Inspector facing the open fridge like a witness stand, lamp on her chest, a milk carton held at arm's length in one hand, the fridge interior glowing behind a phone on the shelf.",
        "first_line_or_action": "She addresses the fridge in a measured whisper: 'You will remain open for the duration.' The door begins to close. Cut on the first beep.",
        "mechanism": "status_contradiction",
        "score": 7,
        "rationale": "Formal address of an appliance is the show's disproportion in one image and the carton foreshadows the wedge, though the problem is stated by line rather than seen in the frame."
      },
      {
        "id": "H4",
        "premise_id": "P1",
        "first_frame": "Chest-lamp beam cuts across a dark counter and lands on a phone lying with its charger lead pulled bar-straight, the plug hovering one visible centimetre from the socket, a kettle standing to one side in shadow.",
        "first_line_or_action": "She lays a spread hand over the gap and whispers, 'One centimetre. Somebody did this.' From off-camera a sleepy voice says, 'Who?'",
        "mechanism": "curiosity_gap",
        "score": 7,
        "rationale": "The short cable is instantly legible and the off-camera 'Who?' sets up a whodunit, but a straight lead on a counter is a quieter image than the fridge and the kettle culprit is not yet signposted."
      },
      {
        "id": "H5",
        "premise_id": "P1",
        "first_frame": "Tight on the base of the kettle in the lamp beam, a charger lead visibly pinned flat beneath its foot, while the Inspector's gloved-looking hand points a pen-sized beam at the empty socket past it.",
        "first_line_or_action": "She delivers in a bureaucratic murmur, 'The kettle is cleared.' A sleepy voice from the dark: 'Is that my kettle on your cable?'",
        "mechanism": "callout",
        "score": 8,
        "rationale": "Showing the cable under the kettle in frame one lets viewers spot the culprit before her, which is the bible's rule, and the flatmate line is a perfect send-to-your-housemate callout, but it spends the reveal that the payoff needs."
      },
      {
        "id": "H6",
        "premise_id": "P1",
        "first_frame": "Mid shot of the Inspector holding her phone up at arm's length, dim screen showing a nearly empty battery shape, lamp on, her free hand measuring the lead against the counter edge with a spread hand-span.",
        "first_line_or_action": "She taps two fingers on her clipboard before any evidence and announces, 'This is a cable matter.' The fridge hum cuts out on the word 'matter'.",
        "mechanism": "recognition",
        "score": 6,
        "rationale": "The near-dead phone and hand-span measuring are instantly relatable, but spending the rationed clipboard tap in the hook breaks the character's gesture rule and gives no visible culprit."
      }
    ],
    "selected": {
      "premise_id": "P2",
      "hook_id": "H1",
      "rationale": "H1 pairs the strongest silent image (a phone sitting in an open fridge on a taut lead, lit only by the two permitted sources) with a sound hook that the first beep makes unmistakable, and it builds directly into the ticking-clock structure and the fridge-phone culprit reveal. The runner-up, P1 H5, scores equally for first-frame culprit-spotting and send-ability, but P1 keeps B1's 'something she placed ate the centimetre' skeleton, so P2 better serves the brief's goal of changing narrative decisions rather than only the setting."
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



## Craft rules (distilled from the content-engine and ugc-influencer-video skills; added after the 2026-10-07 bake-off)
- Hook earns the next second: the most specific word or image first; no warm-up.
- Camera alive, never "tripod": propped phone with one settle-wobble, handheld bob, or placement-open; angle changes come from the character, not cuts.
- Performance = an invested task (goal, obstacle, tactic) with eye-work as action; emotion adjectives are not direction.
- Lighting names key direction, fill, one colour bounce from a named surface and contact shadows; add a light-stability line if the light must not change.
- Audio names ambience plus 3-5 diegetic foley per scene; music none by default.
- The payoff must re-read the opening; the camera notices before the character does.


## Demonstrations
### Demonstration D2_spoken_tool_honesty (spoken_episode)
Input brief: An 18-second spoken episode for a different show (a weather presenter who forecasts social awkwardness). The production tool's JSON support is unverified.
Accepted output (excerpt): {"dialogue_excerpt": [{"speaker": "Presenter", "line": "Light small talk this morning, clearing by the lift.", "on_camera": true, "delivery": "brisk broadcast cadence, eyes to lens then to the 'map'"}, {"speaker": "Colleague", "line": "You're in my lift.", "on_camera": false, "delivery": "flat, close-mic, from behind camera"}], "tool_mapping_excerpt": {"adapter": "higgsfield-mcp/generate_video", "units": [{"generation_unit": "U1", "model": "seedance_2_5", "controls": {"duration": 18, "aspect_ratio": "9:16", "resolution": "720p", "generate_audio": true}, "prompt_text": "TOP PRIORITY ... (free-text house-order prompt)", "manual_steps": ["burn caption in edit", "platform disclosure if sponsored"], "gaps": ["lip-sync quality not controllable; inspect", "no fps control"]}], "notes": "Internal episode JSON is kept for the engine; the tool receives only prompt_text plus the listed native controls. The JSON is NOT a native tool payload."}}
Why it was accepted: Accepted because speech fits the timing (about 2.4 words per second), the second voice is off-camera, and the tool mapping names the free-text prompt as the only creative payload with manual steps and explicit gaps, instead of claiming the internal JSON executes natively.
Rejected alternative: A version that labelled the internal episode JSON as a 'native Higgsfield JSON payload' was rejected: JSON support is unverified and the model catalogue exposes prompt as a string.

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
