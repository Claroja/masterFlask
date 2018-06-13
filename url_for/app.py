# -*- coding:utf-8 -*-
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/url')
def hello():
    return url_for("hello",key="value")#传入函数的名称(字符串的形式)会返回该函数对应的路由url,第二个参数类似于query,相当于form的get请求


@app.route('/jingtai')
def hello():
    return url_for("static",filename="style.css")#传入static则是在模块的文件夹下找static文件夹，filename对应static文件夹下的文件
if __name__ == '__main__':
    app.run(debug=True)
