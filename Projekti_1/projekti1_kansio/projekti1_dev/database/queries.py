from database.connection import getConnection

def addTask(title, user_id):
    conn = getConnection()      # calls getConnection to open connection to the database
    cursor = conn.cursor()      # uses cursor to send SQL commands to the database
    cursor.execute("INSERT INTO Tasks (title, user_id) VALUES (?, ?)", (title, user_id)) 
    conn.commit()               # saves edits into the database
    conn.close()                # closes the connection

    '''
    The (?) is a placeholder, sqlite fills it from the tuple (title, user_id)
    In the query, when you use (?), the query will take it as a placeholder, and fills
    it from the NEXT available value which here is (title,).
    ALWAYS REMEMBER TO USE THE COMMA INSIDE THE VARIABLE, that makes it a tuple
    (title) alone would not work.
    NEVER USE F-STRINGS IN SQL, it leaves you open to SQL injection attacks
    '''

def getAllTasks(user_id):
    conn = getConnection()      
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tasks WHERE user_id = ? ORDER BY id",
                    (user_id,))                           # sends the query to the database, collecting all objects (rows) by id
    tasks = cursor.fetchall()                           # fetcall() collects all of the rows and saves them to a list
    conn.close()                                        # closes the connection
    return tasks                                        # returns the list with the tasks to the caller

def updateTask(new_title, task_id, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Tasks SET title = ? WHERE id = ? AND user_id = ?", (new_title, task_id, user_id))
    conn.commit()
    conn.close()

def deleteTask(task_id, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
    conn.commit()
    conn.close()

def markDone(task_id, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Tasks SET done = 1 WHERE id = ? AND user_id = ?", (task_id, user_id))
    conn.commit()
    conn.close()