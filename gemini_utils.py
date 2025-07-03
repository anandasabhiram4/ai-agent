import google.generativeai as genai
import os

# Try to load from Streamlit secrets first, fallback to .env
try:
    import streamlit as st
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    from dotenv import load_dotenv
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the genai library
genai.configure(api_key=GOOGLE_API_KEY)

# Use a fallback model to avoid free-tier overuse
try:
    model = genai.GenerativeModel("gemini-1.5-pro")
    model.generate_content("Test")  # Dry run
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
