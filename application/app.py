from flask import Flask

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/')
def showHome():
    return "Home"

@app.route('/test')
def showTest():
    return "Test"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)