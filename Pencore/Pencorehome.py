import blogic
import sys



def main():
    while True:
        r = input("Do You want to login(y/n)")
        if r in ['Y', 'y']:
            blogic.login()
        else:
            sys.exit()


if __name__=="__main__":
    print("\nWelcome to Prospect Encore Analysis")
    main()


