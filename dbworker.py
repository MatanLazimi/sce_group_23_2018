import mysql.connector

db = mysql.connector.connect(
    host="e-wizards.co.il",
    user="python-client",
    passwd="Aa12345",
    db="mydatabase")


# Do an insert command with parammeters.
# Return values: -1 = failiure, anything else = rows inserted
def DoSqlInsert(sqlcommand, params):
    cursor = db.cursor()
    cursor.execute(sqlcommand, params)
    db.commit()


def GetUserByCredentials(username, password):
    cursor = db.cursor()
    sqlcommand = "SELECT * FROM Users WHERE Username = %s AND Password = %s;"
    params = (username, password)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()


def GetWorkerById(id):
    cursor = db.cursor()
    sqlcommand = "SELECT * FROM Workers WHERE ID = %s;"
    params = (id,)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()


def GetWorkersByManagerId(id):
    cursor = db.cursor()
    sqlcommand = "SELECT ID, FirstName, LastName, Phone FROM Workers WHERE WorkerManager = %s;"
    params = (id,)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()


def InsertShiftBlock(params):
    sqlcommand = "INSERT INTO ShiftBlocking(BlockDate, WorkerID) VALUES(%s ,%s);"
    cursor = db.cursor()
    if (len(params) == 1):
        cursor.execute(sqlcommand, params[0])
    else:
        cursor.executemany(sqlcommand, params)
    db.commit()


def InsertEvent(date, place, Description, numofwaiters):
    sqlcommand = """INSERT INTO Events(EventDate, Place, Description, WaitersAmount)
     VALUES(%s ,%s, %s, %s);"""
    params = (date, place, Description, numofwaiters)

    return DoSqlInsert(sqlcommand, params)


def GetEvents(datefrom):
    cursor = db.cursor()
    sqlcommand = "SELECT * FROM Events WHERE EventDate >= %s;"
    params = (datefrom,)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()


'''

def InsertUser(id, firstname, lastname, phone, usertype, usermanager, userpassword):
    sqlcommand = """INSERT INTO Users
    (ID, FirstName, LastName, Phone, UserType, UserManager, UserPassword)
     VALUES(%s ,%s, %s, %s, %s, %s, %s );"""
    params = (id, firstname, lastname, phone, usertype, usermanager, userpassword)

    return DoSqlInsert(sqlcommand, params)


def InsertMemo(date, userid, memo):
    sqlcommand = "INSERT INTO Memos(EventDate, UserID, MemoText) VALUES(%s ,%s, %s);"
    params = (date, userid, memo)

    return DoSqlInsert(sqlcommand, params)


def InsertShiftAssignment(date, userid):
    sqlcommand = "INSERT INTO ShiftAssignments(EventDate, UserID) VALUES(%s ,%s);"
    params = (date, userid)

    return DoSqlInsert(sqlcommand, params)


def InsertShiftBlock(date, description):
    sqlcommand = "INSERT INTO ShiftBlocking(StartTime, EndTime, Description) VALUES(%s ,%s, %s);"
    params = (date, description)

    return DoSqlInsert(sqlcommand, params)


def GetAssignment(userid):
    cursor = db.cursor()
    sqlcommand = """SELECT * FROM ShiftAssignments WHERE UserID = %s;"""
    params = (userid)
    cursor.execute(sqlcommand, params)

    return cursor.fetchall()


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



def Update_Worker(userid, firstname, lastname, phone, usertype, usermanager):
        cursor = db.cursor()
        sqlcommand = """UPDATE Users SET firstname = %s AND lastname = %s AND Phone = %s AND usertype = %s   WHERE ID = %s"""
        params = ("Valley 345", "Canyon 123")
        cursor.execute(firstname, lastname, phone, usertype, usermanager, userid)

        db.commit()



def Delete_Table(table):
    cursor = db.cursor()
    sqlcommand = "DELETE FROM %s"
    params = (table)
    cursor.execute(sqlcommand, params)
    db.commit()

'''
