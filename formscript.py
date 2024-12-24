from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register():
    # Ensure 'formfetch.html' exists in the 'templates' folder
    return render_template('formfetch.html')

@app.route('/success', methods=["POST"])
def printdata():
    # Retrieve form data and pass it to the 'result.html' template
    result = request.form
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)




