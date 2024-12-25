from flask import Flask, render_template, request, redirect, abort, flash, session, Blueprint

app = Flask(__name__)
app.secret_key = "abcd"

@app.route('/')
def login1():
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('login.html')

@app.route('/formlogin', methods=["POST"])
def login():
    error = None
    uname = request.form.get('uname')  # Using form data
    password = request.form.get('pass')  # Using form data
    if uname == "preet" and password == "123":
        session['email'] = uname
        flash("Logged in successfully.")
        return render_template('message3.html', name=uname)
    else:
        error = "Invalid username and password"
        return render_template('forms.html', error=error)
 # Rendering forms.html with error message
app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html',name=email)
    else:
        msg = "Login first"
        return render_template('login.html',msg=msg)
    

if __name__ == "__main__":
    app.run(debug=True)