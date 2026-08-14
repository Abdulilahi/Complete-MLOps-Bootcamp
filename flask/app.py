from flask import Flask


app=Flask(__name__)
#this creates an instance of the Flask Class which will be your WSGI application


@app.route("/")
def welcome():
    return "Hey !!! Welcome to this best flask course. This should ba an amazing course"

@app.route("/index")
def index():
    return "Hey !!! Welcome to this best flask course. This should ba an amazing course"

@app.route("/courses")
def courses():
    return "Hey !!! Welcome to this best flask course. This should ba an amazing course"


if __name__=="__main__":
    app.run(debug=True)
