from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from core.llm_recommender import generate_recommendations
from db.database import get_db
from sqlalchemy.orm import Session
from models.patient_model import Patient
from fastapi import Depends

router = APIRouter()

class ChatRequest(BaseModel):
    patient_id: str
    query: str

@router.post("/", response_model=dict)
def chat_with_llm(payload: ChatRequest, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.patient_id == payload.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    # For now, we respond to any query with recipe suggestions
    response = generate_recommendations(patient, [])
    return {"response": "\n".join(response)}
