from sqlmodel import SQLModel, Field


class ProductStockModel(SQLModel, table=True):
    __tablename__ = "productstock"
    toy_id: int = Field(primary_key=True, index=True)
    quantity: int = Field(nullable=False, default_factory=0)
