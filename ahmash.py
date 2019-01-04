#(2.7)
global request
request = {}
def request_manpower():
    print("For getting more waiters to the relvant shift, press the relevant date dd/mm/yyyy")
    date_req=input("")
    amount=input("Insert the amount of waiters that you need: ")
    request[date_req]=int(amount)

request_manpower()
print(request)
