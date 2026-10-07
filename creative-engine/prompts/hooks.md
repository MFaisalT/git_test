# Stage 2 - Scored hook variants

Your responsibility: for the top two premises, write three hook variants each (six total) and score them. A hook is the first frame plus the first line or action; it must work muted and read in about one second.

## Brief
{{BRIEF}}
## Bible (identity anchors and rule)
{{BIBLE}}
## Prior stage output
{{CONTEXT}}

<<IF TRENDS>>
## Current trend radar (dated; adapt mechanisms, never copy protected assets)
{{TRENDS}}
<<ENDIF TRENDS>>

Mechanisms allowed: curiosity_gap, recognition, visible_problem, status_contradiction, escalating_ritual, callout, other.
Scoring (0-10): legibility in first frame (0-3), specificity of the problem (0-3), promise of the bible's rule/payoff (0-2), send-ability to a specific person (0-2). Report the score and a one-sentence rationale per hook.
<<IF SILENT>>
No spoken words. first_line_or_action must be an action.
<<ENDIF SILENT>>
<<IF COMMERCIAL>>
The product may appear in the first frame only as an object in the world, never with a claim.
<<ENDIF COMMERCIAL>>

## Output contract (JSON only)
{
  "hook_variants": [ {"id": "H1", "premise_id": "P?", "first_frame": "", "first_line_or_action": "", "mechanism": "", "score": 0, "rationale": ""}, ... 6 items ],
  "selected": {"premise_id": "P?", "hook_id": "H?", "rationale": "why this premise+hook pair, in 2-3 sentences; mention the trade-off against the runner-up"}
}
