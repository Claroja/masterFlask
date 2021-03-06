'''
M模块(model)只用来放置数据库的结构
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User {}>'.format(self.username)




