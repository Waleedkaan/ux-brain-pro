import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

heuristics = [
    "Visibility of system status",
    "Match between system and real world",
    "User control and freedom",
    "Consistency and standards",
    "Error prevention",
    "Recognition rather than recall",
    "Flexibility and efficiency of use",
    "Aesthetic and minimalist design",
    "Help users recognize, diagnose, and recover from errors",
    "Help and documentation"
]

def run():
    st.header("Heuristic Evaluation Scanner")
    uploaded = st.file_uploader("Upload UI screenshot", type=["png","jpg","jpeg"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded UI Screenshot", use_column_width=True)
        arr = np.array(img)
        gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        st.subheader("Extracted Text")
        st.code(text)
        st.subheader("Heuristic Results")
        for h in heuristics:
            if h.lower() in text.lower():
                st.success(f"{h} detected")
            else:
                st.warning(f"{h} may be missing")
