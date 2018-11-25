#personal information
FirstName=None
LastName=None
ID=None
EmailAddress=None
PhoneNumber=None


def PersonalInformation():
    global FirstName
    global LastName
    global ID
    global EmailAddress
    global PhoneNumber
    if FirstName == None:#insert personal information for the first time
        FirstName=str(input('Enter your first name: '))
        LastName=str(input('Enter your last name: '))
        ID=int(input('Enter your ID: '))
        PhoneNumber=str(input('Enter your phone number: '))
        EmailAddress=str(input('Enter your email address: '))
    else:#see all your personal information
        print('Your first name is: ',FirstName)
        print('Your last name is: ',LastName)
        print('Your ID is: ',ID)
        print('Your phone number is: ',PhoneNumber)
        print('Your email address is: ',EmailAddress)
        print('')
        UpdatePI=int(input('if you want to change your personal information press 1 else press 0: '))
        if UpdatePI==1:
            ChangePI()
    print('')
    print('The personal information you registered is: ')
    print('Your first name is: ', FirstName)
    print('Your last name is: ', LastName)
    print('Your ID is: ', ID)
    print('Your phone number is: ', PhoneNumber)
    print('Your email address is: ', EmailAddress)

def ChangePI():#update the personal information
    global FirstName
    global LastName
    global EmailAddress
    global PhoneNumber
    UpdatePI = int(input('do you want to change the first name:(yes-1,no-0) '))
    if UpdatePI == 1:
        FirstName=str(input('Update your first name: '))
    UpdatePI = int(input('do you want to change the last name:(yes-1,no-0) '))
    if UpdatePI == 1:
        LastName = str(input('Update your last name: '))
    UpdatePI = int(input('do you want to change the phone number:(yes-1,no-0) '))
    if UpdatePI == 1:
        PhoneNumber = str(input('Update your phone number: '))
    UpdatePI = int(input('do you want to change the email address:(yes-1,no-0) '))
    if UpdatePI == 1:
        EmailAddress = str(input('Update your email address: '))



"""PersonalInformation() #check the fuction
print('')
PersonalInformation()"""





