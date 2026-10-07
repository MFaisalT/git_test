<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{
  "brief_id": "HELDOUT_hook_overload_two_part",
  "title": "The Case of the Overloaded Hook (Part 1 of 2)",
  "project": "heldout",
  "bible_ref": "inspector-v1",
  "format": "serial_cliffhanger",
  "platform": "multi",
  "duration_target_s": 28,
  "language": "English",
  "objective": "Write Part 1 of a two-episode arc set in the hallway with coat hooks. The Inspector investigates why one coat hook is sagging under a heap of coats while the four hooks beside it hang empty. Part 1 must end on an unresolved cliffhanger in which the camera, before the Inspector does, reveals evidence that she is the culprit, and she does not yet react. Also supply a one-paragraph outline of Part 2 that pays off the cliffhanger, resolves with the Inspector exposed as the culprit, and fits the same 30 s limit.",
  "constraints": [
    "Two-episode arc: Part 1 must stand alone as a watchable short but end unresolved; the Part 2 outline must resolve it without introducing new characters or locations.",
    "Hard prop limit: no more than three props besides the Inspector's fixed costume (lamp, clipboard, jacket). The hook rail counts as set, not a prop. The coat heap counts as one prop.",
    "Time-of-day lighting: early-morning blue hour only. The only light is cool daylight through one frosted door panel plus the Inspector's chest inspection lamp. No overhead or practical room lights are switched on.",
    "One on-camera character only; any second voice must be off camera and limited to one line at most.",
    "Duration 30 s or less; the cliffhanger beat lands in the last 4 s.",
    "Signature two-finger clipboard tap used at most once across Part 1. If it is saved for the Part 2 verdict, say so explicitly.",
    "No fine hand-object choreography: no buttoning, knot-tying, or sorting small items. Actions must read in wide or medium shots."
  ],
  "commercial": null,
  "negative_constraints": [
    "No cables, chargers, sockets, plugs, light switches, group chats, or cable boxes.",
    "Not set at the living-room side table or in the shared kitchen.",
    "No crowds and no second on-camera person, including hands or limbs entering the frame.",
    "No music bed; foley only, per the bible's sound language.",
    "No product endorsements, brand logos, or identifiable brand-name clothing.",
    "No deprivation or luxury contrast as the joke.",
    "No mugging or raised voice; comedy comes from disproportion only."
  ]
}
## Bible
{
  "bible_id": "inspector-v1",
  "version": 1,
  "show_title": "Inspector of Tiny Problems (working title; name/IP uncleared)",
  "logline": "A composed inspector treats trivial household faults as major infrastructure investigations, and always ends up committing the same fault herself.",
  "character": {
    "name": "The Inspector (unnamed on screen)",
    "age_range": "35-45",
    "silhouette": "Aubergine utility jacket with four flap pockets, bright circular inspection lamp on a chest strap, tiny clipboard on a lanyard, hair in a tight low bun.",
    "identity_anchors": "Oval face, straight dark brows, small round glasses pushed slightly down the nose, neutral expression that breaks into warm disappointment rather than anger.",
    "desire": "To restore order to a world that keeps producing one-centimetre problems.",
    "flaw": "She is the main source of the faults she investigates.",
    "rule": "Every investigation ends with the Inspector exposed as the culprit or the next offender; the camera notices before she does.",
    "performance_register": "Stillness and procedure; comedy comes from disproportion, never from mugging.",
    "voice": "Measured, bureaucratic cadence; short declarative lines; never raises her voice.",
    "signature_gesture": "A slow two-finger tap on the clipboard before delivering a verdict (rationed: once per episode)."
  },
  "world": {
    "recurring_locations": [
      "living room side table",
      "shared kitchen",
      "hallway with coat hooks"
    ],
    "visual_language": "Clean modern phone look, eye-level, slightly too formal framing for the triviality; procedural colour accents (aubergine, safety-orange tape).",
    "sound_language": "Diegetic foley exaggerated one notch (clicks, tape, clipboard); no music by default; optional licensed sting only in edit."
  },
  "do_not": [
    "No bob/moustache/white-tunic combination or any researched creator's identity.",
    "No deprivation/luxury contrast as the joke.",
    "No firsthand product endorsements."
  ],
  "evolution_policy": "Costume and locations may vary per episode; silhouette, rule, register and signature gesture are fixed until a versioned bible bump with a stated reason.",
  "provenance": {
    "created": "2026-10-07",
    "basis": "comedy-report.md hypothesis 1, sharpened per independent-audit.md C2",
    "status": "hypothesis, untested",
    "saved_at": "2026-10-07T23:17:47Z"
  }
}
## Selected premise and hook
{
  "premises": {
    "premises": [
      {
        "id": "P1",
        "logline": "Stakeout: in blue-hour stillness the Inspector keeps watch over the sagging hook, declares that nothing has moved all morning, and the heap quietly grows between jump cuts; the final low shot from inside the heap shows her laying one more coat on top.",
        "audience_emotion": "Dry amusement that tips into the pleasure of a trap closing; mild dread because the viewer knows what Part 2 must say.",
        "character_desire": "To catch the person who keeps overloading one hook, without disturbing the scene.",
        "obstacle": "Nothing is happening. A stakeout needs a suspect, and the hallway stays empty and silent.",
        "escalation": "Three locked-off wide beats separated by hard jump cuts and a title-less time lapse of her standing identical. At each cut the heap is a little taller and the hook a little lower; she logs 'No movement' every time and her lamp beam gets steadier and prouder.",
        "surprise": "Last 4 s: the camera drops to floor level inside the heap, looking out through sleeves, and watches her lean in and lay one more coat on top from her own forearm while her eyes stay on the empty doorway. She does not react.",
        "payoff": "Part 1 ends unresolved on that shot; the clipboard tap is NOT used in Part 1 and is explicitly saved for the Part 2 verdict. Part 2 outline (same hallway, same single character, same 28-30 s): she resolves to review the evidence from inside the heap angle, finds the camera's low position, counts the coats against her own forearm habit, and reconstructs the jump-cut gaps; she lowers the clipboard, delivers the single slow two-finger tap, says 'The culprit works quickly. The culprit is me.' hangs one coat on each empty hook, and ends by turning, with the last coat over her forearm, to hang it on the original hook. Bible rule delivered: the Inspector is the culprit and the camera knew first.",
        "structure": "Observational stakeout built on jump-cut time lapse (pass of time as the escalation device), ending on a low reverse-angle reveal; serial cliffhanger with a saved verdict.",
        "why_send_it": "Send to the friend whose coat has lived on 'the pile' by their own front door for a year: 'this is you, not the guests'. The jump cuts make the gag legible in a muted autoplay feed.",
        "commercial_fit": "None needed and none attempted; no products, logos or branded clothing. Neutral.",
        "rejected_because": ""
      },
      {
        "id": "P2",
        "logline": "Composite sketch: with no witnesses, the Inspector reconstructs the coat-hanger from smudge heights and sleeve creases, draws a suspect sketch on her clipboard, and holds it up to the heap to confirm the likeness.",
        "audience_emotion": "Delight at a slow-dawning resemblance; the viewer is ahead of her and enjoys it.",
        "character_desire": "To put a face to the person overloading the hook.",
        "obstacle": "The only data is physical: the reach height of the hanger, a damp patch, a crease pattern. She has to infer a person from coats.",
        "escalation": "She measures the hook height with a tape (one orange tape tag), reads the smudge, narrows to 'right-handed, short, composed', then sketches and each added feature, bun, brow, round glasses, is stated flatly as a finding.",
        "surprise": "Last 4 s: she raises the sketch beside the heap for comparison and the lamp lights it; the drawing is her, oval face, straight brows, glasses sliding down the nose, low bun, with her real profile soft behind it. She says only 'Distinctive' and does not react.",
        "payoff": "Part 1 ends unresolved on the sketch held beside her face. The two-finger clipboard tap is not used in Part 1; it is saved for the Part 2 verdict. Part 2 outline (same hallway, no new characters): she turns the clipboard over to pair the sketch with the reach-height measurement, discovers the hook is at exactly her shoulder height, and the heap is hung in her right-handed arc; she taps the clipboard once and states 'Likeness confirmed.' She then redraws the sketch with a different bun and re-hangs the first coat on the hook anyway.",
        "structure": "Deductive-profile structure: evidence to a drawn composite, ending on a visual match between drawing and drawer; the reveal is a held close-up comparison.",
        "why_send_it": "Send to a flatmate who always insists the mess is 'someone else's': 'I drew the culprit, look who it looks like'. Easily reposted as a still of the sketch beside her face.",
        "commercial_fit": "None; the sketch is hand-drawn so no brand marks occur.",
        "rejected_because": "the comparison reveal is strong but depends on a small, legible drawing, so it is fussier to stage in a wide or medium shot than the stakeout."
      },
      {
        "id": "P3",
        "logline": "Playback: the Inspector reviews overnight hallway footage on her phone to identify who loaded the hook; she pauses on a blurred figure and says 'Unidentified'.",
        "audience_emotion": "Cosy suspense, the pleasure of being let in on the clue.",
        "character_desire": "A clean ID of the offender from the record.",
        "obstacle": "The footage is dim and blue, the figure is a blur, and she refuses to guess.",
        "escalation": "She advances the footage frame by frame, tagging timestamps on the clipboard; each paused frame sharpens one detail: a bun-shaped silhouette, a bright circular glow at chest height.",
        "surprise": "Last 4 s: her screen swings into the camera's view over her shoulder: the glowing circle on the screen matches her own chest lamp, and the figure in the footage stacks coats on the hook. She says 'Unidentified' and does not react.",
        "payoff": "Part 1 ends unresolved. The two-finger tap is not used in Part 1 and is saved for the Part 2 verdict. Part 2 outline (same hallway, same one character): she resumes the footage with timestamps, sees the figure hang a coat and stay to straighten it, pauses on a clear frame and taps the clipboard once; 'Identified.' She locks the phone, then hangs her own spare coat on the loaded hook.",
        "structure": "Screen-within-screen playback with a delayed ID; dependent on a legible phone screen.",
        "why_send_it": "For the friend who 'swears they never touch it': proof by footage, a screenshot-able frame.",
        "commercial_fit": "A phone screen could carry UI marks that must stay generic; avoid.",
        "rejected_because": "the phone is a small-detail reading problem and its phone-footage mechanic echoes the earlier device-led episodes."
      },
      {
        "id": "P4",
        "logline": "Tagged out: the Inspector puts safety-orange tape tags on the sagging hook as an exhibit, and as she turns, a focus pull reveals each of the four empty hooks wears her own 'Out of Service' tag.",
        "audience_emotion": "A clean visual surprise followed by affectionate disappointment.",
        "character_desire": "To protect the overloaded hook as a scene and to reinstate order.",
        "obstacle": "She cannot reach a verdict while the evidence, the heap, is still on the hook.",
        "escalation": "She photographs nothing but tapes a cordon and states hook ratings one by one; each rating is delivered more formally.",
        "surprise": "Last 4 s: rack focus from her face to the rail behind her: four empty hooks, each with a neat orange tag. She does not react.",
        "payoff": "Part 1 ends on the rack focus. The two-finger tap is saved for Part 2 and is not used in Part 1. Part 2 outline: she reads the tags, recognises her tape, removes them one at a time, and hangs a coat on each freed hook, but she taps the clipboard once and re-tags hook five.",
        "structure": "Procedural audit ending on a focus-pull reveal; close to existing tagging gags.",
        "why_send_it": "For the tidy person who 'protects' a shared space until nobody can use it.",
        "commercial_fit": "None.",
        "rejected_because": "orange tape tagging of a fault repeats the earlier episode's tag-the-evidence skeleton."
      },
      {
        "id": "P5",
        "logline": "Reach: she discovers the four empty hooks sit above head height, measures the rail against herself, and the only hook within her reach is the overloaded one.",
        "audience_emotion": "Warm recognition; a quiet 'oh' rather than a laugh.",
        "character_desire": "To explain why one hook carries everything.",
        "obstacle": "She cannot see a fault in the hook itself and must account for the other four.",
        "escalation": "She measures each hook's height with a tape; only hook five is within her reach, while she stands on tiptoe at the others.",
        "surprise": "Last 4 s: wide shot beside the rail shows a column of pencil height marks, each one at her shoulder; she does not react.",
        "payoff": "Part 1 ends unresolved. The two-finger tap is not used in Part 1 and is saved for Part 2, which resolves with the verdict.",
        "structure": "Spatial measurement gag resolved by a wide comparison; quiet and static.",
        "why_send_it": "To the shortest person in the house.",
        "commercial_fit": "None.",
        "rejected_because": "the reach logic, once explained, is weaker as a cliffhanger because the viewer has no unresolved question left."
      }
    ],
    "ranking": [
      "P1",
      "P2",
      "P3",
      "P4",
      "P5"
    ],
    "ranking_rationale": "P1 gives the cleanest stand-alone short: a wide, deadpan stakeout, a time-lapse escalation that reads on mute, and a last-4-second reverse angle in which the camera sees the culprit before she does, with the tap honestly saved for a Part 2 verdict that needs no new character or location. P2 has the strongest single image but is harder to stage within the no-fine-handwork limit. P3 and P4 lean on devices or gags the earlier episodes already used, and P5 resolves too quickly to sustain a cliffhanger."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Locked-off wide, eye-level, blue hour: cool daylight through one frosted door panel, a hallway rail with four empty hooks and a fifth bowed hard under a tall coat heap; the Inspector stands square to it, chest lamp beam pinned on the sagging hook.",
        "first_line_or_action": "She lifts the clipboard, makes one flat tick, and says: 'No movement.' while the rail gives a one-notch-exaggerated creak.",
        "mechanism": "visible_problem",
        "score": 9,
        "rationale": "One glance shows four empty hooks beside one buckling hook, and her calm 'No movement' over a visibly moving problem sets the stakeout joke and the rule in under a second (legibility 3, specificity 3, promise 2, send-ability 1)."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Medium-wide on the rail from slightly low: the fifth hook visibly bent under the heap in blue light, the four bare hooks sharp in the foreground, the Inspector soft and still at the edge of frame.",
        "first_line_or_action": "Her lamp beam sweeps along the four empty hooks one by one, a click on each, then drops onto the heap; she says: 'Four vacant. One overdrawn.'",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "The four-versus-one count is shown by the beam sweep and reads on mute, but the inspector's presence is less immediate in the first frame (legibility 2, specificity 3, promise 1, send-ability 2)."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "The same locked-off wide as the stakeout, the Inspector motionless with lamp on, the heap already knee-high on the fifth hook and the other four bare.",
        "first_line_or_action": "Hard jump cut: she has not moved, the heap is visibly taller, and she says the same two words, 'No movement.', as the clipboard scratches once.",
        "mechanism": "escalating_ritual",
        "score": 8,
        "rationale": "The repeated identical pose against a growing heap reads on mute and promises the camera-knows-first rule, though the ritual pays off after the first second (legibility 2, specificity 2, promise 2, send-ability 2)."
      },
      {
        "id": "H4",
        "premise_id": "P2",
        "first_frame": "Medium shot, the Inspector crouched beside the sagging heap, lamp on a faint smudge on the wall at her own shoulder height, clipboard held with a half-drawn oval visible.",
        "first_line_or_action": "She traces the smudge height with one slow lamp pass and says: 'Right-handed. Short. Composed.'",
        "mechanism": "curiosity_gap",
        "score": 6,
        "rationale": "The profile-of-a-suspect idea is intriguing and sendable, but the half-drawn oval and smudge are small details that need a beat to read in a wide or medium shot (legibility 1, specificity 2, promise 1, send-ability 2)."
      },
      {
        "id": "H5",
        "premise_id": "P2",
        "first_frame": "Medium shot beside the heap: the Inspector holds the clipboard sketch up next to it, the drawn face showing a low bun, straight brows and round glasses, while her own face stays turned toward the heap in soft profile.",
        "first_line_or_action": "She holds the sketch against the heap for comparison and says one flat word: 'Distinctive.'",
        "mechanism": "recognition",
        "score": 7,
        "rationale": "The sketch-beside-the-face match is a strong, screenshot-able still that reads as 'that is her' on mute, but it spends the cliffhanger in the first frame and needs a legible small drawing (legibility 2, specificity 2, promise 2, send-ability 1)."
      },
      {
        "id": "H6",
        "premise_id": "P2",
        "first_frame": "Wide, blue hour, the Inspector facing the four empty hooks like a row of witnesses, the heavily loaded fifth hook beside her, lamp beam level and steady.",
        "first_line_or_action": "She addresses the empty hooks in a level voice, 'Which of you did this?', then waits, still, for an answer that does not come.",
        "mechanism": "callout",
        "score": 5,
        "rationale": "The deadpan interrogation of hooks is funny and sendable to a flatmate, but the problem is stated rather than shown and the line adds little to the premise's sketch payoff (legibility 2, specificity 1, promise 0, send-ability 2)."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "H1 shows the whole problem (four bare hooks, one buckling hook) in a single wide frame and sets the deadpan 'No movement' register that the final low-angle reveal inverts, so it reads on mute and sets up the camera-knows-first rule without any new prop or person. The trade-off against the runner-up (P2 with H5) is that H5 gives the more striking single image, a sketch matching her face, but it gives away the cliffhanger early and relies on a small legible drawing that is harder to stage in the no-fine-handwork wide shot; the clipboard tap stays unused in Part 1 and is saved for the Part 2 verdict."
    }
  }
}

