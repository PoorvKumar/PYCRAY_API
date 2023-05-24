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
3. Activate the Virtual Enviroment:
```python
  .venv/Scripts/Activate.ps1
```
4. Install the dependencies:
```python
pip install -r requirements.txt
```
5. Set up the database:
 - Create a PostgreSQL database on your local machine or use the default postgres database **(or to use online ElephantSQL uncomment line 11-12 in app.py and comment below connection)**
 - Modify the .env file according to your database,by default `DATABASE_NAME=postgres DB_USERNAME=postgres DB_PASSWORD=root` 
 - Open psql(PostgreSQL) and copy paste the queries in users.txt and orders.txt to create table and insert sample data in your tables in the same database.
6. Run the Application:
```python
flask run
```

The Flask API will be running at `http://localhost:5000/`.

## Note :
- You can run the API even without using virtual environment but make sure all the packages in requirements.txt are installed globally using pip
- Example: `pip install psycopg2`

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




