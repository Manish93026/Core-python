import pymysql
connection = pymysql.connect(host='localhost',user='root',port=3306,password='root',db='advpython')
cursor = connection.cursor()
sql = "select * from bank"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0],data[1],data[2],data[3],data[4])
connection.commit()
connection.close()
print("Data is Successfully read")