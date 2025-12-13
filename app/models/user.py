from sqlmodel import Field, SQLModel
from datetime import datetime
import uuid


class UserModel(SQLModel, table=True):
    """
        User table in database.
    """

    __tablename__ = "user"
    id: uuid.UUID = Field(default_factory=uuid.uuid4,
                          primary_key=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, nullable=False, max_length=255)
    name: str = Field(max_length=100, nullable=False)
    hashed_password: str = Field(nullable=False, max_length=255)
    image_url: (str | None) = Field(default=None, max_length=500)
    is_active: bool = Field(default=True, nullable=False)
    is_deleted: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
