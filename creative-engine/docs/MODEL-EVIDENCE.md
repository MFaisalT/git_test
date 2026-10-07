# Runtime, model and skill evidence (captured 2026-10-07 UTC)

## Claude Code runtime (observed, not self-reported)

| Item | Observed value | Source |
|---|---|---|
| Claude Code version | `2.1.293` | `claude --version` in container; `CLAUDE_CODE_VERSION` env also present (2.1.42, stale launcher value) |
| Session configured model | `claude-sonnet-5-5` | `get_session.configured_model` |
| User switch | `/model claude-fable-5-1` → `user_switched_model=claude-fable-5-1` | `/model` command output + `get_session.external_metadata` |
| Last served model (orchestrator) | `claude-fable-5-1` | `get_session.external_metadata.last_served_model` |
| Effort | `medium` (`CLAUDE_EFFORT=medium`, `session_context.effort_level=medium`) | env + `get_session` |
| Billing route | `rate_limit_info.rateLimitType=ccr_promotional`, `isUsingOverage=false`, status allowed | `get_session` |
| Permission mode | `auto` | `get_session` |
| Subagent depth | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` → delegation depth is 1 from this orchestrator; deeper fan-out must be parent-brokered | env |
| Refusal fallback | `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1` | env |
| Context | 1M window, 109,626 used at capture | `get_session.external_metadata.context_usage` |
| Fallback evidence | none observed; no `model_fallback` notice in this session | session transcript |

Uncertainty: the Agent tool returns worker text, not serving metadata. Worker runs are recorded as `requested_model=sonnet; observed_model=not independently observable`. Only the orchestrator's served model is independently observable via `get_session`. A model's self-description is not treated as verification.

## Official documentation read (2026-10-07)

- `code.claude.com/docs/en/model-config` (fetched): `fable` alias → Fable 5.1 (requires Claude Code ≥ 2.1.257); Fable is never the account default; "Fable usage may bill to usage credits, and interactive sessions show a consent prompt first"; effort levels low/medium/high/xhigh/max; default effort `medium` for Opus 5.5 / Sonnet 5.5 / Haiku 5.5; non-interactive `--output-format json` exposes `modelUsage` as the reliable served-model record; content-based safety fallback can switch Fable/Opus 5.5/Sonnet 5.5 to Opus 5 / Opus 4.8; `CLAUDE_CODE_SUBAGENT_MODEL` sets worker default.
- `anthropic.com/claude/fable` (fetched): model id `claude-fable-5-1`; $10/M input, $50/M output, cache read $0.25/M; available on Pro/Max/Team/Enterprise plans and API; 30-day retention default.

Consequence for this build: Fable is used only for interactive orchestration in this authorised session. The engine's `claude_cli` provider (non-interactive `claude -p`) exists in code but was **not exercised live**, to avoid triggering usage credits through a non-interactive command. The `broker` provider, fulfilled by Agent-tool workers inside this session, is the live Claude path used for all generation here.

## Skills actually read (not merely named)

| Skill | Source | What was applied |
|---|---|---|
| prompt-engineering-patterns (SKILL.md + references/details.md) | github.com/wshobson/agents, main, fetched 2026-10-07 | Typed output contracts per stage; progressive disclosure (constraints → examples); dynamic few-shot retrieval (small, diverse, by tag; demo/eval separation); self-verification checklist at the end of each stage prompt; role framing with concrete responsibilities; token economy; prompts versioned as files |
| content-engine | `~/.claude/skills/synced/.../content-engine/SKILL.md` | Hook mechanics (first word, muted legibility, draft-3-pick-1), hold mechanics, producibility filter (one on-camera speaker, simple settings, no fine hand-object work), AI-tell kill list for dialogue, monetisation lens (never undercut product; product earns the view) |
| ugc-influencer-video | `~/.claude/skills/synced/.../ugc-influencer-video/SKILL.md` | Prompt section order, RELIGHT block, alive camera (propped/handheld/placement-open), ACTING TASK over emotion adjectives, prop-from-frame-one rule, ≤1 cut per generation, 30 s cap, speech-rate estimate, known-failure → fix table |
| deep-research | `~/.claude/skills/synced/.../deep-research/SKILL.md` | Coordinator pattern for bounded research workers (used for the Step-3 refresh worker) |
| Higgsfield workflow catalogue | `get_workflow_instructions()` (12 workflows) | Confirms `ugc-video`, `character-sheet`, `video-montage`, `narration` exist; none was activated (no production requested) |

Not installed / not available here: a dedicated storytelling or video-evaluation skill. The rubric in `eval/rubric.md` fills that role explicitly.

## Delegation budget used

Max 3 concurrent workers, depth 1 (hard-limited by runtime), ≤2 repair passes per stage, model `sonnet` for all generation workers (lowest-cost adequate; see bake-off), `opus` for the blind judge (different model from the generators to reduce self-preference), Fable 5.1 for orchestration only.
