from flask import Flask

from controllers.teacher import teacher_blueprint
from controllers.student import student_blueprint




app = Flask(__name__)


app.register_blueprint(student_blueprint)
app.register_blueprint(teacher_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
