from flask import Flask, render_template, request, redirect, abort, flash

app = Flask(__name__)
app.secret_key = "abcd"


@app.route('/')
def sss():
    return render_template('forms.html')


@app.route('/formlogin', methods=["POST"])
def login():
    error = None
    uname = request.form.get('uname')  # Using form data
    password = request.form.get('pass')  # Using form data
    if uname == "preet" and password == "123":
        flash("Logged in successfully.")
        return render_template('message3.html', name=uname)
    else:
        error = "Invalid username and password"
        return render_template('forms.html', error=error)
 # Rendering forms.html with error message


if __name__ == "__main__":
    app.run(debug=True)

