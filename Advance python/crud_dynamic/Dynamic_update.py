import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
    cursor = connection.cursor()
    sql = "update bank set account_type = 'saving' where id =112"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
    cursor = connection.cursor()
    sql = "update bank set balance = %s where id = %s"
    data = (530000, 112)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated2 successfully')


def testUpdate3(balance, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
    cursor = connection.cursor()
    sql = "update bank set balance = %s where id = %s"
    data = (balance, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated3 successfully')


def testInsert4(data):
    id = data['id']
    account_no = data['account_no']
    dob = data['dob']
    account_type = data['account_type']
    balance = data['balance']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
    cursor = connection.cursor()
    sql = "update bank set account_no= %s, dob= %s ,account_type = %s, balance = %s where id = %s"
    data = (account_no,dob, account_type, balance, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')


#testUpdate1()
#testUpdate2()
#testUpdate3(2498220, 113)
#
#
params = {}
params['id'] = 109
params['account_no'] = '9302699'
params['dob'] = '2005-02-24'
params['account_type'] = 'saving'
params['balance'] = 546782400

testInsert4(params)