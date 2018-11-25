import calendar
from datetime import datetime

global a
global event,feedback_waiter
a=list()
feedback_waiter={}
event={"22/12/2018":"Festival Can"}
now=datetime.now()
print(calendar.calendar(now.year))
###################functions##############
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
"""
#waiter menu
choice=0
while(choice!=8):
    print("Menu")
    print('To choose your days you want to work press (1)')#
    print('To see your pressed days that you want to work (2)')
    print('To see your work schedule press (3)')
    print('To see your personal information press (4)')#in this fuction need to another button to update the personal information
    print('To send feedback on event press (5)')
    print('To exit press (8)')
    """print('to see the report shifts of the last month press 5')
    print('to send application for change the work schedule press 6')
    print('to send general application to manager or responsible shift 7')"""
    choice=int(input("Insert your choice here: "))

    if(choice==1):
        Insert_days_to_work()
        x = input("Press any key to return the menu: ")
    if(choice==2):
        for i in a:
            print(calendar.day_name[(int(i)+5)%7])
        x=input("Press any key to return the menu: ")
    if(choice==5):
        feedback()
        print("Sucess to put feedback",feedback_waiter)
        x = input("Press any key to return the menu: ")
