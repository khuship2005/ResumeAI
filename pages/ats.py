import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from ats.ats_score import score_resume
st.set_page_config(page_title="ATS Score Checker", page_icon="📊", layout="wide")
score_resume()

