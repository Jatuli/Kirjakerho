CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    book_name TEXT,
    author TEXT,
    description TEXT,
    user_id INTEGER REFERENCE users
);