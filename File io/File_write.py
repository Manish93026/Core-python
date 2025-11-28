def Filewirte():
    file = open("../files/hello.txt",'w')

    file.write("Hello \n")
    file.write("Manish \n")
    file.write("How is going your day \n")

    file.close()

Filewirte()