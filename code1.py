from flask import Flask,render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'neuroline'
    myresult = 10+20
    mylist = [10,20,30,40,50]
    return render_template('first.html',myvalue=myvalue,myresult=myresult,mylist=mylist)


if __name__=='__main__':
    app.run(debug=True)