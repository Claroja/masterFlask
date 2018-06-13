from flask import Flask, abort
app = Flask(__name__)

@app.route('/wrong')
def index():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(debug=True)
