from typing import Any
from sqlalchemy.orm import Session
from fastapi import Depends, Response
from app.core.db import get_db
from app.services.user_service import UserService
from app.services.order_service import OrderService
from app.exceptions.exceptions import InvalidTokenError, ExpiredTokenError, ResourceNotFound

from uuid import UUID
from fastapi.security import OAuth2PasswordBearer
from app.models.user import UserModel
from app.helpers.jwt_helper import decode_access_token


oauth_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)


def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)) -> UserModel:
    try:
        payload = decode_access_token(token)
        user_id: str | None = payload.get("sub")

        if not user_id:
            raise InvalidTokenError("Invalid token payload")
    except ExpiredTokenError:
        raise ExpiredTokenError("Expired token payload")

    user = db.get(UserModel, UUID(user_id))

    if not user:
        raise ResourceNotFound("User not found")
    return user
