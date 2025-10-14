import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from resume.resume_form import build_resume
st.set_page_config(page_title="Resume Builder", page_icon="📄", layout="wide")
build_resume()