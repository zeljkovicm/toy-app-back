from sqlmodel import Session, select, func
from app.models.review import ReviewModel
from app.schemas.review import Review
from app.models.user import UserModel


class ReviewRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_reviews(self, toy_id: int) -> list[Review]:
        rows = self.db.exec(
            select(ReviewModel, UserModel.name)
            .join(UserModel, UserModel.id == ReviewModel.user_id)
            .where(ReviewModel.toy_id == toy_id)
            .order_by(ReviewModel.created_at.desc())
        ).all()

        return [
            Review(
                review_id=review.review_id,
                toy_id=review.toy_id,
                user_id=review.user_id,
                user_name=user_name,
                rating=review.rating,
                title=review.title,
                comment=review.comment,
                created_at=review.created_at,
            )
            for review, user_name in rows
        ]

    def get_average_rating(self, toy_id: int) -> float:
        avg = self.db.exec(
            select(func.avg(ReviewModel.rating)).where(
                ReviewModel.toy_id == toy_id)
        ).first()

        return float(avg) if avg is not None else 0.0

    def get_review_count(self, toy_id: int) -> int:
        cnt = self.db.exec(
            select(func.count(ReviewModel.review_id)).where(
                ReviewModel.toy_id == toy_id)
        ).first()

        return cnt if cnt is not None else 0
