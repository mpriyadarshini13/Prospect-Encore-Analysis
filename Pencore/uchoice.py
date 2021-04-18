
import graphlogic
import os


# User choices for graph
def plot():
    os.system("cls")
    print("""-----------------------------------------
          1.Bar Plot
          2.Line Plot
          ----------------------------------------------""")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(""""
              1. Individual Plot
              2. Combined Plot
              """)
        ch = int(input("Enter your choice:-"))
        if ch == 1:
            graphlogic.drawplotindi("bar")
        elif ch == 2:
            graphlogic.drawplotcombi("bar")

    elif choice == 2:
        print(""""
              1. Individual Plot
              2. Combined Plot
              """)
        ch = int(input("Enter your choice:-"))
        if ch == 1:
            graphlogic.drawplotindi("line")
        elif ch==2:
            graphlogic.drawplotcombi("line")

    else:
        print("Wrong input")

plot()