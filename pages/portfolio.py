import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from portfolio.portfolio_builder import build_portfolio
st.set_page_config(page_title="Portfolio Builder", page_icon="🌐", layout="wide")
build_portfolio()