from tkinter import *
from tkinter import messagebox
from PLI import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650X400")

upload = Image.open("app_Phantom.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = label(root,
text="Hey User! Welcome to the Denomination Counter Application",
bg="light blue")
label1=place(relx=0.5, y=340, anchor=CENTRE)

def msg():
    MsgBox = mesagebox.showinfo(
        "Alert", "Do You Want To Calculate The Denomination Count?")
    if MsgBox =="ok":
        topwin()
button1 = Button(root,
                 text="Lets Get Started!",
                 command=msg,
                 bg="brown",
                 fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominatios Calculator")
    top.configure(bg="light grey")
    top.geometry("600X350+50+50")
    