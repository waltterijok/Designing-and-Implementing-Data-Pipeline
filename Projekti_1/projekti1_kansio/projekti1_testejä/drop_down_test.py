from tkinter import *

root = Tk()
root.title("Alasvetovalikko")
root.geometry("400x400")

options= [
    "Ensimmäinen",
    "Toinen",
    "Kolmas",
    "Neljäs",
    "Viides"
]

selectItem = StringVar()
selectItem.set(options[0])

def show():
    myLabel = Label(root, selectItem.get())
    myLabel.pack()

drop = OptionMenu(root, selectItem, *options)
drop.pack()

myButton = Button(root, text= "Valitse tästä", command= show)
myButton.pack()

root.mainloop()