# -*- coding: utf-8 -*-
from models import db, User
from flask import Flask, render_template


def create_app():
    '''
    因为要注册数据库，所以需要返回一个注册完数据库的网站应用
    '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    return app


app = create_app()
db.create_all(app=app)  # 创建数据库


@app.route('/<name>')
def insert(name):
    '''
    这个路由用来添加数据
    '''
    user = User(username=name)
    db.session.add(user)
    db.session.commit()
    return "已成功添加%s" % user.username


@app.route('/')
def homepage():
    '''
    这个路由用来查询数据
    '''
    user = User.query.first()
    name = user.username
    return render_template('home.html', name=name)


if __name__ == "__main__":
    app.debug = True
    app.run()
