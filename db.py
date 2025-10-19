import sqlite3
import os
from flask import g

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def init_db():
    try:
        con = get_connection()
        with open(SCHEMA_PATH, "r") as f:
            con.executescript(f.read())  
        con.commit()
        con.close()
        print("taulut luotu")
    except Exception as e:
        print("Virhe tietokannan alustamisessa:", e)

def get_connection():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    try:
        result = con.execute(sql, params)
        con.commit()
        g.last_insert_id = result.lastrowid
    except sqlite3.Error as e:
        print("Virhe SQL-kyselyssä:", e)
    finally:
        con.close()

def last_insert_id():
    return g.last_insert_id    
    
def query(sql, params=[]):
    con = get_connection()
    try:
        result = con.execute(sql, params).fetchall()
        return result
    except sqlite3.Error as e:
        print("Virhe SQL-kyselyssä:", e)
        return []  
    finally:
        con.close()

