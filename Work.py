import calendar
from datetime import datetime

global a
global event,feedback_waiter
feedback_waiter={}
event={"22/12/2018":"Festival Can"}


now=datetime.now()
print(calendar.calendar(now.year))

#waiter menu
print('to choose your days you want to work press 1')#1.2
print('to see your work schedule press 2')
print('to see your personal information press 3')#in this fuction need to another button to update the personal information
print('to aaaa')
