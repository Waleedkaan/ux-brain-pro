### app.py
import streamlit as st
from modules import design_thinking, heuristic_scanner, accessibility_auditor, feedback_generator

st.set_page_config(page_title="UX Brain Pro", layout="wide")
st.title("UX Brain Pro - AI UX Assistant")

page = st.sidebar.radio("Select Module", [
    "Design Thinking Wizard",
    "Heuristic Evaluation Scanner",
    "Accessibility Auditor",
    "UI Feedback Generator"
])

if page == "Design Thinking Wizard":
    design_thinking.run()
elif page == "Heuristic Evaluation Scanner":
    heuristic_scanner.run()
elif page == "Accessibility Auditor":
    accessibility_auditor.run()
elif page == "UI Feedback Generator":
    feedback_generator.run()
