from flask import Flask
'''
It Creates an instance fo the Flask Class,
Which will be your WSGI(Web Server Gaewa Interface)application'''

## ESGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this Best Flask Course . This should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to this Best Index Page ."


if __name__ == "__main__":
    app.run(debug=True)
    