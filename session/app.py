from flask import Flask, session
import os

app=Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) # 加密session，盐

@app.route("/")
def hello_world():
    session["username"] = "session"
    return 'hello world'

@app.route("/get")
def get():
    return session.get('username')

@app.route("/delete")
def delete():
    print(session.get("username"))
    session.pop("username")
    print(session.get("username"))

@app.route("/clear")
    print(session.get("username"))
    session.clear()
    print(session.get("username"))

if __name__ == '__main__':
    app.run(debug = True)