import tkinter as tk
from tkinter import messagebox, simpledialog            # simpledialog lets us show a simple input popup
from models.auth_service import *
from models.task_service import *
from ui.login_screen import *

class TaskScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # top bar with welcome label and logout button
        topBar = tk.Frame(self)                         # a frame to hold the top bar widgets side by side
        topBar.pack(fill="x", padx=20, pady=10)         # fill="x" stretches it across the full width

        self.welcomeLabel = tk.Label(topBar, text="", font=("Arial", 14))
        self.welcomeLabel.pack(side="left")             # side="left" pushes it to the left of the bar

        tk.Button(topBar, text="Logout", command=self.handleLogout).pack(side="right")  # pushed to the right

        # filter buttons
        filterBar = tk.Frame(self)
        filterBar.pack(pady=5)

        tk.Button(filterBar, text="All", width=10, command=lambda: self.loadTasks("all")).pack(side="left", padx=5)
        tk.Button(filterBar, text="Pending", width=10, command=lambda: self.loadTasks("pending")).pack(side="left", padx=5)
        tk.Button(filterBar, text="Done", width=10, command=lambda: self.loadTasks("done")).pack(side="left", padx=5)
        # lambda: is used here to pass an argument to the function when the button is clicked

        # task listbox
        self.listbox = tk.Listbox(self, width=50, height=15, font=("Arial", 12))  # Listbox displays a scrollable list
        self.listbox.pack(padx=20, pady=10)

        # action buttons
        buttonBar = tk.Frame(self)
        buttonBar.pack(pady=5)

        tk.Button(buttonBar, text="Add Task", width=14, command=self.handleAdd).pack(side="left", padx=5)
        tk.Button(buttonBar, text="Mark Done", width=14, command=self.handleComplete).pack(side="left", padx=5)
        tk.Button(buttonBar, text="Delete", width=14, command=self.handleDelete).pack(side="left", padx=5)

        self.currentTasks = []

    def onShow(self):                                   # called by app.py every time this screen is shown
        user = getCurrentUser()
        if user:
            self.welcomeLabel.config(text=f"Welcome, {user.username}!")  # config() updates a widget's properties
        self.loadTasks("all")                           # load all tasks when the screen appears

    def loadTasks(self, filter):
        self.listbox.delete(0, tk.END)                  # clear the listbox before reloading
        if filter == "all":
            self.currentTasks = getTasks()
        elif filter == "pending":
            self.currentTasks = getPendingTasks()
        elif filter == "done":
            self.currentTasks = getDoneTasks()
        for task in self.currentTasks:
            status = "✓" if task.done else "○"
            self.listbox.insert(tk.end, f"{status} {task.title}")

    def getSelectedTasks(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task first.")
            return None
        index = selection[0]
        return self.currentTasks[index]
    
    def handleAdd(self):
        title = simpledialog.askstring("New Task", "Enter task Titles:")
        if title:
            createTask(title)
            self.loadTasks("All")

    def handleComplete(self):
        task = self.getSelectedTasks()
        if task:
            completeTask(task.id)
            self.loadTasks("All")

    def handleDelete(self):
        task = self.getSelectedTasks()
        if task:
            confirm = messagebox.askyesno("Confirm", f"Delete '{task.title}'?")
            if confirm:
                removeTask(task.id)
                self.loadTasks("All")

    def handleLogout(self):
        logout()
        self.controller.showFrame(LoginScreen)