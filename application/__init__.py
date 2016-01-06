from flask import Flask

app = Flask(__name__)
app.config.from_object('application.config')

from models import Base

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
from routes.v0.progress import api as api_v0_progress_bp
from routes.v0.progress.activity import api as api_v0_progress_activity_bp
from routes.v0.role import api as api_v0_role_bp
from routes.v0.role.user import api as api_v0_role_user_bp
from routes.v0.skill import api as api_v0_skill_bp
from routes.v0.skill.exercise import api as api_v0_skill_exercise_bp
from routes.v0.skill.skill import api as api_v0_skill_skill_bp
from routes.v0.student import api as api_v0_student_bp
from routes.v0.user import api as api_v0_user_bp
from routes.v0.user.role import api as api_v0_user_role_bp

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
app.register_blueprint(api_v0_progress_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_progress_activity_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_role_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_role_user_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_skill_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_skill_exercise_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_skill_skill_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_student_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_user_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_user_role_bp, url_prefix='/api/v0')


@app.route('/')
def showHome():
    return "Home"

@app.route('/test')
def showTest():
    return "Test"


if __name__ == '__main__':
    import config
    app.config.from_object('config.DevelopmentConfig')

    engine = create_engine(app.config['DATABASE_URI'])

    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    sessionmaker(bind=engine)

    app.run(host='0.0.0.0', port=4000)