import db

def create_book(book_name, author, description, user_id):
    sql = """INSERT INTO books (book_name, author, description, user_id) VALUES (?,?,?,?)"""
<<<<<<< HEAD
    db.execute(sql, [book_name, author, description, user_id])

def get_books():
    sql = "SELECT id, book_name, author, description, user_id FROM books ORDER by id DESC"
    return db.query(sql) 

def get_book(book_id):
    sql = """SELECT books.book_name,
                    author,
                    description,
                    users.username
            FROM books, users
            WHERE books.user_id = users.id AND 
                    books.id = ?"""
    return db.query(sql, [book_id])[0]
=======
    db.execute(sql, [book_name, author, description, user_id])
>>>>>>> 1a0a905242cc3569dadc92f716f9b28ba8ea4e36
