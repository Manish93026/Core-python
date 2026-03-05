import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advpython')
cursor = connection.cursor()
# slq1 = "select * from employee"
# cursor.execute(slq1)
# result = cursor.fetchall()
sql2 = "select * from employee where id = 20"
cursor.execute(sql2)
result = cursor.fetchall()
for data in result:
    print(data[0],data[1],data[2],data[3],data[4])

connection.commit()
connection.close()
print("Data read Successfully")