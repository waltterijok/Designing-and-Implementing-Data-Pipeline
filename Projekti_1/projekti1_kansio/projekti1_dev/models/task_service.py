from database.queries import *
from models.task import Task
from models.auth_service import getCurrentUser

def createTask(title):                      # function to create tasks, takes the title string as variable
    user = getCurrentUser()   
    if not user:
        print(f"You must be logged in to create tasks.")  
        return             
    title = title.strip()                   # .strip removes any possible spaces in front of or behind the title
    if not title:                           # checks if the title is empty after stripping
        print("Title cannot be empty.")     # if title is empty, prints out the message and stops the function
        return
    addTask(title, user.id)                 # calls the addTask function from queries file and saves the task
    print(f"Task '{title}' added")          # confirms to the user that the task was saved successfully

def getTasks():                             # function to fetch and return all tasks
    user = getCurrentUser() 
    if not user:
        print("You must be logged in to view tasks")
    rows = getAllTasks(user.id)                            # fetches the raw database rows 
    return [Task.from_row(row) for row in rows]     # uses Task.from_row (from task.py) to convert the raw data into task objects and returns them

def getPendingTasks():                                      # function to fetch only pending tasks
    return [task for task in getTasks() if not task.done]     # filters the list of tasks to fetch only unfinished tasks and returns them

def getDoneTasks():                                         # does the same but for finished tasks
    return [task for task in getTasks() if task.done]         

def completeTask(task_id):                      # function to mark a task as done
    user = getCurrentUser()  
    if not user:
        print("You must be logged in")           
        return
    if isinstance(task_id, list):
        for id in task_id:
            markDone(id, user.id)                    # calls the markDone from queries.py and sends the task_id to it    
            print(f"Task {id} marked as done")  # prints out and informs the user the task has been marked done successfully
    else:
        markDone(task_id, user.id)
        print(f"Task {task_id} marked as done")

def removeTask(task_id):                        # does the same as completeTask but for deleting a task
    user = getCurrentUser()
    if not user:
        print("You must be logged in")
        return
    deleteTask(task_id, user.id)                                     
    print(f"Task {task_id} has been removed from list")

def renameTask(task_id, new_title):
    user = getCurrentUser()
    if not user:
        print("You must be logged in")
        return
    new_title = new_title.strip()
    if not new_title:
        print("Task name cannot be empty")
        return
    updateTask(task_id, new_title, user.id)
    print(f"Task {task_id} name updated to '{new_title}'")