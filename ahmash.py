#(2.7)
global request
request = {}
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
    def request_manpower():
        print("For getting more waiters to the relvant shift, press the relevant date dd/mm/yyyy")
        date_req=input("")
        amount=input("Insert the amount of waiters that you need: ")
        request[date_req]=int(amount)

    request_manpower()
    print(request)
