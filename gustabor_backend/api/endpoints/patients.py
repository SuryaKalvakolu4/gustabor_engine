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
        subjective_input=patient.subjective_input.dict(),  # ✅ FIXED
        objective_input=patient.objective_input.dict()  # ✅ FIXED
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
