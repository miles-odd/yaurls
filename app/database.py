import sqlite3

DB_FILE = "yaurls.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.close()
