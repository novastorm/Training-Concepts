from application import app

app.config.from_object('application.config')

app.run(debug=True)
