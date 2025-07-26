import requests

def get_bot_response(message):
    msg = message.lower()

    if "top" in msg or "top-5" in msg or "most sold" in msg:
        try:
            res = requests.get("http://127.0.0.1:5000/top-products")
            data = res.json()
            top_products = [f"{i+1}. {p['product_name']} ({p['orders_count']} orders)" for i, p in enumerate(data)]
            return "Top 5 Products:\n" + "\n".join(top_products)
        except Exception as e:
            return "Error fetching top products."

    elif "tankini" in msg or "cap" in msg:
        return "Yes, we have that item available."

    elif "status" in msg and "12345" in msg:
        return "Order 12345 is Cancelled."

    else:
        return "Sorry, I didn't understand that."
