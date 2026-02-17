from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_post_card():
    response = client.post(
        "/card",
        json={
            "name": "test",
            "description": "test",
            "deck_id": "0"
        }
    )
    assert response.status_code == 200


def test_get_card_by_id():
    response = client.get("/card/0")
    assert response.status_code == 200


def test_get_cards():
    response = client.get("/card")
    assert response.status_code == 200


def test_put_card():
    response = client.put(
        "/card/0",
        json={
            "name": "put_test",
            "description": "put_test",
            "deck_id": "0"
            }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "put_test"
    assert response.json()["description"] == "put_test"


def test_post_answer():
    good_response = client.post("/card/answer/0?quality=5")
    assert good_response.status_code == 200

    bad_response = client.post("/card/answer/0?quality=0") 
    assert bad_response.status_code == 200

    assert good_response.json()["interval"] > bad_response.json()["interval"]


def test_delete_card():
    response = client.delete("/card/0")
    assert response.status_code == 200
