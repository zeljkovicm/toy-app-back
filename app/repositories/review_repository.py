from sqlmodel import Session, select, func, text
from app.models.review import ReviewModel
from app.schemas.review import Review
from app.models.user import UserModel
from uuid import UUID


class ReviewRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_reviews_by_toy_id(self, toy_id: int):
        return self.db.exec(
            select(ReviewModel, UserModel.name)
            .join(UserModel, UserModel.id == ReviewModel.user_id)
            .where(ReviewModel.toy_id == toy_id)
            .order_by(ReviewModel.created_at.desc())
        ).all()

    def get_average_rating(self, toy_id: int) -> float:
        avg = self.db.exec(
            select(func.avg(ReviewModel.rating))
            .where(ReviewModel.toy_id == toy_id)
        ).first()

        return float(avg) if avg else 0.0

    def get_review_count(self, toy_id: int) -> int:
        return self.db.exec(
            select(func.count(ReviewModel.review_id))
            .where(ReviewModel.toy_id == toy_id)
        ).one()

    def get_rating_breakdown(self, toy_id: int) -> dict[int, int]:
        rows = self.db.exec(
            select(ReviewModel.rating, func.count())
            .where(ReviewModel.toy_id == toy_id)
            .group_by(ReviewModel.rating)
        ).all()

        return {rating: count for rating, count in rows}
