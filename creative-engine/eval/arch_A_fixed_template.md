# Architecture A - fixed-template baseline (one call, rigid template, no bible reasoning fields, no demonstrations)

Write a short-form video episode for the brief below. Fill the template. Output JSON only.

BRIEF:
{{BRIEF}}

CHARACTER (one line): {{CHARACTER_LINE}}

TEMPLATE:
{
  "selected_premise": {"logline": "", "payoff": ""},
  "hook": {"first_frame": "", "first_line_or_action": ""},
  "script": {"title": "", "synopsis": "", "beats": [{"beat": "", "function": "hook|setup|escalation|turn|payoff|button|cta"}], "dialogue": [{"speaker": "", "line": "", "on_camera": true}], "caption_text": "", "disclosure_line": ""},
  "scenes": [{"scene_id": "S1", "start_s": 0, "end_s": 0, "location": "", "action": "", "performance": "", "microexpression": "", "dialogue": [], "camera": {"shot": "", "lens": "", "movement": ""}, "lighting": "", "environment": "", "sound": {"ambience": "", "foley": [], "music": "none"}, "transition_out": "", "props_from_frame_one": [], "cuts_inside_clip": 0}],
  "continuity": {"identity_anchors": "", "costume": "", "props": [], "notes": ""}
}
Scenes must cover 0 to the target duration.
