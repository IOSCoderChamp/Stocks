from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calculator", methods=["GET", "POST"])
def calc():
    x = request.form.get('x')
    y = request.form.get('y')
    ans = 0
    if x is not None and y is not None:
        ans = int(x) + int(y)


    return render_template("calc.html", ans=ans)