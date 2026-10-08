"""KPI-triggered reminders. Each reminder fires when its conditions hold in the metrics passed to the weekly review (gate G4 onward),
not on a date. A fired reminder is a prompt to ask the owner; it never authorises the action.

Owner 2026-10-08 on the rival move (Vince challenges Jean Phil to a dance-off by duet/stitch): "maybe when we master the system more
and start gaining traction. put a reminder based on kpi". Thresholds are pilot hypotheses, not industry benchmarks; edit them here.
"""
from __future__ import annotations

from statistics import median

REMINDERS = [
    {
        "id": "vince-rival-dance-off",
        "ask_owner": "Vince has traction and production is stable. Approve the rival move: Vince challenges Jean Phil (@jean_philanthrope) "
                     "to a dance-off via TikTok duet/stitch? Public interaction with another creator: owner approval required.",
        "account": "vince",
        "conditions": {  # all must hold
            "followers_min": 5000,                # traction: an audience worth lending to the challenge
            "median_views_last5_min": 20000,      # traction: not one lucky post
            "shares_per_1k_min": 8, "shares_posts_min": 3,  # shares/1k views >= 8 on at least 3 of the last 5 posts
            "episodes_published_min": 6,          # mastery: enough episodes shipped
            "first_pass_qa_rate_min": 0.6,        # mastery: >= 60% of shots pass QA without a retake
        },
    },
]


def _check(c: dict, m: dict) -> list[str]:
    """Return the unmet conditions (empty list = due)."""
    posts = m.get("last_posts") or []  # newest first: [{"views": int, "shares": int}, ...]
    last5 = posts[:5]
    views = [p.get("views", 0) for p in last5]
    share_hits = sum(1 for p in last5 if p.get("views") and 1000 * p.get("shares", 0) / p["views"] >= c["shares_per_1k_min"])
    unmet = []
    if m.get("followers", 0) < c["followers_min"]:
        unmet.append(f"followers {m.get('followers', 0)} < {c['followers_min']}")
    if len(last5) < 5 or median(views) < c["median_views_last5_min"]:
        unmet.append(f"median views of last 5 posts {median(views) if views else 0} < {c['median_views_last5_min']}")
    if share_hits < c["shares_posts_min"]:
        unmet.append(f"{share_hits} of last 5 posts reach {c['shares_per_1k_min']} shares per 1,000 views (need {c['shares_posts_min']})")
    if m.get("episodes_published", 0) < c["episodes_published_min"]:
        unmet.append(f"episodes published {m.get('episodes_published', 0)} < {c['episodes_published_min']}")
    if m.get("first_pass_qa_rate", 0.0) < c["first_pass_qa_rate_min"]:
        unmet.append(f"first-pass QA rate {m.get('first_pass_qa_rate', 0.0):.0%} < {c['first_pass_qa_rate_min']:.0%}")
    return unmet


def due_reminders(metrics_by_account: dict) -> list[dict]:
    """metrics_by_account: {"vince": {...}, ...}. Returns every reminder with its status: due, or the conditions still unmet."""
    out = []
    for r in REMINDERS:
        unmet = _check(r["conditions"], metrics_by_account.get(r["account"]) or {})
        out.append({"id": r["id"], "due": not unmet, "ask_owner": r["ask_owner"] if not unmet else None, "unmet": unmet})
    return out
