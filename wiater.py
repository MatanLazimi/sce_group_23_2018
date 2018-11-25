import calendar
from datetime import datetime

now=datetime.now()
print(calendar.calendar(now.year))

#waiter menu
print('to choose your days you want to work press 1')
print('to see your work schedule press 2')
print('to see your personal information press 3')#in this fuction need to another button to update the personal information
print('to send feedback on event press 4')
print('to see the report shifts of the last month press 5')
print('to send application for change the work schedule press 6')
print('to send general application to manager or responsible shift 7')

