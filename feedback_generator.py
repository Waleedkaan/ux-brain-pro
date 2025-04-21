import streamlit as st
from transformers import pipeline
from modules.heuristic_scanner import heuristics
from modules.accessibility_auditor import contrast_ratio, luminance

@st.cache_resource
def get_summarizer():
    return pipeline("summarization")

@st.cache_resource
def get_sentiment():
    return pipeline("sentiment-analysis")

def run():
    st.header("UI Feedback Generator")
    summarizer = get_summarizer()
    sentiment = get_sentiment()
    notes = st.text_area("Enter UI description or paste extracted text")
    if st.button("Generate Feedback"):
        if notes:
            summary = summarizer(notes, max_length=100, min_length=20, do_sample=False)
            st.subheader("Summary")
            st.write(summary[0]['summary_text'])
            sent = sentiment(notes[:500])
            st.subheader("Sentiment")
            st.json(sent)
            st.subheader("Actionable Feedback")
            st.write("• Check visibility and consistency")
            st.write("• Ensure error prevention mechanisms")
            st.write("• Review contrast ratios and WCAG compliance")
