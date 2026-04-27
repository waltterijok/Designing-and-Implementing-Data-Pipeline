from tkinter import Tk
from ui import UI

'''from welcome_view import WelcomeView
from login_view import LoginView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._handle_logout)
        self._current_view.pack()

    def _show_welcome_view(self):
        self._hide_current_view()
        self._current_view = WelcomeView(self._root, self._handle_logout)
        self._current_view.pack()

    def _handle_login(self):
        self._show_welcome_view()

    def _handle_logout(self):
        self._show_login_view()'''

window = Tk()
window.title("Example 3")

ui = UI(window)
ui.start()

window.mainloop()