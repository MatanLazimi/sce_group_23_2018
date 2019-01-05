import calendar
from datetime import datetime
import dbworker, auth, waiter, shiftmanager
from prettytable import PrettyTable
def menu():
    ###################Start_Manager#######################
    print("ok")
    global a
    global event,feedback_waiter,waiters
    waiters=[]
    a=list()
    feedback_waiter={}
    event={"22/12/2018":"Festival Can"}
    now=datetime.now()
    print(calendar.calendar(now.year))
    ###################functions##############
    global FirstName
    global LastName
    global ID
    global EmailAddress
    global PhoneNumber
    #personal information
    FirstName=None
    LastName=None
    ID=None
    EmailAddress=None
    PhoneNumber=None

    def PersonalInformation():
        global FirstName
        global LastName
        global ID
        global EmailAddress
        global PhoneNumber
        if FirstName == None:#insert personal information for the first time
            FirstName=str(input('Enter your first name: '))
            LastName=str(input('Enter your last name: '))
            ID=int(input('Enter your ID: '))
            PhoneNumber=str(input('Enter your phone number: '))
            EmailAddress=str(input('Enter your email address: '))
            dict_IP = {'FirstName': FirstName, 'LastName': LastName, 'ID': ID, 'PhoneNumber': PhoneNumber,
                           'EmailAddress': EmailAddress}
            # צריך לשים את הפרטים האיישים במסד נתונים

        else:#see all your personal information
            print('Your first name is: ',FirstName)
            print('Your last name is: ',LastName)
            print('Your ID is: ',ID)
            print('Your phone number is: ',PhoneNumber)
            print('Your email address is: ',EmailAddress)
            print('')
            UpdatePI=int(input('if you want to change your personal information press 1 else press 0: '))
            if UpdatePI==1:
                dict_IP = ChangePI()
                # צריך לעדכן את מסד הנתונים של פרטיים האישיים של העובדים
        print('')
        print('The personal information you registered is: ')
        print('Your first name is: ', FirstName)
        print('Your last name is: ', LastName)
        print('Your ID is: ', ID)
        print('Your phone number is: ', PhoneNumber)
        print('Your email address is: ', EmailAddress)

    def ChangePI():#update the personal information
        global FirstName
        global LastName
        global EmailAddress
        global PhoneNumber
        UpdatePI = int(input('do you want to change the first name:(yes-1,no-0) '))
        if UpdatePI == 1:
            FirstName=str(input('Update your first name: '))
        UpdatePI = int(input('do you want to change the last name:(yes-1,no-0) '))
        if UpdatePI == 1:
            LastName = str(input('Update your last name: '))
        UpdatePI = int(input('do you want to change the phone number:(yes-1,no-0) '))
        if UpdatePI == 1:
            PhoneNumber = str(input('Update your phone number: '))
        UpdatePI = int(input('do you want to change the email address:(yes-1,no-0) '))
        if UpdatePI == 1:
            EmailAddress = str(input('Update your email address: '))
        return {'FirstName':FirstName, 'LastName':LastName, 'ID':ID, 'PhoneNumber':PhoneNumber, 'EmailAddress':EmailAddress}

    #(3.1)
    def insert_event():
        date = str(input('Enter the date off the event:(YYYY/MM/DD): '))
        place = str(input('were you do the event: '))
        Descrip = input('Describ the event: ')
        number_of_waitres = int(input('Enter the numbers off waiters to this event: '))
        dbworker.InsertEvent(date, place,Descrip,number_of_waitres)
        #צריך להכניס את האירוע למסד נתונים של האירועים

    def show_events():
        print("The details of your waiters in your team is: ")
        waiters = dbworker.GetEvents(datetime.now())
        t = PrettyTable(['EventDate', 'Place', 'Description', 'WaitersAmount'])
        if(len(waiters)!=0):
            for i in waiters:
                t.add_row(i)
            print(t)
        else:
            print("There is no waiters in your team")
    #(3.7)
    def show_details_of_waiters():
        print("The details of your waiters in your team is: ")
        waiters = dbworker.GetWorkersByManagerId(auth.user["id"])
        t = PrettyTable(['Id', 'First Name', 'Last Name', 'Phone'])
        if(len(waiters)!=0):
            for i in waiters:
                t.add_row(i)
            print(t)
        else:
            print("There is no waiters in your team")
    #waiter menu
    choice=0
    print('To see your personal information or update press (1)')#in this fuction need to another button to update the personal information
    print('To insert new event press (2)')
    print('Show details of waiters in the relevant team (3)')
    print('Show details of waiters in the relevant team (4)')
    print('To exit press (8)')

    choice=int(input("Insert your choice here: "))

    if(choice==1):
        waiter.ShowPersonalDetails()
        x = input("Press any key to return the menu: ")
    if(choice==2):
        insert_event()
        x = input("Press any key to return the menu: ")
    if(choice==3):
        show_details_of_waiters()
        x = input("Press any key to return the menu: ")
    if(choice==4):
        show_events()
        x = input("Press any key to return the menu: ")