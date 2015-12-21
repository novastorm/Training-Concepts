from flask import Flask

# from routes.v0.course import app as course_bp
from routes.v0.course import api as api_v0_course_bp
from routes.v0.course.skill import api as api_v0_course_skill_bp
from routes.v0.skill import api as api_v0_skill_bp

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# app.register_blueprint(course_bp)
app.register_blueprint(api_v0_course_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_course_skill_bp, url_prefix='/api/v0')
app.register_blueprint(api_v0_skill_bp, url_prefix='/api/v0')

@app.route('/')
def showHome():
    return "Home"

@app.route('/test')
def showTest():
    return "Test"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)