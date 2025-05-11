from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db, SessionLocal
from models.recipe_model import Recipe
from core.gpt_explainer import explain_recipe
from api.endpoints.profile import _PROFILES

router = APIRouter()

@router.get("/{profile_id}/{recipe_name}", response_model=dict)
def explain(profile_id: int, recipe_name: str, db: Session = Depends(get_db)):
    if profile_id not in _PROFILES:
        raise HTTPException(status_code=404, detail="Profile not found")

    recipe = db.query(Recipe).filter(Recipe.name == recipe_name).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    explanation = explain_recipe(_PROFILES[profile_id], {
        "name": recipe.name,
        "flavor": recipe.flavor
    })
    return {"explanation": explanation}
