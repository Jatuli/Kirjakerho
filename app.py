import sqlite3
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import db
import config
import books
import users
from forms import RegistrationForm, LoginForm, NewBookForm, EditBookForm, EmptyForm

app = Flask(__name__)
app.secret_key = config.secret_key
csrf = CSRFProtect(app)

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
    classifications = books.get_book_classification(book_id)
    book_classification = classifications if classifications else [] 
    return render_template("show_book.html", book=book, book_classification=book_classification)

@app.route("/search")
def search_book():
    query = request.args.get("query")  
    if query:
        results = books.search(query)
    else:
        query = ""
        results = []
    return render_template("search.html", query=query, results=results)
    

@app.route("/new_book", methods=["GET", "POST"])
def new_book():
    check_login()
    user_id = session["user_id"]
    form = NewBookForm()  # Luo lomakeinstanssi
    if form.validate_on_submit():  # Tarkista, onko lomake lähetetty ja kelvollinen
        book_name = form.book_name.data
        author = form.author.data
        description = form.description.data
        book_classification = form.book_classification.data

        # Tarkista kenttien pituudet
        if len(book_name) > 40 or len(author) > 40 or len(description) > 1000:
            abort(403)

        # Tallenna kirja tietokantaan
        books.create_book(book_name, author, description, user_id, book_classification)

        return redirect("/")
    
    return render_template("new_book.html", form=form)



@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    check_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    print("Book data:", dict(book))

    form = EditBookForm(obj=book)  

    if form.validate_on_submit(): 
       
        books.update_book(book_id, form.book_name.data, form.author.data, form.description.data, form.book_classification.data)
        return redirect(f"/book/{book_id}")  

    return render_template("edit_book.html", form=form, book=book)  



@app.route("/remove_book/<int:book_id>", methods=["GET", "POST"])
def remove_book(book_id):
    check_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    form = EmptyForm()

    if request.method == "POST":
        if "remove" in request.form:
            sql = "DELETE FROM book_classification WHERE book_id = ?"
            db.execute(sql, [book_id])
            books.remove_book(book_id)
            return redirect("/")
        else:
            return redirect("/book/" + str(book_id))
    return render_template("remove_book.html", book=book, form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if len(username) > 20:
            abort(403)
        if len(password1) > 30:
            abort(403)
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
    
    return render_template("register.html", form=form)

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    # Tarkista salasanat ja käyttäjänimi
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
    form = LoginForm()  
    if form.validate_on_submit():  
        username = form.username.data
        password = form.password.data

        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])

        if not result: 
            return "VIRHE: väärä tunnus tai salasana"

        user_id = result[0]["id"]
        password_hash = result[0]["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"
    
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")

if __name__ == "__main__":
    print("Alustetaan tietokanta...")
    db.init_db()  # Alustetaan tietokanta
    print("Tietokannan alustus valmis.")
    app.run(debug=True)