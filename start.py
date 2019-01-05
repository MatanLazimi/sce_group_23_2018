import waiter,ahmash,maneger

def ReadDict(username,password):
    # Dict that will contain keys and values
    dictionary = {}
    with open("try.txt", "rt") as file:
        for line in file:
            s = line.strip().split(", ")
            dictionary[s[0]] = int(s[1])

    if username in dictionary:
        if int(dictionary[username]) == int(password):
            print("Login Seccess")
            #########################################################################
            type_user=3
            id=12345678
            flag={type_user: id}
            ##########################################################################
        else:
            print("Wrong Password, try again")
            return False
    else:
        print("Wrong Username, Plaese Check your Username Or Password")
        return False
    return flag



print("Welcome To ShiftOrganizer")
print("enjoy!")
print()
print()
print('Login')
###################Start_Login#######################
flag = False
Username = input("Enter your User Name: \n")
Password = input("Enter Password: \n")
temp_login=ReadDict(Username, Password)
if(temp_login != False):
    if(1 in temp_login):
        waiter
    elif(2 in temp_login):
        ahmash
    elif(3 in temp_login):
        maneger
else:
    print("ShutDown the program Username and Password incorrect")
