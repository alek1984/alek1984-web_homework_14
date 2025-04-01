import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_note():
    response = client.get("/notes/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

# Додайте інші тести для маршрутів API