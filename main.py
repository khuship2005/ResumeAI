import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from resume.resume_form import build_resume
from portfolio.portfolio_builder import build_portfolio
from ats.ats_score import score_resume

st.set_page_config(page_title="ResumeAI Pro", page_icon="🏠", layout="wide")
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'resume':
    build_resume()
    if st.button("← Back to Home"):
        st.session_state.page = 'main'
        st.rerun()
elif st.session_state.page == 'portfolio':
    build_portfolio()
    if st.button("← Back to Home"):
        st.session_state.page = 'main'
        st.rerun()
elif st.session_state.page == 'ats':
    score_resume()
    if st.button("← Back to Home"):
        st.session_state.page = 'main'
        st.rerun()
else:
    st.markdown("""
    <style>
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .feature-card h3 { margin-bottom: 1rem; }
    .stat-box {
        background: #f3f4f6;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        border-left: 4px solid #667eea;
    }
    .stat-number { font-size: 2.5rem; font-weight: bold; color: #667eea; }
    .stat-label { color: #6b7280; font-size: 1rem; }
    </style>
    """, unsafe_allow_html=True)

    st.title("🏠 Welcome to ResumeAI Pro")
    st.markdown("---")
    st.markdown("""
    <style>
        /* Hide sidebar completely */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* Hide the hamburger menu (≡) */
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

    st.markdown("""
    ## 🚀 Build Your Professional Future
    ResumeAI Pro is your all-in-one solution for creating stunning resumes and portfolios. 
    Whether you're a fresher or an experienced professional, we've got you covered!
    """)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📄 AI Resume Builder</h3>
            <ul>
                <li>Choose from 3 professional templates</li>
                <li>Customize colors and layouts</li>
                <li>ATS-friendly formatting</li>
                <li>Save and manage multiple versions</li>
                <li>Download as PDF instantly</li>
                <li>Upload and improve existing resumes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Start Building Resume", key="home_resume"):
            st.session_state.page = 'resume'
            st.rerun()

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🌐 Portfolio Generator</h3>
            <ul>
                <li>Create stunning portfolio websites</li>
                <li>Mobile-responsive designs</li>
                <li>Showcase your projects beautifully</li>
                <li>Generate QR codes for sharing</li>
                <li>Instant deployment</li>
                <li>Share with recruiters easily</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🌐 Create Portfolio", key="home_portfolio"):
            st.session_state.page = 'portfolio'
            st.rerun()

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 ATS Resume Scorer</h3>
            <ul>
                <li>Upload your resume folder</li>
                <li>Check ATS compatibility</li>
                <li>Get instant scoring and suggestions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Check ATS Score", key="home_ats"):
            st.session_state.page = 'ats'
            st.rerun()
    st.markdown("---")
    st.markdown("## 📊 Why Choose ResumeAI Pro?")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown('<div class="stat-box"><div class="stat-number">3</div><div class="stat-label">Professional Templates</div></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">ATS Compatible</div></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="stat-box"><div class="stat-number">∞</div><div class="stat-label">Unlimited Versions</div></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="stat-box"><div class="stat-number">24/7</div><div class="stat-label">Available</div></div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("## 🎯 How It Works")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("### 1️⃣ Fill Details\nEnter your personal info and skills")
    with col2: st.markdown("### 2️⃣ Choose Template\nSelect professional designs")
    with col3: st.markdown("### 3️⃣ Generate Resume/Portfolio\nInstant preview")
    with col4: st.markdown("### 4️⃣ Download & Share\nGet PDF or deploy website")
    
    st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 2rem;'>
        <p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>© 2024 ResumeAI Pro. All rights reserved.</p>
        <p style='font-size: 0.9rem;'>Built with ❤️ using Streamlit | Your Success is Our Mission</p>
        <p style='font-size: 0.8rem; margin-top: 1rem;'>🔒 Secure | 🚀 Fast | 💯 Professional</p>
    </div>
    """, unsafe_allow_html=True)