import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advpython')
cursor = connection.cursor()

sql1 = "select* from employee where id=4"
cursor.execute(sql1)
result = cursor.fetchall()
for data in result:
    print(data[0],data[1],data[2],data[3],data[4])

sql2 = "DELETE FROM employee WHERE `id` = 4"

cursor.execute(sql2)
connection.commit()
connection.close()
print("Data Deleted Successfully")