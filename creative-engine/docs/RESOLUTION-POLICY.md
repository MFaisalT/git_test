# Resolution policy: what the platforms want, what the top accounts actually do, what we will do (2026-10-08)

## The real answer, with its evidence class

**Nobody can read a competitor's generation resolution off their posted video.** Instagram, TikTok and YouTube re-encode every upload, so a posted clip tells you the delivery ladder, not the source. The lab's own frame inspections of Abu Shalab / Charles Robinson clips (comedy-report.md, silent frames) could not establish source resolution either. Any claim that "the top AI accounts render at X" is therefore inference from (a) what the generators output natively, (b) what the platforms accept, and (c) what creators publicly describe. Here is that inference, labelled:

| Question | Answer | Evidence class |
|---|---|---|
| What do platforms ask you to upload? | **1080x1920 (9:16), MP4/H.264, 30 fps.** TikTok adds an "Upload HD / high-quality uploads" toggle (on by default on desktop); Instagram has "Upload at highest quality"; YouTube's official encoding page gives 8 Mbps (1080p SDR) and 35-45 Mbps (2160p). Uploading 720p forces the platform to upscale it (looks worse); uploading 4K is downscaled to 1080p for playback on TikTok/Reels, with a possible codec benefit on YouTube. | platform-official (YouTube), third-party guides (TikTok/Instagram; official pages egress-blocked here) |
| What do AI video generators output natively? | Seedance 2.x and Veo 3.x are native **720p/1080p**; Seedance 2.5 on Higgsfield exposes 480p / 720p / 1080p and a 480p draft -> 1080p finalize. 4K from these models is an upscale pass, not native. | catalogue (verified today) + vendor docs |
| What do AI creators publicly describe? | The dominant described workflow is **generate at 720p or 1080p -> optionally upscale to 1080p/4K with a separate tool (Topaz Video AI, CapCut upscaler, SeedVR2) -> export 1080x1920 -> upload with HD on.** Several guides argue a clean 1080p source beats a noisy native 4K attempt, and that at phone size the difference between a Topaz and a free upscale is hard to see. | creator/tool blogs (commercially interested) |
| Do "the top others" post 720p, 1080p, or 720p-then-upscale? | **Unknown per account; structurally, all three paths end as a 1080p delivery on Reels/TikTok.** The only honest inference: anyone posting from Seedance/Veo-class tools is delivering 1080p-class video, reached either by native 1080p generation or by 720p + upscale. Which one a given account used is not observable from the post. | inference |

## Real credit numbers (Higgsfield, get_cost preflights, 9:16, 16 s, Seedance 2.5)

| Path | Credits | Notes |
|---|---|---|
| 480p draft | 48 | approve the take here |
| 720p | 112 | |
| 1080p | 192 | native 1080p, no upscale step |
| 480p draft -> finalize 1080p | 48 + finalize (quote not yet captured; finalize is a separate job within 7 days) | likely the cheapest route to an approved 1080p master |
| Seedance 2.0 Mini 12 s 720p silent | 12 | max 720p; would need an upscale for a 1080p master |

Owner's own ledger shows Cinema Studio 4.0 jobs on 2026-10-06 at 112-154 credits each - consistent with the 720p-class quotes above.

## Policy for this engine

1. **Drafts and takes selection at 480p/720p** (Mini for <=15 s silent; Seedance 2.5 draft for the rest). Never judge identity or comedy on an upscaled draft.
2. **Masters at 1080p**: finalize the approved Seedance 2.5 take at 1080p, or, for Mini output, run one upscale pass to 1080x1920 in post (free/cheap upscaler first; Topaz only if a side-by-side on a phone shows a difference).
3. **Export 1080x1920, H.264 MP4, 30 fps, 10-15 Mbps; upload with the platform's HD/high-quality toggle on.** No 4K uploads for Reels/TikTok; optional 4K test on Shorts only.
4. **Measure, don't assume**: the first two renders (Mini 720p -> upscale vs Seedance 2.5 1080p finalize) are compared side by side on a phone; the cheaper path wins unless identity or texture visibly suffers. Record the result in `evidence.jsonl`.
5. The adapter records `resolution` per unit; `export.resolution` stays 1080x1920; a `MASTER_BELOW_1080` warning is emitted when a unit is planned below 1080p without an upscale step in `export.edit_plan`.
