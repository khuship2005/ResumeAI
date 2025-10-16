# ResumeAI

*AI-powered Streamlit app to create resumes, portfolios & analyze ATS scores*

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## Overview

### 🔑 Key Features
- ✅ AI Resume Generation using OpenAI API  
- ✅ Portfolio Builder with integrated QR Code  
- ✅ ATS Score Checker for resume optimization  
- ✅ Export to PDF, DOCX, and TXT formats  
- ✅ User-friendly Streamlit interface  

### 🧩 Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Integration:** OpenAI API  
- **File Export:** FPDF, python-docx  
- **QR Generation:** qrcode  

### ⚙️ How It Works
- ✅ User inputs personal and professional details  
- ✅ OpenAI generates professional resume text  
- ✅ Portfolio website is auto-created from data  
- ✅ ATS module scores resume keywords & structure  
- ✅ Download your **Resume** in PDF or DOCX format, and your **Portfolio** as an interactive HTML page or a shareable QR code  

---

## Installation & Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/khuship2005/ResumeAI.git
    cd ResumeAI
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # on Windows
    source venv/bin/activate  # on macOS/Linux
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**
    ```bash
    streamlit run main.py
    ```

---

## Deployment

You can deploy **ResumeAI** using Streamlit Cloud or any Python hosting platform.

### ▶️ Streamlit Cloud

1. Push the project to GitHub  
2. Go to [share.streamlit.io](https://share.streamlit.io)  
3. Connect your repository and select `main.py` as the entry point  
4. Add your OpenAI API key under "Secrets"  

---
