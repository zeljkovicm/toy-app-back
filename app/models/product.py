from sqlmodel import SQLModel, Field
from datetime import date


class ProductModel(SQLModel, table=True):
    __tablename__ = "product"

    toy_id: int = Field(primary_key=True, index=True)
    name: str
    permalink: str
    description: str
    target_group: str
    production_date: date
    price: float
    image_path: str
    age_group_id: int = Field(foreign_key="age_group.age_group_id")
    type_id: int = Field(foreign_key="product_type.type_id")
