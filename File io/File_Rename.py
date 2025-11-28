import os

os.rename(r"E:\A.My\python-codes\PycharmProjects\core-python\Files\hii.txt",r"E:\A.My\python-codes\PycharmProjects\core-python\Files\hello.txt")


# import os
#
# source = r"E:\A.My\python-codes\PycharmProjects\core-python\Files\hello.txt"
# dest = r"E:\A.My\python-codes\PycharmProjects\core-python\Files\hi.txt"
#
# if os.path.exists(source):
#     os.rename(source, dest)
#     print(f"Renamed {source} to {dest}")
# else:
#     print(f"File not found: {source}")
#     print("Files in directory:")
#     dir_path = os.path.dirname(source)
#     for f in os.listdir(dir_path):
#         print(f"  {f}")
