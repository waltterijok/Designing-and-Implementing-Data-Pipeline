from tkinter import Tk, ttk

root = Tk()

root.geometry("500x500")
root.title("My firts gui")

label = ttk.Label(root, text= "hello world!", font=('Arial', 18))
label.pack()

root.mainloop()