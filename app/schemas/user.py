from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


from pydantic import EmailStr, Field
from app.schemas.camel_case_model import CamelCaseModel


class UserRegisterRequest(CamelCaseModel):
    email: str
    name: str
    password: str
    confirm_password: str


class UserLoginRequest(CamelCaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(CamelCaseModel):
    id: UUID
    email: str
    name: str
    image_url: str | None = None
    created_at: datetime
    updated_at: datetime


class LoginResponse(CamelCaseModel):
    user: UserResponse
    access_token: str
    token_type: str = "bearer"
