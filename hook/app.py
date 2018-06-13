from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    print("index")
    return "index"

@app.route('/login')
def login():
    print("login")
    return 'login'

@app.before_request
def my_before_request():
    print("hook")