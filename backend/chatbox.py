import pandas as pd

# 📁 Base path to your dataset folder
base_path = r"C:\Users\navee\Desktop\ecommerce-chatbox\archive"

# ✅ Load all required datasets
products_df = pd.read_csv(f"{base_path}\\products.csv")
orders_df = pd.read_csv(f"{base_path}\\orders.csv")
order_items_df = pd.read_csv(f"{base_path}\\order_items.csv")
inventory_df = pd.read_csv(f"{base_path}\\inventory_items.csv")
users_df = pd.read_csv(f"{base_path}\\users.csv")

# ✅ API 1: Top 5 most sold products
def get_top_5_products():
    try:
        # Join order_items with products using product_id
        merged = order_items_df.merge(products_df, left_on="product_id", right_on="id")
        
        # Group by product name (from products.csv), count number of times ordered
        summary = merged.groupby("name")['id_x'].count().reset_index()
        summary.columns = ['product_name', 'orders_count']
        
        # Get top 5
        top_5 = summary.sort_values(by='orders_count', ascending=False).head(5)
        return top_5.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}

# ✅ API 2: Get stock for a product by name
def get_stock(product_name):
    try:
        # Merge inventory with product names
        merged = inventory_df.merge(products_df, left_on="product_id", right_on="id")

        # Case-insensitive and stripped match
        row = merged[merged['name'].str.lower().str.strip() == product_name.lower().strip()]
        
        if row.empty:
            return {"message": f"Product '{product_name}' not found"}

        return {
            "product_name": row.iloc[0]['name'],
            "stock": int(row.iloc[0]['available_quantity'])  # Ensure this column exists in your inventory
        }
    except Exception as e:
        return {"error": str(e)}

# ✅ API 3: Get order status by order ID
def get_order_status(order_id):
    try:
        row = orders_df[orders_df['order_id'] == int(order_id)]
        if row.empty:
            return {"message": "Order not found"}
        return {
            "order_id": order_id,
            "status": row.iloc[0]['status']
        }
    except Exception as e:
        return {"error": str(e)}
