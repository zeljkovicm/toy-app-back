from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.exceptions.exceptions import (
    AuthenticationError,
    UserAlreadyExistsError,
    ResourceNotFound,
    ValidationError,
    InvalidTokenError,
    ExpiredTokenError,
    OrderNotFound,
    ReviewAlreadyExistError,
    ReviewNotAllowedError
)


async def authentication_error_handler(request: Request, exception: AuthenticationError):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exception)})


async def user_already_exists_error_handler(request: Request, exception: UserAlreadyExistsError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exception)})


async def resource_not_found_handler(request: Request, exception: ResourceNotFound):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exception)})


async def validation_error_handler(request: Request, exception: ValidationError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exception)})


async def invalid_token_error_handler(request: Request, exception: InvalidTokenError):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exception)})


async def expired_token_error_handler(request: Request, exception: ExpiredTokenError):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exception)})


async def order_not_found_error_handler(request: Request, exception: OrderNotFound):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exception)})


async def review_exist_error_handler(request: Request, exception: ReviewAlreadyExistError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exception)})


async def review_not_allowed_error_handler(request: Request, exception: ReviewNotAllowedError):
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": str(exception)})
