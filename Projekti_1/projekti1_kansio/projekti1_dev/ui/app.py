import tkinter as tk                                    # import tkinter and give it the alias tk
from ui.login_screen import LoginScreen                 # import the login screen
from ui.register_screen import RegisterScreen           # import the register screen
from ui.task_screen import TaskScreen 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("W's To-Do App")
        self.geometry("500x600")
        self.resizable(True, True)

        self.container = tk.Frame(self)
        self.container.pack(fill= "both", expand= True)

        self.frames = {}

        for Screen in (LoginScreen, RegisterScreen, TaskScreen):
            frame = Screen(self.container, self)
            self.frames[Screen] = frame
            frame.grid(row= 0, column= 0, sticky= "nsew")

        self.showFrame(LoginScreen)

    def showFrame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()
        if hasattr(frame, "onShow"):
            frame.onShow()

if __name__ == "__main__":
    app = App()
    app.mainloop()