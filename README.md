<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ResumeAI - Project Overview</title>
  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background-color: #0e0e10;
      color: #e6e6e6;
      line-height: 1.7;
      margin: 0;
      padding: 0;
    }

    header {
      background:  #111827;
      color: #fff;
      text-align: center;
      padding: 2.5rem 1rem;
      box-shadow: 0 3px 15px rgba(0, 0, 0, 0.3);
    }

    header h1 {
      margin: 0;
      font-size: 2.5rem;
      letter-spacing: 1.5px;
    }

    header p {
      font-size: 1.1rem;
      margin-top: 0.6rem;
      color: #cbd5e1;
    }

    section {
      max-width: 950px;
      background: #18181b;
      margin: 2rem auto;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 3px 15px rgba(0, 0, 0, 0.4);
    }

    h2 {
      color: #dfe4e8;
      border-bottom: 2px solid #d4d8df;
      padding-bottom: 0.5rem;
      margin-bottom: 1rem;
    }

    h3 {
      color: #dae1e8;
      margin-top: 1.5rem;
    }

    ul {
      list-style: none;
      padding: 0;
    }

    ul li {
      margin: 0.4rem 0;
    }

    ul li::before {
      content: "✅ ";
      color: #22c55e;
    }

    ol {
      padding-left: 1.3rem;
    }

    code, pre {
      background-color: #27272a;
      border-radius: 6px;
      padding: 0.4rem 0.6rem;
      color: #d1d5db;
      font-family: Consolas, monospace;
    }

    pre {
      padding: 1rem;
      overflow-x: auto;
      border-left: 4px solid #394457;
    }

    a {
      color: #60a5fa;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .meta {
      margin-top: 1.2rem;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0.6rem;
    }

    .badge img {
      height: 22px;
      border-radius: 5px;
    }

    footer {
      text-align: center;
      background-color: #111827;
      color: #9ca3af;
      padding: 1.8rem 0;
      margin-top: 3rem;
      font-size: 0.95rem;
      border-top: 1px solid #1f2937;
    }
  </style>
</head>
<body>

  <header>
    <h1>ResumeAI</h1>
    <p>AI-powered Streamlit app to create resumes, portfolios & analyze ATS scores</p>
    <div class="meta">
      <div class="badge"><img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python"></div>
      <div class="badge"><img src="https://img.shields.io/badge/Streamlit-App-red.svg" alt="Streamlit"></div>
      <div class="badge"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT"></div>
    </div>
  </header>

  <section id="overview">
    <h2>Overview</h2>

    <div class="subsection">
      <h3>🔑 Key Features</h3>
      <ul>
        <li>AI Resume Generation using OpenAI API</li>
        <li>Portfolio Builder with integrated QR Code</li>
        <li>ATS Score Checker for resume optimization</li>
        <li>Export to PDF, DOCX, and TXT formats</li>
        <li>User-friendly Streamlit interface</li>
      </ul>
    </div>

    <div class="subsection">
      <h3>🧩 Tech Stack</h3>
      <ul>
        <li><b>Frontend:</b> Streamlit</li>
        <li><b>Backend:</b> Python</li>
        <li><b>AI Integration:</b> OpenAI API</li>
        <li><b>File Export:</b> FPDF, python-docx</li>
        <li><b>QR Generation:</b> qrcode</li>
      </ul>
    </div>

    <div class="subsection">
      <h3>⚙️ How It Works</h3>
      <ul>
        <li>User inputs personal and professional details</li>
        <li>OpenAI generates professional resume text</li>
        <li>Portfolio website is auto-created from data</li>
        <li>ATS module scores resume keywords & structure</li>
        <li>Download your <b>Resume</b> in PDF or DOCX format, and your <b>Portfolio</b> as an interactive HTML page or a shareable QR code</li>
      </ul>
    </div>
  </section>

  <section id="installation">
    <h2>Installation & Setup</h2>
    <ol>
      <li><b>Clone the repository</b>
        <pre><code>git clone https://github.com/khuship2005/ResumeAI.git
cd ResumeAI</code></pre>
      </li>
      <li><b>Create a virtual environment</b>
        <pre><code>python -m venv venv
venv\Scripts\activate  # on Windows
source venv/bin/activate  # on macOS/Linux</code></pre>
      </li>
      <li><b>Install dependencies</b>
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li><b>Run the Streamlit app</b>
        <pre><code>streamlit run main.py</code></pre>
      </li>
    </ol>
  </section>

  <section id="deployment">
    <h2>Deployment</h2>
    <p>You can deploy <b>ResumeAI</b> using Streamlit Cloud or any Python hosting platform.</p>

    <div class="subsection">
      <h3>▶️ Streamlit Cloud</h3>
      <ol>
        <li>Push the project to GitHub</li>
        <li>Go to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a></li>
        <li>Connect your repository and select <code>main.py</code> as the entry point</li>
        <li>Add your OpenAI API key under "Secrets"</li>
      </ol>
    </div>
  </section>

  <section id="future-scope">
    <h2>Future Scope</h2>
    <ul>
      <li>More advanced and customizable resume templates</li>
      <li>Enhanced AI-based text generation and keyword optimization</li>
      <li>Multilingual support for global users</li>
      <li>Smart job-matching and analytics integration</li>
    </ul>
  </section>
</body>
</html>
