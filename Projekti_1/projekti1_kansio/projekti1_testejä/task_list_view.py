from tkinter import ttk, constants

class TaskListView:
    def __init__(self, root, handle_open_add):
        self._root = root
        self._handle_open_add = handle_open_add
        self._frame = None
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill= constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master= self._root)

        label = ttk.Label(master= self._frame, text= "My tasks")
        button = ttk.Button(
            master= self._frame,
            text= "Add task",
            command= self._handle_open_add
        )

        label.grid(row= 0, column= 0, padx= 5, pady= 5)
        button.grid(row= 1, column= 0, padx= 5, pady= 5)
