import blogic
import Pencorehome
import monitorlogic
import os
import uchoice


def adminmenu():
    while(True):
        os.system("cls")
        print("""--------------------------------------------------------------------
                Main Menu
                1. Create User Account
                   (a)Monitor          (b)Admin
                2. View All Users(Employees)
                3. View All Prospects
                4. Change Password
                5. Search Prospect
                    (a)By Priority      (b)Prospect Id
                6. Activate/Deactivate Account
                7. Data Analysis
                8. Signout     
                ----------------------------------""")
        choice=int(input("Enter Your choice:-"))
        if choice==1:
            createusr()
            input("Press any key to continue:-")

        elif choice==2:
            blogic.showdetails("employee")
            input("Press any key to continue:-")
            pass
        elif choice==3:
            blogic.showdetails("prospect")
            input("Press any key to continue:-")
            pass
        elif choice==4:
            blogic.changepassword()
            input("Press any key to continue:-")
            pass
        elif choice==5:
            monitorlogic.search()
            input("Press any key to continue:-")
            pass
        elif choice==6:
            blogic.activateordeactivate()
            input("Press any key to continue:-")
            pass
        elif choice==7:
            uchoice.plot()
            pass
        elif choice==8:
            print("Signed out successfully")
            return Pencorehome.main()
        else:
            print("Invalid choice")
            input("Press any key to continue:-")




def createusr():
    while(True):
        print("""Select user type:
              1. Admin
              2. Monitor
              3. Exit
              """)
        choice = int(input("Enter Your choice:-"))
        if choice == 1:
            blogic.createuser()
        elif choice==2:
            blogic.createuser()
            pass
        elif choice == 3:
            break
        else:
            print("Invalid Choice:-")
            return Pencorehome.main()







