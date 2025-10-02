import db

def create_book(book_name, author, description, user_id, book_classification):
    sql = """INSERT INTO books (book_name, author, description, user_id) VALUES (?,?,?,?)"""
    db.execute(sql, [book_name, author, description, user_id])

    book_id = db.last_insert_id()

    if book_classification:
        sql ="INSERT INTO book_classification(book_id, book_name, value) VALUES (?, ?, ?) "
        db.execute(sql, [book_id, book_name, book_classification])

def get_book_classification(book_id):
    sql = "SELECT book_name, value FROM book_classification WHERE book_id = ?"
    return db.query(sql, [book_id])

def get_books():
    sql = "SELECT id, book_name, author, description, user_id FROM books ORDER by id DESC"
    results = db.query(sql) 
    return results if results else []

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
    result =  db.query(sql, [book_id])
    return result[0] if result else None

def update_book(book_id, book_name, author, description, book_classification):
    sql ="""UPDATE books SET book_name = ?,
                        author = ?,
                        description = ?
                    WHERE id = ?"""
    db.execute(sql, [book_name, author, description, book_id])
    if book_classification:
        sql = """UPDATE book_classification SET value = ? WHERE book_id = ?"""
        db.execute(sql, [book_classification, book_id]) 
    

def remove_book(book_id):
    sql = "DELETE FROM books WHERE id = ?"
    db.execute(sql, [book_id])

def search(query):
    sql = """SELECT id AS book_id, user_id, book_name, author, description
             FROM books
             WHERE book_name LIKE ? OR author LIKE ? OR description LIKE ?
             ORDER BY book_name DESC"""
    return db.query(sql, ["%" + query + "%", "%" + query + "%", "%" + query + "%"])