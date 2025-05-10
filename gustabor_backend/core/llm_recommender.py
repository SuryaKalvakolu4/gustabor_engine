import openai
import os
from models.recipe_model import Recipe
from models.patient_model import Patient

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recommendations(patient: Patient, recipes: list[Recipe]) -> list[str]:
    recipe_descriptions = "\n".join([
        f"- {r.name}: flavor={r.flavor}, texture={r.texture}, tags={r.nutrition_tags}, ingredients={r.ingredients}, prep_time={r.prep_time}, difficulty={r.difficulty}"
        for r in recipes
    ])

    prompt = f"""
You are an AI medical nutrition assistant for cancer patients with taste disorders.
Your job is to recommend 5 personalized recipes from the list below.

Patient ID: {patient.patient_id}
Name: {patient.name}
Subjective Input (taste preferences, texture likes, restrictions, symptoms):
{patient.subjective_input}

Objective Taste Test Results (taste scores, known deficits):
{patient.objective_input}

Here is a list of recipes:
{recipe_descriptions}

Choose 5 that best match the patient's profile. For each, explain why it's a good fit based on their taste perception, dietary needs, and health profile.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700
    )

    return response.choices[0].message.content.strip().split('\n')
