from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from gustabor_backend.db.database import get_db
from gustabor_backend.models.profile_model import ProfileIn

router = APIRouter()

# we store profiles only in memory for now
_PROFILES = {}
_COUNTER = 1

@router.post("/", response_model=dict)
def submit_profile(profile: ProfileIn):
    global _COUNTER
    pid = _COUNTER
    _PROFILES[pid] = profile.dict()
    _COUNTER += 1
    return {"profile_id": pid}
