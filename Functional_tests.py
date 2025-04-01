# tests/test_functional_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_note():
    response = client.get("/notes/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_read_note_not_found():
    response = client.get("/notes/999")
    assert response.status_code == 404

def test_create_note():
    new_note = {"title": "Test Note", "content": "This is a test note"}
    response = client.post("/notes/", json=new_note)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Note"

# Додайте тести для інших маршрутів API (update_note, delete_note, etc.)