## Rules
- Scenes tile [0, duration_target_s] exactly: first start_s = 0, each start_s = previous end_s, last end_s = target.
- Each scene: location, action, performance (an invested task, not an emotion adjective), microexpression, camera {shot, lens, movement, rig}, lighting (key direction + colour bounce + contact shadows), environment, sound {ambience, foley[], music, voice}, transition_out, props_from_frame_one, cuts_inside_clip (0 or 1), generation_unit (which clip this belongs to; clips are 4-30 s).
- One on-camera speaker per scene at most; a second voice is off-camera.
- Signature gesture at most once. The bible's rule must cause the payoff.
- Continuity: restate identity anchors verbatim from the bible; list every moving prop; costume per episode.
- No readable brand text, logos or real-app UI. No researched creator's identity markers.


- Dialogue lines fit their scene at <=2.8 words/s. Write for the ear: short lines, no thesis sentences.



## Craft rules (distilled from the content-engine and ugc-influencer-video skills; added after the 2026-10-07 bake-off)
- Hook earns the next second: the most specific word or image first; no warm-up.
- Camera alive, never "tripod": propped phone with one settle-wobble, handheld bob, or placement-open; angle changes come from the character, not cuts.
- Performance = an invested task (goal, obstacle, tactic) with eye-work as action; emotion adjectives are not direction.
- Lighting names key direction, fill, one colour bounce from a named surface and contact shadows; add a light-stability line if the light must not change.
- Audio names ambience plus 3-5 diegetic foley per scene; music none by default.
- The payoff must re-read the opening; the camera notices before the character does.


