from flask import Blueprint, render_template

teacher_blueprint = Blueprint(
        'teacher',
        __name__,
        template_folder="../templates/teacher",
        url_prefix="/teacher"
        )


@teacher_blueprint.route('/')
def home():
    return render_template('teacher.html')
