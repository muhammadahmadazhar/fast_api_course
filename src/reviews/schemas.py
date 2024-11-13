import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.books.models import Book


class BookModel(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    # Add other fields as necessary

    class Config:
        orm_mode = True


class ReviewModel(BaseModel):
    uid: uuid.UUID
    rating: int = Field(lte=5)
    review_text: str
    user_uid: Optional[uuid.UUID]
    book_uid: Optional[uuid.UUID]
    book: Optional[BookModel]
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


class ReviewCreateModel(BaseModel):
    rating: int = Field(lt=5)
    review_text: str