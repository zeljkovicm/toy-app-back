from app.services.pequla_service import PequlaService
from app.repositories.product_stock_repository import ProductStockRepository
from app.repositories.review_repository import ReviewRepository
from app.schemas.product import Product
from sqlmodel import Session


class ProductService:

    @staticmethod
    async def get_all_products(db: Session) -> list[Product]:
        products = await PequlaService.get_all_toys()

        stock_repo = ProductStockRepository(db)
        review_repo = ReviewRepository(db)

        enriched = []
        for p in products:
            p.quantity = stock_repo.get_quantity(p.toy_id)
            p.review_count = review_repo.get_review_count(p.toy_id)
            p.average_rating = review_repo.get_average_rating(p.toy_id)
            p.reviews = review_repo.get_reviews(p.toy_id)

            enriched.append(p)
        return enriched

    @staticmethod
    async def get_product_by_permalink(db: Session, permalink: str) -> Product:
        product = await PequlaService.get_toy_by_permalink(permalink)

        stock_repo = ProductStockRepository(db)
        review_repo = ReviewRepository(db)
        product.quantity = stock_repo.get_quantity(product.toy_id)
        product.review_count = review_repo.get_review_count(product.toy_id)
        product.average_rating = review_repo.get_average_rating(product.toy_id)
        product.reviews = review_repo.get_reviews(product.toy_id)

        return product
