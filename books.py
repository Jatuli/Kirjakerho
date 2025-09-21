import db

def create_book(book_name, author, description, user_id):
    sql = """INSERT INTO books (book_name, author, description, user_id) VALUES (?,?,?,?)"""
    db.execute(sql, [book_name, author, description, user_id])

def get_books():
    sql = "SELECT id, book_name, author, description, user_id FROM books ORDER by id DESC"
    return db.query(sql) 

def get_book(book_id):
    sql = """SELECT books.id,
                    books.book_name,
                    books.author,
                    books.description,
                    users.id user_id,
                    users.username
            FROM books, users
            WHERE books.user_id = users.id AND 
                books.id = ?"""
    return db.query(sql, [book_id])[0]

def update_book(book_id, book_name, author, description):
    sql ="""UPDATE books SET book_name = ?,
                        author = ?,
                        description = ?
                    WHERE id = ?"""
    db.execute(sql, [book_name, author, description, book_id])