import streamlit as st
from portfolio.qr_generator import generate_qr
import zipfile
import os

def build_portfolio():
    st.header("Portfolio Builder")
    name = st.text_input("Your Name")
    bio = st.text_area("Short Bio")
    projects = st.text_area("Projects (Comma separated)")

    if st.button("Generate Portfolio Website"):
        html_content = f"""
        <html>
        <head><title>{name}'s Portfolio</title></head>
        <body>
            <h1>{name}</h1>
            <p>{bio}</p>
            <h2>Projects</h2>
            <ul>
                {''.join(f'<li>{p.strip()}</li>' for p in projects.split(','))}
            </ul>
        </body>
        </html>
        """
        filename = f"{name}_portfolio.html"
        with open(filename, "w") as f:
            f.write(html_content)
        with open(filename, "rb") as f:
            st.download_button("Download Portfolio HTML", f, file_name=filename)

        generate_qr(f"{filename}", f"{name}_portfolio_qr.png")