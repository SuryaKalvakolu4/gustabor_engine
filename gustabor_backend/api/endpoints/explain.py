from fastapi import APIRouter, HTTPException
from gustabor_backend.api.endpoints.profile import _PROFILES
from gustabor_backend.db.database import SessionLocal
from gustabor_backend.models.recipe_model import Recipe
from gustabor_backend.core.gpt_explainer import explain_recipe

router = APIRouter()

@router.get("/{profile_id}/{recipe_name}", response_model=dict)
def explain(profile_id: int, recipe_name: str):
    if profile_id not in _PROFILES:
        raise HTTPException(status_code=404, detail="Profile not found")
    db = SessionLocal()
    recipe = db.query(Recipe).filter(Recipe.name == recipe_name).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    explanation = explain_recipe(_PROFILES[profile_id], {
        "name": recipe.name, "flavor": recipe.flavor
    })
    return {"explanation": explanation}
