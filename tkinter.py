from tkinter import *

window=Tk()
window.title("My profile card")
window.geometry("400x380")

title = Label(Window, text="my profile card", fg="white", bg="purple", width=40)
title.grid(row=0, column=0, columnspan=0, padx=10, pady=10)

name_label = Label(window, text = "name:", fg= "black", bg= "white")
name_label.grid(row=1, column=0, padx=10, pady=5)