import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
cursor = connection.cursor()
sql = "INSERT INTO bank VALUES(110,7472,'2002-04-13','corrent',18000)"
cursor.execute(sql)
connection.commit()
connection.close()
print("successfully inserted into employee")
