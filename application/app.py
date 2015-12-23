from flask import Flask

# from routes.v0.course import app as course_bp
from routes.v0.course import api as api_v0_course_bp
from routes.v0.course.exercise import api as api_v0_course_exercise_bp
from routes.v0.course.enrollment import api as api_v0_course_enrollment_bp
from routes.v0.course.question import api as api_v0_course_question_bp
from routes.v0.course.skill import api as api_v0_course_skill_bp
from routes.v0.course.student import api as api_v0_course_student_bp
from routes.v0.exercise import api as api_v0_exercise_bp
from routes.v0.exercise.exercise import api as api_v0_exercise_exercise_bp
from routes.v0.exercise.skill import api as api_v0_exercise_skill_bp
from routes.v0.profile import api as api_v0_profile_bp
from routes.v0.profile.course import api as api_v0_profile_course_bp
from routes.v0.skill import api as api_v0_skill_bp
from routes.v0.user import api as api_v0_user_bp
from routes.v0.user.role import api as api_v0_user_role_bp

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# app.register_blueprint(course_bp)
app.register_blueprint(api_v0_course_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_course_exercise_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_course_enrollment_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_course_question_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_course_skill_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_course_student_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_exercise_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_exercise_exercise_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_exercise_skill_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_profile_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_profile_course_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_skill_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_user_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_user_role_bp, url_prefix='/api/v0')

@app.route('/')
def showHome():
    return "Home"

@app.route('/test')
def showTest():
    return "Test"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)