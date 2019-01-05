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
            type_user=1
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
