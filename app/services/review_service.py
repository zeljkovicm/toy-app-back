from fastapi import HTTPException, status
from sqlmodel import Session
from uuid import UUID


from app.repositories.review_repository import ReviewRepository
from app.models.review import ReviewModel
from app.schemas.review import Review, RatingBreakdownItem, RatingSummary


class ReviewService:

    def __init__(self, db: Session):
        self.review_repository = ReviewRepository(db)

    def get_reviews_for_product(self, toy_id: int) -> list[Review]:
        rows = self.review_repository.get_reviews_by_toy_id(toy_id)
        return [self.map_reviews(review=r, user_name=u) for r, u in rows]

    def get_rating_summary(self, toy_id: int) -> RatingSummary:
        average = self.review_repository.get_average_rating(toy_id)
        count = self.review_repository.get_review_count(toy_id)
        breakdown_raw = self.review_repository.get_rating_breakdown(toy_id)

        breakdown = []
        for stars in [5, 4, 3, 2, 1]:
            star_count = breakdown_raw.get(stars, 0)
            percentage = (star_count / count * 100) if count > 0 else 0

            breakdown.append(
                RatingBreakdownItem(
                    stars=stars,
                    count=star_count,
                    percentage=percentage
                )
            )

        return RatingSummary(
            average_rating=average,
            review_count=count,
            breakdown=breakdown
        )

    @staticmethod
    def map_reviews(review: ReviewModel, user_name: str) -> Review:
        return Review(
            review_id=review.review_id,
            toy_id=review.toy_id,
            user_id=review.user_id,
            user_name=user_name,
            rating=review.rating,
            title=review.title,
            comment=review.comment,
            created_at=review.created_at
        )
