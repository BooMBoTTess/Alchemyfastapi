import uvicorn
from fastapi import FastAPI
from src.authentication.router import router as user_router
from src.Informations.router import router as info_router

app = FastAPI(
    title='Training application'
)

app.include_router(user_router)
app.include_router(info_router)

@app.get('/')
def uuu(num):
    return 'Иииуносит меня'

if __name__ == '__main__':

    uvicorn.run('test:app', host='127.0.0.1', port=8000, reload=True)