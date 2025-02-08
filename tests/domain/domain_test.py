# tests/domain/test_services.py
import pytest
from app.domain.services import UserService
from app.representation.schemas.user_schemas import UserCreateSchema

def test_create_user_success(temp_db):
    user_data = UserCreateSchema(username="testuser", email="test@example.com")
    user = UserService.create_user(user_data)
    assert user is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"

def test_create_user_duplicate(temp_db):
    # 같은 유저명으로 두 번 생성 시도
    user_data = UserCreateSchema(username="duplicate", email="dup@example.com")
    user1 = UserService.create_user(user_data)
    user2 = UserService.create_user(user_data)
    
    assert user1 is not None
    assert user2 is None  # 혹은 예외가 발생해야 함
