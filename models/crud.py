from models.tables import Login, User, Product, db
from datetime import datetime

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

    profile = User(email = "", name = u, avatar = "", phone = "", address = "", pcode = "", card = "{}", scart="[]", orders="")
    db.session.add(profile)

    db.session.commit()
    return "User created."

#Update profile
def update_profile(form, id):    
    db.session.query(User).filter_by(uid = id).update({
        User.name: form.fullname.data, 
        User.email: form.email.data, 
        User.phone: form.phone.data, 
        User.address: form.address.data})     

    try:
        db.session.commit()
        return "Profile updated!"    
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
    
#Get products by category
def get_category(c_name):
    result = db.session.query(Product).filter_by(category = c_name).all()
    return result