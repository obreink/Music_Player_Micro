
# flask app to display data from the catalog service
from flask import Flask, render_template
import requests
app = Flask(__name__)
# route get-catalog, returns a web page built from a jinja template
@app.route('/get-catalog')
def get_catalog():
 '''
 return the catalog in a web page
 '''
 catalog = requests.get('http://catalog:5000/get-catalog', timeout=5)
 data = catalog.json()
 # render and return the template
 return render_template('shop-front.html.j2',
 catalog=data['catalog'].values())
if __name__ == '__main__':
 app.run(debug=True, host="0.0.0.0", port=5000)
