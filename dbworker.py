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
