"""Production routing: which Higgsfield model for which job, with verified constraints, cost quotes and test status.

Catalogue verified read-only through the Higgsfield MCP server on 2026-10-07 (models_explore get/search/recommend) and
cost quotes via generate_video(get_cost=true) the same day. Quotes are not measured completed-output costs; retakes
multiply them. "status" tells the truth about what has actually been exercised:
  verified_controls   - parameters/roles read from the live catalogue
  recommended_untested - chosen on catalogue evidence; no output has been generated or inspected in this build
  gap                  - a capability the catalogue exposes but we cannot drive yet (e.g. control ids not retrieved)
"""
from __future__ import annotations

CATALOGUE = {
    # ---- images (reference assets) ----
    "nano_banana_pro": {"kind": "image", "res": ["1k", "2k", "4k"], "aspect": ["1:1", "3:2", "2:3", "4:3", "3:4", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        "roles": ["image_references"], "notes": "Google; 'ultimate quality, text and diagrams'; supports_unlim flag present; default 2k", "status": "verified_controls"},
    "nano_banana_2_1": {"kind": "image", "res": ["1k", "2k", "4k"], "aspect": ["auto", "1:1", "3:2", "2:3", "4:3", "3:4", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        "roles": ["image_references", "mask", "video_references"], "notes": "Google; image+video references, inpaint mask, thinking_level, seed. The 'NB 2' the owner wants tested; it is 2.1 in this catalogue", "status": "recommended_untested"},
    "cinematic_studio_2_5": {"kind": "image", "res": ["1k", "2k", "4k"], "aspect": ["1:1", "3:2", "2:3", "4:3", "3:4", "4:5", "5:4", "16:9", "9:16", "21:9"], "roles": ["image"], "notes": "Cinema Studio Image 2.5: cinematic stills; single image input", "status": "verified_controls"},
    # ---- video ----
    "seedance_2_5": {"kind": "video", "min_s": 4, "max_s": 30, "res": ["480p", "720p", "1080p"], "aspect": ["auto", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"],
                     "roles": ["start_image", "end_image", "image_references", "video_references", "audio_references"], "modes": ["t2v", "omni_reference", "video_edit", "video_extension"],
                     "extras": ["draft (480p, finalize within 7 days)", "bitrate_mode"], "status": "verified_controls"},
    "seedance_2_0_mini": {"kind": "video", "min_s": 4, "max_s": 15, "res": ["480p", "720p"], "aspect": ["auto", "16:9", "9:16", "4:3", "3:4", "1:1", "21:9"],
                          "roles": ["start_image", "end_image", "image_references", "video_references", "audio_references"], "extras": ["genre", "bitrate_mode", "unlim-capable"], "status": "verified_controls"},
    "cinematic_studio_video_4_0": {"kind": "video", "min_s": 4, "max_s": 30, "res": ["480p", "720p", "1080p"], "aspect": ["auto", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"],
                                   "roles": ["start_image", "end_image", "image_references", "video_references", "audio_references"], "modes": ["t2v", "omni_reference", "video_edit", "video_extension"],
                                   "extras": ["era_id", "camera_model_id", "camera_lens_id", "camera_aperture_id", "pacing_id", "genre_id", "light/light_id/light_custom", "color_palette"],
                                   "notes": "Cinema Studio 4.0: the only model exposing NATIVE camera-body/lens/aperture/lighting/pacing controls - but they take creative-control ids from a catalogue this build has not retrieved", "status": "gap"},
    "cinematic_studio_3_0": {"kind": "video", "min_s": 4, "max_s": 15, "res": ["480p", "720p", "1080p", "4k"], "aspect": ["auto", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"],
                             "roles": ["image", "start_image", "end_image"], "notes": "Cinema Studio Video 3.0: premium look, but no identity image_references role -> weaker character lock", "status": "verified_controls"},
    "cinematic_studio_video_v2": {"kind": "video", "min_s": 3, "max_s": 12, "res": [], "aspect": ["1:1", "4:3", "3:4", "16:9", "9:16"], "roles": ["image", "start_image", "end_image"],
                                  "extras": ["multi_shots + multi_prompt", "speedramp", "genre", "cfg_scale"], "notes": "native multi-shot planning inside one clip; no identity refs", "status": "verified_controls"},
    "kling3_0": {"kind": "video", "min_s": 3, "max_s": 15, "res": ["std", "pro", "4k"], "aspect": ["16:9", "9:16", "1:1"], "roles": ["start_image", "end_image"], "notes": "multi-shot, audio sync; no identity refs", "status": "verified_controls"},
    "hf_mult_motion_control": {"kind": "video", "min_s": 4, "max_s": 30, "res": ["480p", "720p", "1080p"], "aspect": [], "roles": ["image_references", "video_references"], "notes": "Genjutsu motion transfer; needs owned/licensed driving video", "status": "verified_controls"},
}

# generate_video(get_cost=true) on 2026-10-07, 9:16, 720p unless noted; credits
# 2026-10-08 get_cost preflights, 12 s, 9:16, audio on: seedance_2_0 fast 480p 12 / fast 720p 30 / std 720p 54;
# kling_o3_image_reference std 15; minimax_h3_max 768p 30; gemini_omni 720p 30 per 10 s (max 10 s);
# seedance_2_5 480p 36 (draft or not); cinematic_studio_video_4_0 omni_reference 480p 36 / 720p 84. Quotes, not quality claims.
QUOTES = {
    ("seedance_2_5", 16, "720p"): 112, ("seedance_2_5", 16, "480p-draft"): 48, ("seedance_2_0_mini", 15, "720p"): 15,
    ("seedance_2_0_mini", 8, "720p"): 8, ("seedance_2_5", 8, "720p"): 56,  # lab captures 2026-10-07 18:22 UTC
    ("cinematic_studio_video_4_0", 16, "720p"): 112, ("cinematic_studio_3_0", 15, "720p"): 75,
    # measured charges 2026-10-08 (five-model comparison, 12 s 9:16): CS4 480p 36, 720p 84 (quote); CS4 has no draft flag, its 480p is the test tier
    ("cinematic_studio_video_4_0", 12, "480p-draft"): 36, ("cinematic_studio_video_4_0", 12, "720p"): 84, ("seedance_2_5", 12, "480p-draft"): 36,
}
IMAGE_QUOTES = {("nano_banana_pro", "2k"): 2, ("nano_banana_2_1", "2k"): 2}  # generate_image(get_cost=true) 2026-10-07, 16:9


def quote_for(model: str, duration: int, res: str = "720p") -> int | None:
    """Nearest recorded quote scaled linearly by duration; None when no quote exists. Still a quote, not a cost."""
    cands = [(k, v) for k, v in QUOTES.items() if k[0] == model and k[2] == res]
    if not cands:
        return None
    (m, d, r), credits = min(cands, key=lambda kv: abs(kv[0][1] - duration))
    return int(round(credits * duration / d))


def route_video_unit(pf: dict, duration: float, audio_mode: str, has_driving_footage: bool, identity_critical: bool = True, budget_mode: bool = False, handles_props: bool = False,
                     interaction: bool = False) -> dict:
    """Pick a video model for one generation unit and explain it.
    Owner verdict 2026-10-08 on five models, one identical prompt (Uncle Verdict): Cinema Studio 4.0 best, Seedance 2.5 second;
    so identity-critical units up to 15 s go to Cinema Studio 4.0, with Seedance 2.5 as the fallback."""
    sa = (pf or {}).get("shot_architecture", "")
    silent = audio_mode in ("silent_ambience", "text_over_broll", "music_driven")
    if has_driving_footage or sa == "motion_transfer_owned_footage":
        return {"model": "hf_mult_motion_control", "mode": None, "generate_audio": False, "why": "owned/licensed driving footage declared: Genjutsu motion transfer keeps human timing", "status": "verified_controls",
                "fallback": "seedance_2_5 omni_reference if transfer artefacts are unacceptable"}
    if sa == "continuation_from_last_frame":
        return {"model": "seedance_2_5", "mode": "video_extension", "generate_audio": not silent, "why": "video_extension (forward) continues from the approved reference clip", "status": "recommended_untested", "fallback": "cinematic_studio_video_4_0 video_extension"}
    if interaction:
        return {"model": "cinematic_studio_video_4_0", "mode": "omni_reference", "generate_audio": not silent,
                "why": "shown hand-object interaction: animated between the approved start and end keyframes (start_image/end_image) with character and prop references; Cinema Studio 4.0 ranked first by the owner 2026-10-08 and again on the keyframed interaction test (job 77ecb61d)",
                "status": "verified_controls", "fallback": "seedance_2_5 omni_reference, draft 480p, same start/end frames (owner: far less realistic on the keyframed paddle push, 2026-10-08)", "optimisation": "test at 480p (3 credits/s measured); 720p quoted 7 credits/s"}
    if duration > 15:
        return {"model": "seedance_2_5", "mode": "omni_reference", "generate_audio": not silent, "why": f"{duration:.0f}s exceeds the 15 s mini/Cinema-3.0 ceiling; Seedance 2.5 keeps identity refs + native audio up to 30 s", "status": "verified_controls",
                "fallback": "cinematic_studio_video_4_0 omni_reference (same ranges; native lens/lighting controls once control ids are retrieved)",
                "optimisation": "draft=true at 480p first (quoted 48 vs 112 credits at 16 s), finalize the approved take at 1080p within 7 days"}
    if (budget_mode or silent) and not handles_props:  # Mini only for hands-free units (owner inspection 2026-10-08)
        return {"model": "seedance_2_0_mini", "mode": None, "generate_audio": not silent, "why": "<=15 s; identity refs supported; cheapest adequate (15 credits / 15 s / 720p quoted)", "status": "verified_controls",
                "fallback": "seedance_2_5 omni_reference if identity or physics fail on mini"}
    if identity_critical:
        return {"model": "cinematic_studio_video_4_0", "mode": "omni_reference", "generate_audio": not silent,
                "why": "identity-critical unit (dialogue or handled props): Cinema Studio 4.0 ranked first by the owner in the same-prompt comparison 2026-10-08; image + audio references, native audio",
                "status": "verified_controls", "fallback": "seedance_2_5 omni_reference (ranked second; draft 480p -> finalize 1080p)", "optimisation": "test at 480p (36 credits / 12 s measured), final at 720p (84 quoted)"}
    return {"model": "cinematic_studio_3_0", "mode": None, "generate_audio": not silent, "why": "premium cinematic look where the character is not in frame (inserts, establishing shots)", "status": "recommended_untested", "fallback": "seedance_2_5"}


def route_image_asset(kind: str, nb2_testing: bool = False) -> dict:
    """Reference assets: character sheet, location stills, product stills."""
    primary = "nano_banana_2_1" if nb2_testing else "nano_banana_pro"
    if kind == "character_reference":
        return {"model": primary, "controls": {"resolution": "2k", "aspect_ratio": "16:9"}, "why": "split-screen character sheet per Higgsfield character-sheet workflow (photoreal-unretouched preset); 16:9 for split-screen", "status": "recommended_untested" if nb2_testing else "verified_controls",
                "alternatives": ["nano_banana_2_1 (NB 2.1: image+video refs, inpaint - to be tested)", "soul_2 / soul_cast (Higgsfield identity models; different pipeline)"]}
    if kind == "location_still":
        return {"model": primary, "controls": {"resolution": "2k", "aspect_ratio": "9:16"}, "why": "empty lived-in location, no people, planned key light; reused across episodes for a consistent world", "status": "recommended_untested" if nb2_testing else "verified_controls",
                "alternatives": ["cinematic_studio_2_5 for dramatic establishing stills"]}
    if kind in ("prop_reference", "keyframe"):
        # Owner 2026-10-08: stills follow the recommended image model (NB Pro), not an ad-hoc pick; the first paddle board was made on
        # gpt_image_2_5 by mistake and is kept only as a comparison. NB 2 tested once on the same prompts (nb2_testing).
        return {"model": primary, "controls": {"resolution": "2k", "aspect_ratio": "3:4" if kind == "prop_reference" else "9:16"},
                "why": "prop reference (exact design, front view, no hands)" if kind == "prop_reference" else "keyframe board still: start/end frame for a shown interaction; end frame edits the start frame",
                "status": "recommended_untested" if nb2_testing else "verified_controls", "alternatives": ["nano_banana_2 (one-time test 2026-10-08)", "gpt_image_2_5 (first board, comparison only)"]}
    if kind == "product_image":
        return {"model": primary, "controls": {"resolution": "2k", "aspect_ratio": "1:1"}, "why": "generic product reference, no brand text", "status": "recommended_untested", "alternatives": ["product-photoshoot workflow"]}
    return {"model": primary, "controls": {"resolution": "2k", "aspect_ratio": "9:16"}, "why": "generic", "status": "recommended_untested", "alternatives": []}


def character_sheet_prompt(bible: dict) -> str:
    """Slot architecture from the Higgsfield character-sheet workflow (read 2026-10-07), filled from the bible. Original character only.
    Sex presentation, hair and lower-body wardrobe come from the bible (added 2026-10-08 for the character bake-off); defaults keep the inspector-v1 wording."""
    c = bible.get("character", {})
    sex = c.get("sex_presentation", "woman")
    person = {"woman": "female", "man": "male"}.get(sex, "")
    hair = c.get("hair", "hair in a tight low bun with a matte finish")
    lower = c.get("lower_body", "plain dark trousers, flat black work shoes")
    return (
        "Split-screen character sheet composition, left side a full-body shot of the character standing upright in a neutral straight standing pose facing the camera with both feet flat on the ground and arms relaxed at the sides, "
        f"full head-to-toe framing with the whole body and both feet visible, right side a tight close-up chest-up portrait of the same character, identical original {person} character on both sides, single subject only exactly one person with only the character in frame, "
        f"pure white seamless studio background, professional character sheet presentation, adult {sex} aged {c.get('age_range', '35-45')}, {c.get('identity_anchors', '')}, mature adult bone structure and facial proportions, not a youthful rounded babyface, "
        f"naturally muted catchlights, no oversized specular glare in the iris, eye color muted rather than glowing, {hair}, "
        "visible fine skin texture with natural pores, fine lines, subtle asymmetries and texture irregularities, natural minimal grooming, slight natural sheen rather than glossy retouched finish, no digital smoothing, no beauty filter, no AI-airbrushed look, matte-to-natural complexion, "
        f"balanced natural proportions, wearing {c.get('silhouette', '')}, {lower}, no jewellery, no bag, "
        "natural anatomy, high-end but unretouched commercial photography style, soft diffused studio lighting without harsh reflections, cinematic realism, clean white background, 4K quality, sharp focus on skin texture detail, "
        "single subject only, exactly one person, only the character in frame, no other people, no duplicate figures, no mannequin, no reflections, no props other than items worn or carried in the described silhouette, no furniture, no background objects, empty seamless studio, left panel standing full-body head-to-toe not cropped not sitting, right panel tight close-up not full body, "
        "no text, no watermark, no logos, no frame borders, no babyface, no plastic skin, original character that does not resemble any real person or existing copyrighted character"
    )


def location_still_prompt(label: str, bible: dict) -> str:
    vl = bible.get("world", {}).get("visual_language", "")
    return (f"Authentic candid iPhone photo of an empty {label}, no people, lived-in not staged, casual slightly imperfect framing, eye level, "
            f"{vl}, soft window daylight from one side already planned as the key light for a later video, mild HDR, true-to-life colors, subtle sensor grain, no retouching, "
            "no readable text, no brands, no logos, vertical 9:16 composition with calm upper third for captions")


def asset_requests(packet: dict, bible: dict, nb2_testing: bool = False) -> list[dict]:
    """Image generations the packet needs before any video unit (dry run; media ids filled after owner-approved generation)."""
    reqs = []
    seen = set()
    for r in packet.get("asset_rights", []):
        k = r.get("kind")
        if k == "character_reference" and "char" not in seen:
            route = route_image_asset("character_reference", nb2_testing)
            reqs.append({"asset_id": (bible.get("approved_assets", {}).get("character_reference") or {}).get("asset_id", "char-ref"), "kind": k, **route, "prompt_text": character_sheet_prompt(bible), "reuse": "approved once, reused every episode (continuity_reuse.costume=same unless bumped)"})
            seen.add("char")
        elif k == "location_still":
            label = r.get("asset", "location")
            if label in seen:
                continue
            route = route_image_asset("location_still", nb2_testing)
            reqs.append({"asset_id": f"loc-{label[:30].lower().replace(' ', '-')}", "kind": k, **route, "prompt_text": location_still_prompt(label, bible), "reuse": "approved once per recurring location; continuity_reuse.location=same reuses it"})
            seen.add(label)
        elif k == "product_image" and "product" not in seen:
            reqs.append({"asset_id": "product-ref", "kind": k, **route_image_asset("product_image", nb2_testing), "prompt_text": f"Plain generic {r.get('asset', 'product')} on a neutral surface, no brand text, soft daylight, 1:1", "reuse": "per advertiser"})
            seen.add("product")
    return reqs


def routing_table_markdown() -> str:
    rows = ["| Job | Model | Why | Status |", "|---|---|---|---|",
            "| Character reference sheet | nano_banana_pro (NB 2.1 to be tested) | 2k/4k, image refs, split-screen sheet recipe | verified controls / NB2.1 untested |",
            "| Location stills (reused per location) | nano_banana_pro | 9:16 2k empty lived-in scene with planned key light | verified controls |",
            "| Video <=15 s, silent or draft | seedance_2_0_mini | identity refs + audio, 15 credits/15 s quoted | verified controls |",
            "| Video with dialogue / identity-critical, <=30 s | seedance_2_5 omni_reference (480p draft -> 1080p finalize) | image + audio refs (voice lock), native audio; 112 credits/16 s/720p, draft 48 | verified controls |",
            "| Single take > 15 s | seedance_2_5 omni_reference | only identity-ref model besides Cinema 4.0 that reaches 30 s | verified controls |",
            "| Premium cinematic look, character off-frame | cinematic_studio_3_0 | 4k, premium; no identity refs | recommended, untested |",
            "| Native lens/lighting/pacing controls | cinematic_studio_video_4_0 | exposes camera_lens_id, light_custom, pacing_id... but needs control ids not retrieved | gap |",
            "| Multi-shot inside one clip | cinematic_studio_video_v2 (multi_shots) or kling3_0 | native shot planning; no identity refs -> use for inserts only | recommended, untested |",
            "| Owned footage re-cast | hf_mult_motion_control | Genjutsu; driving video + character refs | verified controls |",
            "| Continuation (part 2) | seedance_2_5 video_extension | extends an approved clip | recommended, untested |"]
    return "\n".join(rows)
