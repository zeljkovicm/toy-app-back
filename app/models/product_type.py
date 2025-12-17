from sqlmodel import SQLModel, Field


class ProductTypeModel(SQLModel, table=True):
    __tablename__ = "product_type"

    type_id: int = Field(primary_key=True)
    name: str
    description: str
