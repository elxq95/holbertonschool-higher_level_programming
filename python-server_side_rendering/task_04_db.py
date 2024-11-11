from flask import Flask, request, render_template
import sqlite3
import json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json():
    with open('products.json') as f:
        return json.load(f)["products"]

# Function to read CSV data
def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

# Function to read SQLite data
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    
    # Select source based on query parameter
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template("product_display.html", error="Wrong source")
    
    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)