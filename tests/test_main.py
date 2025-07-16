from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import patch
import pytest

def test_ping():
    client = TestClient(app)
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

@patch("src.main.generate_text")
def test_chat_success(mock_generate_text):
    client = TestClient(app)
    mock_generate_text.return_value = "Ciao Chief!"
    response = client.post("/chat", json={"prompt": "Saluta"})
    assert response.status_code == 200
    assert response.json() == {"response": "Ciao Chief!"}

@patch("src.main.generate_text")
def test_chat_error(mock_generate_text):
    client = TestClient(app)
    mock_generate_text.side_effect = Exception("Gemini error")
    response = client.post("/chat", json={"prompt": "Errore"})
    assert response.status_code == 500
    assert response.json()["detail"] == "Gemini error"

@patch("src.main.generate_text")
def test_generate_content_success(mock_generate_text):
    client = TestClient(app)
    mock_generate_text.return_value = "Generated content!"
    response = client.post("/generate-content", json={"prompt": "Write something"})
    assert response.status_code == 200
    assert response.json() == {"content": "Generated content!"}

@patch("src.main.generate_text")
def test_generate_content_error(mock_generate_text):
    client = TestClient(app)
    mock_generate_text.side_effect = Exception("Gemini error")
    response = client.post("/generate-content", json={"prompt": "fail"})
    assert response.status_code == 500
    assert response.json()["detail"] == "Gemini error"

@patch("src.main.generate_text")
def test_analyze_text_success(mock_generate_text):
    client = TestClient(app)
    mock_generate_text.return_value = "Sentiment: Positive\nSummary: ...\nParaphrase: ..."
    response = client.post("/analyze-text", json={"text": "This is a great day!"})
    assert response.status_code == 200
    assert response.json() == {"analysis": "Sentiment: Positive\nSummary: ...\nParaphrase: ..."}

@patch("src.main.generate_text")
def test_analyze_text_error(mock_generate_text):
    client = TestClient(app)
    mock_generate_text.side_effect = Exception("Gemini error")
    response = client.post("/analyze-text", json={"text": "fail"})
    assert response.status_code == 500
    assert response.json()["detail"] == "Gemini error" 