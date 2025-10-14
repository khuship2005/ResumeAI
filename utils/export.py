from fpdf import FPDF
from docx import Document
import streamlit as st

def export_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)
    with open(filename, "rb") as f:
        st.download_button("Download PDF", f, file_name=filename)

def export_docx(text, filename):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)
    with open(filename, "rb") as f:
        st.download_button("Download DOCX", f, file_name=filename)
