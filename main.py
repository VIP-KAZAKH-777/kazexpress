from flask import render_template, redirect, url_for, flash
from app import app, db
from models.forms import LoginForm, RegisterForm
from models.tables import Login

#Routes
@app.route('/')
def home():
    data = Login.query.filter_by(uid=0)
    user = Login(uid=2, username='hellowlrld', password='nothelloworld')
    db.session.add(user)
    db.session.commit()
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, password={}'.format(
            form.username.data, form.password.data))
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, password={}'.format(
            form.username.data, form.password.data))
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

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
