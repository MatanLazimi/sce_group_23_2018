import calendar
from datetime import datetime
def run():
    ###################Start_Login#######################
    print("ok")
    global a
    global event,feedback_waiter
    a=list()
    feedback_waiter={}
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
            FirstName=(input('Enter your first name: '))
            LastName=(input('Enter your last name: '))
            PhoneNumber=(input('Enter your phone number: '))
            EmailAddress=(input('Enter your email address: '))
            ID=(input('Enter your ID: '))
            if type(FirstName) != str:
                raise ValueError


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

    """PersonalInformation() #check the fuction
    print('')
    PersonalInformation()"""
    #(1.4 and 1.1)
    def Insert_days_to_work():
        global a
        if(a==list()):
            print('Welcome to page of choosing days for working')
            print("Press days that you want to work: ")
            a=list(input("Every day in week is a number 1-7, space between values: "))
            i=1

            while(i<len(a)):
                a.pop(i)
                i=i+1
        else:
            print("There is alredy chosen days,"
                        ,"please contact your administrator to change days.")
    def feedback():
        global feedback_waiter,event
        print("Your events that you are participed is:",event)
        date1=input("Please insert date for doing relevant feedback: ")
        if (date1 in event):
            if(date1 in feedback_waiter):
                print("There is exist feedback for this event")
            else:
                feedback_waiter[date1]=input("Insert your feedback here: ")
        else:
            print("Wrong date input, return to main page")
    """
    feedback()
    feedback()
    print(feedback_waiter) 
    (1.6)"""
    def Dismis_Work_Day():
        global FirstName
        global LastName
        global ID
        dismis_day = int(input('Input the day you want to cancel the work for the next week:(chose betwin 1-7): '))
        dict_dismis_day = {'FirstName':FirstName,'LastName':LastName,'ID':ID,'dismis_day':dismis_day}
    #(1.7)
    def swip_with_waiter():
        global FirstName
        global LastName
        global ID
        FirstName_SiwpWaiter= input('Enter the first name of the wiater how replace you: ')
        LastName_SiwpWaiter= input('Enter the last name of the wiater how replace you: ')
        ID_SiwpWaiter= int(input('Enter the name of the wiater how replace you: '))
        swip_with = {'FirstName':FirstName, 'LastName':LastName, 'ID':ID, 'FirstName_SiwpWaiter':FirstName_SiwpWaiter, 'LastName_SiwpWaiter':LastName_SiwpWaiter, 'ID_SiwpWaiter':ID_SiwpWaiter}
        # צריך לשים את ה swip_with במאגר מידע.
    #(1.10)
    def General_Recuest():
        global FirstName
        global LastName
        global ID
        Recuest = input('insert your request: ')
        General_Recuest = {'FirstName':FirstName, 'LastName':LastName, 'ID':ID, 'Recuest':Recuest}
        # צריך לייצא את המילון למאגר מידע
    #waiter menu
    def Print_my_events():
        global event
        print("Your events that you are participed is:", event)
    choice=0
    while(choice!=8):
        print('To choose your days you want to work press (1)')#
        print('To see your pressed days that you want to work (2)')
        print('To see your personal information or update press (3)')#in this fuction need to another button to update the personal information
        print('To send feedback on event press (4)')
        print('To send application for change the work schedule press (5)')
        print('To see the report shifts press (6)')
        print('To exit press (8)')
        #print('to send general application to manager or responsible shift 7')

        choice=int(input("Insert your choice here: "))
        if(choice==1):
            Insert_days_to_work()
            x = input("Press any key to return the menu: ")
        if(choice==2):
            for i in a:
                print(calendar.day_name[(int(i)+5)%7])
            x=input("Press any key to return the menu: ")
        if(choice==3):
            PersonalInformation()
            x = input("Press any key to return the menu: ")
        if(choice==4):
            feedback()
            print("Sucess to put feedback",feedback_waiter)
            x = input("Press any key to return the menu: ")
        if(choice==5):
            RequestChangeShift = ChangeWorkSchedule()
            print(RequestChangeShift['Appl'])
            x = input("Press any key to return the menu: ")
        #צריך להוסיף מאגר מידע עבור הבקשות של ביטול משמרת.
        if(choice==6):
            Print_my_events()
            x = input("Press any key to return the menu: ")

        print("Menu")
