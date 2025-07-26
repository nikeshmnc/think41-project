from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load all datasets from archive folder
products_df = pd.read_csv("archive/products.csv")
order_items_df = pd.read_csv("archive/order_items.csv")
distribution_centers_df = pd.read_csv("archive/distribution_centers.csv")
inventory_items_df = pd.read_csv("archive/inventory_items.csv")
orders_df = pd.read_csv("archive/orders.csv")
users_df = pd.read_csv("archive/users.csv")

# Chatbot route using logic from chatbox.py
from chatbox import get_bot_response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    reply = get_bot_response(message)

    # ✅ Save chat to history.txt
    with open("chat_history.txt", "a", encoding='utf-8') as f:
        f.write(f"You: {message}\nBot: {reply}\n\n")

    return jsonify({"reply": reply})


# Top 5 most sold products
@app.route('/top-products', methods=['GET'])
def top_products():
    merged = order_items_df.merge(products_df, left_on="product_id", right_on="id")
    top_products = merged['name'].value_counts().head(5).reset_index()
    top_products.columns = ['product_name', 'orders_count']
    return jsonify(top_products.to_dict(orient='records'))

# All products list
@app.route('/all-products', methods=['GET'])
def all_products():
    return jsonify(products_df['name'].dropna().unique().tolist())

# Get stock for a product name
@app.route('/get-stock/<product_name>', methods=['GET'])
def get_stock(product_name):
    filtered = products_df[products_df['name'].str.contains(product_name, case=False, na=False)]
    if filtered.empty:
        return jsonify({"message": f"Product '{product_name}' not found"})
    product_ids = filtered['id'].tolist()
    stock_count = inventory_items_df[inventory_items_df['product_id'].isin(product_ids)].shape[0]
    return jsonify({"product_name": product_name, "stock_available": stock_count})

# Get order status by order ID
@app.route('/order-status/<order_id>', methods=['GET'])
def get_order_status(order_id):
    order = orders_df[orders_df['id'].astype(str) == str(order_id)]
    if order.empty:
        return jsonify({"message": "Order not found"})
    return jsonify({"order_id": order_id, "status": order.iloc[0]['status']})

# Get all distribution centers
@app.route('/distribution-centers', methods=['GET'])
def distribution_centers():
    return jsonify(distribution_centers_df.to_dict(orient='records'))

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_df.to_dict(orient='records'))

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders_df.to_dict(orient='records'))

# Get all inventory items
@app.route('/inventory-items', methods=['GET'])
def get_inventory():
    return jsonify(inventory_items_df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
