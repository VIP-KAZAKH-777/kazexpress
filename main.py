from flask import Flask, render_template

#Create a Flask instance
app = Flask(__name__)

#Routes
@app.route('/')
def home():
    return "Hello world!"

@app.route('/user')
def user():
    return "adwdaw"

#Error pages
#Invalid URL
@app.errorhandler(404)
def not_found(e):
    return "error 404", 404

#Internal Server Error
@app.errorhandler(500)
def serv_err(e):
    return "error 500", 500
