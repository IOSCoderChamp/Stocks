from flask import *
import random

app = Flask(__name__)
app.secret_key =str(random.randbytes(16))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "DhruvaYeetz" and password == "123456dhruva":
            session["user"] = username
            return redirect(url_for("index"))
        elif username =="FRIENDSHIP POWER" and password == "PFUDOR":
            session["user"] = username
            return redirect(url_for("index"))

    return render_template('login.html', username=session.get("user"))

@app.route("/")
def index():
    return render_template('index.html', username=session.get("user"))

@app.route("/logout") 
def logout():
    del session["user"]
    return redirect(url_for("login"))

@app.route("/add")
def add():
    return render_template('add.html', username=session.get("user"))

@app.route("/account")
def account():
    return render_template('account.html', username=session.get("user"))
