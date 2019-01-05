import calendar
from datetime import datetime
import auth, dbworker


def menu():
    print("-------- WAITER MENU ----------")
    print('(1) - Enter block dates')
    print('(2) - See shifts')
    print('(3) - See Personal information')  # in this fuction need to another button to update the personal information
    print('(4) - Enter a memo')
    print('(5) - Enter worker request')
    print('(6) - Logout')
    # print('to send general application to manager or responsible shift 7')

    choice = int(input("Option: "))
    if (choice == 1):
        EnterBlockes()
    elif (choice == 2):
        printShifts()

    elif (choice == 3):
        ShowPersonalDetails()

    elif (choice == 4):
        EnterMemo()

    elif (choice == 5):
        General_Request()

    elif (choice == 6):
        auth.logout()
        return

    x = input("Press any key to return the menu: ")


def EnterBlockes():
    num = int(input("Enter number of blockes: "))
    params = []
    for i in range(0, num):
        date = input(str(i) + " - enter block date: ")
        params.append((date, auth.user["id"]))

    dbworker.InsertShiftBlock(params)


def ShowPersonalDetails():
    print("ID: " + auth.user["id"])
    print("First Name: " + auth.user["firstname"])
    print("last Name: " + auth.user["lastname"])
    print("phone number: " + auth.user["phone"])


def EnterMemo():
    memo = input("Please insert date for doing relevant feedback: ")
    print("request recived")


def General_Request():
    Request = input('insert your request: ')
    print("request recived")


def printShifts():
    now = datetime.now()
    c = calendar.TextCalendar(calendar.SUNDAY)
    c_str = c.formatmonth(now.year, now.month)
    print(c_str)
