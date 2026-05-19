"""Starter code for the FastAPI REST API assignment.

Run locally with:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# Task 1: Add starter records or keep this empty.
books: list[Book] = []


@app.get("/")
def health_check() -> dict[str, str]:
    """Return a simple API status response."""
    return {"status": "ok", "message": "Books API is running"}


# Task 2: Implement CRUD endpoints below.
# - POST /books
# - GET /books
# - GET /books/{book_id}
# - PUT /books/{book_id}
# - DELETE /books/{book_id}


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> Book:
    # TODO: Add duplicate-id check, then append and return the book.
    raise NotImplementedError


@app.get("/books")
def list_books() -> list[Book]:
    # TODO: Return all books.
    raise NotImplementedError


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    # TODO: Return matching book or raise HTTPException(status_code=404).
    raise NotImplementedError


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book) -> Book:
    # TODO: Replace matching book and return it, or raise 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Remove matching book or raise 404.
    raise NotImplementedError
