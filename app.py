import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import db
import config
import books

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/new_book")
def book():
    return render_template("new_book.html")

@app.route("/create_book", methods=["POST"])
def create():
    book_name = request.form["book_name"]
    author = request.form["author"]
    description = request.form["description"]
    user_id = session["user_id"]

    books.create_book(book_name, author, description, user_id)

    return redirect ("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")

if __name__ == "__main__":
    db.init_db()   # alustaa tietokannan ennen Flaskin käynnistystä
    app.run(debug=True)
