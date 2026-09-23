from tkinter import *
from tkinter import messagebox

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found.")

root = Tk()
root.geometery("200x200")

button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=40)

root.mainloop()