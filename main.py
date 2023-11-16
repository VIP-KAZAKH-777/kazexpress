from flask import render_template
from app import app

#Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/cart/<user_id>')
def cart(user_id):
    return render_template('cart.html')

@app.route('/orders/<user_id>')
def orders(user_id):
    return render_template('orders.html')

@app.route('/user/<user_id>')
def userpage(user_id):
    return render_template('userpage.html')

@app.route('/topsales')
def topsales():
    return render_template('topsales.html')

@app.route('/product/<p_id>')
def productpage(p_id):
    return render_template('productpage.html')

@app.route('/category/<c_name>')
def categorized(c_name):
    return render_template('categorized.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

#Error pages
#Invalid URL
@app.errorhandler(404)
def not_found(e):
    return render_template('error404.html'), 404

#Internal Server Error
@app.errorhandler(500)
def serv_err(e):
    return "error 500", 500
