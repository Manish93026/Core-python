import pymysql

def testinsert1():
    connection = pymysql.connect(host='localhost',user='root',port=3306,password='root',db='advpython')
    cursor=connection.cursor()
    sql = "insert into bank values(117,328743,'2006-05-17','saving',51000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("successfully inserted into bank")

def testinsert2():
    connection=pymysql.connect(host='localhost',user='root',port=3306,password='root',db='advpython')
    cursor=connection.cursor()
    sql="insert into bank values(%s,%s,%s,%s,%s)"
    values=(112,32876,'2002-05-17','debit',520500)
    cursor.execute(sql,values)
    connection.commit()
    connection.close()
    print("successfully inserted into bank  using sql,values")


def testinsert3(id,account_no,dob,account_type,balance):
    connection=pymysql.connect(host='localhost',user='root',port=3306,password='root',db='advpython')
    cursor=connection.cursor()
    sql="insert into bank values(%s,%s,%s,%s,%s)"
    data=(id,account_no,dob,account_type,balance)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully inserted into bank  using sql,values")


def testinsert4(data={}):
    id=data['id']
    account_no=data['account_no']
    dob=data['dob']
    account_type=data['account_type']
    balance=data['balance']
    connection=pymysql.connect(host='localhost',user='root',port=3306,password='root',db='advpython')
    cursor=connection.cursor()
    sql="insert into bank values(%s,%s,%s,%s,%s)"
    data=(id,account_no,dob,account_type,balance)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully inserted into bank  using key value pair")


#testinsert1()
#testinsert2()
#testinsert3(113,35632,'2001-12-17','saving',250000)
testinsert4({'id':116,'account_no':62445,'dob':'2010-05-15','account_type':'saving','balance':53000})