import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
cursor = connection.cursor()
sql = "INSERT INTO employee VALUES (16, 'shalini', 'Rays','Indore', 70000)"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Inserted Successfully")