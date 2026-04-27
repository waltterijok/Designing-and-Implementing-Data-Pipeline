from tkinter import Tk, ttk
from _hello_view import HelloView
from _goodbye_view import GoodByeView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
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

        self._current_view.pack()

    def _show_good_bye_view(self):
        self._hide_current_view()

        self._current_view = GoodByeView(
            self._root,
            self._handle_hello
        )

        self._current_view.pack()

    '''def _handle_button_click(self):
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
        )'''

window = Tk()
window.title("Tkinter example")
window.configure(bg="white")

ui = UI(window)
ui.start()

window.mainloop()