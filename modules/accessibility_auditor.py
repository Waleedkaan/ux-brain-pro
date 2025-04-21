import streamlit as st
from PIL import Image
import numpy as np

def luminance(r, g, b):
    a = [v/255.0 for v in (r, g, b)]
    a = [x/12.92 if x <= 0.03928 else ((x+0.055)/1.055)**2.4 for x in a]
    return 0.2126*a[0] + 0.7152*a[1] + 0.0722*a[2]

def contrast_ratio(rgb1, rgb2):
    l1 = luminance(*rgb1)
    l2 = luminance(*rgb2)
    ratio = (l1+0.05)/(l2+0.05) if l1>l2 else (l2+0.05)/(l1+0.05)
    return ratio

def run():
    st.header("Accessibility Auditor")
    uploaded = st.file_uploader("Upload UI screenshot", type=["png","jpg","jpeg"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, use_column_width=True)
        st.info("Select colors to compute contrast ratio")
        c1 = st.color_picker("Text color", "#000000")
        c2 = st.color_picker("Background color", "#FFFFFF")
        rgb1 = tuple(int(c1[i:i+2],16) for i in (1,3,5))
        rgb2 = tuple(int(c2[i:i+2],16) for i in (1,3,5))
        ratio = contrast_ratio(rgb1, rgb2)
        st.write(f"Contrast Ratio: {ratio:.2f}")
        if ratio >= 4.5:
            st.success("Passes WCAG AA for normal text")
        else:
            st.error("Fails WCAG AA for normal text")
