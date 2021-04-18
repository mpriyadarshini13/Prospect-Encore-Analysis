import blogic
import Pencorehome
import monitorlogic
import os
import uchoice

def monitormenu():

    while(True):
        os.system("cls")
        print("""--------------------------------------------------------------------
        Main Menu
        1. Add New Prospect
        2. View All prospect
        3. Update Prospect
            (a)Phone    (b)Model    (c)Colour   (d)Priority        
        4. Search Prospect
            (a)By Priority      (b)Prospect Id
        5. Change own password
        6. Insert car sale details
        7. Data Visualization
        8. Signout     
        """)

        choice=int(input("Enter your choice:-"))
        if choice == 1:
            blogic.addnewprospect()
            input("Press any key to continue:-")
            pass
        elif choice == 2:
            blogic.showdetails("prospect")
            input("Press any key to continue:-")
            pass
        elif choice == 3:
            blogic.updateprospect()
            input("Press any key to continue:-")
            pass
        elif choice == 4:
                monitorlogic.search()
                input("Press any key to continue:-")
                pass
        elif choice == 5:
            blogic.changepassword()
            input("Press any key to continue:-")
            pass
        elif choice == 6:
            blogic.insertcardetails()
            input("Press any key to continue:-")
            pass
        elif choice == 7:
            uchoice.plot()
            pass
        elif choice == 8:
            print("Signed out Successfully")
            return Pencorehome.main()
        else:
            print("Invalid choice:-")
            Pencorehome.main()