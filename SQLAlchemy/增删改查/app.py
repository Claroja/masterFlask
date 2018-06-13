from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False  )

db.drop_all()
db.create_all()

@app.route("/zeng")
def zeng():
    article = Article(title = 'aaa', content = 'bbb')
    db.session.add(article)
    db.session.commit()
    return article

@app.route("/cha")
def cha():
    result = Article.query.filter(Article.title == 'aaa').all()
    print(result[0].content)
    return result[0].content

@app.route("/gai")
def gai():
    article = Article.query.filter(Article.title == 'aaa').first()
    article.title = 'new title'
    db.session.add(article)
    db.session.commit()
    return article

@app.route("/shan")
def shan():
    article = Article.query.filter(Article.title == 'aaa').first()
    db.session.delete(article)
    db.session.commit()
    return article

if __name__ == '__main__':
    app.run(debug = True)
    
    
    
    
    
    
    
    
    
    
    