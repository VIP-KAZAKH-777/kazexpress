from models.tables import Login, User, db
from datetime import datetime

# Login
def login(u:str, p:str):
    user = Login.query.filter_by(username=u).first()
    if user and user.check_password(p):
        #HERE WHILL BE CHANGES
        return {
            "Result":"Welcome!",
            "Authenticated":True,
            "UID": user.uid,
            "DATETIME": datetime.utcnow()
        }
        
        #JUST FOR NOW, TOMORROW I WILL WRITE IT IN CORRECT WAY
    return {
            "Result":"Incorrect username or password."
        }

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
    #HERE CHANGES TOO
    return ["Success", new_user.uid]