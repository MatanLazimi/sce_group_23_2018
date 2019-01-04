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
    print("For request from manager first insert your details-")
    FirstName = str(input('Enter your first name: '))
    LastName = str(input('Enter your last name: '))
    ID = int(input('Enter your ID: '))
    print("Insert a request for your manager: (when you finish press enter)")
    request=input()
    request_manager['FirstName']=FirstName
    request_manager['LastName']=LastName
    request_manager['ID']= ID
    request_manager['request']=request
"""
request_from_manager()
print(request_manager)
"""