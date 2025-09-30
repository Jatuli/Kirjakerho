import db

def get_user(user_id):
    sql = """SELECT id, username
            FROM users
            WHERE id = ?"""
    result =  db.query(sql, [user_id])
    return result[0] if result else None

def get_books(user_id):
    sql = "SELECT id, book_name FROM books WHERE id = ? ORDER by id DESC"
    return db.query(sql, [user_id])
    