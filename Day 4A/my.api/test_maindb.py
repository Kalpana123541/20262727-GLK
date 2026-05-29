from fastapi.testclient import TestClient
from maindb import app

client = TestClient(app)


# Test Home Route
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert "Northwind DB" in response.json()["message"]

# Test Get All Products
def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    if len(data) > 0:
        product = data[0]
        assert "ProductID" in product
        assert "ProductName" in product
        assert "UnitPrice" in product
        assert "available" in product


# Test Get Available Products
def test_get_product_availability():
    response = client.get("/products/1/availability")

    assert response.status_code == 200

    data = response.json()

    for product in data:
       assert data["available"] == "Product not found"
       return  


# Test Get Specific Product Availability
def test_get_product_availability():

    response = client.get("/products/1/availability")

    assert response.status_code == 200

    data = response.json()

    assert data["title"] is not None
    assert data["available"] == True


# Test Update Product
def test_update_product_name():

    response = client.put(
        "/products",
        json={
            "ProductName": "Chai Updated"
        }
    )
    data = response.json()
    if response.status_code == 200:
        assert data["detail"] == "Product not found"
        return

    


# Test Delete Product
def test_delete_product():

    response = client.delete("/products/99999")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product not found"