## Demonstrations
### Demonstration D1_silent_gag (silent_gag)
Input brief: A silent 12-second gag for a different show (a night-shift museum guard who salutes every object before moving it). Problem: one framed photo hangs crooked.
Accepted output (excerpt): {"scenes_excerpt": [{"scene_id": "S1", "start_s": 0, "end_s": 3.5, "action": "Guard enters frame-right already mid-salute to a crooked frame; torch beam lands on the tilt first, his face second.", "performance": "Invested task: assess the tilt like a structural fault; eyes travel the frame edge, not the camera.", "microexpression": "Single slow blink when the beam reaches the corner.", "camera": {"shot": "medium, eye level", "lens": "35mm feel, mild phone wide", "movement": "static propped phone with one settle-wobble", "rig": "phone propped on a radiator"}, "lighting": "Torch is the key from frame-right; cool corridor fill from a far window; warm bounce off the oak floor; hard contact shadow under the frame.", "sound": {"ambience": "empty corridor hum, distant HVAC", "foley": ["torch click", "two boot steps", "fabric creak of the salute"], "music": "none"}, "transition_out": "continuous"}, {"scene_id": "S3", "start_s": 9.0, "end_s": 12.0, "action": "He straightens the frame with two fingers, salutes it, steps back; the frame behind HIM is now crooked. He does not notice. Final pose matches frame one.", "microexpression": "Satisfied exhale through the nose.", "sound": {"ambience": "same hum", "foley": ["frame tick against wall", "single boot step"], "music": "none"}, "transition_out": "loop"}], "dialogue": [], "payoff": "The fix displaces the fault to where he cannot see it; the camera sees it first."}
Why it was accepted: Accepted because the gag is legible with no words: the problem is visible in frame one, the payoff is a visible displacement, the final pose loops, every scene has camera, lighting with bounce and contact shadows, ambience and foley, and no dialogue was invented for a silent brief.
Rejected alternative: A version where the guard mutters 'not on my watch' was rejected: it added speech to a silent brief and told the joke instead of showing it.

