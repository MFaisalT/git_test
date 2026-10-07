# Architecture A - fixed-template baseline (one call, rigid template, no bible reasoning fields, no demonstrations)

Write a short-form video episode for the brief below. Fill the template. Output JSON only.

BRIEF:
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

CHARACTER (one line): The Inspector (unnamed on screen): A composed inspector treats trivial household faults as major infrastructure investigations, and always ends up committing the same fault herself.

TEMPLATE:
{
  "selected_premise": {"logline": "", "payoff": ""},
  "hook": {"first_frame": "", "first_line_or_action": ""},
  "script": {"title": "", "synopsis": "", "beats": [{"beat": "", "function": "hook|setup|escalation|turn|payoff|button|cta"}], "dialogue": [{"speaker": "", "line": "", "on_camera": true}], "caption_text": "", "disclosure_line": ""},
  "scenes": [{"scene_id": "S1", "start_s": 0, "end_s": 0, "location": "", "action": "", "performance": "", "microexpression": "", "dialogue": [], "camera": {"shot": "", "lens": "", "movement": ""}, "lighting": "", "environment": "", "sound": {"ambience": "", "foley": [], "music": "none"}, "transition_out": "", "props_from_frame_one": [], "cuts_inside_clip": 0}],
  "continuity": {"identity_anchors": "", "costume": "", "props": [], "notes": ""}
}
Scenes must cover 0 to the target duration.
