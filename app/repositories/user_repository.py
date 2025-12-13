from uuid import UUID
from sqlmodel import Session, select
from app.models.user import UserModel


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, user: UserModel) -> UserModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str) -> UserModel | None:
        return self.db.exec(statement=select(UserModel).where(
            UserModel.email == email, UserModel.is_deleted == False)).first()

    def get_by_id(self, user_id: UUID) -> UserModel | None:
        return self.db.exec(select(UserModel).where(UserModel.id == user_id,
                                                    UserModel.is_deleted == False)).first()
