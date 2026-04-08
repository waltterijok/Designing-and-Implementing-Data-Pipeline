# This file cretaes a class called 'Task' which is used as a blueprint for task objects

class Task:
    def __init__(self, id, title, done, created_at):        # This is the constructor that creates a new task object
        self.id = id                                        # new task id is stored here
        self.title = title                                  # new task title is stored here
        self.done = bool(done)                              # task completion is stored here, and changed from 1/0 to boolean true/false
        self.created_at = created_at                        # stores the creation date

    @classmethod
    def from_row(cls, row):         # cls builds a task object using the data directly inside a row of the database
        return cls(                 # calls the init constructor (line 4)to create a task using the values found in the database row
            id = row["id"],
            title = row["title"],
            done = row["done"],
            created_at = row["created_at"]
        )
    
    def __repr__(self):                                 # __repr__ defines what gets printed when you use print(task)
        status = "done" if self.done else "Pending"     # prints status as done if self.done is set to 'done', else prints 'pending'
        return f"[{self.id}] {self.title} ({status})"