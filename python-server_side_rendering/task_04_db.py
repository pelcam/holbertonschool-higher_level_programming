from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to display items from a JSON file
@app.route('/items')
def items():
    try:
        # Open and read the JSON file containing items data
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_data = data.get("items", [])
    except FileNotFoundError:
        item_data = []  # Return an empty list if the file is not found

    return render_template('items.html', items=item_data)

# Route to display products, fetching from JSON, CSV, or SQL based on the query parameter
@app.route('/products', methods=['GET'])
def display_products():
    # Retrieve the source (json, csv, or sql) from query parameters
    source = request.args.get('source', '')
    # Retrieve the product ID (if provided)
    product_id = request.args.get('id', type=int)
    message = None
    products = []

    # Check if the source is valid
    if source not in ['json', 'csv', 'sql']:
        message = "Wrong source"
        return render_template('product_display.html', products=products, message=message)

    try:
        # Load products from JSON file
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)

        # Load products from CSV file
        elif source == 'csv':
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]

        # Load products from SQL database
        elif source == 'sql':
            con = sqlite3.connect("products.db")
            cur = con.cursor()

            # If a product ID is provided, filter products by ID
            if product_id:
                query = "SELECT * FROM Products WHERE id = ?"
                cur.execute(query, (product_id,))
            else:
                query = "SELECT * FROM Products"
                cur.execute(query)

            # Convert SQL results into a list of dictionaries
            products = [
                {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
                for row in cur.fetchall()
            ]
            con.close()

        # Filter products by the given product ID (if provided)
        if product_id:
            products = [product for product in products if product['id'] == product_id]
            # If no product matches the given ID, set an error message
            if not products:
                message = "Product not found."

    except FileNotFoundError:
        message = "File not found."
    except Exception as e:
        message = f"An error occurred: {e}"

    # Render the products page with the fetched products or error message
    return render_template('product_display.html', products=products, message=message)

# Run the app in debug mode on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
