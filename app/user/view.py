from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.user.schema import UserSchema, CreateUserSchema
from app.user.service import UserService, get_users_service

router = APIRouter(tags=["user"])


@router.post("/users/", response_model=UserSchema, status_code=HTTPStatus.CREATED)
def create_user(
    user: CreateUserSchema, user_service: UserService = Depends(get_users_service)
):
    return user_service.create(user)


@router.get("/users/", response_model=list[UserSchema])
def read_users(user_service: UserService = Depends(get_users_service)):
    return user_service.list()
