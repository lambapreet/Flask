import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('formfile.html')

@app.route('/success', methods=["POST"])
def success():
    if request.method == 'POST':
        f = request.files['file']
        save_dir = 'static'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)  # Create 'static/' directory if it doesn't exist
        save_path = os.path.join(save_dir, f.filename)
        f.save(save_path)
        return f"File saved at {save_path}"

if __name__ == "__main__":
    app.run(debug=True)
