from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to load products from JSON
def load_products_from_json():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# Function to load products from CSV
def load_products_from_csv():
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
            return products
    except (FileNotFoundError, csv.Error):
        return None

# Function to load products from SQLite database
def load_products_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        conn.close()
        return products
    except sqlite3.Error as e:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Load products based on source
    if source == 'json':
        products = load_products_from_json()
    elif source == 'csv':
        products = load_products_from_csv()
    elif source == 'sql':
        products = load_products_from_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Handle errors when data cannot be loaded
    if products is None:
        return render_template('product_display.html', error="Error loading products")

    # Filter products by ID if specified
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
