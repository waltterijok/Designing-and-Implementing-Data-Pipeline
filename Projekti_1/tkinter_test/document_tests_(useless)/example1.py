from tkinter import Tk, ttk
from _hello_view import HelloView
from _goodbye_view import GoodByeView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        '''self._entry= ttk.Entry(
            master= self._root
        ) 

        button = ttk.Button(
            master= self._root,
            text= "Button",
            command= self._handle_button_click
        )

        self._entry.grid(row= 0, column= 0)
        button.grid(row= 1, column= 0)'''



        ''''heading_label = ttk.Label(
            master = self._root, 
            text = "Login"
            )

        username_label = ttk.Label(
            master = self._root, 
            text = "Username"
            )
        username_entry = ttk.Entry(
            master = self._root
            )

        password_label = ttk.Label(
            master = self._root, 
            text = "Password"
            )
        password_entry = ttk.Entry(
            master = self._root
            )

        button = ttk.Button(
            master = self._root, 
            text = "Sign in"
            )
        
        heading_label.grid(row= 0, column= 0, columnspan= 2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(row= 1, column= 0)
        username_entry.grid(row= 1, column= 1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row= 2, column= 0)
        password_entry.grid(row= 2, column= 1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure(1, weight = 1, minsize=400)'''

        self._show_hello_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

            self._current_view = None

    def _handle_good_bye(self):
        self._show_good_bye_view()

    def _handle_hello(self):
        self._show_hello_view()

    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = HelloView(
            self._root,
            self._handle_good_bye()
        )

    def _show_good_bye_view(self):
        self._hide_current_view()

        self._current_view = GoodByeView(
            self._root,
            self._handle_hello
        )

        self._current_view.pack()

    def _handle_button_click(self):
        entry_value = self._entry.get()
        print(f"Value of entry is: {entry_value}")

        button_a = ttk.Button(
            master= self._root,
            text= "Button A",
            command= lambda:self._handle_button_click("button a")
        )

        button_b = ttk.Button(
            master= self._root,
            text= "Button B",
            command= lambda:self._handle_button_click("button b")
        )


'''class HelloView:
    def __init__(self, root, handle_good_bye):
        self._root = root
        self._handle_good_bye = handle_good_bye
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill= constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master= self._root)
        label = ttk.Label(master= self._frame, text= "Hello!")

        button = ttk.Button(
            master= self._frame,
            text= "Say goodbye",
            command= self._handle_good_bye
        )

        label.grid(row= 0, column= 0)

        button.grid(row= 1, column= 0)'''

window = Tk()
window.title("Tkinter example")
window.configure(bg="white")

ui = UI(window)
ui.start()

window.mainloop()