import calendar
from datetime import datetime, date


###################Start_Login#######################
flag = False
Username = input("Enter your User Name: \n")
Password = input("Enter Password: \n")

def ReadDict(username,password):
    # Dict that will contain keys and values
    dictionary = {}
    with open("try.txt", "rt") as file:
        for line in file:
            s = line.strip().split(", ")
            dictionary[s[0]] = int(s[1])


    if username in dictionary:
        if int(dictionary[username]) == int(password):
            print("Login Seccess")
            flag=True
        else:
            print("Wrong Password, try again")
            return False
    else:
        print("Wrong Username, Plaese Check your Username Or Password")
        return False

    return flag

###################End_Login#######################
if (ReadDict(Username, Password)==True):
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

    #RequestChangeShift = ChangeWorkSchedule()
    '''print(RequestChangeShift['FirstName'])
    print(RequestChangeShift['LastName'])
    print(RequestChangeShift['ID'])
    print(RequestChangeShift['Appl'])'''
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
        print('Enter the date off the event:')
        y = int(input('Enter full year'))
        m = int(input('Enter full month'))
        d = int(input('Enter full day'))
        event = date(y,m,d)
        name_commpany = input('Enter the name off the commpany that have the event:')
        dict_event = {'name_commpany':name_commpany, 'event':date}
        #צריך להכניס את האירוע למסד נתונים של האירועים

    #(3.7)
    def show_details_of_waiters():
        print("The details of your waiters in your team is: ")
        if(len(waiters)!=0):
            for i in waiters:
                print(i)
        else:
            print("There is no waiters in your team")
    #waiter menu
    choice=0
    while(choice!=8):
        print('To see your personal information or update press (1)')#in this fuction need to another button to update the personal information
        print('To insert new event press (2)')
        print('Show details of waiters in the relevant team (3)')
        print('To exit press (8)')

        choice=int(input("Insert your choice here: "))

        if(choice==1):
            PersonalInformation()
            x = input("Press any key to return the menu: ")
        if(choice==2):
            insert_event()
            x = input("Press any key to return the menu: ")
        if(choice==3):
            show_details_of_waiters()
            x = input("Press any key to return the menu: ")
