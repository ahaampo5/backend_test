# app/representation/routers/user_router.py
from fastapi import APIRouter, HTTPException
from app.domain.services import UserService
from app.representation.schemas.user_schemas import (
    UserCreateSchema,
    UserResponseSchema
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponseSchema, status_code=201)
def create_user(user_data: UserCreateSchema):
    """
    새 유저를 생성하는 엔드포인트
    """
    created_user = UserService.create_user(user_data)
    if not created_user:
        raise HTTPException(status_code=400, detail="User not created.")
    return created_user

@router.get("/{user_id}", response_model=UserResponseSchema)
def get_user(user_id: int):
    """
    특정 유저를 조회하는 엔드포인트
    """
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user
