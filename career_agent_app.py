# career_agent_app.py
import streamlit as st
from gemini_utils import get_career_advice

st.set_page_config(page_title="AI Career Coach", layout="centered")

st.title("🤖 AI Career Coach")
st.markdown("Improve your resume, get job suggestions, and boost your career!")

with st.form("career_form"):
    name = st.text_input("👤 Your Name")
    resume = st.text_area("📄 Paste your Resume or Summary")
    interests = st.text_input("🎯 Career Interests (e.g., Data Science, AI)")
    goals = st.text_area("🚀 Career Goals (optional)")
    submitted = st.form_submit_button("Ask Career Coach")

if submitted:
    if not resume or not interests:
        st.warning("Please provide both resume and interests.")
    else:
        with st.spinner("🤖 Thinking..."):
            try:
                response = get_career_advice(name, resume, interests, goals)
                st.success("✅ Career Advice:")
                st.markdown(response)
            except Exception as e:
                st.error("❌ Something went wrong.")
                st.exception(e)
