import tkinter as tk
from tkinter import messagebox
from models.auth_service import register
from ui.login_screen import LoginScreen

class RegisterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # create account label settings
        tk.Label(self, text= "Create Account", font= ("Arial", 24, "bold")).pack(pady= 40)

        # username field settings
        tk.Label(self, text="Username").pack()
        self.usernameEntry = tk.Entry(self, width=30)
        self.usernameEntry.pack(pady=5)

        # password field settings
        tk.Label(self, text="Password").pack()
        self.passwordEntry = tk.Entry(self, width=30, show="*")
        self.passwordEntry.pack(pady=5)

        # confirm password field settings
        tk.Label(self, text="Confirm Password").pack()
        self.confirmEntry = tk.Entry(self, width=30, show="*")   # second password field for confirmation
        self.confirmEntry.pack(pady=5)

        # register and back to login button settings
        tk.Button(self, text="Register", width=20, command=self.handleRegister).pack(pady=20)
        tk.Button(self, text="Back to Login", command=self.goToLogin).pack()

    def handleRegister(self):
        username = self.usernameEntry.get()             # get() reads the input in the self.usernameEntry field
        password = self.passwordEntry.get()
        confirm = self.confirmEntry.get()

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        success = register(username, password)
        if success:
            messagebox.showinfo("Success", f"Account Created! Please log in.")
            self.clearFields()
            self.controller.showFrame(LoginScreen)
        else:
            messagebox.showerror("Error", "Username already exists.")

    def clearFields(self):
        self.usernameEntry.delete(0, tk.END)
        self.passwordEntry.delete(0,tk.END)
        self.confirmEntry.delete(0, tk.END)

    def goToLogin(self):
        self.controller.showFrame(LoginScreen)
