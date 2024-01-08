from flask import Flask

#Testing FLASK

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

hello()