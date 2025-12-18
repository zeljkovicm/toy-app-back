from fastapi import APIRouter, Depends

from app.core.dependencies import get_review_service, get_current_user
from app.schemas.review import Review, RatingSummary, ReviewCreate
from app.services.review_service import ReviewService


router = APIRouter()


@router.get("/{toy_id}", response_model=list[Review])
def get_reviews_for_product(toy_id: int, review_service=Depends(get_review_service)):
    return review_service.get_reviews_for_product(toy_id)


@router.get("/{toy_id}/summary", response_model=RatingSummary)
def get_rating_summary(toy_id: int, review_service: ReviewService = Depends(get_review_service)):
    return review_service.get_rating_summary(toy_id)


@router.post("/", response_model=Review)
def create_review(data: ReviewCreate, user=Depends(get_current_user), service: ReviewService = Depends(get_review_service)):
    return service.create_review(user, data)
