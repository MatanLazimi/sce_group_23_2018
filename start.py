import waiter,ahmash,maneger,dbworker

print("Welcome To ShiftOrganizer")
print("enjoy!")
print()
print()
print('Login')
def ReadDict(username,password):
    # Dict that will contain keys and values
    flag=False
    dictionary = {}
    with open("try.txt", "rt") as file:
        for line in file:
            s = line.strip().split(", ")
            dictionary[s[0]] = int(s[1])
    if username in dictionary:
        if int(dictionary[username]) == int(password):
            print("Login Seccess")
            type_user=3
            id=12345678
            flag={type_user: id}
            return flag
            ##########################################################################
        else:
            print("Wrong Password, try again")
            return False
    else:
        print("Wrong Username, Plaese Check your Username Or Password")
        return False
    return flag



###################Start_Login#######################
Username = input("Enter your User Name: \n")
Password = input("Enter Password: \n")
temp_login= ReadDict(Username, Password)
if(temp_login != False):
    if(1 in temp_login):
        print("Run profile of waiter {}".format(temp_login[1]))
        waiter.run()
    elif(2 in temp_login):
        print("Run profile of Responsible shift {}".format(temp_login[2]))
        ahmash.run()
    elif(3 in temp_login):
        print("Run profile of Manager {}".format(temp_login[3]))
        maneger.run()
else:
    print("ShutDown the program Username and Password incorrect")
