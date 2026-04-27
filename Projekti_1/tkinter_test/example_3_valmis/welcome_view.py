from tkinter import ttk, constants

class WelcomeView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill= constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master= self._root)

        label = ttk.Label(master= self._frame, text= "LWelcome")
        button = ttk.Button(
            master= self._frame,
            text= "Log out",
            command= self._handle_logout
        )

        label.grid(row= 0, column= 0, padx= 5, pady= 5)
        button.grid(row= 1, column= 0, padx= 5, pady= 5)