# Growth and production reverse-engineering: refresh and evidence ledger (2026-10-07 UTC)

Scope: a bounded refresh on top of the lab's 7 Oct research run (growth-report.md, growth-evidence.csv E01–E35, comedy-report.md, audience-report.md, independent-audit.md). New observations today are tagged **NEW**. Access level per item: `full-av` (watched with audio), `partial`, `frames` (silent sampled frames), `text` (captions/comments/articles), `index` (search snippet only), `none`. **No video was watched with audio in this refresh**: instagram.com, tiktok.com and youtube playback are not reachable from this container, and no browser runtime is available. This is a coverage gap, not a finding.

## 1. Classification of claims

| Class | Cases | Verdict |
|---|---|---|
| Verified strict cold-start, organic, ≥500K on one platform within 240 h | — | **Still zero.** Nothing found today changes that. |
| Partially documented rapid-growth stories | Abu Shalab (IG), Charles Robinson 62 (IG), Fruit Love Island / @ai.cinema021 (TikTok), Chloe vs History (30 days, publisher claim) | Scale plausible; baseline, first-post timestamp, crossing time and spend all unverified |
| Same-wave slower comparators | Jean Phil / @jean_philanthrope, Archibald Brown, Derek Mercer, Benjamin (unresolved) | Below-threshold observations; **NEW**: Jean's account predates the character (see ledger N3) → not a cold start even if the counts were verified |
| Later-breakout / older AI formats | Nothing Forever, ask_jesus | Launch ≠ breakout; audience fade hypothesis |
| Established creators / celebrities / institutional | Leah Halton, Jennie, Caitlyn Jenner, Dude with Sign, Candace Payne, TUIDE, world_record_egg | Excluded from startup equivalence |
| Commercial benchmarks | Lu do Magalu, Lil Miquela, Khaby Lame | Activity verified, fees/profit not |

## 2. New ledger rows (today's bounded refresh; all `index`/`text` access)

| ID | Claim | Source (exact URL) | Date | Observation | Confidence | Unresolved alternatives |
|---|---|---|---|---|---|---|
| N1 | Abu Shalab "reached 510K followers in just 25 posts" | https://x.com/vadooai/status/2107116096415506632 | undated in snippet; ≤ 7 Oct 2026 | AI-video vendor marketing post; count/post-count pair repeated from elsewhere | low | Vendor incentive; no capture time; 25 vs 24 vs 26 posts still unresolved |
| N2 | Abu's own X account: "now 650k follower instagram tiktok" and pinned "500K Instagram, goal 1M" | https://x.com/AbuShalab_/status/2106403008234029269 ; https://x.com/abushalab_ | ≤ 7 Oct 2026 | Self-reported, **cross-platform sum** (IG+TikTok) → not one-platform evidence; account promotes $ABU token | low | Promotional self-claim; two posts conflict; token-marketing incentive |
| N3 | Jean Phil: Instagram account registered June 2025, six username changes, X account @JeanPhilMadame opened 20 Sep 2026, coin launched same day; earliest known post 17 Sep 2026 | https://www.sprites.ai/ai-characters/jean-philanthrope ; https://www.character.app/guides/who-is-jean-phil ; https://knowyourmeme.com/memes/jean-philanthrope-jean-phil | Sep–Oct 2026 | Secondary/commercial sources; if accurate, the account is a **renamed pre-existing account**, which disqualifies strict cold-start status regardless of growth | low-medium | Sources sell "make your own Jean Phil" tools; registration date not independently checked (Instagram "about this account" not reachable here) |
| N4 | Jean Phil: ~50K TikTok / ~150K IG "within three days"; 228–235K late Sep; one listing 260.3K | https://sg.news.yahoo.com/jean-philanthrope-ai-mysterious-frenchman-170114829.html ; https://www.dexerto.com/tiktok/who-is-jean-phil-ai-character-behind-multimillion-dollar-meme-coin-sparks-fake-persona-trend-3412528/ | Sep 2026 | Press/secondary; consistent with lab E23–E25; still below 500K | medium for assertion | Baseline unknown; coin-funnel hypothesis (ZDFheute "run from Belgium" per secondary) |
| N5 | Charles Robinson 62: no new independent coverage found | search 2026-10-07 (results were generic growth-tool ads) | — | Lab's 725K (6 Oct) / 892K (7 Oct browser) stand; no history | — | Handle continuity essential; nothing new |
| N6 | Abu ↔ Genjutsu pipeline link | search 2026-10-07: Higgsfield docs https://docs.higgsfield.ai/docs/models/genjutsu/motion-transfer ; https://higgsfield.ai/blog/higgsfield-genjutsu | 2026 | Genjutsu capability documented (4–30 s source video, 1–8 image refs, prompt optional). **No source links any Abu clip to Genjutsu or to a specific driving clip.** | capability: high; attribution: none | Lab's position stands: tool cannot be inferred from appearance; Charles's bio says "Creative Partner @higgsfield.ai" (lab E05 context) which is an association, not a per-clip pipeline proof |
| N7 | Archibald Brown / Derek Mercer | search 2026-10-07 | — | Zero coverage beyond Dexerto's 25 Sep snapshot (lab E24) | — | Account ages unknown; remain comparators, not failures |
| N8 | Higgsfield structured-prompt support | https://docs.higgsfield.ai/how-to/sdk ; third-party Seedance guides (kapwing, wavespeed, atlascloud) | 2026 | SDK takes string `prompt` in a flat arguments dict; no official JSON prompt spec; third-party guides disagree on prompt layout | high (negative) | ByteDance-side spec not checked |

