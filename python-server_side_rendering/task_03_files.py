from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_products_from_json():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return None

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

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = load_products_from_json()
    elif source == 'csv':
        products = load_products_from_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if products is None:
        return render_template('product_display.html', error="Error loading products")

    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
