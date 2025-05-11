from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models import patient_model
from schemas import patient_schema

router = APIRouter()

@router.post("/")
def create_patient(patient: patient_schema.PatientIn, db: Session = Depends(get_db)):
    db_patient = patient_model.Patient(
        patient_id=patient.patient_id,
        name=patient.name,
        subjective_input={
            "taste_preferences": patient.subjective_input.taste_preferences,
            "texture_likes": patient.subjective_input.texture_likes,
            "dietary_restrictions": patient.subjective_input.dietary_restrictions,
            "symptoms": patient.subjective_input.symptoms,
        },
        objective_input={
            "sweet": patient.objective_input.sweet,
            "salty": patient.objective_input.salty,
            "bitter": patient.objective_input.bitter,
            "umami": patient.objective_input.umami,
            "sour": patient.objective_input.sour,
            "deficits": patient.objective_input.deficits,
        }
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return {"message": "Patient added successfully", "patient_id": db_patient.id}
