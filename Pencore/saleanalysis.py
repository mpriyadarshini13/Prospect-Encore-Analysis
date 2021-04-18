import pymysql as db

conn=db.connect("localhost","root","","pencore")
cur=conn.cursor()

def test():
    qry="""select date_format(saledate,'%y') year,modelid, count(*)
           from caranalysis
           group by date_format(saledate, '%y'), modelid """

    cur.execute(qry)
    ds=cur.fetchall()
    carlist=[]
    years=[]
    for i in ds:
        if i[1] not in carlist:
            carlist.append(i[1])
        if i[0] not in years:
            years.append(i[0])

    years.sort()


    dic={}
    for mod in carlist:
        lst=[]
        yr=[]
        for y,m,c in ds:
            if m==mod and y not in yr:
                lst.append(c)
                yr.append(y)
            elif m==mod and y in yr:
                lst.pop()
                lst.append(c)
            else:
                if y not in yr:
                    lst.append(0)
                    yr.append(y)
        dic[mod]=lst
    return (years,dic)



