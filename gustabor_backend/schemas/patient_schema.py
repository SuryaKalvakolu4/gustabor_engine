from pydantic import BaseModel
from typing import List, Dict

class SubjectiveInput(BaseModel):
    taste_preferences: List[str]
    texture_likes: List[str]
    dietary_restrictions: List[str]
    symptoms: List[str]

class ObjectiveInput(BaseModel):
    sweet: float
    sour: float
    bitter: float
    salty: float
    umami: float
    deficits: List[str]

class PatientIn(BaseModel):
    patient_id: str
    name: str
    subjective_input: SubjectiveInput
    objective_input: ObjectiveInput
