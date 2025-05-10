from sqlalchemy import Column, Integer, String, JSON
from db.database import Base
from pydantic import BaseModel
from typing import List, Optional

# DB model
class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True)
    name = Column(String)
    subjective_input = Column(JSON)  # preferences, symptoms, etc.
    objective_input = Column(JSON)  # taste test results

# Pydantic input model
class PatientIn(BaseModel):
    patient_id: str
    name: str
    subjective_input: dict
    objective_input: dict

# Output
class PatientOut(PatientIn):
    id: int

    class Config:
        orm_mode = True
