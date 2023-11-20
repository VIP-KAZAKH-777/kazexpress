from dotenv import dotenv_values
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_restful import Api

#Create a Flask instance
app = Flask(__name__)

#API objects
api = Api(app)

#Configure app
env_values = dotenv_values('.env')
app.config['SECRET_KEY'] = env_values['FLASK_SECRET_KEY']

#FOR DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = env_values['MYSQL_CONNECTION']
db = SQLAlchemy(app)
