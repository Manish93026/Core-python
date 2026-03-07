import pymysql
from InternetPackage import InternetPackage


class InternetModel:
    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, password='root', user='root', db='advpython')
        cursor = connection.cursor()
        sql = "select max(id) from internetpackage"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[0] is not None:
            pk = result[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = self.nextPk()
        package_name = data['package_name']
        price = data['price']
        data_limit = data['data_limit']

        connection = pymysql.connect(host='localhost', port=3306, password='root', user='root', db='advpython')
        cursor = connection.cursor()
        sql = "insert into internetpackage values(%s, %s, %s, %s)"
        data = (id, package_name, price, data_limit)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")


m = InternetModel()
packages_list = [

    {'package_name': 'Daily Plus', 'price': 29.0, 'data_limit': 2},
    {'package_name': 'Weekly Lite', 'price': 99.0, 'data_limit': 7},
    {'package_name': 'Weekly Pro', 'price': 149.0, 'data_limit': 14},
    {'package_name': 'Monthly Basic', 'price': 299.0, 'data_limit': 30},
    {'package_name': 'Monthly Standard', 'price': 499.0, 'data_limit': 60},
    {'package_name': 'Monthly Premium', 'price': 799.0, 'data_limit': 150},
    {'package_name': 'Monthly Ultra', 'price': 999.0, 'data_limit': 300},
    {'package_name': 'Student Special', 'price': 150.0, 'data_limit': 20},
    {'package_name': 'Gamer Pack', 'price': 1200.0, 'data_limit': 500},
    {'package_name': 'Work From Home', 'price': 650.0, 'data_limit': 200},
    {'package_name': 'Streaming Pro', 'price': 850.0, 'data_limit': 250},
    {'package_name': 'Binge Night', 'price': 49.0, 'data_limit': 10},
    {'package_name': 'Social Media Lite', 'price': 99.0, 'data_limit': 5},
    {'package_name': 'Business Gold', 'price': 2500.0, 'data_limit': 1000},
    {'package_name': 'Business Platinum', 'price': 5000.0, 'data_limit': 5000},
    {'package_name': 'Fiber Starter', 'price': 399.0, 'data_limit': 100},
    {'package_name': 'Fiber Speedster', 'price': 599.0, 'data_limit': 250},
    {'package_name': 'Annual Saver', 'price': 3500.0, 'data_limit': 1200},
    {'package_name': 'Weekend Binge', 'price': 75.0, 'data_limit': 15},
    {'package_name': 'Traveler Pack', 'price': 199.0, 'data_limit': 25},
    {'package_name': 'Corporate Lite', 'price': 1500.0, 'data_limit': 800},
    {'package_name': 'Family Plan', 'price': 1100.0, 'data_limit': 400},
    {'package_name': 'Infinite Data', 'price': 1999.0, 'data_limit': 9999},
    {'package_name': 'Emergency Topup', 'price': 15.0, 'data_limit': 1}
]

for package in packages_list:
    m.add(package)
