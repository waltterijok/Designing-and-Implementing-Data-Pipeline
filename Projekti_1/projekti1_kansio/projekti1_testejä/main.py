from tkinter import Tk
from main_ui import UI

window = Tk()
window.title("Task List")

ui = UI(window)
ui.start()

window.mainloop()