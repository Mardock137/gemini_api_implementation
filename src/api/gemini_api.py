import requests
from src.utils.config import get_gemini_api_key

GEMINI_API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"

def generate_text(prompt: str, model: str = "gemini-2.5-pro") -> str:
    """
    Sends a prompt to the Gemini API and returns the generated text.
    You can specify the Gemini model (default: 'gemini-2.5-pro').
    Raises an exception if the request fails or the response structure is unexpected.
    """
    api_key = get_gemini_api_key()
    url = f"{GEMINI_API_BASE_URL}/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code != 200:
            raise RuntimeError(f"Gemini API error: {response.status_code} - {response.text}")
        data = response.json()
        # Extract the generated text from the typical Gemini API response
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            raise RuntimeError(f"Unexpected Gemini API response: {data}")
    except Exception as e:
        raise 