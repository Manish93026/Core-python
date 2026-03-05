import pymysql

connection = pymysql.connect(host='localhost',password='root',port= 3306,user='root',db='advpython')
cursor = connection.cursor()
sql = "insert into employee values(18,'neha','tcs','nagpur',52000)"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Inserted Successfull")

