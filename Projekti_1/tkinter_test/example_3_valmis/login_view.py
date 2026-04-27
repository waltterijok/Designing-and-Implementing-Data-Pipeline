from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_login):
        self._root = root                   # valitsee näyttöalueen, Root = koko ikkuna
        self._handle_login = handle_login   # tallentaa funktion "handle_login" (main.py) lähettämän parametrin tähän
        self._frame = None                  # alkutilanne ennen kuin _initialize luo näyttöalueen (framen)
        self._initialize()                  # rakentaa framen

    def pack(self):
        self._frame.pack(fill= constants.X) # luo framen ja täyttää ikkunan x-akselilta

    def destroy(self):
        self._frame.destroy()               # kun self._frame.destroy kutsutaan, tuhoaa framen

    def _initialize(self):
        self._frame = ttk.Frame(master= self._root)

        label = ttk.Label(master= self._frame, text= "Login")
        username_label = ttk.Label(master= self._frame, text= "Username")
        username_entry = ttk.Entry(master= self._frame)
        password_label = ttk.Label(master= self._frame, text= "Password")
        password_entry = ttk.Entry(master= self._frame)
        button = ttk.Button(
            master=self._frame,
            text= "Login",
            command= self._handle_login
        )

        label.grid(row= 0, column= 0, columnspan= 2, sticky= constants.W, padx= 5, pady= 5)
        username_label.grid(row= 2, column= 0, padx= 5, pady= 5)
        username_entry.grid(row= 2, column= 1, sticky= (constants.E, constants.W), padx= 5, pady= 5)
        password_label.grid(row= 3, column= 0, padx= 5, pady=5)
        password_entry.grid(row= 3, column= 1, sticky= (constants.E, constants.W), padx= 5, pady= 5)
        button.grid(row= 1, column= 0, columnspan= 2, sticky= (constants.E, constants.W), padx= 5, pady= 5)

        self._frame.grid_columnconfigure(1, weight= 1, minsize= 400)