## 3. Account identity and timeline resolution (Abu vs Jean)

- Abu Shalab and Jean Phil are **distinct personas and accounts** (different handles, looks, launch narratives, tokens $ABU vs $JEANPHIL). Nothing today merges them; N3 adds that Jean's account is likely older than its character, Abu's account age remains unknown.
- Abu timeline bounds (unchanged): start "around 25–27 Sep" (conflicting secondary), 364K/14 posts screenshot-described 1 Oct, 479,584 described 3 Oct (403-blocked blog), ~516K 6 Oct (newsletter), 519–525K 7 Oct (index/browser). Elapsed-time interval straddles 240 h with unknown hours/timezones → **unresolved**, not verified.
- Deleted-post gap: 14 → 24/25/26 posts across captures is consistent with normal posting cadence (~1–2/day) or removals; cannot be separated.
- Organic/paid: no spend data in any source; token promotion present on both Abu and Jean accounts is a documented **commercial incentive**, not proof of paid distribution.

## 4. Per-account inspection status (ordinary / breakout / later posts)

| Account | Ordinary | Breakout | Later | Comparators | Comments sampled |
|---|---|---|---|---|---|
| Abu Shalab | 2 clips `frames` (car 4 Oct 12.2 s; bird 5 Oct 19.1 s) by lab specialist; 0 today | not identified | 6 Oct airplane `text` only | Jean, Archibald, Derek | 51 (lab, convenience, four posts, 13/11/13/14); 0 new |
| Charles Robinson 62 | 1 clip `frames` (7 Oct, 14.7 s) by lab | not identified | — | — | 0 coded |
| Fruit Love Island | `text` only (press) | episode 1 / largest episode URLs known, not watched | removals/pivot reported | The Shore Between Us (owned migration) | 0 |
| Nothing Forever | `text` (press, tracker) | Jan–Feb 2023 window | 131,793 followers tracker (provisional) | ask_jesus | 0 |
| Khaby Lame (human benchmark) | 1 clip `frames` (banana, 2021) | — | — | — | 0 |

Required for full-inspection claims: a session with browser/media playback and audio, or owner-supplied downloads of public clips (no credentials needed). Until then "watched full videos with audio" is **not** claimed for any account.

## 5. Mechanisms → testable rules (hypotheses unless marked otherwise)

| Observation (evidence class) | Rule for the engine | How the engine implements it | Falsifier in the pilot |
|---|---|---|---|
| Seed thumbnails show the problem/situation in frame one (`frames`) | Hook must be legible muted in ≤1.5 s | `hooks` stage scores first_frame legibility; rubric dim 2 | Posts with clear first-frame problems do not out-share posts without |
| Friend/self-recognition tags in comments (`text`, 5/38) | Every premise states `why_send_it` to a specific recipient | Required premise field; judge threshold | Recognition premises do not raise shares/reach vs spectacle premises |
| Identity survives varied situations (`frames`) | Fixed silhouette/rule, variable situation | Bible `evolution_policy`; continuity validator restates anchors | Viewers recall costume but cannot state the character's rule |
| Objection to perceived animal harm (`text`, 1 comment) | Negative constraint: no premise depends on perceived harm | `negative_constraints` in packet; QA checks | — (safety rule, not a growth lever) |
| Multilingual reactions (`text`) | Prefer visual payoffs; dialogue optional | Silent-format support; validator forbids invented dialogue | Silent versions lose comprehension/sends vs native-dialogue versions |
| Hybrid replacement may inherit human performance timing (lab PRODUCTION-PROVENANCE, `text`) | Allow motion transfer only with owned/licensed driving footage; record provenance | Adapter routes `driving_footage` → Genjutsu; rights validator blocks render otherwise | — (rights rule) |
| Serial escalation / recurring world in Fruit Love Island press (`text`) | Episode history feeds repetition check; serial hooks allowed | `history` fingerprints into prompts; `serial_cliffhanger` format | Return-attention proxies do not improve with serialisation |
| Posting cadence ~1–2/day in rapid-growth leads (`index`, uncertain) | Capacity plan, not a rule | LAUNCH-EXPERIMENT.md cadence options | Cadence changes without reach change |

Nothing above is causal. Median post performance at equal account age could not be computed (no dated per-post series retrievable); 30/60/90-day persistence remains not yet observable for Sep-2026 launches and missing for older cases.

## 6. Coverage gaps (explicit)

No archived snapshots retrieved; no Instagram/TikTok playback; no private analytics; no creator statements on spend; Arabic/Portuguese/German sources only via English summaries today; comment sampling not repeated. Research-refresh cadence recommended in LAUNCH-EXPERIMENT.md (no automation created).
