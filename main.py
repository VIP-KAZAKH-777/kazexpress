from flask import render_template, redirect, url_for, flash, request, abort
from app import app, api
from models.forms import *
from models.tables import User
import models.crud
from flask_login import login_user, login_required, logout_user, current_user
from managers.loginmanager import login_manager
from api.flask_api import Product
from ast import literal_eval
from models.categories import get_categories
from werkzeug.utils import secure_filename
import os

#Routes
@app.route('/')
def home():
    product = models.crud.get_products('all')
    products = []
    for i in product:
        mydict = literal_eval(i)
        products.append(mydict)

    return render_template('home.html', products=products, categories = get_categories())

@app.route('/search', methods=['POST'])
def search():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        post = search_form.searched.data
        products = models.crud.search_product(post)
    return render_template('search.html', search_form=search_form, post=post, products = products, categories = get_categories())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #MUST CHANGE HERE
        result = models.crud.login(form.username.data, form.password.data)
        if result:
            login_user(result)
            return redirect(url_for('userpage', user_id=current_user.uid))
        flash("Incorrect username or password.")
    return render_template('login.html', form=form)

@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        result = models.crud.register(form.username.data, form.password.data)
        flash(result)
    return render_template('register.html', form=form)

@app.route('/cart/<int:user_id>')
def cart(user_id):
    cart=literal_eval(current_user.scart)
    forweb = []
    products = []
    for i in cart:
        if i not in forweb:
            forweb.append(i)
            products.append(literal_eval(models.crud.get_products(i)))
        
    return render_template('cart.html', products=products, orders=forweb)

@app.route('/cart/add/<int:pid>')
def add_cart(pid):
    flash(models.crud.add_to_cart(pid, current_user))
    return redirect(url_for('home'))

@app.route('/cart/del/<int:pid>')
def del_from_cart(pid):
    flash(models.crud.del_from_cart(pid, current_user))
    return redirect(url_for('cart', user_id=current_user.uid))

@app.route('/orders/<int:user_id>')
def orders(user_id):
    orders=literal_eval(current_user.orders)
    products = []
    for i in orders:
        products.append(literal_eval(models.crud.get_products(i)))
    return render_template('orders.html', user=current_user, orders = products)

@app.route('/order/<orders>')
def makeorder(orders):
    models.crud.add_order(orders, current_user.uid)
    return redirect(url_for('orders', user_id=current_user.uid))

@app.route('/user/<int:user_id>', methods=["GET", "POST"])
@login_required
def userpage(user_id):
    profile_form = ProfileForm()
    delivery_form = DeliveryForm()
    if profile_form.validate_on_submit():
        uploaded_file = request.files['pic']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        flash(models.crud.update_profile(profile_form, filename, user_id))
    if delivery_form.validate_on_submit():
        flash(models.crud.update_delivery(delivery_form, user_id))

    last_order = literal_eval(models.crud.get_products(literal_eval(current_user.orders)[-1]))
    return render_template('userpage.html', 
                           user=current_user, 
                           profile_form=profile_form,
                           delivery_form=delivery_form,
                           last_order=last_order)

@app.route('/topsales')
def topsales():
    top = models.crud.top25products()
    return render_template('topsales.html', top = top)

@app.route('/product/<int:p_id>')
def productpage(p_id):
    product = literal_eval(models.crud.get_products(p_id))
    return render_template('productpage.html', product = product, categories = get_categories())

@app.route('/category/<c_name>')
def categorized(c_name):
    product = models.crud.get_category(c_name)
    products = []
    for i in product:
        mydict = literal_eval(str(i))
        products.append(mydict)
    return render_template('categorized.html', products = products, category = c_name, categories = get_categories())

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

#API
api.add_resource(Product, "/api/product/<pid>")

#Some global things
@app.context_processor
def navbar_search():
    search_form = SearchForm()
    return dict(search_form=search_form)