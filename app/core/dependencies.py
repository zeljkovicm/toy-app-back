from typing import Any
from sqlalchemy.orm import Session
from fastapi import Depends, Response
from app.core.db import get_db
from app.services.user_service import UserService

from uuid import UUID


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)
