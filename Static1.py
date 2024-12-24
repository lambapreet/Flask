from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('Css1.html')

@app.route('/page/<uname>')
def user_page(uname):  # Renamed function to avoid conflict
    return f"Hello, {uname}!"

@app.route('/index')
def index_page():  # Renamed function to avoid conflict
    return render_template('index.html') 

@app.route('/name')
def is_name():
    return "SONAM"

if __name__ == "__main__":
    app.run(debug=True)

