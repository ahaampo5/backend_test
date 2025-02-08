# app/representation/schemas/user_schemas.py
from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr

class UserResponseSchema(BaseModel):
    user_id: int
    username: str
    email: EmailStr
