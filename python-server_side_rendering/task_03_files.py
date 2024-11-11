from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)
# read_json and read_csv Functions: These functions read data from the respective files. 
# They handle possible file errors and return None if there’s an issue reading the file.
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv(file_path):
    products = []
    try:
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if products is None:
        return render_template('product_display.html', error="Error reading data file")

    if product_id:
        products = [p for p in products if p.get("id") == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)