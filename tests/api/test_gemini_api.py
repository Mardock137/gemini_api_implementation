import pytest
from unittest.mock import patch, Mock
from src.api.gemini_api import generate_text

@patch("src.api.gemini_api.requests.post")
def test_generate_text_success(mock_post, monkeypatch):
    # Mock della risposta API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "candidates": [
            {"content": {"parts": [{"text": "Hello, world!"}]}}
        ]
    }
    mock_post.return_value = mock_response
    # Mock della chiave API
    monkeypatch.setenv("GEMINI_API_KEY", "fake_key")
    result = generate_text("Say hello")
    assert result == "Hello, world!"

@patch("src.api.gemini_api.requests.post")
def test_generate_text_api_error(mock_post, monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.text = "Bad Request"
    mock_post.return_value = mock_response
    monkeypatch.setenv("GEMINI_API_KEY", "fake_key")
    with pytest.raises(RuntimeError) as exc:
        generate_text("fail test")
    assert "Gemini API error" in str(exc.value)

@patch("src.api.gemini_api.requests.post")
def test_generate_text_unexpected_response(mock_post, monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"unexpected": "structure"}
    mock_post.return_value = mock_response
    monkeypatch.setenv("GEMINI_API_KEY", "fake_key")
    with pytest.raises(RuntimeError) as exc:
        generate_text("bad structure")
    assert "Unexpected Gemini API response" in str(exc.value) 