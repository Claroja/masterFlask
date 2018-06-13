from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
    return render_template("request.html")
    
@app.route('/get', methods = ['GET','POST'])
def get():
    method=request.method
    key1=request.args["get-key1"]
    key2=request.args["get-key2"]
    cookies=request.cookies
    headers=request.headers
    return "%s<br>%s<br>%s<br>%s<br>%s"%(method, key1, key2, cookies, headers)

@app.route('/post', methods = ['GET','POST'])
def post():
    method=request.method
    key1=request.form["post-key1"]
    key2=request.form["post-key2"]
    cookies=request.cookies
    headers=request.headers
    return "%s<br>%s<br>%s<br>%s<br>%s"%(method, key1, key2, cookies, headers)

if __name__ == '__main__':
    app.run(debug=True)
