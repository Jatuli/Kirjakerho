import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import db
import config
import books
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def check_login():
    if "user_id" not in session:
        abort(403)


@app.route("/")
def index():
   all_books = books.get_books()
   return render_template("index.html", books=all_books)

@app.route("/show_user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
       abort(404)
    books = users.get_books(user_id)
    return render_template("show_user.html", user=user, books=books)

@app.route("/book/<int:book_id>")
def show_book(book_id):
    book = books.get_book(book_id)
    if book is None:
       abort(404)
    return render_template("show_book.html", book=book)

@app.route("/search")
def search_book():
    query = request.args.get("query")  
    if query:
        results = books.search(query)
    else:
        query = ""
        results = []
    return render_template("search.html", query=query, results=results)
    

@app.route("/new_book")
def book():
    check_login()
    return render_template("new_book.html")

@app.route("/create_book", methods=["POST"])
def create():
    check_login()
    book_name = request.form["book_name"]
    if len(book_name) > 40:
        abort(403)
    author = request.form["author"]
    if len(author) > 40:
        abort(403)
    description = request.form["description"]
    if len(description) > 1000:
        abort(403)
    user_id = session["user_id"]

    books.create_book(book_name, author, description, user_id)

    return redirect ("/")

@app.route("/edit_book/<int:book_id>")
def edit_book(book_id):
    check_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_book.html", book=book)

@app.route("/update_book", methods=["POST"])
def update_book():
    check_login()
    book_id = request.form["book_id"]
    book_name = request.form["book_name"]
    if len(book_name) > 40:
        abort(403)
    author = request.form["author"]
    if len(author) > 40:
        abort(403)
    description = request.form["description"]
    if len(description) > 1000:
        abort(403)
    
    books.update_book(book_id, book_name, author, description)

    return redirect ("/book/" + str(book_id))

@app.route("/remove_book/<int:book_id>", methods=["GET", "POST"])
def remove_book(book_id):
    check_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)
    if request.method == "GET":
        book = books.get_book(book_id)
        return render_template("remove_book.html", book=book)

    if request.method == "POST":
        if "remove" in request.form:
            books.remove_book(book_id)
            return redirect("/")
        else:
            return redirect("/book/" +str(book_id))



    

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    if len(username) > 20:
        abort(403)
    password1 = request.form["password1"]
    if len(password1) > 30:
        abort(403)
    password2 = request.form["password2"]
    if len(password2) > 40:
        abort(403)
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return redirect("/")

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
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")

if __name__ == "__main__":
    print("Alustetaan tietokanta...")
    db.init_db()
    print("Tietokannan alustus valmis.")
    app.run(debug=True)