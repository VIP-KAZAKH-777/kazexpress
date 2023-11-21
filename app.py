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

#Only accept requests that are up to 1MB in size
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
#Type of files that we accept
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
#Upload path
app.config['UPLOAD_PATH'] = 'static/uploads'

#FOR DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://sql12662982:zeLHvUa2UV@sql12.freesqldatabase.com/sql12662982"
db = SQLAlchemy(app)
