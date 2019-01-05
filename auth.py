import dbworker, main


user = {
    "userid": -1,
    "id": "000000000",
    "workertype": -1,
    "workermanagerid": "000000000",
    "firstname": "none",
    "lastname": "none",
    "phone": "00000000000",
    }

logedin = False

def authenticate(username, password):
    userdata = dbworker.GetUserByCredentials(username, password)

    if len(userdata) == 1:
        user["userid"] = userdata[0][0]
        user["id"] = userdata[0][3]
        
        workerdata = dbworker.GetWorkerById(user["id"])
        user["firstname"] = workerdata[0][1]
        user["lastname"] = workerdata[0][2]
        user["phone"] = workerdata[0][3]
        user["workertype"] = workerdata[0][4]
        user["workermanagerid"] = workerdata[0][5]

        return True
    else:
        return False


def login():
    loginattempts = 1
    while loginattempts <= 3:
        username = input("username: ")
        password = input("password: ")

        if (authenticate(username, password)):
            print("\n********* login succesful! *********\n")
            return True
            
        
        loginattempts = loginattempts + 1

    print("\n####### login Failed! ########\n")
    return False

def isLogedIn():
    if (user["userid"] != -1):
        return True
    else:
        return False

def logout():
    user["userid"] = -1
    print("\n\n ****** Good Bye! ********\n\n")