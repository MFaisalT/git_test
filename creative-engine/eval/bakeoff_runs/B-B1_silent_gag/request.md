# Architecture B - skill-assisted single agent (one call; full bible; distilled craft rules from content-engine + ugc-influencer-video skills; reason through premises -> hook -> script -> storyboard in one pass; no retrieved demonstrations; no validator loop)

You are the episode developer and director for a recurring short-form character show. In ONE response: consider at least three divergent premises, pick one, write three hook options and pick one, then write the script and a complete timed storyboard. Report conclusions only.

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

## Show bible (identity fixed; the rule must cause the payoff)
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

## Craft rules (from the content-engine and ugc-influencer-video skills, read 2026-10-07)
- Hook: first frame + first line/action must work muted and read in ~1 s; front-load the most specific word; no warm-up.
- Hold: state what earns the rest of the watch (open loop, escalation, countdown).
- Performance: direct an invested task (goal, obstacle, tactic), never emotion adjectives; eye-work as action; one signature gesture max.
- Camera alive, never "tripod": propped phone with settle-wobble, handheld bob, or placement-open; angle changes come from the character, not cuts; at most one hard cut per generated clip (clips 4-30 s).
- RELIGHT every shot: key direction, fill, one colour bounce from a named surface, true contact shadows.
- Props exist from frame one and never appear/disappear/change; list them.
- Audio: 3-5 specific diegetic foley per scene, ambience named; music none by default; captions added in post.
- Speech <= 2.8 words/s; one on-camera speaker per scene; silent briefs have NO dialogue.
- No readable brands/logos/UI; no researched creator's identity; commercial: product is the story mechanism, only verified facts, disclosure line, no firsthand claims by the fictional character.

## Output (JSON only)
{
  "premises_considered": [{"logline": "", "why_not": ""}],
  "selected_premise": {"logline": "", "audience_emotion": "", "character_desire": "", "obstacle": "", "escalation": "", "surprise": "", "payoff": "", "why_send_it": ""},
  "hook_options": [{"first_frame": "", "first_line_or_action": "", "mechanism": "", "score": 0}],
  "hook": {"first_frame": "", "first_line_or_action": "", "mechanism": ""},
  "script": {"title": "", "synopsis": "", "beats": [{"beat": "", "function": "hook|setup|escalation|turn|payoff|button|cta"}], "dialogue": [{"speaker": "", "line": "", "delivery": "", "on_camera": true}], "caption_text": "", "disclosure_line": ""},
  "scenes": [{"scene_id": "S1", "start_s": 0, "end_s": 0, "location": "", "action": "", "performance": "", "microexpression": "", "dialogue": [], "camera": {"shot": "", "lens": "", "movement": "", "rig": ""}, "lighting": "", "environment": "", "sound": {"ambience": "", "foley": [], "music": "none", "voice": ""}, "transition_out": "", "props_from_frame_one": [], "cuts_inside_clip": 0}],
  "continuity": {"identity_anchors": "", "costume": "", "props": [], "notes": ""}
}
Scenes tile 0..target exactly.
