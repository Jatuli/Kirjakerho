CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    book_name TEXT,
    author TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE IF NOT EXISTS book_classification (
    id INTEGER PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    book_name TEXT,
    value TEXT
);