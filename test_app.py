import json
from app import app

def test_analyze_no_code():
    client = app.test_client()
    rv = client.post("/analyze", json={})
    assert rv.status_code == 400

def test_analyze_with_code():
    client = app.test_client()
    rv = client.post("/analyze", json={"filename": "calc.py", "code": "def add(a,b): return a+b"})
    assert rv.status_code == 200
    data = rv.get_json()
    assert "linter" in data
    assert "ai" in data
