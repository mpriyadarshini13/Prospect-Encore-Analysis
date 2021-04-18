import pymysql as db
import saleanalysis
import numpy as np
from matplotlib import pyplot as plt



conn=db.connect("localhost","root","","pencore")
cur=conn.cursor()


def drawplotindi(fig):
    plt.figure(figsize=(6*3.13, 4*3.13))
    year,di = saleanalysis.test()
    for i in (enumerate(di,1)):
        plt.subplot((len(di)//2)+1,2,i[0])
        if fig =="bar":
            plt.bar(year, di[i[1]], label=i[1], width=.1)

        elif fig == "line":
            plt.plot(year, di[i[1]], label=i[1], marker="*")

            plt.xlabel("year")
            plt.ylabel("Unit sold")
            plt.legend()

        plt.show()

def drawplotcombi(fig):
    plt.figure(figsize=(6*3.13, 4*3.13))
    year,di = saleanalysis.test()
    year=np.array(year,np.dtype("int"))
    val=0
    model=list(di.keys())
    arr=np.zeros(len(di["A3"]))

    for i in (enumerate(di, 1)):
        if fig=="bar":
            plt.subplot(1,2,1)
            plt.bar(year+val,di[i[1]], label=i[1],width=.1)
            plt.xlabel("year")
            plt.ylabel("Unit sold")
            plt.legend()
            plt.subplot(1,2,2)
            plt.bar(year, di[i[1]], label=i[1], width=.1,bottom=arr)
            arr += np.array(di[i[1]])
            plt.xlabel("year")
            plt.ylabel("unit sold")
            plt.legend()


        elif fig == "line":
            plt.plot(year, di[i[1]], label=i[1], marker="*")
        plt.xlabel("year")
        plt.ylabel("Unit sold")
        plt.legend()

    plt.show()



