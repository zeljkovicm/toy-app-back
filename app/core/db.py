from app.core.config import settings
from sqlmodel import Session, create_engine
from app.models.product_stock import ProductStockModel
from app.models.user import UserModel
from app.models.review import ReviewModel

engine = create_engine(str(settings.db_settings.database_uri()))


def get_db():
    with Session(engine) as session:
        yield session
