import tkinter as tk
from tkinter import messagebox
from models.auth_service import login

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label settings
        tk.Label(self, text = "W's To-Do App", font= ("Arial", 24, "bold")).pack(pady=40)

        # username field settings
        tk.Label(self, text= "Username").pack()
        self.usernameEntry = tk.Entry(self, width= 30)
        self.usernameEntry.pack(pady= 5)

        # password field settings
        tk.Label(self, text= "Password").pack()
        self.passwordEntry = tk.Entry(self, width= 30, show= "*")       # show= "*" hides the password input
        self.passwordEntry.pack(pady= 5)

        # login button settings
        tk.Button(self, text= "Login", width= 20, command= self.handleLogin).pack(pady= 20)

        # registration button settings
        tk.Button(self, text= "Don't have an account? Register here!", command= self.goToRegister).pack()

    def handleLogin(self):
        username = self.usernameEntry.get()             # get() reads the input in the self.usernameEntry field
        password = self.passwordEntry.get()
        success = login(username, password)
        if success:
            self.passwordEntry.delete(0, tk.END)        # .delete clears the password field after successful login
            self.controller.showFrame(
                __import__("ui.task_screen", fromlist= ["TaskScreen"]).TaskScreen
            )
        else:
            messagebox.showerror("Login failed", "Invalid username or password")

    def goToRegister(self):
        from ui.register_screen import RegisterScreen
        self.controller.showFrame(RegisterScreen)