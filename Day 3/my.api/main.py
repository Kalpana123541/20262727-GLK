from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Harry Potter", "available": True},
    {"id": 2, "title": "Harry Potter2", "available": False},
    {"id": 3, "title": "Harry Potter3", "available": True}
]
# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to the Book API"}

#Get All Book
@app.get("/books")
def get_books():
    return books

#Get availbility of all book
def get_available_books():

    available_books = [
        book for book in books if book["available"] == True
    ]

    return available_books

#Get Only Available Books
@app.get("/books/available")
def get_available_books():
    available_books = [
        book for book in books if book["available"] == "True"
    ]   
    return available_books

#Get Availbility of Specific Book
@app.get("/books/{book_id}/availability")
def get_book_availability(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"title": book["title"],
                    "available": book["available"]
                }
    return {"Message": "Book not found"}

#Update Book Title
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):

    for book in books:

        if book["id"] == book_id:

            if "title" in updated_book:
                book["title"] = updated_book["title"]

            return {
                "message": "Book updated successfully",
                "book": book
            }

    return {"message": "Book not found"}



#Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for index, book in enumerate(books):

        if book["id"] == book_id:

            deleted_book = books.pop(index)

            return {
                "message": "Book deleted successfully",
                "deleted_book": deleted_book
            }

    return {"message": "Book not found"}