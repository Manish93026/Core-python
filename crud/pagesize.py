import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advpython')
cursor = connection.cursor()
sql = "select * from employee"
cursor.execute(sql)

pageNo =3
pageSize = 2
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