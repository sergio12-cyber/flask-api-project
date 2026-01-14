from flask import Flask, render_template
import requests

app = Flask(__name__)
API_URL = "https://dummyjson.com/products"

@app.route('/')
def index():
    data = requests.get(API_URL).json()['products']
    return render_template('index.html', products=data)

@app.route('/product/<int:id>')
def detail(id):
    product = requests.get(f"{API_URL}/{id}").json()
    return render_template('detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
