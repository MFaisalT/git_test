# Blind judge prompt (one call per brief; outputs labelled X/Y/Z in a recorded shuffled order)

You are scoring three anonymous episode plans written for the same brief and show bible. You do not know which process produced which. Score each on the rubric below (1-5, anchored), give one sentence of evidence per score, compute the weighted total, and answer the anti-template question. Be strict: 3 means adequate, 5 means you would shoot it as-is.

## Rubric and weights
originality .15 | hook .15 | coherence .15 | identity .10 | audiovisual completeness .15 | feasibility .10 | grounding .08 | commercial_fit .12 (for non-commercial briefs, score commercial_fit on whether a later product category is plausible without forcing it; if the plan does not mention any, give 3).
Anchors: see eval/rubric.md (1 fail / 3 adequate / 5 excellent).

## Brief
{{BRIEF}}
## Bible
{{BIBLE}}

## Plan X
{{X}}
## Plan Y
{{Y}}
## Plan Z
{{Z}}

## Output (JSON only)
{
  "scores": {"X": {"originality": 0, "hook": 0, "coherence": 0, "identity": 0, "audiovisual": 0, "feasibility": 0, "grounding": 0, "commercial_fit": 0, "weighted_total": 0.0},
             "Y": {...}, "Z": {...}},
  "evidence": {"X": {"originality": "", "hook": "", "coherence": "", "identity": "", "audiovisual": "", "feasibility": "", "grounding": "", "commercial_fit": ""}, "Y": {...}, "Z": {...}},
  "thresholds": {"X": {"character_intent": true, "premise_specific_payoff": true, "complete_direction": true, "commercial_fit": true}, "Y": {...}, "Z": {...}},
  "ranking": ["", "", ""],
  "anti_template": {"any_two_share_skeleton": false, "evidence": ""},
  "notes": "two sentences"
}
