import calendar
from datetime import datetime


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
    global event,feedback_ahmash
    a=list()
    feedback_ahmash={}
    event={"22/12/2018":"Festival Can"}
    now=datetime.now()
    print(calendar.calendar(now.year))
    ###################functions##############
    def ChangeWorkSchedule():
        print('Enter the next details to send the application to change the shift:')
        firstName = str(input('Enter your first name: '))
        lastName = str(input('Enter your last name: '))
        id = int(input('Enter your ID: '))
        Appli = str(input('Enter your application and all the details on the shift: '))
        ChangeWorkApplication = {'FirstName': firstName, 'LastName': lastName, 'ID': id, 'Appl': Appli}
        return ChangeWorkApplication

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
            else:
                dict_IP = {'FirstName': FirstName, 'LastName': LastName, 'ID': ID, 'PhoneNumber': PhoneNumber,
                           'EmailAddress': EmailAddress}
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

    def feedback():
        global feedback_ahmash,event
        print("Your events that you are participed is:",event)
        date1=input("Please insert date for doing relevant feedback: ")
        if (date1 in event):
            if(date1 in feedback_ahmash):
                print("There is exist feedback for this event")
            else:
                feedback_ahmash[date1]=input("Insert your feedback here: ")
        else:
            print("Wrong date input, return to main page")





    #(2.7)
    global request, request_manager
    request = {}
    request_manager= {}
    def request_manpower():
        print("For getting more waiters to the relvant shift, press the relevant date dd/mm/yyyy")
        date_req=input("")
        amount=input("Insert the amount of waiters that you need: ")
        request[date_req]=int(amount)

    """
    request_manpower()
    print(request)
    """
    #matan
    #(2.11)
    def request_from_manager():
        print("For request from manager first insert your details:")
        FirstName = str(input('Enter your first name: '))
        LastName = str(input('Enter your last name: '))
        ID = int(input('Enter your ID: '))
        print("Insert a request for your manager: (when you finish press enter)")
        request=input()
        request_manager = {'FirstName': FirstName, 'LastName': LastName, 'ID': ID, request}


