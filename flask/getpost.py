from flask import Flask,render_template,request


app=Flask(__name__)
#this creates an instance of the Flask Class which will be your WSGI application


@app.route("/")
def welcome():
    return "<HTML><h1>WELCOME TO THE FLASK COURSE</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/courses")
def courses():
    return "Hey !!! Welcome to this best flask course. This should ba an amazing course"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'HELLO {name}!'
    return render_template('form.html')

@app.route("/form",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'HELLO {name}!'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
