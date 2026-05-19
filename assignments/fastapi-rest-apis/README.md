# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and Python. In this assignment, you will design endpoints, validate data with Pydantic models, and return clear JSON responses for clients.

## 📝 Tasks

### 🛠️	Set Up the FastAPI Application

#### Description
Create a FastAPI app with a health-check route and an in-memory data store for managing a collection of books.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Define a `GET /` or `GET /health` endpoint that returns a status message.
- Store book records in memory (list or dictionary).
- Include fields for each book such as `id`, `title`, `author`, and `year`.


### 🛠️	Build CRUD Endpoints

#### Description
Implement Create, Read, Update, and Delete endpoints for books. Use request/response models so input is validated and output format stays consistent.

#### Requirements
Completed program should:

- Add an endpoint to create a new book (`POST /books`).
- Add endpoints to read all books and one book by ID (`GET /books`, `GET /books/{book_id}`).
- Add an endpoint to update a book (`PUT /books/{book_id}`).
- Add an endpoint to delete a book (`DELETE /books/{book_id}`).
- Return appropriate HTTP status codes and clear error messages when a book is not found.
