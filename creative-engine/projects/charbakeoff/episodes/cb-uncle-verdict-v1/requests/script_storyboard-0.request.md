<!-- requested_model: sonnet; effort: medium; tag: script_storyboard-0 -->

# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{
  "brief_id": "CB1_intro_uncle-verdict-v1",
  "title": "Character bake-off intro: 12-second first public appearance of uncle-verdict-v1",
  "project": "charbakeoff",
  "bible_ref": "uncle-verdict-v1",
  "format": "other",
  "platform": "tiktok",
  "duration_target_s": 12,
  "language": "English or none - the engine decides with the audio mode",
  "objective": "Introduce the character to a cold viewer in 12 seconds in a public setting so that the character's energy, rule and silhouette are legible muted; make the viewer want to see the next one. This is a bake-off: the same brief runs for three characters and the owner compares the rendered tests.",
  "constraints": [
    "Public setting from the bible's recurring locations; generic blurred passers-by allowed, never the joke.",
    "Render tier: draft_mini (one 12 s Seedance 2.0 Mini unit, <=15 s, one generation unit, at most one cut) - this is a cost-capped test render.",
    "The bible rule must land inside 12 seconds; the signature gesture may be used once.",
    "Any dance or move is original and fully described; no trending dance or sound."
  ],
  "production_format": {},
  "commercial": null,
  "render_tier": "draft_mini",
  "negative_constraints": [
    "Do not copy any researched creator's look, catchphrase or footage.",
    "No readable brand text in frame.",
    "No real people or recognisable locations."
  ]
}
## Bible
{
  "bible_id": "uncle-verdict-v1",
  "version": 1,
  "show_title": "Uncle Verdict (working title; name/IP uncleared)",
  "logline": "A serene 55-year-old man in a mustard suit sets up a plastic chair in public places and rates everyday things with total confidence and total wrongness, and when the world proves him wrong in front of him, he doubles down.",
  "character": {
    "name": "Uncle Verdict",
    "age_range": "52-58",
    "sex_presentation": "man",
    "silhouette": "Mustard-yellow three-piece suit slightly too big, open collar, a folding white plastic garden chair he carries everywhere, a large wooden scoring paddle with a dial from 0 to 10, brown leather loafers with no socks.",
    "identity_anchors": "Round soft face, heavy-lidded calm eyes, neat salt-and-pepper beard trimmed short, bald shining crown with a ring of grey hair, slow blink, serene half-smile that never changes.",
    "hair": "bald crown with a short ring of grey hair, neat short salt-and-pepper beard",
    "lower_body": "mustard suit trousers slightly too long, brown leather loafers, no socks",
    "desire": "To be the final authority on how things should be.",
    "flaw": "He is confidently wrong about everything measurable and immune to evidence.",
    "rule": "He rates an everyday thing on the paddle with serene certainty; the world shows the obvious truth in frame; he adjusts the dial further in the wrong direction and says 'Final.' The camera shows the evidence before he does.",
    "performance_register": "Seated stillness and calm; the loudness is in the opinion, not the voice; comedy from the gap between certainty and evidence; invites the viewer to argue.",
    "voice": "Slow, warm, certain; verdict format: '[Thing]. [Score] out of ten. Correct answer: [absurd alternative].' Never raises his voice.",
    "signature_gesture": "A slow turn of the paddle dial with one finger, then he holds the paddle up to the lens (once per episode)."
  },
  "world": {
    "recurring_locations": [
      "outside a corner shop on a pavement",
      "public park bench row",
      "laundrette window seat"
    ],
    "visual_language": "Locked-off phone at seated eye level, centred, like a portrait; mustard against grey; the evidence enters frame from an edge.",
    "sound_language": "Quiet street ambience; the paddle dial click exaggerated; no music."
  },
  "do_not": [
    "No bob/moustache/white-tunic combination or any researched creator's identity, catchphrase, costume or footage.",
    "No real people, no real brands, no religion, no politics, no mocking of strangers' bodies, accents, disabilities or faith; strangers in frame are generic extras who never become the joke.",
    "No trending dance or sound that is not cleared; any dance is an original move described in the storyboard.",
    "No firsthand product endorsements.",
    "Opinions are about objects, food, habits and everyday choices only; never about people, groups, places' inhabitants, beliefs or bodies."
  ],
  "evolution_policy": "The rated thing varies every episode; silhouette, rule, register and gesture are fixed until a versioned bump.",
  "provenance": {
    "created": "2026-10-08",
    "basis": "owner feedback 2026-10-08: reference accounts provoke argument; hypothesis C provokes argument about taste only, keeping platform and legal exposure low",
    "status": "hypothesis, untested",
    "saved_at": "2026-10-08T05:53:57Z",
    "bump_reason": "character bake-off hypothesis"
  },
  "audience": {
    "target": "global; wrong takes on universal objects (tea, toast, umbrellas); subtitle-ready",
    "language_default": "English when spoken; captions always"
  }
}
## Selected premise and hook
{
  "premises": {
    "premises": [
      {
        "id": "P1",
        "logline": "Outside a corner shop, Uncle Verdict unfolds his chair and scores a closed umbrella 2 out of 10; rain arrives from the top edge, a dry stranger's umbrella drifts past, and he turns the dial down to 1.",
        "audience_emotion": "Delighted exasperation: the viewer sees the rain before he admits it and itches to argue in the comments.",
        "character_desire": "To be the final authority on umbrellas, today.",
        "obstacle": "The rain and the plainly useful umbrella in the background contradict him in frame.",
        "escalation": "Verdict at 2, first drops on the paddle, a generic passer-by's open umbrella slides through the frame edge, dial goes lower to 1.",
        "surprise": "He does not move, shelter or blink; the rain lands on his bald crown and the serenity does not change.",
        "payoff": "He turns the dial with one finger, holds the paddle to the lens, and says: 'Umbrella. Two out of ten. Correct answer: a tiny roof for nobody.' Rain pours, a dry umbrella passes, he lowers the dial to 1: 'Final.'",
        "structure": "Rule-complete single beat: claim, evidence enters, doubling down, hold on the face.",
        "why_send_it": "Sent to the friend who always argues about umbrellas with the message 'this is you'; the wrong take invites a reply.",
        "commercial_fit": "None needed; no brands. Umbrellas are a universal object and suit sponsor-safe categories later.",
        "rejected_because": "",
        "production_format": {
          "shot_architecture": "single_take_static",
          "audio_mode": "on_camera_dialogue",
          "camera_style": "Locked-off phone at seated eye level, centred portrait; rain and the passing umbrella enter from the frame edges.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "The cleanest cold-viewer introduction: static portrait shows silhouette, the verdict format and the rule within one generation unit, with the quiet delivery doing the work."
        }
      },
      {
        "id": "P2",
        "logline": "In a laundrette window seat, Uncle Verdict scores a warm folded towel zero out of ten while a slow push-in reveals the dryer door swinging open and fresh towels spilling over his loafers.",
        "audience_emotion": "Cosy absurdity with a slow-burn laugh at the pile building up.",
        "character_desire": "To rule that towels are a failure.",
        "obstacle": "Warm, clean, plainly excellent towels keep arriving in frame.",
        "escalation": "Towel handed down from the edge, door pops, pile reaches his shoe, the dial already at 0 has nowhere lower so he taps the paddle itself as if the dial were broken.",
        "surprise": "He treats the dial's floor as the world's fault.",
        "payoff": "Voice-over: 'Towel. Zero out of ten. Correct answer: a sad flat blanket.' He turns the dial the wrong way, holds up the paddle, 'Final.'",
        "structure": "Slow reveal; the camera finds the evidence while the voice stays certain.",
        "why_send_it": "Sent to the flatmate who folds towels wrong, with the caption 'rate this'.",
        "commercial_fit": "Laundry categories are generic; no brand text in frame.",
        "rejected_because": "the dial floor makes the rule's wrong-direction step weaker than P1",
        "production_format": {
          "shot_architecture": "single_take_moving_camera",
          "audio_mode": "voiceover_narration",
          "camera_style": "Slow motivated push-in from window height to his face, steam and dryer drum glow as practical light.",
          "continuity_reuse": {
            "voice": "same",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Moves the show to a second recurring location and voice-over so mouth sync is not a risk in a cheap render; the push-in motivates the reveal."
        }
      },
      {
        "id": "P3",
        "logline": "On a park bench row, Uncle Verdict rates a paper cup of tea 10 out of 10 in a main shot; one cutaway insert shows the tea is cold with a leaf floating in it, and he turns the dial up to 10 anyway.",
        "audience_emotion": "Smug disbelief; the insert lets the viewer feel superior to him.",
        "character_desire": "To crown tea the best thing on earth.",
        "obstacle": "The insert shows still, cold, leaf-dotted tea.",
        "escalation": "Verdict 8, cut to insert, back to the main shot with 10.",
        "surprise": "The insert shows what the camera knows and he does not.",
        "payoff": "Text: 'Tea. Eight out of ten. Correct answer: warm water in a hurry.' After the insert he turns the dial up and holds up the paddle: 'Final.'",
        "structure": "Main shot plus insert (the one allowed cut); evidence before the character sees it.",
        "why_send_it": "Sent to the tea-obsessed sibling with 'you in a nutshell'.",
        "commercial_fit": "Tea is a universal object; no brand shown.",
        "rejected_because": "the insert spends the one cut and the caption-only delivery makes the character less warm than a spoken take",
        "production_format": {
          "shot_architecture": "split_or_insert",
          "audio_mode": "text_over_broll",
          "camera_style": "Locked medium main shot plus a single macro insert of the cup.",
          "continuity_reuse": {
            "voice": "none",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Silent text option tests whether the character reads without any voice; the insert proves the evidence-before-him rule visually."
        }
      },
      {
        "id": "P4",
        "logline": "Outside the corner shop, an unseen friend behind the phone asks Uncle Verdict about a banana; he scores it 4 out of 10, a hand from frame edge holds up a perfect one, and he lowers the dial to 2.",
        "audience_emotion": "Warm, conversational comedy; the viewer feels like the third person in the chat.",
        "character_desire": "To be asked, and to answer with authority.",
        "obstacle": "The friend's spotless banana contradicts the score.",
        "escalation": "Question, verdict, banana offered, verdict lowered.",
        "surprise": "The off-camera voice stays kind and never mocks him.",
        "payoff": "Friend: 'And the banana?' Uncle: 'Banana. Four out of ten. Correct answer: a yellow apology.' The banana is perfect; he turns the dial down to 2, holds the paddle to the lens: 'Final.'",
        "structure": "Question-and-answer exchange with a visible object as evidence.",
        "why_send_it": "Sent to a family member who has strong food opinions.",
        "commercial_fit": "Fruit is generic; no brand text.",
        "rejected_because": "off-camera voice dilutes the solo seated stillness and adds a second voice to a 12 s clip",
        "production_format": {
          "shot_architecture": "interview_offcamera",
          "audio_mode": "off_camera_dialogue",
          "camera_style": "Handheld phone at seated eye level, held by the friend, with slight settle; the friend's hand enters from an edge.",
          "continuity_reuse": {
            "voice": "same",
            "location": "same",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "Adds a relationship and a second voice to test whether the character holds a two-person beat in one cheap unit."
        }
      },
      {
        "id": "P5",
        "logline": "Silent loop in a laundrette window seat: a leaf blows past, Uncle Verdict dials a verdict on the leaf, and the clip ends on the same empty-chair pose it opened with.",
        "audience_emotion": "Hypnotic calm; the loop invites a second watch.",
        "character_desire": "To rate even a leaf.",
        "obstacle": "The leaf keeps coming back and he keeps reappraising it.",
        "escalation": "Dial moves one notch each pass until the loop closes.",
        "surprise": "The last frame equals the first, so the verdict starts again.",
        "payoff": "He turns the dial, holds the paddle to the lens in silence, and the frame returns to where it began.",
        "structure": "Loop with a repeated beat and no words.",
        "why_send_it": "Sent to a friend as a mood clip.",
        "commercial_fit": "None.",
        "rejected_because": "silence leaves the verdict format and the wrongness illegible to a cold viewer",
        "production_format": {
          "shot_architecture": "loop",
          "audio_mode": "silent_ambience",
          "camera_style": "Locked-off window-seat portrait; first and last frames identical.",
          "continuity_reuse": {
            "voice": "none",
            "location": "new",
            "costume": "same"
          },
          "trend_refs": [],
          "rationale": "A silent loop tests the silhouette and the dial click alone, but the rule is hard to land without the spoken verdict."
        }
      }
    ],
    "ranking": [
      "P1",
      "P4",
      "P2",
      "P3",
      "P5"
    ],
    "ranking_rationale": "P1 lands the full bible rule (claim, evidence entering from the edge, a lower wrong dial, 'Final.') in one locked take, so a cold viewer meets silhouette, voice and rule muted or with sound. P4 and P2 add relationship and location variety but each dilutes the solo stillness or the rule. P3 and P5 trade the spoken verdict for caption or silence and are the least legible as a first appearance."
  },
  "hooks": {
    "hook_variants": [
      {
        "id": "H1",
        "premise_id": "P1",
        "first_frame": "Locked-off seated-eye-level portrait outside a grey corner shop: Uncle Verdict centred in the mustard three-piece on the white plastic chair, serene half-smile, holding the wooden paddle with the dial already pointing at 2, a closed umbrella across his knees, a thin grey rain edge visible at the top of frame.",
        "first_line_or_action": "He turns the dial with one finger (exaggerated click) and holds the paddle to the lens; caption and voice: 'Umbrella. Two out of ten.'",
        "mechanism": "status_contradiction",
        "score": 9,
        "rationale": "The mustard silhouette, paddle reading 2 and closed umbrella read in one second muted, and the dark sky promises the contradiction, so anyone with an umbrella argument will want to send it."
      },
      {
        "id": "H2",
        "premise_id": "P1",
        "first_frame": "Tight on the paddle held up to the lens with the dial at 2 and a single wet drop landing on the wood, Uncle Verdict's calm half-smile soft-focus behind it, the closed umbrella resting on his knee.",
        "first_line_or_action": "A second drop hits his bald crown and he does not blink; the dial clicks down one notch toward 1 while the caption reads 'Umbrella: 2/10'.",
        "mechanism": "visible_problem",
        "score": 8,
        "rationale": "The rain on the paddle and his unmoved face make the problem concrete in the first frame, though the tighter crop shows less of the silhouette than a full portrait."
      },
      {
        "id": "H3",
        "premise_id": "P1",
        "first_frame": "Full portrait: the white plastic chair unfolded alone on the pavement outside the corner shop, empty, with the mustard-suited man's loafers just entering frame as he carries the paddle in.",
        "first_line_or_action": "He sits, settles the paddle on his knee and slowly lifts a closed umbrella; caption: 'Rating things. Correctly.'",
        "mechanism": "curiosity_gap",
        "score": 6,
        "rationale": "The empty chair and the deliberate sit-down are a curious setup, but the wrong take is not visible yet, so it is slower to read and less likely to be sent."
      },
      {
        "id": "H4",
        "premise_id": "P4",
        "first_frame": "Slightly handheld seated-eye-level shot outside the corner shop: Uncle Verdict on the white chair in mustard, paddle dial at 4, looking calmly just past the lens; a hand enters from the right edge holding a perfect, unmarked banana.",
        "first_line_or_action": "He eyes the banana and says, slow and warm, 'Banana. Four out of ten.' while a finger rests on the dial.",
        "mechanism": "status_contradiction",
        "score": 8,
        "rationale": "The perfect banana against a 4 shows the wrongness instantly and is easy to send to a friend with strong food opinions, but the second hand adds clutter to the stillness."
      },
      {
        "id": "H5",
        "premise_id": "P4",
        "first_frame": "Close seated portrait of Uncle Verdict with a caption 'Rate the banana' across the lower third, the paddle dial at 4 visible, the white chair edge in frame, and a yellow blur at the right edge.",
        "first_line_or_action": "He gives one slow blink, then turns the dial a notch down with one finger as the banana comes fully into view.",
        "mechanism": "callout",
        "score": 7,
        "rationale": "The caption invites the viewer to take part and the slow blink shows his calm, but the banana is only a blur so the proof arrives half a beat late."
      },
      {
        "id": "H6",
        "premise_id": "P4",
        "first_frame": "Wide locked shot of the corner-shop pavement: the white chair, Uncle Verdict in mustard with the paddle at his side, and a tilted banana hanging into frame from the top edge.",
        "first_line_or_action": "He raises the paddle to the lens without a word, the dial reading 2, and the caption lands: 'Banana. Final.'",
        "mechanism": "curiosity_gap",
        "score": 6,
        "rationale": "Starting at the verdict makes a strong image, but it skips the setup, so the wrongness is harder to read cold and the rule feels rushed."
      }
    ],
    "selected": {
      "premise_id": "P1",
      "hook_id": "H1",
      "rationale": "H1 shows the full silhouette, the dial at 2, the umbrella and the rain edge in the first frame, so the rule and the coming contradiction read muted in about one second, and the on_camera_dialogue / single_take_static pair is not in the recent list. The trade-off against the runner-up (P4 with H4) is that the banana hook has a cleaner single prop but adds a second hand and a more handheld frame that dilutes the seated stillness."
    }
  },
  "production_format": {
    "shot_architecture": "single_take_static",
    "audio_mode": "on_camera_dialogue",
    "camera_style": "Locked-off phone at seated eye level, centred portrait; rain and the passing umbrella enter from the frame edges.",
    "continuity_reuse": {
      "voice": "same",
      "location": "same",
      "costume": "same"
    },
    "trend_refs": [],
    "rationale": "The cleanest cold-viewer introduction: static portrait shows silhouette, the verdict format and the rule within one generation unit, with the quiet delivery doing the work."
  }
}

## Production format to realise (declared by the selected premise; the validator checks it)
{
  "shot_architecture": "single_take_static",
  "audio_mode": "on_camera_dialogue",
  "camera_style": "Locked-off phone at seated eye level, centred portrait; rain and the passing umbrella enter from the frame edges.",
  "continuity_reuse": {
    "voice": "same",
    "location": "same",
    "costume": "same"
  },
  "trend_refs": [],
  "rationale": "The cleanest cold-viewer introduction: static portrait shows silhouette, the verdict format and the rule within one generation unit, with the quiet delivery doing the work."
}
Realisation rules: single-take architectures = no cuts and one generation unit (<=30 s) with the camera move written into every scene's camera.movement; multi_scene_cut = hard cuts between scenes, each scene its own unit; jump_cut_timelapse = >=3 jump cuts, same framing, visible accumulation; loop = last transition_out says "loop"; silent_ambience / text_over_broll = empty dialogue (text_over needs caption_text); voiceover_narration = speaker "VO" lines with on_camera false; off_camera_dialogue = at least one on_camera:false line; music_driven = name the licensed/owned cue in sound.music and declare a music asset; continuity_reuse voice/location "same" = declare the voice / location_still assets from the bible's approved_assets by asset_id.

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
