from app.schemas.camel_case_model import CamelCaseModel
from uuid import UUID
from datetime import datetime


class Review(CamelCaseModel):
    review_id: int
    toy_id: int
    user_id: UUID
    user_name: str
    rating: int
    title: str | None = None
    comment: str
    created_at: datetime
