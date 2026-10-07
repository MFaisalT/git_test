"""Bake-off tooling: structural checks on A/B/C outputs, blind judge prompt assembly, aggregation.

Usage (from creative-engine/):
  python3 eval/bakeoff_tools.py structural
  python3 eval/bakeoff_tools.py judge        # writes eval/bakeoff_runs/judge-<brief>/request.md + mapping.json (shuffle seed recorded)
  python3 eval/bakeoff_tools.py aggregate    # reads judge responses, maps X/Y/Z back, writes results.json + results.md
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from engine.validators import Report, validate_direction, validate_timing  # noqa: E402

BRIEFS = ["B1_silent_gag", "B2_dialogue_episode", "B3_commercial"]
C_DIRS = {"B1_silent_gag": "c-b1-silent-gag", "B2_dialogue_episode": "c-b2-dialogue-episode", "B3_commercial": "c-b3-commercial"}
RUNS = os.path.join(HERE, "bakeoff_runs")
WEIGHTS = {"originality": .15, "hook": .15, "coherence": .15, "identity": .10, "audiovisual": .15, "feasibility": .10, "grounding": .08, "commercial_fit": .12}


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def outputs_for(brief):
    """Return {arch: plan-dict} in a comparable shape (premise, hook, script, scenes, continuity)."""
    out = {}
    for arch in ("A", "B"):
        r = load(os.path.join(RUNS, f"{arch}-{brief}", "response.json"))
        out[arch] = {"premise": r.get("selected_premise"), "hook": r.get("hook"), "script": r.get("script"), "scenes": r.get("scenes"), "continuity": r.get("continuity")}
    p = load(os.path.join(ROOT, "projects", "bakeoff", "episodes", C_DIRS[brief], "packet.json"))
    sel = p["selected"]
    prem = next(x for x in p["premises"] if x["id"] == sel["premise_id"]); hook = next(x for x in p["hook_variants"] if x["id"] == sel["hook_id"])
    out["C"] = {"premise": {k: prem[k] for k in ("logline", "audience_emotion", "character_desire", "obstacle", "escalation", "surprise", "payoff", "why_send_it")},
                "hook": {k: hook[k] for k in ("first_frame", "first_line_or_action", "mechanism")}, "script": p["script"], "scenes": p["scenes"], "continuity": p["continuity"]}
    return out


def structural():
    rows = []
    for brief in BRIEFS:
        b = load(os.path.join(HERE, "briefs", f"{brief}.json"))
        for arch, plan in outputs_for(brief).items():
            shell = {"brief": b, "scenes": plan["scenes"] or [], "script": plan["script"] or {}}
            rep = Report(); validate_timing(shell, rep); validate_direction(shell, rep)
            rows.append({"brief": brief, "arch": arch, "scenes": len(plan["scenes"] or []), "errors": len(rep.errors), "codes": sorted({f.code for f in rep.errors})})
    with open(os.path.join(RUNS, "structural.json"), "w") as fh:
        json.dump(rows, fh, indent=2)
    for r in rows:
        print(r)


def judge():
    bible = load(os.path.join(HERE, "bibles", "inspector-v1.json"))
    tpl = open(os.path.join(HERE, "judge_prompt.md"), encoding="utf-8").read()
    rng = random.Random(20261007)
    for brief in BRIEFS:
        b = load(os.path.join(HERE, "briefs", f"{brief}.json"))
        plans = outputs_for(brief)
        archs = ["A", "B", "C"]; rng.shuffle(archs)
        mapping = dict(zip(["X", "Y", "Z"], archs))
        d = os.path.join(RUNS, f"judge-{brief}"); os.makedirs(d, exist_ok=True)
        txt = tpl.replace("{{BRIEF}}", json.dumps(b, indent=1)).replace("{{BIBLE}}", json.dumps(bible, indent=1))
        for lab, arch in mapping.items():
            txt = txt.replace("{{" + lab + "}}", json.dumps(plans[arch], indent=1, ensure_ascii=False))
        open(os.path.join(d, "request.md"), "w", encoding="utf-8").write(txt)
        json.dump({"seed": 20261007, "mapping": mapping}, open(os.path.join(d, "mapping.json"), "w"), indent=2)
        print(brief, "->", d, "(mapping sealed in mapping.json)")


def aggregate():
    res = {"per_brief": {}, "mean_by_arch": {}, "structural": load(os.path.join(RUNS, "structural.json")) if os.path.exists(os.path.join(RUNS, "structural.json")) else []}
    sums = {"A": [], "B": [], "C": []}
    for brief in BRIEFS:
        d = os.path.join(RUNS, f"judge-{brief}")
        mp = load(os.path.join(d, "mapping.json"))["mapping"]
        j = load(os.path.join(d, "response.json"))
        per = {}
        for lab, arch in mp.items():
            s = j["scores"][lab]
            wt = round(sum(WEIGHTS[k] * s[k] for k in WEIGHTS), 3)
            per[arch] = {"scores": s, "weighted_total_recomputed": wt, "thresholds": j.get("thresholds", {}).get(lab), "evidence": j.get("evidence", {}).get(lab)}
            sums[arch].append(wt)
        res["per_brief"][brief] = {"mapping": mp, "ranking_by_arch": [mp[x] for x in j.get("ranking", [])], "anti_template": j.get("anti_template"), "notes": j.get("notes"), "plans": per}
    res["mean_by_arch"] = {a: round(sum(v) / len(v), 3) for a, v in sums.items() if v}
    json.dump(res, open(os.path.join(RUNS, "results.json"), "w"), indent=2, ensure_ascii=False)
    print(json.dumps({"mean_by_arch": res["mean_by_arch"], "rankings": {b: res["per_brief"][b]["ranking_by_arch"] for b in BRIEFS}}, indent=2))


if __name__ == "__main__":
    {"structural": structural, "judge": judge, "aggregate": aggregate}[sys.argv[1]]()
