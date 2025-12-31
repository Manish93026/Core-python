import pymysql
def deleteAccount1():
    connection = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='advpython')
    cursor = connection.cursor()
    sql = "delete from bank where id = 108"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data deleted successfully')

def deleteAccount2():

    connection = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='advpython')
    cursor = connection.cursor()
    sql = "delete from bank where id = %s"
    data =(102,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print('data deleted successfully')

def deleteAccount3(id):

    connection = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='advpython')
    cursor = connection.cursor()
    sql = "delete from bank where id = %s"
    data =(id,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print('data deleted successfully')

#deleteAccount1()
#deleteAccount2()
deleteAccount3(106)