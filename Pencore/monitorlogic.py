import pymysql as db



conn=db.connect("localhost","root","","pencore")
cur=conn.cursor()
# Program to show details
def showdetails(tname, extra="1=1"):
    qry="select * from "+tname+" where "+extra
    cur.execute(qry)
    rs=cur.fetchall()
    if cur.rowcount>0:
        print("userName\tuserPass\tuserType\tfullName\tgender\tphone\temail\tstatus")
        for rows in rs:
            for cols in rows:
                print(str(cols)+"\t",end="")
            print()

    else:
        print("No such record with given input match")

# program to search
def search():
    print("""Select:-
          1. By id
          2. By Priority
          """)
    ch = input("Enter choice")
    if ch == '1':
        pid = input("Enter prospect id")
        showdetails("prospect","prospId="+pid)
    elif ch == '2':
        priority = input("Enter Priority")
        showdetails("prospect", "priority='" + priority+"'")

    else:
        print("Invalid input")







