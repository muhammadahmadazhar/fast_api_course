from fastapi import FastAPI, APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import Optional, List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel, BookCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.services import BookService
from src.db.main import get_session
from src.auth.dependencies import AccessTokenBearer

book_router = APIRouter()
book_service = BookService()
acccess_token_bearer = AccessTokenBearer()

# @book_router.get('/')
# async def root():
#     return {"message": "Hello World"}
#
#
# @book_router.get('/greet/{name}')
# async def greet_name(name: str, age: int) -> dict:
#     return {"message": f"Hello {name}", "age": age}
# # name is url path and age is queryparam
#
# @book_router.get('/greeting')
# async def greeting(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}", "age": age}
# # name and age are optional queryparams with default values
#
# @book_router.get("/books", response_model=List[Book])
# async def get_all_books():
#     return books
#
#
# @book_router.post("/books", status_code=status.HTTP_201_CREATED)
# async def create_a_book(book_data: Book) -> dict:
#     # model_dump method convert book_data into a dictionary
#     new_book = book_data.model_dump()
#
#     books.append(new_book)
#
#     return new_book
#
#
# @book_router.get("/book/{book_id}")
# async def get_book(book_id: int) -> dict:
#     for book in books:
#         if book["id"] == book_id:
#             return book
#
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
#
#
# @book_router.patch("/book/{book_id}")
# async def update_book(book_id: int,book_update_data:BookUpdateModel) -> dict:
#
#     for book in books:
#         if book['id'] == book_id:
#             book['title'] = book_update_data.title
#             book['publisher'] = book_update_data.publisher
#             book['page_count'] = book_update_data.page_count
#             book['language'] = book_update_data.language
#
#             return book
#
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
#
#
# @book_router.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
# async def delete_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             books.remove(book)
#
#             return {}
#
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session),
                        token_details=Depends(acccess_token_bearer)):
    books = await book_service.get_all_books(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session),
    token_details: dict = Depends(acccess_token_bearer),
) -> dict:
    user_id = token_details.get("user")["user_uid"]
    new_book = await book_service.create_book(book_data,user_id, session)
    return new_book


@book_router.get("/{book_uid}", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_uid, session)

    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
) -> dict:

    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    else:
        return updated_book


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if book_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:

        return {}