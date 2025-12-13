from datetime import datetime, timedelta, timezone
from fastapi import Response
from uuid import UUID

from jose import jwt

from app.core.config import settings
jwt_settings = settings.jwt_settings

SECRET_KEY = jwt_settings.jwt_secret_key
ALGORITHM = jwt_settings.jwt_algorithm
ACCESS_EXPIRE_MINUTES = jwt_settings.jwt_access_expiration_minutes
REFRESH_EXPIRE_MINUTES = jwt_settings.jwt_refresh_expiration_minutes


def _create_token(data: dict, minutes: int, token_type: str) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=minutes)
    to_encode.update({"exp": expire, "type": token_type})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_access_token(data: dict) -> str:
    return _create_token(data, ACCESS_EXPIRE_MINUTES, "access")


def create_refresh_token(data: dict) -> str:
    return _create_token(data, REFRESH_EXPIRE_MINUTES, "refresh")


def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("type") != "access":
        raise ValueError("Invalid token type")
    return payload


def decode_refresh_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("type") != "refresh":
        raise ValueError("Invalid token type")
    return payload


def set_refresh_cookie(response: Response, token: str):
    response.set_cookie(
        key="refresh_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
        max_age=60 * 60 * 24 * 30,
    )
