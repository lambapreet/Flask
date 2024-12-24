from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome"

@app.route('/student')
def Student():
    return "Welcome Student"

@app.route('/teacher')
def Teacher():
    return "Welcome Teacher"

@app.route('/user/<name>')
def User(name):
    if name == 'student':
        return redirect(url_for('Student'))
    elif name == 'teacher':
        return redirect(url_for('Teacher'))
    else:
        return "Invalid user type!"

# if __name__ == '__main__':

app.run(debug=True)
