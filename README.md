# PYCRAY RESTful API

This repository contains a Flask RESTful API that exposes endpoints to retrieve user and order data from a database.

## Requirements

- Python 3.11
- Flask
- psycopg2
- dotenv

## Database Used
- PostgreSQL

## Note
- Make sure that Python 3.11  and PostgreSQL are installed in your system.

## Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/PoorvKumar/PYCRAY_API.git
 cd PYCRAY_API
``` 
2. Create a Virtual Environment in the project directory:
```python
python -m venv .venv
```
3. Install the dependencies:
```python
pip install -r requirements.txt
```
4. Set up the database:
 - Create a PostgreSQL database on your local machine **(or to use online ElephantSQL uncomment line 11-12 in app.py)**
 - Modify the `connection` configuration in `app.py` with your database details(database name,usernmae,password). Alternatively, you can use environment variables by configuring up the `.env` file in the project directory and providing the necessary database credentials or use existing credentials. 
 - Use the Queries in User.txt and Orders.txt to create table and insert sample data in your tables in the same database.
5. Activate the Virtual Enviroment:
```python
  .venv/Scripts/Activate.ps1
```
5. Run the Application:
```python
flask run
```

The Flask API will be running at `http://localhost:5000/`.

## Endpoints

### Get all users

- **Endpoint**: `/users`
- **Method**: GET
- **Response**: Returns a list of all users in the system.

### Get user details

- **Endpoint**: `/users/{id}`
- **Method**: GET
- **Response**: Returns the details of a specific user identified by `{id}`.

### Get all orders

- **Endpoint**: `/orders`
- **Method**: GET
- **Response**: Returns a list of all orders in the system.

### Get order details

- **Endpoint**: `/orders/{id}`
- **Method**: GET
- **Response**: Returns the details of a specific order identified by `{id}`.

## Database Schema

The API uses a PostgreSQL database with the following schema:

### Users Table

| Column       | Type        | Description                   |
|--------------|-------------|-------------------------------|
| id           | SERIAL      | Unique identifier for the user |
| name         | VARCHAR(255) | User's name                   |
| email        | VARCHAR(255) | User's email address          |
| created_at   | TIMESTAMP   | Creation timestamp            |

### Orders Table

| Column       | Type        | Description                             |
|--------------|-------------|-----------------------------------------|
| id           | SERIAL      | Unique identifier for the order          |
| user_id      | INTEGER     | ID of the user who placed the order      |
| product_name | VARCHAR(255) | Name of the ordered product              |
| quantity     | INTEGER     | Quantity of the product in the order     |
| total_price  | DECIMAL     | Total price of the order                 |
| created_at   | TIMESTAMP   | Creation timestamp                      |


## License

This project is licensed under the [MIT License](LICENSE).




