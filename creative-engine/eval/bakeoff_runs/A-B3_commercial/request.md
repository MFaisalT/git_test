# Architecture A - fixed-template baseline (one call, rigid template, no bible reasoning fields, no demonstrations)

Write a short-form video episode for the brief below. Fill the template. Output JSON only.

BRIEF:
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
    "Advertiser facts available: 'holds up to six cables', nothing else \u2014 do not invent features."
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
