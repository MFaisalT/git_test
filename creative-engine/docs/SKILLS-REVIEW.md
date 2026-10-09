# Independent review of community skills (2026-10-08)

The owner asked for an "honest independent review" of the skills people recommend: the four synced skills (charsheet-soul, content-engine, digital-product, ugc-influencer-video), "higgsfield-timed-prompts", and others. A reviewer agent with no stake in any skill, including this engine, did the review.

**Method:**
- All skill text was treated as untrusted reference.
- Nothing was installed or run, and no credits were spent.
- The reviewer read every file of the four synced skills; each is a single SKILL.md.
- Community repos were read through raw GitHub fetches.
- Three Higgsfield first-party `ugc-video` files were read with read-only tools.

## Verdicts

| Skill | Verdict | Why |
|---|---|---|
| ugc-influencer-video (synced) | Port specific rules | Useful: pre-recorded line audio per clip, a language lock, a relight line. Drop: its "fake-UGC" framing, which has no disclosure rule, and its borrowed personas. Its camera "wobble/sway" advice contradicts Higgsfield's own `ugc-clip.md`. |
| content-engine (synced) | Port specific rules | Useful: a muted-viewer hook caption, the kill filter, the AI-tell list for scripts. Reject: its ban on hand-object interaction and product demos, which conflicts with the owner's goal. |
| charsheet-soul (synced) | Port specific rules | Useful: put critical facts first (Soul truncates the tail of long prompts; anecdotal) and copy identity anchors verbatim. The rest is specific to Soul. |
| digital-product (synced) | Skip | It sells ebooks, which is out of scope. |
| higgsfield-timed-prompts | Skip | Not found anywhere. Its contents were not guessed. |
| OSideMedia/higgsfield-ai-prompt-skill (703 stars) | Port specific rules only | The best-sourced pack. It has a failure-mode list, with modes 7, 8, 9 and 13 worth porting. Never install it whole: its content-factory module auto-publishes to Meta Ads, and it suggests installing a CLI with curl\|sh. It also says the Cinema Studio 4.0 control ids are unpublished. |
| robonuggets/higgsfield-skill | Skip | It only adds a cost gate, which the engine already has. |
| beshuaxian seedance2 packs, dexhunter seedance2-skill (4.2k stars) | Skip | They target Seedance 2.0 on Jimeng, not our stack. |

**Where the skills are better:** fixing the length of the line audio before the render, keeping a complete prompt skeleton when it shrinks, and muted-first hook craft.

**Where the engine is ahead:**
- Deterministic validators
- Keyframe boards, with closer framings cropped rather than regenerated
- The rotation `direction` field
- The enforced voice lock, with measured QA
- Routing based on measured costs
- Rights and disclosure checks
- Real-render QA: Whisper transcripts and frame inspection

## Rules to port, by impact

1. **Rain beat (lost because the line filled the slot):**
   - Check speech against the character's measured speaking rate from the locked voice. Fall back to Higgsfield's density limits, about 2.3 words/s at most; the engine now allows 2.8 (`SPEECH_WPS_MAX`, lowered from 3.3 on 2026-10-08).
   - World events happen *under* the line, not after it.
2. **Prompts over budget:**
   - Count every word.
   - Put the timed beats and dialogue before the boilerplate.
   - Add an English language lock and a one-line relight to the compact prompt.
3. **Interaction shots:** add a hold clause after the move ("stays on {to_state}"), and fill the rest of the shot with a non-hand action.
4. **Comprehension:** add a cold-viewer QA step. A fresh reviewer gets only frames plus the transcript, and also a muted version, and is asked "what's the joke?". Add a muted hook caption.
5. **Assembly and captions:** use Higgsfield's first-party `video-montage` workflow. Uploads stay gated on the owner.
6. **Camera:** run one A/B test, "breathing sway" vs "locked framing + one deliberate push-in". Higgsfield's own `ugc-clip.md` bans sway, the owner liked the punch-in, and the engine currently rewards sway.
7. **Script craft:** add the AI-tell kill list for spoken lines (low priority).

**Unverified:**
- higgsfield-timed-prompts
- Several listing-only packs (egress blocked)
- Every "proven" claim in the synced skills
- Whether CS4 or Seedance lip-sync to a full supplied line audio
- The Cinema Studio 4.0 control ids. These are now moot: the owner ruled on 2026-10-08 that camera and lens are named in plain language.

