# Held-out brief: instructions for the independent reviewer worker

Write ONE novel brief JSON for the Inspector of Tiny Problems show that is materially different from every brief in eval/briefs/ (do not read them; the differences below are sufficient): not about cables, chargers, sockets, group chats, or cable boxes; a different location than a living-room side table; a different format axis (e.g. serial_cliffhanger or a spoken episode with an off-camera voice); a constraint the generator has not seen (e.g. a hard prop limit, a time-of-day lighting constraint, or a two-episode arc requirement). Keep it producible: one on-camera character, <=30 s, no crowds, no fine hand-object choreography.

Schema (all fields required):
{"brief_id": "HELDOUT_...", "title": "", "project": "heldout", "bible_ref": "inspector-v1", "format": "silent_gag|spoken_episode|sponsored_episode|serial_cliffhanger|other", "platform": "instagram_reels|tiktok|youtube_shorts|multi", "duration_target_s": 3-30, "language": "", "objective": "", "constraints": [""], "commercial": null, "negative_constraints": [""]}

Write it to eval/heldout/HELDOUT_brief.json and nothing else.
