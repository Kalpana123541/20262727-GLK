# API Notes

## Overview
This API was built using FastAPI and connected to a Microsoft SQL Server (Northwind Database). The API allows users to retrieve, update, and manage product information through RESTful endpoints.

The API follows REST principles and returns data in JSON format, making it easy to integrate with web, desktop, or mobile applications.

# What is an API?
An API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other.

In a web API:

A client sends a request
The server processes the request
The API returns a response
Example: GET /products
The API retrieves product data from the database and returns it as JSON.

APIs are commonly used for:
Web applications
Mobile apps
Cloud services
Payment systems
Authentication systems
Data sharing between applications

# What you built and why it could be useful?
This project implements a REST API connected to the Northwind SQL Server database.
Features Implemented:
1.  Retrieve All Products: 
    GET /products
    Returns all available products from the database.

2.  Retrieve Available Products: 
    GET /products/available
    Returns only products currently in stock.

3.  Check Product Availability:
    GET /products/{product_id}/availability
    Checks whether a specific product is available.

4.  Update Product Information:
    PUT /products/{product_id}
    Updates product details such as product name.

5.  Delete a Product:
    DELETE /products/{product_id}
    Deletes a product if it is not linked to existing orders.

6.  Test cases:
    Created the Test cases for all above scenarios

Why This API Is Useful:
This API demonstrates:
    Real database integration using SQL Server
    RESTful API development
    CRUD operations
    Error handling
    API testing with pytest
    SQL query execution using SQLAlchemy

Potential real-world uses:
    Inventory management systems
    E-commerce platforms
    Warehouse management
    Internal business systems
    Product catalog services

# Best practise Used:   
    
    1.  RESTful Routing: Endpoints follow standard REST conventions:

        GET → Retrieve data
        PUT → Update data
        DELETE → Remove data

    2.  Database Integration
        Instead of using a fake in-memory list, the API connects to a real SQL Server database.

        Benefits:
        Persistent storage
        Real-world scalability
        Better testing and validation
    
    3.  Error Handling:
        The API safely handles:
        Missing products
        Invalid requests
        Foreign key constraint errors
        Database exceptions
        Example: return {"message": "Product not found"}
    4.  Parameterized SQL Queries
        SQL queries use parameters to help prevent SQL injection attacks.

        Example:text("SELECT * FROM Products WHERE ProductID = :id")

    5.  API Testing
        Test cases were written using:
        pytest
        FastAPI TestClient

        Testing ensures:
        API reliability
        Stable functionality
        Easier debugging

Future Scope of Work:
    1.1Add Authentication:
        Implement:  
        JWT Authentication
        OAuth2
        Role-based access control

    This would secure the API for production environments.

    2.  Add POST Endpoint:
        Allow users to create new products:
        POST /products

    3.  Pagination and Filtering: 
        Support:
            Page-based results
            Search functionality
            Sorting
            Filtering
            Example:GET /products?page=1&limit=10

    4.  CI/CD Integration
        Automate:
            Testing
            Deployment
            Code quality checks
        Using:
            GitHub Actions
            Azure DevOps    

    5.  API Documentation Improvements:
        Enhance Swagger/OpenAPI documentation with:
            Detailed schemas
            Response examples
            Authentication examples        

 Running the Project or Terminal Commands:

1. Navigate to Project Folder
cd "C:\Users\Admin\Desktop\20262727-GLK\Day 3\my.api"

2. Create Virtual Environment
python -m venv venv

3. Activate Virtual Environment: Windows PowerShell
.\venv\Scripts\Activate

4. Install Required Packages
pip install fastapi uvicorn sqlalchemy pyodbc pytest httpx

5. Verify Installed Packages
pip list


Run FastAPI Server:
1. Start the API Server: If file name is main.py:
uvicorn main:app --reload

2. Expected Successful Output:
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.

3. Open Swagger Documentation:
http://127.0.0.1:8000/docs

Run Tests:
1.  Execute All Tests:
    pytest -v

2.  Run Tests with Print Statements:
    pytest -s

3.  Run Specific Test File:
    pytest test_maindb.py -v

Debugging Commands    
1.  Check Files in Current Folder:
    dir

2.  Test Python File Directly:    
    python main.py

3.  Stop Server:    
    CTRL + C

4.  Final Workflow Summary:
    cd "Day 4A\my.api"
    pip install fastapi uvicorn sqlalchemy pyodbc pytest httpx

    uvicorn main:app --reload

    pytest -v


 Conclusion:
This project demonstrates the development of a production-style REST API using:
        FastAPI
        SQL Server
        SQLAlchemy
        pytest  
It showcases database integration, CRUD functionality, API testing, and error handling while following modern backend development practices.            