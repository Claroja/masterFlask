from flask import abort, redirect, url_for
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
