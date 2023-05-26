from flask import *
from flask_sqlalchemy import SQLAlchemy
import random

import hashlib 

def md5(text):
    return hashlib.md5(text.encode("utf-8")).digest().hex()

# initialization
db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stocks.db"

app.secret_key =str(random.randbytes(16))
db.init_app(app)

#database model classes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

class Stock(db.Model):
    
    __tablename__ = "Stocks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) 
    symbol = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False, default=1)
    user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

def userstuff():

    userid = session.get("userid")
    user = db.session.query(User).get(userid)
    return user

def cu():
    user = userstuff()
    return user.username if user else None

#app configuration
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = md5(request.form.get("password"))

            user = db.session.query(User).filter_by(username=username).first()
            if user and user.password == password:
                session["userid"] = user.id
                return redirect(url_for("index"))
            else: 
                render_template('login.html', error="invalid login")
        except Exception as error:
            render_template('login.html', error=error)

    return render_template('login.html')

@app.route("/")
def index():
    user = userstuff()
    return render_template('index.html', username=cu())

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            username = request.form["username"]
            password = md5(request.form["password"])
            if username and password:
                user = User(username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("login"))
            else:
                return render_template("signup.html", error="no empty strings")
        except Exception as error:
            return render_template("signup.html", error="Username Already Exists")
    return render_template("signup.html")
@app.route("/logout") 
def logout():
    user = userstuff()
    del session[user.username]
    return redirect(url_for("login"))

@app.route("/add",  methods=["GET", "POST"])
def add():
    user = userstuff()
    if request.method == "POST":
        try:
            name = request.form["name"]
            Symbol = request.form["symbol"]
            price = request.form["$"]
            quantity = request.form["Num"]
            if name and Symbol and price and quantity and user:
                e = Stock(name=name, symbol=Symbol, price = price, quantity = quantity, user = user.id)
                db.session.add(e)
                db.session.commit()
                return redirect(url_for("account.html"))
            else:
                return render_template("add.html", error="At least one of the fields was left blank")
        except Exception as error:
            print("Problem Achieved")
            print(error)
    return render_template('add.html', username=cu())


@app.route("/account")
def account():
    user = userstuff()

    stocks = db.session.query(Stock).filter_by(user=user.id).all()
    return render_template("account.html", username=cu(), stocks=stocks)