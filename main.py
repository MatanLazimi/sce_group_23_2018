
import  auth, dbworker, waiter,shiftmanager, maneger



def main():

    print("\n\n\nWelcome To Shift Organizer\nEnjoy!")
    auth.login()
    while auth.isLogedIn():
        typeid = auth.user["workertype"]
        print("\n")
        print("Hello " + str(auth.user["firstname"]) + " " + str(auth.user["lastname"]) + "!")
        print("\n")
        if (typeid == 1):
            waiter.menu()
        elif (typeid == 2):
            shiftmanager.menu()
        elif (typeid == 3):
            maneger.menu()
        else:
            print("error in worker type!!!")



  
if __name__== "__main__":
  main()