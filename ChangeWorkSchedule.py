

def ChangeWorkSchedule():
    print('Enter the next details to send the application to change the shift:')
    firstName=str(input('Enter your first name: '))
    lastName=str(input('Enter your last name: '))
    id=int(input('Enter your ID: '))
    Appli=str(input('Enter your application and all the details on the shift: '))
    ChangeWorkApplication = {'FirstName': firstName, 'LastName': lastName, 'ID': id, 'Appl': Appli}
    return ChangeWorkApplication

RequestChangeShift =ChangeWorkSchedule()
'''print(RequestChangeShift['FirstName'])
print(RequestChangeShift['LastName'])
print(RequestChangeShift['ID'])
print(RequestChangeShift['Appl'])'''