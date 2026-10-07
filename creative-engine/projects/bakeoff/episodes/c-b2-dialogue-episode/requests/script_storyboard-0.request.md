<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

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
        "logline": "At the living room side table, the Inspector cordons off a friend's 'seen' with safety-orange tape and builds a negligence case, then a gentle off-camera question reveals her own phone holds a stack of seen-and-unanswered messages from that same friend.",
        "audience_emotion": "Guilty recognition with affection: everyone has been the one who saw it and meant to reply later.",
        "character_desire": "A formal finding of fault against the friend who has not replied, so the world is orderly again.",
        "obstacle": "The evidence is a single tick of silence; she needs it to amount to wrongdoing, and a second voice keeps asking neutral questions.",
        "escalation": "Findings climb from 'delay' to 'negligence' to 'dereliction', each stated in a calmer voice. She tapes off the phone, then the thread, then the whole table, while the off-camera voice asks one mild question.",
        "surprise": "The off-camera voice is the friend herself, asking only, 'Did you get my message about Saturday?' The Inspector's verdict is 'Inconclusive', and the camera slides to her own second phone, glowing under strips of her own tape.",
        "payoff": "Rule delivered: she is exposed as the next offender. The two-finger clipboard tap lands on 'Inconclusive' as the camera finds her stack of identical, ignored threads.",
        "structure": "Procedural accusation in a single locked frame, with a two-voice cross-examination, building to a reversal reveal on the camera move. Roughly 45 words of speech in 20 seconds.",
        "why_send_it": "Send to the friend you keep leaving on 'seen' (or who keeps leaving you) with 'this is us'. It lets the sender accuse and confess in one forward.",
        "commercial_fit": "None required; the brief has no commercial. Fully brand-safe: no real app, no readable UI, no endorsement.",
        "rejected_because": ""
      },
      {
        "id": "P2",
        "logline": "In the hallway by the coat hooks, the Inspector narrates the forensic timeline of her own reply as she drafts, deletes and redrafts it aloud, never sending it, while the off-camera flatmate's patient 'Any news?' arrives for the third time.",
        "audience_emotion": "Cringe-laugh at the overthinking reply spiral; self-recognition in the anxious drafter rather than the ignorer.",
        "character_desire": "To produce one reply of perfect proportion: warm but not overeager, brief but not curt.",
        "obstacle": "Each candidate reply has a measurable flaw: too many exclamation marks, too few, an emoji with ambiguous intent.",
        "escalation": "Drafts get shorter and more bureaucratic ('Acknowledged.') while the delay grows from hours to days, marked by moving the hooks' coats one by one to a new hook as 'time passing'.",
        "surprise": "The finished, perfect reply is simply 'ok', and she reads it aloud and approves it, but then sets the phone face-down in a coat pocket on the hook, 'for review'.",
        "payoff": "She is the culprit of her own investigation: the final shot is the pocketed phone buzzing against the hook as the lamp dims.",
        "structure": "Monologue-driven escalating montage in one hallway, rapid cut rhythm of draft, delete and verdict, with a hard-cut button.",
        "why_send_it": "Send to the friend who writes and rewrites replies, with 'you at 2am'. Self-directed rather than accusatory.",
        "commercial_fit": "None; no commercial in brief.",
        "rejected_because": "Mostly a single-note spiral with a weaker reversal; the culprit reveal is implied rather than caught by the camera."
      },
      {
        "id": "P3",
        "logline": "The Inspector opens with the verdict already delivered ('The culprit saw it, and did not reply'), then rewinds through three exhibits that each point to a different suspect, until the final exhibit is a mirror-framed shot of herself.",
        "audience_emotion": "Smug satisfaction turning to sheepish recognition: the accuser's lamp swings round.",
        "character_desire": "To close the case in under twenty seconds with a clean conviction.",
        "obstacle": "Her own chain of evidence keeps looping back through places she has been.",
        "escalation": "Exhibit A (the quiet group thread), Exhibit B (a three-dot indicator that vanished), Exhibit C (a 'thumbs up' she insists is not a reply) each narrow the suspect pool until only one remains.",
        "surprise": "Exhibit C is her own thumbs-up, deployed as a pretend reply last week; her lamp reflects in the glossy phone screen.",
        "payoff": "Verdict stands, read in the same measured voice, but the culprit is her; the reflected lamp in the dark screen shows her face. Tap lands before she notices.",
        "structure": "Reverse-chronological: verdict first, then evidence, then reflexive reveal. Hard pacing with three short exhibit beats.",
        "why_send_it": "Send to the group chat itself, with 'Exhibit C: the thumbs up'. It names a shared, specific cheat.",
        "commercial_fit": "None; no commercial in brief.",
        "rejected_because": "Strong concept but needs a mirror/reflection set-up and three exhibits inside 20 seconds, crowding the speech budget."
      },
      {
        "id": "P4",
        "logline": "In the shared kitchen, a flatmate off-camera lists the Inspector's unanswered messages while she, stirring tea with total composure, issues formal 'rulings' that reclassify each one as 'not a message'.",
        "audience_emotion": "Defensive-comic fondness: the pleasure of watching someone lawyer their way out of a small neglect.",
        "character_desire": "To be found not guilty without ever admitting a single message existed.",
        "obstacle": "The flatmate's evidence is dated and specific, and the voice never rises.",
        "escalation": "Rulings go from 'a draft, not a message' to 'a meme, not a message' to 'a voice note is a weather event, not a message', each ruling sharper than the last.",
        "surprise": "The flatmate stops listing and calmly says, 'I was only asking if you wanted tea.' The Inspector has been holding two mugs for the whole scene.",
        "payoff": "She is the next offender: the mug she poured for the flatmate three messages ago is cold on the counter, caught in a slow push-in.",
        "structure": "Two-hander dialogue (one on camera) in the kitchen with a deflating anticlimax; call-and-response rhythm.",
        "why_send_it": "Send to the sibling or flatmate who never answers anything, with 'rulings'. Banter-forward, replies expected.",
        "commercial_fit": "None; no commercial in brief.",
        "rejected_because": "The dialogue is the funniest on paper but the reveal (tea) drifts from the 'seen' topic the brief names."
      },
      {
        "id": "P5",
        "logline": "The Inspector holds a vigil over a friend's silent thread at the side table, lamp trained on the phone, and quietly narrates the long wait as an unsolved disappearance until her own phone gives a small ping, and she flips it face-down.",
        "audience_emotion": "Soft wistful humour: waiting is relatable and the ending is unresolved enough to prompt a reply from the viewer.",
        "character_desire": "A reply, any reply, so the file can be closed.",
        "obstacle": "The phone does nothing; she cannot act without breaking procedure.",
        "escalation": "Lamp gets brighter, narration slower, a pencil is placed beside the phone as a 'marker'; time passes through a changing shadow.",
        "surprise": "Her own phone pings with a message from someone she left unanswered, and her professional calm cracks into a single warm, disappointed sigh.",
        "payoff": "Open ending: she turns the pinging phone face-down 'pending review', and the camera lingers on the dark, quiet table.",
        "structure": "Slow-burn vigil, long takes, minimal speech (about 25 words), ending on an open loop rather than a verdict.",
        "why_send_it": "Send to someone you are waiting on, as a wordless nudge. Low-key and kind.",
        "commercial_fit": "None; no commercial in brief.",
        "rejected_because": "Too quiet for a TikTok hook, and the culprit rule is only a glance rather than a clear exposure."
      }
    ],
    "ranking": [
      "P1",
      "P4",
      "P3",
      "P2",
      "P5"
    ],
    "ranking_rationale": "P1 is strongest because it gives the bible's rule a visible, camera-led payoff (the Inspector's own tape-wrapped stack of ignored threads) and keeps the topic exactly on 'seen with no reply', with one on-camera voice and an off-camera friend that fits the 2.5 words per second budget. P4 and P3 are funnier in concept but one drifts off topic and the other overloads the speech budget. P2 and P5 are valid but have weaker reversals and less shareable hooks."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Locked eye-level shot at the living room side table: a phone lies face-up, its screen blank except a small generic 'seen' tick glyph (no logo, no readable text), already ringed with a square of safety-orange tape. The Inspector sits behind it, lamp on the phone, clipboard raised.",
        "first_line_or_action": "She presses the last strip of tape down with one finger, then says: 'Seen. Four hours ago. Case opened.'",
        "mechanism": "visible_problem",
        "score": 8,
        "rationale": "A cordoned phone is legible muted in one second and the spoken 'seen, four hours' names the exact friend-offence, though it does not yet tease the self-reversal."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Tight on the Inspector's face, brows level, lamp glowing, glasses low; foreground blur of an orange-taped phone. Burned-in subtitle: 'She saw it.'",
        "first_line_or_action": "Flat, measured: 'She saw my message. She did not reply. This is negligence.'",
        "mechanism": "callout",
        "score": 7,
        "rationale": "The accusation is instantly relatable and quotable, but a face-led frame is less distinctive than a taped object and the specificity rests on the line alone."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Same locked side-table frame, but a second phone sits half out of shot at the edge of the table, face-down under a few torn strips of orange tape, while the Inspector faces the camera and the taped main phone.",
        "first_line_or_action": "Two-finger-free, deadpan: 'Everyone who leaves a friend on seen is a suspect.' Her eyes do not move toward the second phone.",
        "mechanism": "curiosity_gap",
        "score": 8,
        "rationale": "The half-hidden taped second phone plants the rule payoff for the camera to find later and rewards a rewatch, at the cost of slightly diluting the one-second read of the main problem."
      },
      {
        "id": "H4",
        "premise_id": "P4",
        "first_frame": "Shared kitchen, eye-level: the Inspector stirs a mug with total composure, a second full mug steaming beside it, lamp on her chest. An off-camera voice is signalled only by her slow glance left.",
        "first_line_or_action": "Off-camera voice: 'You left me on seen.' The Inspector, still stirring: 'That is not a message. That is a draft.'",
        "mechanism": "status_contradiction",
        "score": 7,
        "rationale": "The instant deflection is funny and reads quickly with subtitles, but the stirring-tea frame is not obviously about a messaging problem without sound."
      },
      {
        "id": "H5",
        "premise_id": "P4",
        "first_frame": "Kitchen counter: a neat row of five mugs with small safety-orange tape labels in a straight line, the Inspector behind them holding a clipboard, a lamp spot on the row. No phone visible.",
        "first_line_or_action": "She taps nothing, speaks in her measured cadence: 'Five messages. Zero messages. Allow me to explain.'",
        "mechanism": "escalating_ritual",
        "score": 6,
        "rationale": "The row of labelled mugs is visually striking and promises an escalating ruling ritual, but with no phone the 'seen with no reply' problem is vague for the first second."
      },
      {
        "id": "H6",
        "premise_id": "P4",
        "first_frame": "Kitchen, the Inspector facing camera and holding two mugs, one in each hand, as if about to deliver one; her lamp is lit and her expression neutral. A pencil-thin strip of orange tape marks a line on the counter in front of her.",
        "first_line_or_action": "Off-camera: 'You never replied to anything.' Inspector, evenly: 'Define replied.'",
        "mechanism": "recognition",
        "score": 7,
        "rationale": "'Define replied' is a sharply shareable lawyering line to send to a flatmate, and the two mugs seed the reveal, but the topic anchor is verbal rather than visual."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H3",
      "rationale": "H3 keeps P1's exact 'seen with no reply' topic, shows a taped-off problem the viewer reads in one second, and quietly plants the second taped phone so the bible's rule (the camera notices before she does) pays off on the reveal and invites a rewatch. The trade-off against the runner-up H1 is a slightly less clean first-second read of the main phone in return for the planted payoff and a more shareable line aimed at 'everyone who leaves a friend on seen'; H1 is the safer fallback if testing shows the second phone clutters the frame."
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
