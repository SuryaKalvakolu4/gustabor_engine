import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "")

def explain_recipe(profile: dict, recipe: dict) -> str:
    prompt = (
        f"A patient has taste sensitivities: {profile}. "
        f"Explain why the recipe '{recipe['name']}' with flavor '{recipe['flavor']}' "
        f"is suitable, in patient-friendly language."
    )
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=150
    )
    return resp.choices[0].message.content.strip()
