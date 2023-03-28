from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    #res = requests.get(url)

    return "Hello"#res.text