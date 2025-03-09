# Provides functions to interact with SQLite database
import sqlite3

DB_FILE = "yaurls.db"

# Create yaurls.db if it doesn't already exist in local project directory
def init_db():
    con = sqlite3.connect(DB_FILE)
    con.close()
