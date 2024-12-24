from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_table():
    result = {
        "Name": "John Doe",
        "Age": 30,
        "Occupation": "Developer",
        "Country": "USA"
    }
    return render_template('message2.html', result=result)

@app.route('/<uname>/')
def is_name(uname):
    return render_template('message.html', name=uname)

if __name__ == "__main__":
    app.run(debug=True)



