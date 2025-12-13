from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import router as auth_router
from app.routers.pequla import router as pequla_router
from app.routers.product import router as product_router
from app.exceptions.exceptions import (
    AuthenticationError, UserAlreadyExistsError, ResourceNotFound, ValidationError)
from app.exceptions.exception_handlers import (
    authentication_error_handler, user_already_exists_error_handler, resource_not_found_handler, validation_error_handler)

app = FastAPI(title="Toy Store API", version="1.0.0")

origins = [
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(pequla_router, prefix="/pequla")
app.include_router(product_router, prefix="/enriched")

app.add_exception_handler(AuthenticationError, authentication_error_handler)
app.add_exception_handler(UserAlreadyExistsError,
                          user_already_exists_error_handler)
app.add_exception_handler(ResourceNotFound, resource_not_found_handler)
app.add_exception_handler(ValidationError, validation_error_handler)
