from flask import Flask, request

app = Flask(__name__)

@app.route('/formlogin', methods=['POST'])
def login():
    uname = request.form['uname']
    pasd = request.form['pass']
    if uname == "sonam" and pasd == "pass":
        return "Welcome %s" % uname
    else:
        return "Try again"

@app.route('/name')
def is_name():
    return "SONAM"

if __name__ == "__main__":
    app.run(debug=True)



