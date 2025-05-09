from flask_app import db
import bcrypt
from flask_login import UserMixin

class Login(db.Model, UserMixin):
    __tablename__="Login"
    uid = db.Column(db.Integer, primary_key=True) #user id
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, u, p):
        self.username = u
        self.set_password(p)

    def set_password(self, p):
        self.password = bcrypt.hashpw(p.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, p):
        if bcrypt.checkpw(p.encode('utf-8'), self.password.encode('utf-8')):
            return True
        return False

    def get_id(self):
           return (self.uid)
    #Representation
    def __repr__(self):
        return '<Login: %r>' %self.login

class User(db.Model, UserMixin):
    __tablename__="User"
    uid = db.Column(db.Integer, primary_key=True) #user id
    email = db.Column(db.String(128)) # example@example.com
    name = db.Column(db.String(128)) # name and surname
    avatar = db.Column(db.String(128)) # uploads/users/avatar(uid).png
    phone = db.Column(db.String(20)) # +7(777)-777-77-77
    address = db.Column(db.String(128)) # Astana, Imanbaeva 10, 6floor, 18flat
    pcode = db.Column(db.String(6)) #010000
    card = db.Column(db.Text()) #JSON
    scart = db.Column(db.String(128)) #pids
    orders = db.Column(db.Text()) #JSON

    def get_id(self):
           return (self.uid)

    def __repr__(self):
        return '<Name: %r>' %self.name

class Product(db.Model):
    __tablename__="Product"
    pid = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer)
    category = db.Column(db.String(128))
    price = db.Column(db.String(24))
    name = db.Column(db.String(128))
    description = db.Column(db.String(1024))
    media = db.Column(db.String(1024))
    characs = db.Column(db.Text())
    reviews = db.Column(db.Text())
    demand = db.Column(db.Integer)
    stars = db.Column(db.Integer)

    def __repr__(self):
        return "{" + f'"Product id": "{self.pid}", "Name": "{self.name}",  "Category": "{self.category}", "Price": "{self.price}", "Description": "{self.description}",  "Characteristics": {self.characs},  "Reviews": [{self.reviews}],  "Demand": {self.demand},  "Stars": {self.stars}, "Media": "{self.media}"' + "}"

class Shop(db.Model):
    __tablename__="Shop"
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    rate = db.Column(db.Integer)
    orders = db.Column(db.Integer)

    def __repr__(self):
        return '<Name: %r>' %self.name