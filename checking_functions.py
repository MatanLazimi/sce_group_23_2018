def ReadDict(username,password):
    # Dict that will contain keys and values
    flag=False
    dictionary = {}
    with open("try.txt", "rt") as file:
        for line in file:
            s = line.strip().split(", ")
            dictionary[s[0]] = int(s[1])
    if username in dictionary:
        if int(dictionary[username]) == int(password):
            print("Login Seccess")
            type_user=3
            id=12345678
            flag={type_user: id}
            return flag
        else:
            print("Wrong Password")
            raise ValueError
            return False
    else:
        #print("Wrong Username, Plaese Check your Username Or Password")
        raise ValueError
        return False
    return flag

def ChangeWorkSchedule():
    #print('Enter the next details to send the application to change the shift:')
    firstName = "Matan"
    lastName = "Lazimi"
    id = 123456789
    Appli = "I want to replace"
    ChangeWorkApplication = {'FirstName': firstName, 'LastName': lastName,
                             'ID': id, 'Appl': Appli}
    return ChangeWorkApplication

def PersonalInformation1():
    global FirstName
    global LastName
    FirstName=None
    global ID
    global EmailAddress
    global PhoneNumber
    if FirstName == None:#insert personal information for the first time
        FirstName="Matan"
        LastName="Lazimi"
        PhoneNumber="052-3256626"
        EmailAddress="Matan@gmail.com"
        ID=123456789
        if type(FirstName) != str:
            raise ValueError
        dict_IP = {'FirstName': FirstName, 'LastName': LastName, 'ID': ID, 'PhoneNumber': PhoneNumber,
                   'EmailAddress': EmailAddress}
        return dict_IP
def PersonalInformation2():
    global FirstName
    global LastName
    FirstName=None
    global ID
    global EmailAddress
    global PhoneNumber
    if FirstName == None:#insert personal information for the first time
        FirstName=1234 #Error
        LastName="Lazimi"
        PhoneNumber="052-3256626"
        EmailAddress="Matan@gmail.com"
        ID=123456789
        if type(FirstName) != str:
            raise ValueError("error")
        dict_IP = {'FirstName': FirstName, 'LastName': LastName, 'ID': ID, 'PhoneNumber': PhoneNumber,
                   'EmailAddress': EmailAddress}
        return dict_IP
a=[]
def Insert_days_to_work():
    global a
    if(a==list()):
        print('Welcome to page of choosing days for working')
        print("Press days that you want to work: ")
        a=[1,3,6,7]
        i=1

        while(i<len(a)):
            a.pop(i)
            i=i+1
        return a
    else:
        print("There is alredy chosen days,"
                    ,"please contact your administrator to change days.")
        raise ValueError

feedback_waiter={}
event={"22/12/2018":"Festival Can"}
def feedback1():
    global feedback_waiter,event
    print("Your events that you are participed is:",event)
    print("Please insert date for doing relevant feedback: ")
    print("22/12/2018")
    date1 ="22/12/2018"
    if (date1 in event):
        if(date1 in feedback_waiter):
            print("There is exist feedback for this event")
        else:
            feedback_waiter[date1]='Good Job'
            return feedback_waiter
    else:
        print("Wrong date input, return to main page")
        raise ValueError
def feedback2():
    global feedback_waiter,event
    print("Your events that you are participed is:",event)
    print("Please insert date for doing relevant feedback: ")
    print("28/12/2018")
    date1 ="28/12/2018"
    if (date1 in event):
        if(date1 in feedback_waiter):
            print("There is exist feedback for this event")
        else:
            feedback_waiter[date1]="Good Job"
            return feedback_waiter
    else:
        print("Wrong date input, return to main page")
        raise ValueError
def Dismis_Work_Day(day):
    FirstName="Moshe"
    LastName="Perez"
    ID=123456789
    print('Input the day you want to cancel the work for the next week:(chose betwin 1-7): ')
    print(day)
    dismis_day = day
    if(type(day)==int and day>=1 and day<=7):
        dict_dismis_day = {'FirstName':FirstName,'LastName':LastName,'ID':ID,'dismis_day':dismis_day}
        return day
    else:
        raise ValueError