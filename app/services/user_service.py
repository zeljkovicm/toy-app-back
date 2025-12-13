from sqlmodel import Session

from app.models.user import UserModel
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRegisterRequest, UserLoginRequest, UserResponse, LoginResponse

from app.helpers.jwt_helper import create_access_token
from app.helpers.password_helper import hash_password, verify_password
from app.exceptions.exceptions import (
    UserAlreadyExistsError, AuthenticationError, ValidationError)


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, data: UserRegisterRequest) -> LoginResponse:
        existing = self.repository.get_by_email(data.email)
        if existing:
            raise UserAlreadyExistsError(
                f"Email {data.email} je već u upotrebi.")

        if data.password != data.confirm_password:
            raise ValidationError("Lozinke se ne poklapaju!")

        hashed = hash_password(data.password)

        user = UserModel(
            email=data.email,
            name=data.name,
            hashed_password=hashed
        )

        created = self.repository.create(user)
        access_token = create_access_token({"sub": str(user.id)})

        return LoginResponse(
            user=UserResponse.model_validate(created),
            access_token=access_token
        )

    def authenticate_user(self, data: UserLoginRequest) -> LoginResponse:
        user = self.repository.get_by_email(data.email)

        if not user or not verify_password(data.password, user.hashed_password):
            raise AuthenticationError("Pogrešan email ili lozinka.")

        access_token = create_access_token({"sub": str(user.id)})

        return LoginResponse(
            user=UserResponse.model_validate(user),
            access_token=access_token
        )
