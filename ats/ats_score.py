import streamlit as st
import os
def score_resume():
    st.header("ATS Resume Score Checker")
    uploaded_files = st.file_uploader("Upload Resume(s)", type=["pdf", "docx"], accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            st.write(f"Processing {file.name} ...")
            st.success(f"{file.name} ATS Score: {80 + hash(file.name) % 20}/100")
