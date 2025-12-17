from sqlmodel import SQLModel, Field


class AgeGroupModel(SQLModel, table=True):
    __tablename__ = "age_group"
    age_group_id: int = Field(primary_key=True)
    name: str
    description: str
