from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_user_service

from app.schemas.user import (
    UserRegisterRequest,
    UserLoginRequest,
    LoginResponse
)

from app.services.user_service import UserService


router = APIRouter()


@router.post("/register", response_model=LoginResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserRegisterRequest, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(payload)


@router.post("/login", response_model=LoginResponse)
def login(payload: UserLoginRequest, user_service: UserService = Depends(get_user_service)):
    return user_service.authenticate_user(payload)
