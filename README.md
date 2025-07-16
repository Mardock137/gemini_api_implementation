---
language: en
---

- **Python version used**: `3.12.10`

# 📋 Index
- [📄 Description](#-description)
- [ℹ️ General Info](#️-general-info)
- [⚙️ Configuration Info](#️-configuration-info)
- [🤖 Integrated APIs](#-integrated-apis)

## 📄 Description
This application is an AI suite that integrates Google's Gemini API to provide:
- Intelligent chatbot for answering questions and providing assistance
- Custom content generation (blog posts, emails, social media posts)
- Advanced text analysis (sentiment, summarization, paraphrasing)

The dashboard provides a user-friendly web interface to:
- Chat with the Gemini model
- Generate content
- Analyze text

## ℹ️ General Info

### 📁 Root Directory
- For **Environment Variables** see [.env.example](.env.example)
- For the **List of dependencies** see [requirements.txt](requirements.txt)

### 📁 docs/
- For the **Repository structure** see [repo_structure.md](docs/repo_structure.md)

## ⚙️ Configuration Info
- To start the backend, simply run the following command from the terminal: `uvicorn src.main:app --reload`
- To launch the interactive dashboard for the Gemini API demo, run: `streamlit run dashboard/app.py`

## 🤖 Integrated APIs
- Gemini API
