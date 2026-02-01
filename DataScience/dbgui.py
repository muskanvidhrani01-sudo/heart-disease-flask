import MySQLdb
import tkinter
from tkinter import messagebox 
window=tkinter.Tk()
window.geometry("400x400")
con=MySQLdb.connect("localhost","root","","ds")
def insert():
    try:
        cur=con.cursor()
        id=Textid.get()
        n=TextName.get()
        sal=TextSal.get()
        cur.execute("insert into emp values("+ id +",'"+ n +"',"+ sal +")")
        con.commit()
        con.close()
        messagebox.showinfo("Title","Inserted!!!")
    except:
        messagebox.showerror("Title","Not Inserted")

def delete():
    try:
        cur=con.cursor()
        n=TextName.get()
        cur.execute("delete from emp where ename='"+ n +"'")
        con.commit()
        con.close()
        messagebox.showinfo("Title","Deleted!!!")
    except:
        messagebox.showerror("Title","Unable to delete")

def search():
    try:
        cur=con.cursor()
        id=Textid.get()
        cur.execute("select * from emp where eid='"+ id +"'")
        res=cur.fetchall()
        for details in res:
            n=details[1]
            s=details[2]
        TextName.config(textvariable=n)
        TextSal.config(textvariable=s)
        con.commit()
        con.close()
    except:
        messagebox.showerror("Title","Unable to retrive")

Labelid=tkinter.Label(window, text="Enter Eid: ")
Labelid.place(x="100", y="50")

Textid=tkinter.Entry(window)
Textid.place(x="200",y="50")

ButtonSearch=tkinter.Button(window,text="Search",command=search)
ButtonSearch.place(x="300",y="50")

LabelName=tkinter.Label(window, text="Enter Name: ")
LabelName.place(x="100", y="100")
 
TextName=tkinter.Entry(window)
TextName.place(x="200",y="100")

LabelSal=tkinter.Label(window, text="Enter Salary: ")
LabelSal.place(x="100", y="150")
 
TextSal=tkinter.Entry(window)
TextSal.place(x="200",y="150")
 
ButtonInsert=tkinter.Button(window,text="Insert",command=insert)
ButtonInsert.place(x="150",y="200")

ButtonDelete=tkinter.Button(window,text="Delete",command=delete)
ButtonDelete.place(x="150",y="250")
 
window.mainloop()

