import calendar
from datetime import datetime

global a
global event,feedback_waiter
feedback_waiter={}
event={"22/12/2018":"Festival Can"}


def Insert_days_to_work():
    if(a==list()):
        global a
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
"""
Insert_days_to_work()
print(a)
Insert_days_to_work()
"""

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

now=datetime.now()
print(calendar.calendar(now.year))

#waiter menu
print('to choose your days you want to work press 1')#1.2
print('to see your work schedule press 2')
print('to see your personal information press 3')#in this fuction need to another button to update the personal information
print('to aaaa')

