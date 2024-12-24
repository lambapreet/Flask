from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/<name>/')
def is_name(name):
    return "SONAM" + " " + name

app.run(debug=True)


