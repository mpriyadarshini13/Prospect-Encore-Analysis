import pymysql as db
import Pencorehome
import admin
import monitor


conn=db.connect("localhost","root","","pencore")
cur=conn.cursor()

#program to update prospect:
def updateprospect():
    print("""What do you want to update?
        1.Phone
        2.Model
        3.colour
        4.Priority
        """)
    ch=input("Enter choice")

    if ch=='1':
        prospId = input("Enter prospId")
        prospPhone=input("Enter new phone no.")
        qry="update prospect set prospPhone=%s where prospId=%s"
        cur.execute(qry,(prospPhone,prospId))
        conn.commit()

    elif ch=='2':
        prospId = input("Enter prospId")
        interestedModel=input("Enter new Interested Model")
        qry="update prospect set interestedModel=%s where prospId=%s"
        cur.execute(qry,(interestedModel,prospId))
        conn.commit()

    elif ch == '3':
        prospId = input("Enter prospId")
        interestedColor = input("Enter new Interested Color")
        qry = "update prospect set interestedColor=%s where prospId=%s"
        cur.execute(qry, (interestedColor, prospId))
        conn.commit()

    elif ch=='4':
        prospId = input("Enter prospId")
        priority=input("Enter new priority(high/low/medium):-")
        qry="update prospect set priority=%s where prospId=%s"
        cur.execute(qry,(priority,prospId))
        conn.commit()

    else:
        print("Invalid Input")



#program for login:
def login():
    username=input("Enter username")
    password=input("Enter password")
    cur=conn.cursor()
    qry=f"""select usertype,fullname
           from employee
           where username='{username}' and userpass='{password}' and status='Activated'"""
    cur.execute(qry)
    rs=cur.fetchall()
    if cur.rowcount==1:
        if rs[0][0]=="admin":
            admin.adminmenu()

        elif  rs[0][0]=="Admin":
            admin.adminmenu()

        elif rs[0][0]=="monitor":
            monitor.monitormenu()

        elif rs[0][0]=="Monitor":
            monitor.monitormenu()


    else:
        print("invalid username or password")
        Pencorehome.main()


#program to create new user account:
def createuser():
    userName = input("Enter Username")
    userPass = input("Enter Password")
    userType = input("Enter usertype")
    fullName = input("Enter name")
    gender = input("Enter Gender(M/F)")
    phone = input("Enter Phone number")
    email = input("Enter Email Address")
    status = input("Enter Status(Activated or Deactivated)")
    qry = "insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(qry, (userName, userPass, userType, fullName, gender, phone, email, status))
    conn.commit()




#program to create new prospect:
def addnewprospect():
    pid = input("Enter ProspectId")
    pname = input("Enter Prospect Name")
    pphone = input("Enter Prospect Phone no")
    paddress = input("Enter Prospect Address")
    pcarmod = input("Enter Car Model")
    pcarcolor = input("Enter Car colour")
    visitdate = input("Enter date of visit")
    visitday = input("Enter day of visit")
    bookamount = input("Enter booking amount")
    pgender = input("Enter Prospect Gender(M/F)")
    incgrp = input("Enter Income Group")
    priority = input("Enter priority(high/low/medium)")
    pmode = input("Enter purchase mode(Cash/Installment)")

    qry = "insert into prospect values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(qry, (pid,pname,pphone,paddress,pcarmod,pcarcolor,visitdate,visitday,bookamount,pgender,incgrp,priority,pmode))
    conn.commit()


#program to showdetails:
def showdetails(tname):
    qry="select * from "+tname+""
    cur.execute(qry)
    rs=cur.fetchall()
    if cur.rowcount>0:
        print("userName\tuserPass\tuserType\tfullName\tgender\tphone\temail\tstatus")
        for rows in rs:
            for cols in rows:
                print(str(cols)+"\t",end="")
            print()



#program to change password:
def changepassword():
    unm=input("Enter username")
    pwd=input("Enter new password")
    repwd=input("Retype password to confirm")
    if pwd==repwd:
        qry="update employee set userpass=%s where username=%s"
        cur.execute(qry,(pwd,unm))
        conn.commit()



#program to activate or deactivate account:
def activateordeactivate():
    unm = input("Enter username")
    status=input("Enter status(Activated/Deactivated):")
    qry = "update employee set status=%s where username=%s"
    cur.execute(qry,(status,unm))
    conn.commit()





#program to insert car details:
def insertcardetails():
    modelid = input("Enter Model Id")
    modelname = input("Enter Model Name")
    price = input("Enter price")
    qry = "insert into carmodels values(%s,%s,%s)"
    cur.execute(qry, (modelid, modelname, price))
    conn.commit()











