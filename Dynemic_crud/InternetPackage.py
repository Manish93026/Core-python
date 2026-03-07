# InternetPackage.py
class InternetPackage:
    def __init__(self):
        self.__id = 0
        self.__package_name = ''
        self.__price = 0
        self.__data_limit = 0

    # Getters and Setters
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def get_package_name(self):
        return self.__package_name
    def set_package_name(self, name):
        self.__package_name = name

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def get_data_limit(self):
        return self.__data_limit
    def set_data_limit(self, data_limit):
        self.__data_limit = data_limit