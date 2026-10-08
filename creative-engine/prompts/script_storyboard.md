# Stage 3 - Script and complete timed audiovisual storyboard

Your responsibility: turn the selected premise and hook into a shootable script and a timed storyboard that a generation tool can be prompted from. Every scene needs complete direction. The deterministic validator will reject gaps, overlaps, missing camera/audio, >1 cut per clip, infeasible speech (>3.3 words/s), undeclared props, and total duration off target by more than max(1 s, 10%).

## Brief
{{BRIEF}}
## Bible
{{BIBLE}}
## Selected premise and hook
{{CONTEXT}}

## Production format to realise (declared by the selected premise; the validator checks it)
{{FORMAT_SELECTED}}
Realisation rules: single-take architectures = no cuts and one generation unit (<=30 s) with the camera move written into every scene's camera.movement; multi_scene_cut = hard cuts between scenes, each scene its own unit; jump_cut_timelapse = >=3 jump cuts, same framing, visible accumulation; loop = last transition_out says "loop"; silent_ambience / text_over_broll = empty dialogue (text_over needs caption_text); voiceover_narration = speaker "VO" lines with on_camera false; off_camera_dialogue = at least one on_camera:false line; music_driven = name the licensed/owned cue in sound.music and declare a music asset; continuity_reuse voice/location "same" = declare the voice / location_still assets from the bible's approved_assets by asset_id.

## Rules
- Scenes tile [0, duration_target_s] exactly: first start_s = 0, each start_s = previous end_s, last end_s = target.
- PHYSICS CONTRACT (added 2026-10-08 after rendered tests showed floating props and a whistle hovering in an open mouth): each scene carries ONE `physical_beat` sentence (<=40 words) stating who moves what, with which hand, the contact point (grip, palm, lap, strap, surface), what holds still, AND any world event the joke depends on (rain starts, a light changes, a stranger passes). The render prompt sends only this beat plus dialogue, so anything missing from it will not be rendered. Rules: two hands, so at most two held objects per beat, everything else rests on a strap, lap or surface; an object in the mouth means no speech and no open grin in that beat (put the whistle on its cord before the line); one main physical action per 3 seconds; describe the chain cause -> movement -> contact -> consequence, never an acting label; say what stays still. Dense multi-action beats are where cheap models drift.
- HAND-OBJECT INTERACTION (products will be reviewed, unboxed and tried on, so interaction is staged, never avoided): at most two hands act and each is named ("right hand lifts the lid, left hand steadies the box on the table"); the free hand is parked somewhere specific; every object is either held or resting on a named surface, never floating beside busy hands; one interaction per scene (one press, one lift, one twist), no repetition words (again, twice, repeatedly, back and forth); every scene opens mid-action; when the hand-object moment is the point (turning a dial, opening a lid, peeling a seal, pressing a pump), SHOW it: give it its own scene of at least 3 s, framed closer (medium close-up, object and face in frame), and fill scene.interaction {actor_hand, contact (exact fingertip/palm and the exact spot on the part), object, part, from_state, to_state, motion (path, direction, slow, pivot), support_hand (what the other hand does)}; the engine animates it between a start keyframe and an end keyframe the owner inspects first, and its props come from the bible's exact prop design; only incidental state changes go across a hard cut (state A, cut, scene starts in state B with state_change_by_cut: true); grip matches weight (heavy = both hands, visible effort; light = one relaxed hand; tiny = thumb and index); exactly one of each product, front label side only, never rotated or spun; no mirrors or reflections; try-on never shows dressing: hard cut to already wearing it, fabric moves only from the body (turn, breath, step), hands off the garment in close-ups.
- AUDIO MODE AND SOUNDTRACK: a silent clip may still carry a custom soundtrack. For music_driven, fill production_format.soundtrack {source: custom|licensed|owned|platform_library, title, rights_status, bpm and/or beat_times_s, cue_length_s} and write each physical_beat so its main motion lands on a listed beat time; there is no on-camera speech (lines become captions or VO). For voiceover_narration nobody on screen speaks and lips stay closed. The video model never generates music; the track is laid in the edit.
- Each scene: physical_beat, location, action, performance (an invested task, not an emotion adjective), microexpression, camera {shot, lens, movement, rig}, lighting (key direction + colour bounce + contact shadows), environment, sound {ambience, foley[], music, voice}, transition_out, props_from_frame_one, cuts_inside_clip (0 or 1), interaction (only for a shown hand-object move, see above), generation_unit (which clip this belongs to; clips are 4-30 s).
- One on-camera speaker per scene at most; a second voice is off-camera.
- Signature gesture at most once. The bible's rule must cause the payoff.
- Continuity: restate identity anchors verbatim from the bible; list every moving prop; costume per episode.
- No readable brand text, logos or real-app UI. No researched creator's identity markers.
<<IF SILENT>>
- Silent gag: dialogue arrays must be empty. Use timed action, facial performance, camera, ambience, a reveal, and a loop-friendly final pose.
<<ENDIF SILENT>>
<<IF SPOKEN>>
- Dialogue lines fit their scene at <=2.8 words/s. Write for the ear: short lines, no thesis sentences.
<<ENDIF SPOKEN>>
<<IF COMMERCIAL>>
- Commercial: product solves or escalates the story problem; include disclosure_line and a disclosure_plan entry; use only verified facts {{COMMERCIAL_FACTS}}; never imply the character used or benefited from it. Forbidden topics: {{FORBIDDEN}}.
<<ENDIF COMMERCIAL>>

