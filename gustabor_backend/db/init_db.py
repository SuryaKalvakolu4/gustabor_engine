from gustabor_backend.db.database import Base, engine, SessionLocal
from gustabor_backend.models.recipe_model import Recipe
import csv

def seed_recipes():
    db = SessionLocal()
    with open("data/healthy_recipes_named.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            recipe = Recipe(
                name=row['name'],
                flavor=row['flavor'],
                texture=row['texture'],
                nutrition_tags=row['nutrition_tags'],
                ingredients=row['ingredients'],
                prep_time=row['prep_time'],
                difficulty=row['difficulty']
            )
            db.add(recipe)
        db.commit()
        db.close()
    print("✅ Seeded 100 healthy recipes.")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    seed_recipes()
