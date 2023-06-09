from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL
from SingleTonPattern.product import Product

app = Flask(__name__)

# db configuration

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pos'

mysql = MySQL(app)
product = Product(mysql).get_instance()

@app.route('/')
def home_page():
    return render_template('login.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dash.html')

@app.route('/sales')
def sales_page():
    return render_template('sales.html')

@app.route('/manageproducts')
def manageproducts_page():
    return render_template('manageproducts.html')

@app.route('/manageusers')
def manageusers_page():
    return render_template('manageusers.html')

@app.route('/reports')
def reports_page():
    return render_template('reports.html')


@app.route('/api/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    product.insert_product(name,price,quantity)

    data = {'message': 'Saved successfuly'}
    return jsonify(data)

@app.route('/api/edit', methods=['POST'])
def edit_product():
    id = request.form['id']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    product.edit_product(id,name,price,quantity)

    data = {'message': 'Edited successfuly'}
    return jsonify(data)

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    product.delete_product(id)

    data = {'message': 'Deleted successfuly'}
    return jsonify(data)




@app.route('/api/products')
def products():
    products_list = product.get_products()

    return jsonify(products_list)

@app.route('/api/search', methods=['POST'])
def search():
    querry = request.form['querry']

    products_list = product.find_products(querry)
    
    return jsonify(products_list)

@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
   

    return jsonify({'message': 'Added to cart'})


@app.route('/cart')
def cart():
   return 

if __name__ == "__main__":
    app.run(debug=True)

