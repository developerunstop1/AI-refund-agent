from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_logs_endpoint():
    response = client.get("/logs")

    assert response.status_code == 200

    data = response.json()

    assert "logs" in data