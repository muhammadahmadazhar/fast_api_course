from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from src.config import Config
from src.books.models import Book

async_engine = AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True
))


async def initdb():
    """create a connection to our db"""

    async with async_engine.begin() as conn:
        # statement = text("select 'Hello World'")
        #
        # result = await conn.execute(statement)
        #
        # print(result)
        await conn.run_sync(SQLModel.metadata.create_all)

    ...  # rest of main.py

async def get_session() -> AsyncSession:
    """Dependency to provide the session object"""

    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session