### Demonstration D2_spoken_tool_honesty (spoken_episode)
Input brief: An 18-second spoken episode for a different show (a weather presenter who forecasts social awkwardness). The production tool's JSON support is unverified.
Accepted output (excerpt): {"dialogue_excerpt": [{"speaker": "Presenter", "line": "Light small talk this morning, clearing by the lift.", "on_camera": true, "delivery": "brisk broadcast cadence, eyes to lens then to the 'map'"}, {"speaker": "Colleague", "line": "You're in my lift.", "on_camera": false, "delivery": "flat, close-mic, from behind camera"}], "tool_mapping_excerpt": {"adapter": "higgsfield-mcp/generate_video", "units": [{"generation_unit": "U1", "model": "seedance_2_5", "controls": {"duration": 18, "aspect_ratio": "9:16", "resolution": "720p", "generate_audio": true}, "prompt_text": "TOP PRIORITY ... (free-text house-order prompt)", "manual_steps": ["burn caption in edit", "platform disclosure if sponsored"], "gaps": ["lip-sync quality not controllable; inspect", "no fps control"]}], "notes": "Internal episode JSON is kept for the engine; the tool receives only prompt_text plus the listed native controls. The JSON is NOT a native tool payload."}}
Why it was accepted: Accepted because speech fits the timing (about 2.4 words per second), the second voice is off-camera, and the tool mapping names the free-text prompt as the only creative payload with manual steps and explicit gaps, instead of claiming the internal JSON executes natively.
Rejected alternative: A version that labelled the internal episode JSON as a 'native Higgsfield JSON payload' was rejected: JSON support is unverified and the model catalogue exposes prompt as a string.