## Craft rules (distilled from the content-engine and ugc-influencer-video skills; added after the 2026-10-07 bake-off)
- Hook earns the next second: the most specific word or image first; no warm-up.
- Camera alive, never "tripod" (owner 2026-10-08: "missing creative camera micro movement"): every scene's camera.movement names its micro-movement (breathing sway of a hand-held phone, phone resting on a knee that rises with a breath, small reframes that follow the eyes, a touch of focus breathing) plus at most one motivated move (slow creep-in during a claim, tilt to catch a reveal, whip reframe to the evidence, push-in or punch-in to a close-up). "Locked" or "static" alone is not direction.
- The punchline lands closer: before the final line, the camera reaches a tighter framing by a push-in or a hard cut to a close-up; the line is spoken in that close-up, after any hand action has stopped, followed by a held beat of silence.
- Performance = an invested task (goal, obstacle, tactic) with eye-work as action; emotion adjectives are not direction.
- Lighting names key direction, fill, one colour bounce from a named surface and contact shadows; add a light-stability line if the light must not change.
- Audio names ambience plus 3-5 diegetic foley per scene; music none by default.
- The payoff must re-read the opening; the camera notices before the character does.
<<IF COMMERCIAL>>
- disclosure_plan must include all three: the platform's paid-partnership/branded-content tool, a spoken or caption disclosure line, and the AI/fictional-character label.
<<ENDIF COMMERCIAL>>

## Demonstrations
{{DEMOS}}

## Output contract (JSON only)
{
  "script": {"title": "", "synopsis": "", "beats": [{"beat": "", "function": "hook|setup|escalation|turn|payoff|button|cta"}], "dialogue": [{"speaker": "", "line": "", "delivery": "", "on_camera": true}], "caption_text": "", "cta": "", "disclosure_line": ""},
  "scenes": [ {"scene_id": "S1", "start_s": 0, "end_s": 0, "physical_beat": "", "location": "", "action": "", "performance": "", "microexpression": "", "dialogue": [], "camera": {"shot": "", "lens": "", "movement": "", "rig": ""}, "lighting": "", "environment": "", "sound": {"ambience": "", "foley": [], "music": "none", "voice": ""}, "captions": "", "transition_out": "", "props_from_frame_one": [], "cuts_inside_clip": 0, "generation_unit": "U1"} ],
  "continuity": {"identity_anchors": "", "costume": "", "props": [], "notes": ""},
  "asset_rights": [ {"asset": "", "kind": "character_reference|location_still|voice|music|driving_footage|product_image|font|other", "source": "", "rights_status": "owned|licensed|consented|unresolved|not_needed", "scope": ""} ],
  "export": {"aspect_ratio": "9:16", "resolution": "1080x1920", "fps": 30, "container": "mp4", "max_duration_s": 0, "edit_plan": [""], "disclosure_plan": [""]},
  "growth_hypotheses": [ {"hypothesis": "", "metric": "", "falsifier": ""} ],
  "evidence": [ {"claim": "", "kind": "fact|inference|hypothesis", "source": "", "confidence": "low|medium|high"} ]
}
Self-check before answering: every scene has a physical_beat obeying the physics contract; timings tile exactly; every scene has camera.shot/lens/movement and sound.ambience; props used appear in continuity.props; speech rate; one cut max; silent means no dialogue.
