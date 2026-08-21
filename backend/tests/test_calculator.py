import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.calculator import calculate

client = TestClient(app)

def test_addition():
    assert calculate("2 + 3") == 5.0

def test_subtraction():
    assert calculate("10 - 4") == 6.0

def test_multiplication():
    assert calculate("3 * 4") == 12.0

def test_division():
    assert calculate("10 / 2") == 5.0

def test_complex_expression():
    assert calculate("(2 + 3) * 4") == 20.0

def test_empty_expression():
    with pytest.raises(ValueError, match="Expression cannot be empty"):
        calculate("")

def test_invalid_characters():
    with pytest.raises(ValueError, match="Invalid characters"):
        calculate("2 + 3; drop table")

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate("10 / 0")

def test_api_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_api_calculate():
    response = client.post("/calculate", json={"expression": "2 + 3"})
    assert response.status_code == 200
    assert response.json()["result"] == 5.0

def test_api_invalid_expression():
    response = client.post("/calculate", json={"expression": "abc"})
    assert response.status_code == 400