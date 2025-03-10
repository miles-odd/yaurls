# Provides functions to interact with SQLite database
import sqlite3
from pydantic import BaseModel

DB_FILE = "yaurls.db"

class URLRequest(BaseModel):
    original_url: str
    
class Entry(BaseModel):
    slug: str
    url: str
    visits: int

# Initialize the database (+ create it, if it doesn't exist in local project directory)
def init_db():
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, slug TEXT, url TEXT)
    ''')
    
    con.close()

# Insert a new slug/URL mapping into the database
def insert_url(slug: str, url: str) -> None:
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()
    
    cursor.execute('''
        INSERT INTO urls (slug, url)
        VALUES (?, ?)
    ''', (slug, url))
    
    con.commit()
    con.close() 
    
# Get the URL mapped to by the given slug
def get_url(slug: str) -> str:
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()
    
    cursor.execute('''
        SELECT url FROM urls WHERE slug = ?
    ''', (slug,))
    
    url = cursor.fetchone()
    con.close()
    
    if url is not None:
        return url[0]
    else:
        return None