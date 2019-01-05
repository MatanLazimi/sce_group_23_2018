import waiter,ahmash,maneger,dbworker

print("Welcome To ShiftOrganizer")
print("enjoy!")
print()
print()
print('Login')

global workerID
global workerFirstName
global workerLastName
global workerType

def Login(username,password):
    userList = dbworker.GetUserByCredentials(username, password)
    if len(userList) == 1:
        workerID = userList[0][3]
        workerList = dbworker.GetWorkerById(workerID)
        workerFirstName = workerList[0][1]
        workerLastName = workerList[0][2]
        workerType = workerList[0][4]
        return workerType
    else:
        return -1



###################Start_Login#######################
Username = input("Enter your User Name: \n")
Password = input("Enter Password: \n")
temp_login = Login(Username, Password)
if(temp_login != -1):
    if(temp_login == 1):
        print("Run profile of waiter {}".format(temp_login))
        waiter.run()
    elif(temp_login == 2):
        print("Run profile of Responsible shift {}".format(temp_login))
        ahmash.run()
    elif(temp_login == 3):
        print("Run profile of Manager {}".format(temp_login))
        maneger.run()
else:
    print("ShutDown the program Username and Password incorrect")
