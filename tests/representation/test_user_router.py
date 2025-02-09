# tests/representation/test_user_router.py
import pytest

def test_create_user(client, temp_db):
    """ /users 엔드포인트 POST 요청 테스트 """
    response = client.post(
        "/users",
        json={"username": "alice", "email": "alice@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"

def test_get_user(client, temp_db):
    """ /users 엔드포인트 GET 요청 테스트 """
    # 먼저 유저 생성
    create_res = client.post(
        "/users",
        json={"username": "bob", "email": "bob@example.com"}
    )
    user_data = create_res.json()
    user_id = user_data["user_id"]

    # GET으로 조회
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "bob"
    assert data["email"] == "bob@example.com"
