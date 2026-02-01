import MySQLdb
con=MySQLdb.connect("localhost","root","","ds")

try:
    cur=con.cursor()
    cur.execute("create table emp(eid int, ename varchar(200),esal int)")
    con.commit()
    con.close()
    print("Created!!!")
except:
    print("err")

