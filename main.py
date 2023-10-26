from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.authentication.auth import auth_backend
from src.authentication.schemas import UserRead, UserCreate
from src.authentication.user_manager import fastapi_users

from src.authentication.router import router as user_router
from src.Informations.router import router as info_router

app = FastAPI(
    title='Training application'
)

app.include_router(user_router)
app.include_router(info_router)

@app.get('/')
def uuu(num):
    return 'Я не мертв, я живой, муррр'

