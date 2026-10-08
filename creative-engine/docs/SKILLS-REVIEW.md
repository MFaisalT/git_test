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
   - Check speech against the character's measured speaking rate from the locked voice. Fall back to Higgsfield's density limits, about 2.3 words/s at most; the engine currently allows 3.3.
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
