from typing import List

from pydantic import BaseModel
from datetime import datetime, date
import uuid

from src.db.models import Review


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    # reviews: List[Review]
    created_at: datetime
    updated_at:datetime

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

class BookCreateModel(BaseModel):
    """
        This class is used to validate the request when creating or updating a book
    """
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str