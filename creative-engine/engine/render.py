"""Human-readable script + storyboard rendering (usable without parsing JSON)."""
from __future__ import annotations


def storyboard_md(packet: dict) -> str:
    b, sc = packet["brief"], packet["script"]
    sel = packet["selected"]
    prem = next((p for p in packet["premises"] if p["id"] == sel["premise_id"]), {})
    hook = next((h for h in packet["hook_variants"] if h["id"] == sel["hook_id"]), {})
    L = [f"# {sc['title']}", "", f"**Status:** {packet['status']}  ", f"**Brief:** {b['brief_id']} - {b['title']}  ",
         f"**Format / platform / target:** {b['format']} / {b['platform']} / {b['duration_target_s']} s  ",
         f"**Bible:** {packet['bible_version']['bible_id']} v{packet['bible_version']['version']}  ", "",
         "## Premise", prem.get("logline", ""), "",
         f"- Audience emotion: {prem.get('audience_emotion')}", f"- Character desire: {prem.get('character_desire')}",
         f"- Obstacle: {prem.get('obstacle')}", f"- Escalation: {prem.get('escalation')}", f"- Surprise: {prem.get('surprise')}",
         f"- Payoff: {prem.get('payoff')}", f"- Why someone sends it: {prem.get('why_send_it')}", "",
         "## Hook", f"First frame: {hook.get('first_frame')}  ", f"First line/action: {hook.get('first_line_or_action')}  ",
         f"Mechanism: {hook.get('mechanism')} (score {hook.get('score')})  ", "",
         "## Alternatives considered"]
    for p in packet["premises"]:
        mark = "**SELECTED**" if p["id"] == sel["premise_id"] else (p.get("rejected_because") or "not selected")
        L.append(f"- {p['id']}: {p['logline']} - {mark}")
    L += ["", "## Script", sc.get("synopsis", ""), ""]
    for bt in sc["beats"]:
        L.append(f"- [{bt['function']}] {bt['beat']}")
    if sc.get("dialogue"):
        L += ["", "### Dialogue"]
        for d in sc["dialogue"]:
            L.append(f"- **{d['speaker']}**{'' if d.get('on_camera', True) else ' (off-camera)'}: \"{d['line']}\"" + (f" _({d['delivery']})_" if d.get("delivery") else ""))
    if sc.get("caption_text"):
        L.append(f"\nCaption: {sc['caption_text']}")
    if sc.get("disclosure_line"):
        L.append(f"\nDisclosure: {sc['disclosure_line']}")
    L += ["", "## Timed storyboard", "", "| t (s) | Scene | Action | Performance / micro-expression | Camera | Lighting | Sound | Out |", "|---|---|---|---|---|---|---|---|"]
    for s in sorted(packet["scenes"], key=lambda x: x["start_s"]):
        cam = s["camera"]; snd = s["sound"]
        dlg = " ".join(f"\"{d['line']}\"" for d in s.get("dialogue", []) or [])
        L.append(f"| {s['start_s']:.1f}-{s['end_s']:.1f} | {s['scene_id']} @ {s['location']} | {s['action']} {dlg} | {s['performance']} / {s['microexpression']} | "
                 f"{cam['shot']}, {cam['lens']}, {cam['movement']} | {s['lighting']} | amb: {snd['ambience']}; foley: {', '.join(snd.get('foley', []))}"
                 + (f"; music: {snd['music']}" if snd.get('music') else "") + f" | {s['transition_out']} |")
    c = packet["continuity"]
    L += ["", "## Continuity", f"- Identity anchors: {c['identity_anchors']}", f"- Costume: {c['costume']}", f"- Props from frame one: {', '.join(c['props'])}", f"- Notes: {c['notes']}",
          "", "## Rights and approval checklist"]
    for r in packet["asset_rights"]:
        L.append(f"- [{'x' if r['rights_status'] in ('owned', 'licensed', 'consented', 'not_needed') else ' '}] {r['kind']}: {r['asset']} - {r['rights_status']} ({r.get('scope', '')})")
    ap = packet["approval"]
    L.append(f"- [{'x' if ap['render_approved'] else ' '}] Render approved (cap: {ap.get('credit_cap')})")
    L.append(f"- [{'x' if ap['spend_approved'] else ' '}] Spend approved")
    L.append(f"- [{'x' if ap['publish_approved'] else ' '}] Publish approved")
    for d in packet["export"].get("disclosure_plan", []):
        L.append(f"- Disclosure: {d}")
    L += ["", "## Tool mapping (dry run)"]
    for u in packet["tool_mapping"]["units"]:
        L.append(f"- {u['generation_unit']} -> {u['model']} scenes {', '.join(u['scene_ids'])}; controls {u['controls']}; est. credits {u.get('estimated_credits')} ({u.get('quote_source', '')})")
        for g in u["gaps"]:
            L.append(f"  - gap: {g}")
    L += ["", "## Export plan"] + [f"- {e}" for e in packet["export"]["edit_plan"]]
    if packet.get("growth_hypotheses"):
        L += ["", "## Growth hypotheses (testable, not predictions)"]
        for g in packet["growth_hypotheses"]:
            L.append(f"- {g['hypothesis']} - metric: {g['metric']} - falsifier: {g['falsifier']}")
    q = packet["qa"]
    L += ["", "## QA", f"- Deterministic: {'PASS' if q['deterministic'].get('ok') else 'FAIL'} ({q['deterministic'].get('error_count', '?')} errors, {q['deterministic'].get('warning_count', '?')} warnings)",
          f"- Repetition check: {q['repetition'].get('verdict', 'n/a')} flagged={q['repetition'].get('flagged_fields', [])}",
          f"- Creative review: {q['creative'].get('summary', 'pending')}",
          "", f"_Provenance: provider={packet['provenance']['provider']}, requested_model={packet['provenance']['requested_model']}, observed_model={packet['provenance']['observed_model']}, demos={packet['provenance']['demonstrations_used']}_",
          "", f"**{packet['status'].upper()}**"]
    return "\n".join(L)
