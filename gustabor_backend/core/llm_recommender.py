import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Setup OpenAI client
client = openai.OpenAI()


def generate_recommendations(patient, recipes):
    # Convert Pydantic models to plain dicts if needed
    subjective = patient.subjective_input if isinstance(patient.subjective_input, dict) else patient.subjective_input.dict()
    objective = patient.objective_input if isinstance(patient.objective_input, dict) else patient.objective_input.dict()

    # Define system role
    system_prompt = (
        "You are a clinical nutrition assistant for oncology patients. "
        "Your task is to recommend 5 healthy recipes personalized to a patient with taste disorders during chemotherapy. "
        "Be mindful of their dietary restrictions, texture preferences, and known taste deficits. "
        "Avoid ingredients or suggestions that could worsen their symptoms or conflict with restrictions."
    )

    # Build dynamic user prompt
    user_prompt = f"""
Patient Information:
- Name: {patient.name}
- Taste Preferences: {', '.join(subjective['taste_preferences'])}
- Texture Likes: {', '.join(subjective['texture_likes'])}
- Dietary Restrictions: {', '.join(subjective['dietary_restrictions'])}
- Symptoms: {', '.join(subjective['symptoms'])}
- Known Taste Deficits: {', '.join(objective['deficits'])}

Available Healthy Recipes:
{', '.join([r.name for r in recipes])}

Suggest 5 personalized recipe ideas (can be modified versions of the above), with a one-line justification for each.
"""

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    # Parse and return LLM response
    reply = response.choices[0].message.content.strip()
    return reply.split("\n")