from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from db.database import get_db
from models.patient_model import Patient
from models.recipe_model import Recipe
from core.llm_recommender import generate_recommendations
from core.pdf_generator import generate_pdf
import os

router = APIRouter()

@router.get("/{patient_id}")
def generate_report(patient_id: str, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    recipes = db.query(Recipe).limit(20).all()
    recommendations = generate_recommendations(patient, recipes)

    filename = f"{patient.patient_id}_report.pdf"
    filepath = os.path.join("reports", filename)
    os.makedirs("reports", exist_ok=True)
    generate_pdf(patient.name, recommendations, filepath)

    return FileResponse(path=filepath, filename=filename, media_type='application/pdf')
