from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# SQL Server Connection
DATABASE_URL = (
    "mssql+pyodbc://@localhost/Northwind?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes"
    
)

engine = create_engine(DATABASE_URL)


# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to the Northwind DB"}


# Get All Products
@app.get("/products")
def get_products():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT * FROM Products"))

        products = []

        for row in result:
            products.append({
                "ProductID": row.ProductID,
                "ProductName": row.ProductName,
                "UnitPrice": float(row.UnitPrice) if row.UnitPrice is not None else None,
                "available" : row.UnitsInStock > 0
            })

        return products


# Get Available Products
@app.get("/products/available")
def get_available_products():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM Products WHERE UnitsInStock > 0")
        )

        products = []

        for row in result:
            products.append({
                "ProductID": row.ProductID,
                "ProductName": row.ProductName,
                "UnitPrice": float(row.UnitPrice)  if row.UnitPrice is not None else None,
                "available": bool(row.UnitsInStock > 0)
            })

        return products


# Get Specific Product Availability
@app.get("/products/{product_id}/availability")
def get_product_availability(product_id: int):

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM Products WHERE ProductID = :id"),
            {"id": product_id}
        )

        product = result.fetchone()

        if not product:
            return {"message": "Product not found"}

        return {
            "title": product.ProductName,
            "available": product.UnitsInStock > 0
        }
    
    
# Update Product Name
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: dict):

    with engine.begin() as connection:

        result = connection.execute(
            text("""
                UPDATE Products
                SET ProductName = :name
                WHERE ProductID = :id
            """),
            {
                "id": product_id,
                "name": updated_product["ProductName"]
            }
        )

        if result.rowcount == 0:
            return {"message": "Product not found"}

        return {"message": "Product updated successfully"}


# Delete Product
@app.delete("/products/{product_id}")
def delete_book(product_id: int):

    with engine.begin() as connection:

        try:
            result = connection.execute(
                text("DELETE FROM Products WHERE ProductID = :id"),
                {"id": product_id}
            )

            if result.rowcount == 0:
                return {"message": "Product not found"}

            return {"message": "Product deleted successfully"}

        except Exception:
            return {"message": "Cannot delete product (linked to orders)"}