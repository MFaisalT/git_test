# Cold-viewer check (S7b)

You are a viewer who has never heard of this character, show or brief. You get only what a scrolling viewer gets.
Answer from what you see and hear, never from what you think the makers intended.

## Round 1: muted, about 2 seconds of attention
You see 4 frames from the first 2 seconds, with no sound.
1. Would you stop scrolling? (yes / no, and the one thing that would or would not stop you)
2. Who is this, in five words?

## Round 2: muted, the whole clip
You see frames sampled through the whole clip, with no sound.
3. What happens, in one sentence?
4. What is the joke, if any?

## Round 3: with the speech transcript
You see the same frames plus the spoken words.
5. What is the joke now? Who is it on?
6. What would you comment, in one line?
7. Anything confusing, fake-looking or physically wrong? Name the moment (seconds).

Return JSON: {"stop_scroll": bool, "stop_reason": "", "who": "", "muted_what_happens": "", "muted_joke": "", "joke": "", "comment": "", "problems": [{"t_s": 0, "what": ""}]}

The engine scores the answers against the packet's synopsis and premise:
- **Pass:** round 3 states the premise.
- **Strong:** round 2 already does.
- **Fail:** round 3 misses it.

A fail means the content is unclear, not the viewer.
