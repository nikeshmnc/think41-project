from flask import Flask, jsonify
from chatbox import get_top_5_products, get_stock, get_order_status
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/top-products', methods=['GET'])
def top_products():
    return jsonify(get_top_5_products())

@app.route('/all-products', methods=['GET'])
def all_products():
    from chatbox import products_df
    return jsonify(products_df['name'].unique().tolist())


@app.route('/stock/<product_name>', methods=['GET'])
def stock(product_name):
    return jsonify(get_stock(product_name))

@app.route('/order-status/<order_id>', methods=['GET'])
def order_status(order_id):
    return jsonify(get_order_status(order_id))

if __name__ == '__main__':
    app.run(debug=True)
