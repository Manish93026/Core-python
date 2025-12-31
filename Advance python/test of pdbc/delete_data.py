import pymysql

connection = pymysql.connect(host='localhost',user='root',port=3306,password='root',db='advpython')
cursor = connection.cursor()
sql = "delete from bank where id = 105"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Deleted Successfully")