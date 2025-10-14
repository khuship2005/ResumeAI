import streamlit as st
from utils.export import export_pdf, export_docx

def build_resume():
    st.header("Create Your Resume")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    education = st.text_area("Education (Short)")
    skills = st.text_area("Skills (Comma separated)")
    experience = st.text_area("Experience (Short)")

    if st.button("Generate Resume"):
        resume_text = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Education: {education}
        Skills: {skills}
        Experience: {experience}
        """
        st.text_area("Preview Resume", resume_text, height=300)

        col1, col2 = st.columns(2)
        with col1:
            export_pdf(resume_text, f"{name}_Resume.pdf")
        with col2:
            export_docx(resume_text, f"{name}_Resume.docx")