from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints import patients, recommendations, reports, chat  # ✅ Added chat
from db.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gustabor AI",
    description="An AI system for taste-aware recipe suggestions during tumor therapy.",
    version="1.0.0",
)

# Enable CORS (you can restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registrations
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])  # ✅ Newly added

# Health check
@app.get("/")
def read_root():
    return {"message": "Gustabor AI backend is running"}
