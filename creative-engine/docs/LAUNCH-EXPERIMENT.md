# Launch experiment (planning only; no accounts, posts, spend or automations created)

Builds on method-and-pilot.md (16-post organic pilot) with the engine in the loop. Every metric below is a platform-exposed metric; items marked **unavailable** are not pretended.

## Platform-specific packaging

| Platform | Packaging from one packet | Notes |
|---|---|---|
| Instagram Reels (primary) | 9:16, 1080×1920, ≤30 s, caption line from `script.caption_text`, cover = hook first frame, AI label + fictional-character bio line | Shares vs DM sends are distinct only if Insights exposes them; shares/reach is the primary conversion |
| TikTok (replication) | Same master; native text overlay for the hook; "AI-generated" toggle on | Sub-minute content is **not** Creator Rewards eligible; treat as audience test only |
| YouTube Shorts (alternative) | Same master; title = hook line; "altered or synthetic" disclosure | Engaged views and subscribers-gained per engaged view |

Cross-posting is logged as amplification of the primary profile; metrics are never pooled.

## Cadence and capacity

- Engine throughput observed in the bake-off: one planning-ready packet per brief in 4 Claude stages, ~70–80K worker tokens per stage, ~20–70 s wall-clock per stage, 0 repair passes on 3/3 briefs (small sample).
- Production: 1–2 generation units per packet; retake sensitivity 2–4× (untested). On 2026-10-07 quotes: 16–64 credits (mini) or 112–448 (Seedance 2.5) per 8 s shot including retakes. Owner time per packet: ~1 h review + render/QA time (to be measured; provisional).
- Cadence options: A) 2 posts/week × 8 weeks (16 posts; lowest credit burn, slowest signal); B) 4 posts/week × 4 weeks (matches "1–2/day" rapid-growth leads less closely but keeps credits under the observed balance on mini). Choose before launch; do not change mid-pilot.
- Capacity ceiling with current balance (981.16 credits, mini only, 2 retakes): ~40 eight-second shots → roughly 16–20 single-unit episodes. Seedance 2.5 at the same retake rate exhausts the balance in ~8 shots.

## Comments / community

- Code every comment with the audience-report scheme (amusement, recognition, quote, sequel request, crossover, reality/AI inquiry, harm/offence, fatigue, spam, uncodable). Sample rule: first batch exposed on the permalink at 24 h and 7 d; no selection by sentiment; record N and access path.
- Reply policy for the character account: in-character replies only to recognition/sequel comments; never claim product experience; never argue about AI.

## Organic distribution

Zero paid during the pilot. Log earned reposts, duets/stitches, and any press. Owner's own audience promotion is **off** (would contaminate cold-start interpretation).

## Optional ads (separately approved limit)

Not part of the pilot. If later approved, a separate ≤$50/month test runs **after** the 16-post organic read, on one finalist, with its own baseline; the approval is recorded separately from render/publish approvals.

## Measurement (per post, 24 h / 72 h / 7 d, same timezone, actual capture timestamp)

| Metric | Instagram | TikTok | Shorts |
|---|---|---|---|
| Reach / unique viewers | Insights reach | unique viewers if exposed, else **unavailable** | unique viewers if exposed |
| Shares | shares (sends not separable unless exposed) | shares | shares |
| Follows attributed to post | if exposed; else account net change (descriptive only) | if exposed | subscribers gained |
| Retention / avg watch | avg watch time, replays separate | avg watch, completion | avg % viewed, viewed-vs-swiped |
| Return attention | **unavailable** publicly; recurring commenters as weak proxy | **unavailable** | returning viewers if exposed |
| Conversion (commercial) | link clicks via platform/UTM; orders **unavailable** without advertiser data | same | same |

Report medians, min–max, N, totals, and the share of outcomes from the largest outlier.

## Kill / iterate criteria (pre-registered; from method-and-pilot.md, unchanged)

Continue a finalist only if ≥3 of 4 follow-ups reach the data-adequacy floor (≥5,000 unique accounts) and the batch shows ≥20 shares and ≥20 attributed follows with improvement over its own screening median in both; else revise one variable (e.g., payoff type, silent vs spoken) and re-run two posts; stop a concept when medians fall below screening after excluding the top outlier, when audience objections reveal harm/confusion, or when credits per accepted episode exceed the owner cap. Inconclusive is an acceptable outcome; no automatic extension.

## Monetisation tests (only after traction or with explicit authorisation)

1. Service inquiry test (N3): publish one packet's storyboard as a portfolio piece; count inbound inquiries (owner decides whether to reply; contact requires approval).
2. Sponsored-episode fit test: one B3-style packet with a fictional advertiser, measured against the entertainment control at equal age; records whether disclosure reduces shares.
3. Native payouts: $0 until owner region + dashboard eligibility confirmed.

## Research-refresh cadence (recommendation, no automation)

- Event-triggered: before any bible bump; before any sponsored episode; when a platform changes payout/AI-label rules (YouTube 1 Feb 2027 change already known); when a seed account passes a 30/60/90-day checkpoint (Abu: ~27 Oct / 26 Nov / 26 Dec 2026 conditional on the Sep-27 start).
- Periodic: a bounded 30-minute evidence refresh every 2 weeks during the pilot, logged to `evidence.jsonl` via `engine learn`.
