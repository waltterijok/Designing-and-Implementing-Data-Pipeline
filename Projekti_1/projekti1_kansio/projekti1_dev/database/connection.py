import sqlite3
from config import DB_NAME

def getConnection():
    conn = sqlite3.connect(DB_NAME)     # Opens (or creates) the database and connects to it
    conn.row_factory = sqlite3.Row      # tells sqlite3 to return each row as object so we can use row["title"] and not row[0]
    return conn

def init_db():                          # this function initializes the database
    conn = getConnection()              # calls getConnection and opens the connectiong to the database
    cursor = conn.cursor()              # creates a "cursor", it lets us send SQL commands through Python
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL, 
            done INTEGER NOT NULL DEFAULT 0, 
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )
    """)

    conn.commit()
    conn.close()
    
    '''cursor.execute sends the following SQL command, 
    conn.commit saves the database edit and conn.close closes the connection'''