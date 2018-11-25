import Work

flag = False
username=input("Enter your User Name: \n")
Password = input("Enter Password: \n")

def ReadDict():
    # Dict that will contain keys and values
    dictionary = {}
    with open("try.txt", "rt") as file:
        for line in file:
            s = line.strip().split(", ")
            dictionary[s[0]] = int(s[1])

    if username in dictionary:
        if dictionary[username]==Password:
            print("Login Seccess")


    return dictionary







