# app/domain/services.py
from typing import Optional
from app.data.repositories import UserRepository
from app.domain.entities import User
from app.representation.schemas.user_schemas import UserCreateSchema

class UserService:
    @staticmethod
    def create_user(user_data: UserCreateSchema) -> Optional[User]:
        """
        새 유저 생성 비즈니스 로직
        """
        # 간단한 예시: username 중복 검사 등
        existing_user = UserRepository.get_by_username(user_data.username)
        if existing_user:
            return None  # 이미 존재하면 None 리턴 (실제로는 예외 처리 가능)

        # 도메인 엔티티 생성
        new_user = User(
            user_id=0,  # 실제 저장시 자동 생성
            username=user_data.username,
            email=user_data.email
        )
        # DB 저장
        saved_user = UserRepository.save(new_user)
        return saved_user

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """
        유저 조회 비즈니스 로직
        """
        return UserRepository.get_by_id(user_id)
    
    # 필요하다면 다른 비즈니스 로직을 추가
    # ex) update_user, delete_user 등
