from flask import render_template, redirect, url_for, flash, session
from app import app, db
from models.forms import LoginForm, RegisterForm
from models.tables import Login, User
import models.crud
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
from managers.loginmanager import login_manager

#Routes
@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/cart/<user_id>')
def cart(user_id):
    return render_template('cart.html')

@app.route('/orders/<user_id>')
def orders(user_id):
    return render_template('orders.html')

@app.route('/user/<user_id>')
@login_required
def userpage(user_id):
    return render_template('userpage.html', user=current_user)

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
