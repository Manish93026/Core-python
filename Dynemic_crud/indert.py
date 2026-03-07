import pymysql


class Insert:
    # Connection aur Cursor ko class level par rakhne ke bajaye function mein rakhna safe hota hai
    # Lekin aapke logic ke hisaab se ise aise likh sakte hain:

    def get_connection(self):
        return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')

    def insert1(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "insert into employee values(21, 'payal', 'vipro', 'indore', 54100)"
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("Inserted into employee table successfully (Static)")

    def insert2(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "insert into employee values(%s, %s, %s, %s, %s)"
        values = (22, 'raj', 'tcs', 'bangloru', 63990)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        print("Inserted into employee table successfully (Parameterized)")

    def insert3(self, id, name, company, address, salary):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "insert into employee values(%s, %s, %s, %s, %s)"
        values = (id, name, company, address, salary)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        print(f"Employee {name} inserted successfully (Arguments)")

    def insert4(self):
        print("\n--- Enter Employee Details ---")
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        company = input("Enter Company: ")
        address = input("Enter Address: ")
        salary = float(input("Enter Salary: "))

        connection = self.get_connection()
        cursor = connection.cursor()
        sql = "insert into employee values(%s, %s, %s, %s, %s)"
        values = (id, name, company, address, salary)

        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        print(f"Employee {name} inserted successfully (User Input)!")


# --- Program Execution ---
if __name__ == "__main__":
    # 1. Class ka object banayein
    obj = EmployeeInsert()

    # 2. Function call karein
    obj.insert4()