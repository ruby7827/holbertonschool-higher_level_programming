from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute('SELECT name, category, price FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT name, category, price FROM Products')
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error:
        pass
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql(product_id)
        if product_id and not products:
            error = "Product not found"
        return render_template('product_display.html', products=products, error=error)
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
