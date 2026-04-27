from tkinter import Tk, Toplevel, ttk, constants

root = Tk()

class AddTaskView:
    def __init__(self, root, handle_add):
        self._root = root
        self._handle_add = handle_add
        self._frame = None
        self._entry = None
        self._initialize()

    def _initialize(self):
        self._frame = Toplevel(master= self._root)
        self._frame.title = "Add task"
        self._frame.geometry("300x120")

        label = ttk.Label(master= self._root, text= "Task name")
        self._entry = ttk.Entry(master= self._frame)
        button = ttk.Button(master= self._frame, text= "Add", command= self._handle_click)

        label.grid(row= 0, column= 0, padx= 10, pady= 10)
        self._entry.grid(row= 0, column= 1, sticky=(constants.E, constants.W), padx= 10, pady= 10)
        button.grid(row= 1, column= 0, columnspan= 2, sticky=(constants.E, constants.W), padx= 10, pady= 5)

        self._frame.grid_columnconfigure(1, weight= 1)

root.mainloop()