import MySQLdb
import tkinter
from tkinter import messagebox 
window=tkinter.Tk()
window.geometry("400x400")
con=MySQLdb.connect("localhost","root","","ds")
def clear():
    TextName.delete(0,tkinter.END)
    TextDesc.delete(0,tkinter.END)
    Textqty.delete(0,tkinter.END)
    Textcost.delete(0,tkinter.END)
def insert():
    try:
        con=MySQLdb.connect("localhost","root","","ds")
        cur=con.cursor()
        #id=Textid.get()
        n=TextName.get()
        d=TextDesc.get()
        q=Textqty.get()
        c=Textcost.get()
        cur.execute("insert into product(productname,description,quantity,cost) values('"+ n +"','"+ d +"','"+ q +"','"+ c +"')")
        con.commit()
        con.close()
        messagebox.showinfo("Title","Inserted!!!")
        clear()
        
    except:
        messagebox.showerror("Title","Not Inserted")

def delete():
    try:
        con=MySQLdb.connect("localhost","root","","ds")
        cur=con.cursor()
        n=TextName.get()
        cur.execute("delete from product where productname='"+ n +"'")
        con.commit()
        con.close()
        messagebox.showinfo("Title","Deleted!!!")
        clear()
    except:
        messagebox.showerror("Title","Unable to delete")

def update():
    try:
        con=MySQLdb.connect("localhost","root","","ds")
        cur=con.cursor()
        id=Textid.get()
        n=TextName.get()
        d=TextDesc.get()
        q=Textqty.get()
        c=Textcost.get()
        cur.execute("update product set productname='"+ n +"',description='"+ d +"', quantity="+ q +",cost ="+ c +" where productid="+ id +"")
        con.commit()
        con.close()
        messagebox.showinfo("Title","Updated!!!")
        clear()
    except:
        messagebox.showerror("Title","Unable to update")

def search():
    try:
        con=MySQLdb.connect("localhost","root","","ds")
        cur=con.cursor()
        id=Textid.get()
        cur.execute("select * from product where productid='"+ id +"'")
        res=cur.fetchall()
        for details in res:
            n=details[1]
            d=details[2]
            q=details[3]
            c=details[4]
            print(n,d,d,q)
   
        TextName.insert(0,n)
        TextDesc.insert(0,d)
        Textqty.insert(0,q)
        Textcost.insert(0,c)
        con.commit()
        con.close()
    except:
        messagebox.showerror("Title","Unable to retrive")

Labelid=tkinter.Label(window, text="Product id: ")
Labelid.place(x="100", y="50")

Textid=tkinter.Entry(window)
Textid.place(x="200",y="50")

ButtonSearch=tkinter.Button(window,text="Search",command=search)
ButtonSearch.place(x="300",y="50")


LabelName=tkinter.Label(window, text="Product Name: ")
LabelName.place(x="100", y="100")
 
TextName=tkinter.Entry(window)
TextName.place(x="200",y="100")

LabelDesc=tkinter.Label(window, text="Description: ")
LabelDesc.place(x="100", y="150")
 
TextDesc=tkinter.Entry(window)
TextDesc.place(x="200",y="150")
 
Labelqty=tkinter.Label(window, text="Product Quantity: ")
Labelqty.place(x="100", y="200")

Textqty=tkinter.Entry(window)
Textqty.place(x="200",y="200")

Labelcost=tkinter.Label(window, text="Product Cost: ")
Labelcost.place(x="100", y="250")

Textcost=tkinter.Entry(window)
Textcost.place(x="200",y="250")

ButtonInsert=tkinter.Button(window,text="Insert",command=insert)
ButtonInsert.place(x="100",y="300")

ButtonDelete=tkinter.Button(window,text="Delete",command=delete)
ButtonDelete.place(x="200",y="300")
 
ButtonDelete=tkinter.Button(window,text="update",command=update)
ButtonDelete.place(x="300",y="300")

window.mainloop()

