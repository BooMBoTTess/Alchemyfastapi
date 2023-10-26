from fastapi import APIRouter

from src.authentication.auth import auth_backend
from src.authentication.schemas import UserRead, UserCreate
from src.authentication.user_manager import fastapi_users

router = APIRouter(
    prefix='/user',
    tags=['auth']
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)



@router.get('/')
def uwu(num):
    return 1