## Output contract (JSON only)
{
  "script": {"title": "", "synopsis": "", "beats": [{"beat": "", "function": "hook|setup|escalation|turn|payoff|button|cta"}], "dialogue": [{"speaker": "", "line": "", "delivery": "", "on_camera": true}], "caption_text": "", "cta": "", "disclosure_line": ""},
  "scenes": [ {"scene_id": "S1", "start_s": 0, "end_s": 0, "location": "", "action": "", "performance": "", "microexpression": "", "dialogue": [], "camera": {"shot": "", "lens": "", "movement": "", "rig": ""}, "lighting": "", "environment": "", "sound": {"ambience": "", "foley": [], "music": "none", "voice": ""}, "captions": "", "transition_out": "", "props_from_frame_one": [], "cuts_inside_clip": 0, "generation_unit": "U1"} ],
  "continuity": {"identity_anchors": "", "costume": "", "props": [], "notes": ""},
  "asset_rights": [ {"asset": "", "kind": "character_reference|location_still|voice|music|driving_footage|product_image|font|other", "source": "", "rights_status": "owned|licensed|consented|unresolved|not_needed", "scope": ""} ],
  "export": {"aspect_ratio": "9:16", "resolution": "1080x1920", "fps": 30, "container": "mp4", "max_duration_s": 0, "edit_plan": [""], "disclosure_plan": [""]},
  "growth_hypotheses": [ {"hypothesis": "", "metric": "", "falsifier": ""} ],
  "evidence": [ {"claim": "", "kind": "fact|inference|hypothesis", "source": "", "confidence": "low|medium|high"} ]
}
Self-check before answering: timings tile exactly; every scene has camera.shot/lens/movement and sound.ambience; props used appear in continuity.props; speech rate; one cut max; silent means no dialogue.
