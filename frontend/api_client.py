import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def query(question: str) -> dict:
    try:
        response = requests.post(
            f"{API_BASE_URL}/query",
            json={"question": question}
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}