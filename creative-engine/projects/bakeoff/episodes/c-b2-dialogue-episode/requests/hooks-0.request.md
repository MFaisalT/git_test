<!-- requested_model: sonnet; effort: medium; tag: hooks-0 -->

# Stage 2 - Scored hook variants

Your responsibility: for the top two premises, write three hook variants each (six total) and score them. A hook is the first frame plus the first line or action; it must work muted and read in about one second.

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
  }
}

Mechanisms allowed: curiosity_gap, recognition, visible_problem, status_contradiction, escalating_ritual, callout, other.
Scoring (0-10): legibility in first frame (0-3), specificity of the problem (0-3), promise of the bible's rule/payoff (0-2), send-ability to a specific person (0-2). Report the score and a one-sentence rationale per hook.



## Output contract (JSON only)
{
  "hook_variants": [ {"id": "H1", "premise_id": "P?", "first_frame": "", "first_line_or_action": "", "mechanism": "", "score": 0, "rationale": ""}, ... 6 items ],
  "selected": {"premise_id": "P?", "hook_id": "H?", "rationale": "why this premise+hook pair, in 2-3 sentences; mention the trade-off against the runner-up"}
}
