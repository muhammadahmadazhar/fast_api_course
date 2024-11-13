import uuid
from datetime import datetime
from typing import List

from sqlmodel import Field
from pydantic import  BaseModel

from src.books.models import Book


class UserCreateModel(BaseModel):
    first_name: str =Field(max_length=25)
    last_name:  str =Field(max_length=25)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str  = Field(min_length=6)


class UserModel(BaseModel):
    uid: uuid.UUID
    first_name: str
    last_name:  str
    username: str
    email: str
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at:datetime


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str  = Field(min_length=6)


class UserBooksModel(UserModel):
    books: List[Book]