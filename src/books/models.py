from typing import Optional, List

from sqlmodel import SQLModel, Field, Column, Relationship
from datetime import datetime, date
import sqlalchemy.dialects.postgresql as pg
import sqlalchemy as sa
import uuid

from src.auth.models import User


class Book(SQLModel , table=True):
    __tablename__ = "books"

    uid:uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False,
            default=uuid.uuid4
        )
    )

    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language:str
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="user_accounts.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    user: Optional[User] = Relationship(back_populates="books")
    reviews: List["Review"] = Relationship(
        back_populates="book", sa_relationship_kwargs={"lazy": "selectin"}
    )

    def __repr__(self) -> str:
        return f"<Book {self.title}>"