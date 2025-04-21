import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_summarizer():
    return pipeline("summarization")

def run():
    st.header("Design Thinking Wizard")
    summarizer = get_summarizer()
    st.subheader("1. Empathize")
    empathy = st.text_area("Enter user insights, observations, interviews")
    if st.button("Generate Problem Statement"):
        if empathy:
            summary = summarizer(empathy, max_length=60, min_length=20, do_sample=False)
            st.success(summary[0]['summary_text'])
    st.subheader("2. Define")
    define = st.text_input("Define key problem elements")
    st.subheader("3. Ideate")
    ideas = st.text_area("Brainstorm ideas")
    st.subheader("4. Prototype")
    sketch = st.text_input("Link or description of prototype")
    st.subheader("5. Test")
    feedback = st.text_area("Input testing feedback")
