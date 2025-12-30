import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_advice(predictions, alerts):
    prompt = f"""
    You are a personal finance advisor.

    Predictions:
    {predictions}

    Budget Alerts:
    {alerts}

    Give clear, actionable financial advice.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