## Study 2: incorporating skills per workflow stage (2026-10-08, study only, nothing adopted)

The owner clarified the question: not *replace* the engine, but *incorporate* each relevant skill into the relevant stage. A second independent reviewer read Higgsfield's first-party repo `higgsfield-ai/skills`. It was cloned read-only as untrusted text: not installed, nothing run. The reviewer also re-read the four synced skills.

| Skill | Stage | How it would be used | Value | Main risk |
|---|---|---|---|---|
| higgsfield-video-explainer | S2 voice, S8 assembly | Its audio-first procedure: record every line in the locked voice, then video, then pair them 1:1. Not its 10 s-block assembler. | High | Auto-assembles without a gate |
| higgsfield-youtube-thumbnail | S9 packaging | Truthful concepts and a post-render gate; text added by code. Not its imitation of a named creator's style. | High (S9) | Imitates a creator's style |
| higgsfield-brandkit | S5 props, S11 brands | Lock states, plus invalidating dependent keyframes when a prop changes. Not its scripts. | Medium | Installs packages, runs subprocesses |
| higgsfield-generate | S6, S7 | A few prompt rules (image-to-video: describe motion, not the frame). Virality Predictor only as an optional, gated extra. | Medium | Installs the CLI with curl\|sh; "don't pre-estimate cost"; auto-uploads |
| higgsfield-product-photoshoot | S11 | Reference stills of an owner-supplied product only, gated | Medium (later) | The backend writes the prompt |
| higgsfield-soul-id | S1 (future) | Not now: our characters are generated originals | Low | Paid training on face photos; needs consent |
| higgsfield-marketplace-cards, higgsfield-websites | none | Don't use | none | websites deploys live and claims precedence over other skills |
| ugc-influencer-video (synced) | S4, S6 | Per-clip line audio as "the ONLY spoken content", a language lock, a relight line, the continuation pattern | High | "fake-UGC" framing; no disclosure rule |
| content-engine (synced) | S3, S4, S7, S9 | Kill filter, muted hook caption, AI-tell list | Medium-high | Bans product handling (rejected) |
| charsheet-soul (synced) | S1, S5 | Critical facts first, positive phrasing, counted accessories, a face-fix edit | Medium | Mostly specific to Soul |
| digital-product (synced) | S12 | Don't use now | none | Out of scope |

**What `npx skills add higgsfield-ai/skills` would do (from its docs, not run):**
- It installs all eight skills, and their triggers fire on everyday phrases ("make a video").
- Each skill's first step has the agent run a remote CLI installer by curl\|sh, from another repo nobody here has reviewed. It may ask for sudo.
- It stores a second set of credentials in `~/.config/higgsfield/credentials.json`.
- Install verification runs a paid test generation.
- The websites skill deploys live.

**Conclusion so far:** read and port text; don't install.

**Already applied from this study (owner approved the highest-impact items):**
- Audio-first line fixes in assembly. A locked-voice "Final." replaced the model-voiced one.
- Prop-state continuity
- Speech rate fitted to the locked voice
- Every prompt word counted, with beats first
- The montage-based assembly stage
- The cold-viewer check

Everything else above stays a study item until the owner decides.

## Status: review finished (2026-10-08)

Both studies are complete. Final position, pending the owner's call:
- **Do not install** `higgsfield-ai/skills` or any community pack. They run a curl|sh installer from an unreviewed repo, create a second credentials file, run a paid test generation on install, and the websites skill deploys live.
- **Port text, not code**, stage by stage. Already ported: audio-first line fixes, prop-state continuity, speech fitted to the locked voice, beats-first prompts, montage assembly, cold-viewer check.
- **Remaining candidates (owner to approve):**
  1. Audio-first for every line (video-explainer): record all lines in the locked voice before the video, and pair them 1:1.
  2. A cover and thumbnail gate (youtube-thumbnail): truthful concept, post-render check, text added by code.
  3. A prop lock-state that invalidates dependent keyframes (brandkit). Needed for sponsored products (Mansour).
  4. Kill filter and muted hook caption (content-engine).
- These would live as stage reference files inside the packaged plugin, so each stage loads only what it needs.
