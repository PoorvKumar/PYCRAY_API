import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app=Flask(__name__)

# # Uncomment to use ElephantSQL online and comment line 14-20
# url = os.getenv("DATABASE_URL")  
# connection=psycopg2.connect(url)  

## PostgreSQL Connection Configuration
connection=psycopg2.connect(
    host="localhost",
    database=os.getenv("DATABASE_NAME"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD")
)

# Home Route
@app.route("/")
def home():
    return "PYCRAY HOME"

# API Route to fetch all users
@app.route("/users",methods=["GET"])
def getUsers():
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM USERS"
        cursor.execute(query)
        users = cursor.fetchall()

        users_list = []
        for user in users:
            # print(user)
            user_dict = {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'created_at': user[3]
            }
            users_list.append(user_dict)

        cursor.close()
        return jsonify(users_list), 200    # HTTP status code 200 

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # HTTP status code 500

# API Route to fetch details of individual user using id
@app.route("/users/<int:user_id>",methods=["GET"])
def getUserDetails(user_id):
    try:
        cursor=connection.cursor()

        query="SELECT * FROM USERS WHERE id=%s"
        cursor.execute(query,(user_id,))

        user=cursor.fetchone()
        cursor.close()

        if user:
            user_data={
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'created_at': user[3]
            }

            return jsonify(user_data)
        else:
            return jsonify({'error': 'User not found!'}), 400 # HTTP status code 400
    except Exception as e:
        return jsonify({'error': 'An error occured','message':str(e)}), 500 # HTTP status code 500
    
# API Route to fetch all orders
@app.route("/orders",methods=["GET"])
def getOrders():
    try:
        cursor=connection.cursor()

        query="SELECT * FROM ORDERS"
        cursor.execute(query)

        orders=cursor.fetchall()

        orders_list=[]
        for order in orders:
            order_dict={
                'id': order[0],
                'user_id': order[1],
                'product_name': order[2],
                'quantity': order[3],
                'total_price': order[4],
                'created_at': order[5]
            }
            orders_list.append(order_dict)

        cursor.close()
        return jsonify(orders_list), 200    # HTTP status code 200 

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # HTTP status code 500
    
# API Route to fetch details of individual order using id
@app.route("/orders/<int:order_id>",methods=["GET"])
def getOrderDetails(order_id):
    try:
        cursor=connection.cursor()

        query="SELECT * FROM ORDERS WHERE id=%s"
        cursor.execute(query,(order_id,))

        order=cursor.fetchone()
        cursor.close()

        if order:
            order_data={
                'id': order[0],
                'user_id': order[1],
                'product_name': order[2],
                'quantity': order[3],
                'total_price': order[4],
                'created_at': order[5]
            }

            return jsonify(order_data)
        else:
            return jsonify({'error': 'Order not found!'}), 400 # HTTP status code 400
    except Exception as e:
        return jsonify({'error': 'An error occured','message':str(e)}), 500 # HTTP status code 500
    
if __name__ == '__main__':
    app.run()
