

flag = False
Username = input("Enter your User Name: \n")
Password = input("Enter Password: \n")

def ReadDict(username,password):
    # Dict that will contain keys and values
    dictionary = {}
    with open("try.txt", "rt") as file:
        for line in file:
            s = line.strip().split(", ")
            dictionary[s[0]] = int(s[1])

    if username in dictionary:
        if dictionary[username[1]] == password:
            print("Login Seccess")
            flag=True
        else:
            print("Wrong Password, try again")
    else:
        print("Wrong Username, Plaese Check your Username Or Password")


    return flag


ReadDict(Username, Password)


import Work