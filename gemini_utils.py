import google.generativeai as genai
import os

# Replace with your API key
GOOGLE_API_KEY = "AIzaSyAYAq2G5jixQGjV5L_ieOiooqzAdOgqL-E"

genai.configure(api_key=GOOGLE_API_KEY)

# Use a fallback model to avoid free-tier overuse
try:
    model = genai.GenerativeModel("gemini-1.5-pro")
    model.generate_content("Test")
except Exception:
    model = genai.GenerativeModel("gemini-1.5-flash")

def get_career_advice(name, resume, interests, goals):
    prompt = f"""
    Give career advice in simple bullet points.

    - Name: {name}
    - Resume: {resume}
    - Interests: {interests}
    - Goals: {goals}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error generating advice: {str(e)}"
