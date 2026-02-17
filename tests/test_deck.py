from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_post_deck():
    response = client.post(
        "/deck",
        json={
            "name": "test",
            "algorithm": "test"
            }
    )
    assert response.status_code == 200


def test_get_deck_by_id():
    response = client.get("/deck/0")
    assert response.status_code == 200


def test_get_decks():
    response = client.get("/deck")
    assert response.status_code == 200


def test_put_deck():
    response = client.put(
        "/deck/0",
        json={
            "name": "test",
            "algorithm": "test"
            }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "test"
    assert response.json()["algorithm"] == "test"


def test_get_all_deck_cards():
    response = client.get("/deck/0/cards")
    assert response.status_code == 200


def test_get_learn_deck_cards():
    response = client.get("/deck/0/learn")
    assert response.status_code == 200


def test_delete_deck():
    response = client.delete("/deck/0")
    assert response.status_code == 200

