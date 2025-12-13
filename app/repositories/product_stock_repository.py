from sqlmodel import Session, select
from app.models.product_stock import ProductStockModel


class ProductStockRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_quantity(self, toy_id: int) -> int:
        stock = self.db.exec(
            select(ProductStockModel).where(ProductStockModel.toy_id == toy_id)
        ).first()
        return stock.quantity if stock else 0
