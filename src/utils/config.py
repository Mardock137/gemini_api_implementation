import os
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
load_dotenv()

def get_gemini_api_key() -> str:
    """
    Returns the Gemini API key from environment variables.
    Raises an exception if the key is not set.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in environment variables.")
    return api_key 