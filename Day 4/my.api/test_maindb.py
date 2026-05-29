from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test Home Route
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Book API"
    }


# Test Get All Books
def test_get_books():
    response = client.get("/books")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test Get Available Books
def test_get_book_availability():
    response = client.get("/books/1/availability")

    assert response.status_code == 200

    data = response.json()

    assert data["available"] == True


# Test Get Book Availability
def test_get_book_availability():
    response = client.get("/books/1/availability")

    assert response.status_code == 200

    data = response.json()

    assert data["available"] == True


# Test Update Book
def test_update_book_title():

    response = client.put(
        "/books/1",
        json={
            "title": "Updated Harry Potter"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["book"]["title"] == "Updated Harry Potter"


# Test Delete Book
def test_delete_book():

    response = client.delete("/books/3")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Book deleted successfully"