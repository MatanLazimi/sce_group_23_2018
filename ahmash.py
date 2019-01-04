#(2.7)
global request
def request_manpower():
    request={}
    print("For getting more waiters to the relvant shift, press the date the needed dd/mm/yyyy")
    date_req=input("")
    amount=input("Insert the amount of waiters that you need: ")
    request[date_req]=amount

request_manpower()
print(request)
