# test_internetpackage.py
from InternetPackage import InternetPackage
from internet_pagckage import InternetModel

def testadd():
    # 1. Bean mein data set karein
    bean = InternetPackage()
    bean.set_package_name('Daily Starter')
    bean.set_price(19.0)
    bean.set_data_limit(1)

    # 2. Model ka use karke database mein add karein
    model = InternetModel()
    model.add(bean)

if __name__ == "__main__":
    testadd()