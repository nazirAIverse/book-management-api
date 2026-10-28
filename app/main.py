from fastapi import FastAPI

from app.routers.books import router as books_router
from app.routers.auth import router as auth_router


app = FastAPI(title="Book Management API")


app.include_router(books_router)
app.include_router(auth_router)
