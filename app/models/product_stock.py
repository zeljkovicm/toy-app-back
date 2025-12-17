from sqlmodel import SQLModel, Field


class ProductStockModel(SQLModel, table=True):
    __tablename__ = "productstock"
    toy_id: int = Field(primary_key=True, index=True,
                        foreign_key="product.toy_id")
    quantity: int = Field(default=0)
