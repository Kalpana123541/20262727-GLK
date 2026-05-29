from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# SQL Server Connection
DATABASE_URL = (
    "mssql+pyodbc://@localhost/BookAPI?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes"
    
)

engine = create_engine(DATABASE_URL)


# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to the Book API"}


# Get All Books
@app.get("/books")
def get_books():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT * FROM Books"))

        books = []

        for row in result:
            books.append({
                "id": row.id,
                "title": row.title,
                "available": bool(row.available)
            })

        return books


# Get Available Books
@app.get("/books/available")
def get_available_books():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM Books WHERE available = 1")
        )

        books = []

        for row in result:
            books.append({
                "id": row.id,
                "title": row.title,
                "available": bool(row.available)
            })

        return books


# Get Specific Book Availability
@app.get("/books/{book_id}/availability")
def get_book_availability(book_id: int):

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM Books WHERE id = :id"),
            {"id": book_id}
        )

        book = result.fetchone()

        if not book:
            return {"message": "Book not found"}

        return {
            "title": book.title,
            "available": bool(book.available)
        }


# Update Book Title
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):

    with engine.begin() as connection:

        result = connection.execute(
            text("""
                UPDATE Books
                SET title = :title
                WHERE id = :id
            """),
            {
                "id": book_id,
                "title": updated_book["title"]
            }
        )

        if result.rowcount == 0:
            return {"message": "Book not found"}

        return {"message": "Book updated successfully"}


# Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    with engine.begin() as connection:

        result = connection.execute(
            text("DELETE FROM Books WHERE id = :id"),
            {"id": book_id}
        )

        if result.rowcount == 0:
            return {"message": "Book not found"}

        return {"message": "Book deleted successfully"}