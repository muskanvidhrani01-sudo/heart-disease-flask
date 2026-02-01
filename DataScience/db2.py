import MySQLdb
con=MySQLdb.connect("localhost","root","","ds")

try:
    cur=con.cursor()
    id=input("Enter Eid: ")
    n=input("Enter Name: ")
    sal=input("Enter Salary: ")
    cur.execute("insert into emp values("+ id +",'"+ n +"',"+ sal +")")
    con.commit()
    con.close()
    print("Inserted!!!")
except:
    print("err")

