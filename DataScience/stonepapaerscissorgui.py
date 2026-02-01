#STONEPAPERSCISSOR
import random
import tkinter
from tkinter import messagebox
 
window=tkinter.Tk()
window.geometry("400x400")
Options=["stone", "paper" , "scissor"]
def Game():
    Computerchance=random.choice(Options)
    PlayerChance=TextInput.get().lower()
    print(f"Computer : {Computerchance}")
    print(f"Player : {PlayerChance}")
 
    if Computerchance=="stone" and PlayerChance =="paper":
        messagebox.showinfo("Game Winner","Player Wins")
    elif PlayerChance=="stone" and  Computerchance=="paper":
        messagebox.showinfo("Game Winner","Computer Wins")
    elif Computerchance=="paper" and  PlayerChance=="scissor":
        messagebox.showinfo("Game Winner","Player Wins")
    elif PlayerChance=="paper" and  Computerchance=="scissor":
        messagebox.showinfo("Game Winner","Computer Wins")
    elif Computerchance=="scissor" and  PlayerChance=="stone":
        messagebox.showinfo("Game Winner","Player Wins")
    elif PlayerChance=="scissor" and  Computerchance=="stone":
        messagebox.showinfo("Game Winner","Computer Wins")
    elif PlayerChance=="stone" and  Computerchance=="stone":
        messagebox.showinfo("Game Winner","Draw")
    elif PlayerChance=="paper" and  Computerchance=="paper":
        messagebox.showinfo("Game Winner","Draw")
    elif PlayerChance=="scissor" and  Computerchance=="scissor":
        messagebox.showinfo("Game Winner","Draw")
 
LabelName=tkinter.Label(window, text="Enter Choice: ")
LabelName.place(x="100", y="100")
 
TextInput=tkinter.Entry(window)
TextInput.place(x="200",y="100")
 
ButtonName=tkinter.Button(window,text="Submit",command=Game)
ButtonName.place(x="300",y="300")
 
window.mainloop()