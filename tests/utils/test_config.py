import os
import pytest
from src.utils import config

def test_get_gemini_api_key_success(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test_key")
    assert config.get_gemini_api_key() == "test_key"

def test_get_gemini_api_key_missing(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(RuntimeError) as exc:
        config.get_gemini_api_key()
    assert "GEMINI_API_KEY is not set" in str(exc.value) 