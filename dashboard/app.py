import streamlit as st
import requests

# Gemini API Dashboard
# This file provides a basic Streamlit dashboard that communicates with the FastAPI backend via REST API.

# Backend FastAPI URL (can be changed from the sidebar)
BACKEND_URL = st.sidebar.text_input(
    label="Backend FastAPI URL",
    value="http://localhost:8000"
)

st.title("Gemini API Dashboard")
st.write("""
This dashboard allows you to interact with the Gemini-powered backend:
- Chat with Gemini
- Generate content
- Analyze text
""")

tab1, tab2, tab3 = st.tabs(["Chatbot", "Generate Content", "Analyze Text"])

with tab1:
    st.header("Chat with Gemini")
    user_message = st.text_area("Your message:")
    if st.button("Send", key="chat"):
        if user_message.strip():
            try:
                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={"prompt": user_message}
                )
                if response.status_code == 200:
                    st.success(response.json().get("response", "No response"))
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
        else:
            st.info("Please enter a message.")

with tab2:
    st.header("Generate Content")
    prompt = st.text_area("Prompt:", key="gen_content")
    if st.button("Generate", key="generate_content"):
        if prompt.strip():
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate-content",
                    json={"prompt": prompt}
                )
                if response.status_code == 200:
                    st.success(response.json().get("content", "No content generated"))
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
        else:
            st.info("Please enter a prompt.")

with tab3:
    st.header("Analyze Text")
    text_to_analyze = st.text_area("Text to analyze:", key="analyze_text")
    if st.button("Analyze", key="analyze"):
        if text_to_analyze.strip():
            try:
                response = requests.post(
                    f"{BACKEND_URL}/analyze-text",
                    json={"text": text_to_analyze}
                )
                if response.status_code == 200:
                    st.success(response.json().get("analysis", "No analysis returned"))
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
        else:
            st.info("Please enter some text to analyze.") 