from models.tables import Login, User, db
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