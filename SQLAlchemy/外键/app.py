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
    


db.create_all()
@app.route("/user")
def index1():
    user = User(username='wang')
    db.session.add(user)
    db.session.commit()
    return 'index'

@app.route("/article")
def index2():
    article = Article(title='aaa',content='bbb',aurthor_id=1)
    db.session.add(article)
    db.session.commit()
    return 'index'

if __name__ == '__main__':
    app.run(debug = True)