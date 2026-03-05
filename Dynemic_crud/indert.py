import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='advpython')
cursor= connection.cursor()
def insert1():

    sql = "insert into employee values(21,'payal','vipro','indore',54100)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("inserted into employee table successfully")

def insert2():

    sql = "insert into employee values(%s,%s,%s,%s,%s)"
    values = (22,'raj','tcs','bangloru',63990)
    cursor.execute(sql,values)
    connection.commit()
    connection.close()
    print("inserted into employee table successfully")

def insert3(id,name,compnay,address,salary):

    sql = "insert into employee values(%s,%s,%s,%s,%s)"
    values = (id,name,compnay,address,salary)
    cursor.execute(sql,values)
    connection.commit()
    connection.close()
    print("inserted into employee table successfully")

# def insert4(param={}):
#     print("give the details you insert")
#     print("id ,name ,compnay,address ,salary")
#     id = param["id"]
#     name = param["name"]
#     compnay = param["compnay"]
#     address = param["address"]
#     salary = param["salary"]
#
#     sql = "insert into employee values(%s,%s,%s,%s,%s)"
#     values = (id,name,compnay,address,salary)
#     cursor.execute(sql,values)
#     connection.commit()
#     connection.close()
#     print("inserted into employee table successfully")



def insert4():
    print("--- Enter Employee Details ---")

    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    company = input("Enter Company: ")
    address = input("Enter Address: ")
    salary = float(input("Enter Salary: "))

    # Query aur execution
    sql = "insert into employee values(%s, %s, %s, %s, %s)"
    values = (id, name, company, address, salary)

    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    print(f"Employee {name} inserted successfully!")


# Program run karne ke liye
if __name__ == "__main__":
    insert4()


#insert1()
#insert2()
#insert3(23,'udai','rays','indore',54100)
# insert4({'id':24,'name':'khushi','compnay':'google','address':'indore','salary':85400})
#
# a = str(input(insert4()))