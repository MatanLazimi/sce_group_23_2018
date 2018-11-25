global a
def Insert_days_to_work():
    if(a==list()):
        global a
        print('Welcome to page of choosing days for working')
        print("Press days that you want to work: ")
        a=list(input("Every day in week is a number 1-7, space between values: "))
        i=1
        while(i<len(a)):
            a.pop(i)
            i=i+1
    else:
        print("There is alredy chosen days,"
                    ,"please contact your administrator to change days.")
"""
Insert_days_to_work()
print(a)
Insert_days_to_work()
"""