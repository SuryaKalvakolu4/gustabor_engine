from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.patient_model import Patient
from models.recipe_model import Recipe
from core.llm_recommender import generate_recommendations

router = APIRouter()

@router.get("/{patient_id}")
def get_recommendations(patient_id: str, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    recipes = db.query(Recipe).limit(20).all()
    recommendations = generate_recommendations(patient, recipes)
    return recommendations
