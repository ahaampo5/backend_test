# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def temp_db():
    """
    DB 초기화 예시. test 실행 전후로 in-memory DB reset 등.
    """
    # setup
    from app.data.db import fake_db
    fake_db.clear()
    yield
    # teardown
    fake_db.clear()
