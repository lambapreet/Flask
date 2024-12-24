from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("first.html")

@app.route('/name')
def is_name():
    return "SONAM"

app.run(debug=True)


