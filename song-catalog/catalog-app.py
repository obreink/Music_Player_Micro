# flask app for the product catalog
import json
from flask import Flask, request
app = Flask(__name__)
# dummy data: a dictionary of products, keyed by make-model
catalog = {'catalog': {
 "Apple-iPhone 6s":
 {"make": "Apple", "model": "iPhone 6s", "price": 699.99},
 "Apple-iPhone 6s Plus":
 {"make": "Apple", "model": "iPhone 6s Plus", "price": 799.99},


"Apple-iPhone 7":
 {"make": "Apple", "model": "iPhone 7", "price": 749.99},
 "Apple-iPhone 7 Plus":
 {"make": "Apple", "model": "iPhone 7 Plus", "price": 869.99}
}}
# route get-catalog, returns json
@app.route('/get-catalog')
def get_catalog():
 '''
 return the catalog as json
 '''
 data = json.dumps(catalog)
 return data
if __name__ == '__main__':
 app.run(debug=True, host="0.0.0.0", port=5000)

# route to add a new product to the catalog
@app.route('/add-product', methods=['POST'])
def add_product():
 '''
 add the new product to the catalog
 '''
 product = {
 "make": request.json['make'],
 "model": request.json['model'],
 "price": request.json['price']
 }
 # create a 'natural' key from make and model
 key = request.json['make'] + '-' + request.json['model']
 catalog['catalog'][key] = product
 return {"status": "ok"}