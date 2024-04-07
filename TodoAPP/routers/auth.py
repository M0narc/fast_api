from fastapi import APIRouter
from users_requests import CreateUserRequests
from models import Users

router = APIRouter()


@router.post("/auth/")
async def create_users(create_user_request: CreateUserRequests):
    """
    endpoint to create users, we will not be unpackig **create_user_request
    since we can't, we have a password right now in our models
    """
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=create_user_request.password,
        is_active=True
    )

    return create_user_model
