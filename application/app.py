from flask import Flask

from routes.v0.course import course_api as api_v0_course_bp

app = Flask(__name__)
app.secret_key = 'super_secret_key'

app.register_blueprint(api_v0_course_bp, url_prefix='/api/v0/courses')

@app.route('/')
def showHome():
    return "Home"

@app.route('/test')
def showTest():
    return "Test"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)