from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "login"

@app.route('/')
def login1():
    """Route to render the login page."""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Route to handle login logic."""
    username = request.form.get("username")
    password = request.form.get("password")

    if username == 'sonam' and password == '1234':
        session['email'] = username
        return render_template('success.html', email=username)
    else:
        msg = "Invalid username/password"
        return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    """Route to handle logout and clear session."""
    session.pop('email', None)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
