from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "<h1>mi nombre es Dhruva Akkineni</h1>"

@app.route("/")
def index():
    return "<p>What do you want to search for?</p><a href='/about'>about</a>"