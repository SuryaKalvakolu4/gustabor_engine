from core.taste_matcher import match_score
from typing import List, Dict

def rank_recipes(profile: Dict[str, float], recipes: List[Dict]) -> List[Dict]:
    scored = []
    for r in recipes:
        score = match_score(profile, r)
        scored.append({**r, "score": score})
    # sort descending
    return sorted(scored, key=lambda x: x["score"], reverse=True)
