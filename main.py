from flask import *
from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stocks.db"

app.secret_key =str(random.randbytes(16))
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    passwords = db.Column(db.String, nullable=False)





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

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")
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
