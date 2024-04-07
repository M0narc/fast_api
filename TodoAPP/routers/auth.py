from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from users_requests import CreateUserRequests
from models import Users
from passlib.context import CryptContext

router = APIRouter()


def get_db():
    """
    db dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def create_users(db: db_dependency,
                       create_user_request: CreateUserRequests):
    """
    endpoint to create users, we will not be unpackig **create_user_request
    since we can't, we have a password right now in our models
    we are hashing the password using bcrypt
    """
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()
