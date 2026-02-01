from tkinter import *

window=Tk()
window.geometry("200x200")
photo=PhotoImage(file="p1.png")
l1=Label(window,text="Hello Muskan!!!",
         font=("Papyrus",30,"bold"),
         fg="#E01D44",
         bg="#BAC0C2",
         pady=100,
         padx=150,
         image=photo,
         compound="bottom")

l1.pack()

window.mainloop()