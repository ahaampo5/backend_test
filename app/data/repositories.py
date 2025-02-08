# app/data/repositories.py
from typing import Optional
from app.data.db import fake_db
from app.domain.entities import User

# 간단한 In-Memory DB 예시
auto_increment_id = 1

class UserRepository:
    @staticmethod
    def save(user: User) -> User:
        global auto_increment_id
        user.user_id = auto_increment_id
        fake_db[auto_increment_id] = user
        auto_increment_id += 1
        return user

    @staticmethod
    def get_by_id(user_id: int) -> Optional[User]:
        return fake_db.get(user_id)

    @staticmethod
    def get_by_username(username: str) -> Optional[User]:
        for stored_user in fake_db.values():
            if stored_user.username == username:
                return stored_user
        return None
