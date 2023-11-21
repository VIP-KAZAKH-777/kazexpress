from models.tables import Login, User, Product, db
from datetime import datetime
from ast import literal_eval
from sqlalchemy import desc

# Login
def login(u:str, p:str):
    user = Login.query.filter_by(username=u).first()
    if user and user.check_password(p):
        return User.query.filter_by(uid = user.uid).first()
    return None

#Register
def register(u:str, p:str):
    user = Login.query.filter_by(username=u).first()
    if user:
        return "User already exists."

    new_user = Login(u, p)
    db.session.add(new_user)

    profile = User(email = "", name = u, avatar = "defalt_user_profile.jpg", phone = "", address = "", pcode = "", card = "{}", scart="[]", orders="")
    db.session.add(profile)

    db.session.commit()
    return "User created."

#Update profile
def update_profile(form, avatar, id): 
    db.session.query(User).filter_by(uid = id).update({
        User.avatar: avatar,
        User.name: form.fullname.data, 
        User.email: form.email.data, 
        User.phone: form.phone.data, 
        User.address: form.address.data})     

    try:
        db.session.commit()
        return "Profile updated!"    
    except:
        return "Something went wrong."
    
#Add product to cart
def add_to_cart(pid, user):
    current_cart = literal_eval(user.scart)
    if pid in current_cart:
        return "Already have."
    current_cart.append(pid)
    db.session.query(User).filter_by(uid = user.uid).update({
        User.scart: f"{current_cart}"})  
    
    try:
        db.session.commit()
        return "Added to cart!"
    except: 
        return "Something went wrong."

#Delete product from cart
def del_from_cart(pid, user):
    current_cart = literal_eval(user.scart)
    current_cart.remove(pid)
    db.session.query(User).filter_by(uid = user.uid).update({
        User.scart: f"{current_cart}"})  
    
    try:
        db.session.commit()
        return "Deleted from cart!"
    except: 
        return "Something went wrong."

#Update delivery info
def update_delivery(form, id):
    db.session.query(User).filter_by(uid = id).update({
        User.address: form.address.data, 
        User.pcode: form.pcode.data})

    try:
        db.session.commit()
        return "Delivery updated!"    
    except:
        return "Something went wrong."
    
#Get all products or specific one
def get_products(id):
    if id == "all":
        result = Product.query.all()
        ans = []
        for item in result:
            ans.append(str(item))
        return ans
    
    return str(Product.query.filter_by(pid=id).first())

#Get Top25 products
def top25products():
    query = db.session.query(Product).order_by(desc(Product.demand)).all()[:25]
    return query

#Create product (available only from request (look in api/local))
def add_product(args):
    product = Product(sid = args['sid'],
                    category = args['category'],
                    price = args['price'],
                    name = args['name'],
                    description = args['description'],
                    media = args['media'],
                    characs = args['characs'],
                    reviews = args['reviews'],
                    demand = args['demand'],
                    stars = args['stars'])
                    
    db.session.add(product)
    try:
        db.session.commit()
        return "Success!"
    except:
        return "Error, check serverside"
    
#Update product
def update_product(args):
    db.session.query(Product).filter_by(pid = args['pid']).update({
        Product.pid: args['pid'],
        Product.sid: args['sid'],
        Product.category: args['category'],
        Product.price: args['price'],
        Product.name: args['name'],
        Product.description: args['description'],
        Product.media: args['media'],
        Product.characs: args['characs'],
        Product.reviews: args['reviews'],
        Product.demand: args['demand'],
        Product.stars: args['stars']
        })     

    try:
        db.session.commit()
        return "Product updated!"    
    except:
        return "Something went wrong."
    
#Add order
def add_order(orders, uid):
    db.session.query(User).filter_by(uid = uid).update({
        #Let's clear users cart and add them to orders
        User.scart: '[]',
        User.orders: f'{orders}'})

    
    try:
        db.session.commit()
        return "Orders updated!"    
    except:
        return "Something went wrong."

#Get products by category
def get_category(c_name):
    result = db.session.query(Product).filter_by(category = c_name).all()
    return result

#Search for product by its name
def search_product(searched):
    products = Product.query.filter(Product.name.like('%' + searched + '%')).order_by(Product.pid).all()
    return products
