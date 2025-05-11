from pydantic import BaseModel
from typing import List, Optional

class SubjectiveInput(BaseModel):
    taste_preferences: List[str]
    texture_likes: List[str]
    dietary_restrictions: List[str] = []
    symptoms: List[str] = []

class ObjectiveInput(BaseModel):
    sweet: int
    salty: int
    bitter: int
    umami: int
    sour: int
    deficits: List[str] = []

class PatientIn(BaseModel):
    patient_id: str  # Changed to str to match frontend form
    name: str
    subjective_input: SubjectiveInput
    objective_input: ObjectiveInput
