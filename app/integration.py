from pymongo import MongoClient
import mysql.connector

# -------------------------
# Connect to MongoDB
# -------------------------
mongo = MongoClient("mongodb://localhost:27017/")
mdb = mongo["ecommerce"]
products = mdb["products"]

# Fetch product from MongoDB
product = products.find_one({"product_id": "P001"})
price = product["price"]

print("MongoDB Product:", product["name"], "| Price:", price)

# -------------------------
# Connect to MySQL
# -------------------------
sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="ecommerce"
)
cursor = sql.cursor()

# -------------------------
# Insert new order into MySQL
# -------------------------
cursor.execute(
    "INSERT INTO orders (user_id, total_amount) VALUES (%s, %s)",
    (1, price)
)
sql.commit()
order_id = cursor.lastrowid

print("Order Created in MySQL. Order ID:", order_id)

# -------------------------
# Insert order item
# -------------------------
cursor.execute(
    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
    (order_id, "P001", 1, price)
)
sql.commit()

print("Order Item Added for Product P001")

password="yourpassword"
