from fastapi import FastAPI
app = FastAPI()

#Fake 
books = [
    {"id1": 1, "title": "Harry Potter", "available": "True"},
    {"id1": 2, "title": "Harry Potter2", "available": "False"},
    {"id1": 3, "title": "Harry Potter3", "available": "True"}
]
# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to the Book API"}

#Get All Book
@app.get("/books")
def get_books():
    return list(books.values())