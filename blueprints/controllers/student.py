from flask import Blueprint, render_template

student_blueprint = Blueprint(
        'student',
        __name__,
        template_folder="../templates/student",
        url_prefix="/student"
        )


@student_blueprint.route('/')
def home():
    return render_template('student.html')
