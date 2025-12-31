import pymysql


def dynamic_read1():
    connection = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='advpython')
    cursor = connection.cursor()
    sql = "select * from bank"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row[0], row[1], row[2], row[3], row[4])
    connection.commit()
    connection.close()
    print("successfully read from bank")


def dynamic_read2():
    connection = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='advpython')
    cursor = connection.cursor()
    sql = "select * from bank"
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ('id', 'account_no', 'dob,account_type', 'balance')
    for row in result:
        print(row[0], row[1], row[2], row[3], row[4])

    connection.commit()
    connection.close()
    print("successfully read from bank")


def dynamic_read3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
    cursor = connection.cursor()

    # sql = "select * from bank"
    sql = "select * from bank where id = 101"
    # sql = "select * from user where LastName = 'Kumar'"
    # sql = "select * from user where name like 'a%'"
    # sql = "select * from user where Salary = 50000"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()
    print("successfully read from bank")


def dynamic_read4(id, account_no, dob, account_type, balance):
    connection = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='advpython')
    cursor = connection.cursor()
    sql = "select * from bank"
    if id != 0:
        sql += "where id = " + str(id)
    if account_no != 0:
        sql += "where account_no = " + str(account_no)
    if dob != 0:
        sql += "where dob = " + str(dob)
    if account_type != '':
        sql += "where account_type like = '" + account_type + "%d'"
    if balance != 0:
        sql += "where balance = " + str(balance)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ('id', 'account_no', 'dob', 'account_type', 'balance')
    for row in result:
        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
    connection.commit()
    connection.close()
    print("successfully read from bank")


def dynamic_read5(param={}):
    id = param.get('id', 0)
    account_no = param.get('account_no', 0)
    dob = param.get('dob', 0)
    account_type = param.get('account_type', "")
    balance = param.get('balance', 0)

    connection = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='advpython')
    cursor = connection.cursor()
    sql = "select * from bank"
    if id != 0:
        sql += "where id  " + str(id)
    if account_no != 0:
        sql += "where account_no  " + str(account_no)
    if dob != 0:
        sql += "where dob  " + str(dob)
    if account_type != '':
        sql += "where account_type like ' " + account_type + "%d'"
    if balance != 0:
        sql += "where balance  " + str(balance)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])

    connection.commit()
    connection.close()
    print("successfully read from bank")


def dynamic_read6(param={}):
    id = param.get('id', 0)
    account_no = param.get('account_no', 0)
    dob = param.get('dob', 0)
    account_type = param.get('account_type', "")
    balance = param.get('balance', 0)
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='advpython')
    cursor = connection.cursor()
    sql = "select * from bank where  1=1"

    if id != 0:
        sql += " AND id = " + str(id)
    if account_no != 0:
        sql += " AND account_no = " + str(account_no)
    if dob != 0:
        sql += " AND dob  = " + str(dob)
    if account_type != '':
        sql += " AND account_type like ' " + account_type + "%d'"
    if balance != 0:
        sql += " AND  balance  =" + str(balance)

    if pageSize > 0:
        offset = (pageNo - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])

    connection.commit()
    connection.close()
    print("successfully read from bank")


# dynamic_read1()
# dynamic_read2()
# dynamic_read3()
# dynamic_read4(0,'',0)
# dynamic_read5()
param = {'pageNo': 5,
        'pageSize': 2}
dynamic_read6(param)
