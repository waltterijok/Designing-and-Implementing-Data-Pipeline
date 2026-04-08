import bcrypt
from database.connection import getConnection

def createUser(username, password):
    conn = getConnection()
    cursor = conn.cursor()
    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    cursor.execute(
        "INSERT INTO Users (username, password) VALUES (?, ?)",
        (username, hashed)
    )

    conn.commit()
    conn.close()

def getUserByUsername(username):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Users WHERE username = ?", (username,)
    )

    user = cursor.fetchone()             # fetchone() fetches a single row from the database
    conn.close()
    return user