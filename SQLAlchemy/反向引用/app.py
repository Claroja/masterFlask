from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primar_key = True,autoincrement = True)
    username = db.Column(db.String(100),nullable=False)
    
class Article(db.Model):
    id = db.Column(db.Integer, primar_key = True,autoincrement = True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    
    author = db.relationship('User', backref=db.backref('article')) #第一个参数是class名称，相当于在article里添加了User的关系列。第二个参数相当于在User表里添加了article关系列,名称可以定义
    


db.create_all()


@app.route("/zeng")
def index1():
    article = Article(title='aaa',content='bbb')
    article.author = User.query.filter(User.id == 1).first()# 貌似没有直接写user_id=1方便
    db.session.add(article)
    db.session.commit()
    return 'index'

@app.route("/ariticle_user")
def index2():
    #通过文章找对应作者
    article = Article.query.filter(Article.title == 'aaa').first()
    author_di = article.author_id
    user = User.query.filter(User.id == author_id).first()
    
    article = Article.query.filter(Article.title == 'aaa').first()
    
    return article.author.username

@app.route("/user_article")
def index3():
    user = User.query.filter(User.username == 'wang').first()
    result = user.articles
    for article in result:
        print(article.title)
    return 'index'

if __name__ == '__main__':
    app.run(debug = True)