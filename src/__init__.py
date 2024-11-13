from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager

from src.db.main import initdb
from src.reviews.routes import review_router


#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await initdb()
    yield
    print("server is stopping")

version = 'v1'

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version= version,
    # lifespan=lifespan because now we are using alembic for database changes
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["reviews"])