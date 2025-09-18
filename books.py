import db

def create_book(book_name, author, description, user_id):
    sql = """INSERT INTO books (book_name, author, description, user_id) VALUES (?,?,?,?)"""
    db.execute(sql, [book_name, author, description, user_id])