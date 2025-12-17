from typing import List
from sqlmodel import Session
from app.repositories.product_repository import ProductRepository
from app.schemas.product import AgeGroup, Product, ProductType
from app.schemas.product import Product
from app.exceptions.exceptions import ResourceNotFound


class ProductService:

    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    def get_all_products(self) -> List[Product]:
        rows = self.repository.get_all_products()
        return [self.map_row_to_product_schema(row) for row in rows]

    def get_product_by_permalink(self, permalink: str) -> Product:
        row = self.repository.get_product_by_permalink(permalink)
        if not row:
            raise ResourceNotFound("Proizvod ne postoji.")
        return self.map_row_to_product_schema(row)

    def get_product_by_id(self, toy_id: int) -> Product:
        row = self.repository.get_product_by_id(toy_id)
        if not row:
            raise ResourceNotFound("Proizvod ne postoji.")
        return self.map_row_to_product_schema(row)

    def map_row_to_product_schema(self, row: dict) -> Product:
        return Product(
            toy_id=row["toy_id"],
            name=row["name"],
            permalink=row["permalink"],
            description=row["description"],
            target_group=row["target_group"],
            production_date=row["production_date"],
            price=row["price"],
            image_url=row["image_url"],

            age_group=AgeGroup(
                age_group_id=row["age_group_id"],
                name=row["age_group_name"],
                description=row["age_group_description"],
            ),

            type=ProductType(
                type_id=row["type_id"],
                name=row["type_name"],
                description=row["type_description"],
            ),

            quantity=row["quantity"],
            average_rating=float(row["average_rating"]),
            review_count=row["review_count"],
            reviews=[]
        )
