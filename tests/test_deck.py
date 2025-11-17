from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_desks():
    response = client.get("/deck")
    assert response.status_code == 200