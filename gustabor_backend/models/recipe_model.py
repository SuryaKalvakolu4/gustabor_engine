from sqlalchemy import Column, Integer, String
from db.database import Base
from pydantic import BaseModel

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    flavor = Column(String)
    texture = Column(String)
    nutrition_tags = Column(String)
    ingredients = Column(String)
    prep_time = Column(String)
    difficulty = Column(String)

class RecipeOut(BaseModel):
    name: str
    flavor: str
    texture: str
    nutrition_tags: str
    ingredients: str
    prep_time: str
    difficulty: str

    class Config:
        orm_mode = True
