from app.schemas.camel_case_model import CamelCaseModel
from datetime import datetime
from uuid import UUID
from app.schemas.review import Review


class AgeGroup(CamelCaseModel):
    age_group_id: int
    name: str
    description: str


class ProductType(CamelCaseModel):
    type_id: int
    name: str
    description: str


class Product(CamelCaseModel):
    toy_id: int
    name: str
    permalink: str
    description: str
    target_group: str
    production_date: datetime
    price: float
    image_url: str
    age_group: AgeGroup
    type: ProductType

    quantity: int = 0
    average_rating: float = 0.0
    review_count: int = 0
    reviews: list[Review] = []
