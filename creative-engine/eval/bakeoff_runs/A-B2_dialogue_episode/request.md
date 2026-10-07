# Architecture A - fixed-template baseline (one call, rigid template, no bible reasoning fields, no demonstrations)

Write a short-form video episode for the brief below. Fill the template. Output JSON only.

BRIEF:
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
