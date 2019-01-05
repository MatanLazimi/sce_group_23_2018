import mysql.connector

db = mysql.connector.connect(
	host="e-wizards.co.il",
	user="python-client",
	passwd="Aa12345",
    db="mydatabase")

#Do an insert command with parammeters.
# Return values: -1 = failiure, anything else = rows inserted 
def DoSqlInsert(sqlcommand, params):
    cursor = db.cursor()
    try:
        cursor.execute(sqlcommand, params)
        db.commit()
    except:
        return -1
    finally:
        return cursor.rowcount



def GetUserByCredentials(sid, password):
    cursor = db.cursor()
    sqlcommand = "SELECT * FROM Users WHERE SID = %s AND UserPassword = %s;"
    params = (sid, password)
    cursor.execute(sqlcommand, params)
    
    return cursor.fetchall()


def GetUserById(userid):
    cursor = db.cursor()
    sqlcommand = "SELECT * FROM Users WHERE UserID = %s;"
    params = (userid)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()



def InsertUser(sid, firstname, lastname, phone, usertype, usermanager, userpassword):
    sqlcommand = """INSERT INTO Users
    (SID, FirstName, LastName, Phone, UserType, UserManager, UserPassword)
     VALUES(%s ,%s, %s, %s, %s, %s, %s );"""
    params = (sid, firstname, lastname, phone, usertype, usermanager, userpassword)
    
    return DoSqlInsert(sqlcommand, params)



def InsertEvent(starttime, endtime, place, Description, numofwaiters):
    sqlcommand = """INSERT INTO Events(StartTime, EndTime, Place, Description, WaitersAmount)
     VALUES(%s ,%s, %s, %s, %s);"""
    params = (starttime, endtime, place, Description, numofwaiters)
    
    return DoSqlInsert(sqlcommand, params)



def InsertMemo(eventid, userid, memo):
    sqlcommand = "INSERT INTO Memos(EventID, UserID, MemoText) VALUES(%s ,%s, %s);"
    params = (eventid, userid, memo)
    
    return DoSqlInsert(sqlcommand, params)



def InsertShiftAssignment(eventid, userid):
    sqlcommand = "INSERT INTO ShiftAssignments(EventID, UserID) VALUES(%s ,%s);"
    params = (eventid, userid)
    
    return DoSqlInsert(sqlcommand, params)



def InsertShiftBlock(starttime, endtime, description):
    sqlcommand = "INSERT INTO ShiftBlocking(StartTime, EndTime, Description) VALUES(%s ,%s, %s);"
    params = (starttime, endtime, description)
    
    return DoSqlInsert(sqlcommand, params)



def GetBlockes(starttime, endtime):
    cursor = db.cursor()
    sqlcommand = """SELECT UserID FROM ShiftBlocking WHERE
     (StartTime != %s AND EndTime != %s) OR
     (StartTime >= %s AND StartTime <= %s);"""
    params = (starttime, starttime, starttime, endtime)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()
    


def GetEvent(eventid):
    cursor = db.cursor()
    sqlcommand = """SELECT * FROM Events WHERE EvenrID = %s;"""
    params = (eventid)
    cursor.execute(sqlcommand, params)

    return cursor.fetchone()








def test(): 
    #print(InsertUser("123456789", "firstname", "lastname", None, 1, None, "1234567"))

    GetBlockes("2019/12/26 12:00:00", "2019/12/29 12:00:00")
""" 
    if typeId == 1:
        print("he's an admin!")
    elif typeId == 2:
        print("he's a manager!")
    elif typeId == 3:
        print("he's a shift manager!")
    elif typeId == 4:
        print("he's a waiter!!")
    else:
        print("login faild!") """
