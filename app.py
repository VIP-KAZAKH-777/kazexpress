from dotenv import dotenv_values
from flask import Flask

#Create a Flask instance
app = Flask(__name__)

#Configure app
env_values = dotenv_values('.env')
app.config['SECRET_KEY'] = env_values['FLASK_SECRET_KEY']