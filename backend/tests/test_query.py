from fastapi.testclient import TestClient
from app.main import app
from app.services.retrieval import load_retrieval

load_retrieval()

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_query():
    response = client.post("/query", json={"question": "What is machine learning?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data

def test_invalid_input():
    response = client.post("/query", json={})
    assert response.status_code == 422