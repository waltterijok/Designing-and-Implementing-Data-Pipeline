import bcrypt
from database.user_queries import *
from models.user import *

current_user = None

def register(username, password):
    username = username.strip()         # .strip removes any accidental spaces 
    if not username:                        # checks if the username input is empty
        print("Username cannot be empty")
        return False
    if not password:                        # checks the password input is not empty
        print("Password cannot be empty")
        return False
    if getUserByUsername(username):         # checks if the username already exists
        print("Username already exists.")
        return False
    
    createUser(username, password)
    print(f"Account '{username}' created successfully")
    return True

def login(username, password):
    global current_user                     # 'global' tells python were modifying the global "current_user" variable
    row = getUserByUsername(username)       # looks up the username from the database
    if not row:                             # if the username doesnt exist, prints the error
        print("Username not found")
        return False
    
    passwordMatches = bcrypt.checkpw(       # checks the entered password against saved hashes
        password.encode("utf-8"),           # encodes the entered password to bytes 
        row["password"]                     # the stored password hash lives here
    )
    if not passwordMatches:
        print("Incorrect password")
        return False
    
    current_user = User.from_row(row)       # builds the current_user as a user object 
    print(f"Welcome back {current_user}!")
    return True

def logout():                               # clears the current user by setting current_user to None
    global current_user
    current_user = None
    print("Logged out successfully.")

def getCurrentUser():
    return current_user