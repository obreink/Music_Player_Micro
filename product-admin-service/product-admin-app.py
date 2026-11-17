# flask app to add new products to the catalog
from flask import Flask, render_template, request
import requests
app = Flask(__name__)
# route add-product-page, returns the empty form
@app.route('/add-product-page')
def add_product_page():
 '''
 return the add-product page
 '''
 return render_template('add-product.html.j2')
# route add-product, receives the submitted form
@app.route('/add-product', methods=['POST'])
def add_product():
 '''
 send the new product to the catalog
 '''
 product = {
 "make": request.form['make'],
 "model": request.form['model'],
 "price": request.form['price']
 }
 requests.post('http://catalog:5000/add-product',
 json=product, timeout=5)
 return "Success"
if __name__ == '__main__':
 app.run(debug=True, host="0.0.0.0", port=5000)