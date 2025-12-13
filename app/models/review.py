from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class ReviewModel(SQLModel, table=True):
    __tablename__ = "review"
    review_id: int | None = Field(default=None, primary_key=True)
    toy_id: int = Field(index=True)
    title: str | None = Field(default=None, max_length=500)
    user_id: UUID
    rating: int
    comment: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
