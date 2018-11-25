import calendar
from datetime import datetime

now=datetime.now()
print(calendar.calendar(now.year))

#waiter menu
print('to choose your days you want to work press 1')
print('to see your work schedule press 2')
print('to see your personal information press 3')#in this fuction need to another button to update the personal information
print('to aaaa')


global a
a=list()
def Insert_days_to_work():
    global a
    print('Welcome to page of choosing days for working')
    a=list(input("press days that you want to work: "))

Insert_days_to_work()
print(a)