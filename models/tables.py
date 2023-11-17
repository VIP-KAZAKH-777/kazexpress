from app import db

class Login(db.Model):
    __tablename__="User"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)

    #Representation
    def __repr__(self):
        return '<Login: %r>' %self.login
