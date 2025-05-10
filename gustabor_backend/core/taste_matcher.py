from typing import Dict

def match_score(profile: Dict[str, float], recipe: Dict[str, str]) -> float:
    """
    Simple content-based score: map recipe.flavor -> profile.
    """
    taste_val = profile.get(recipe["flavor"], 0.5)
    # boost if texture matches a preference? for now flat.
    return taste_val
