def swapFileData():
    fileName1 = input("Enter the file name: ")
    fileName2 = input("Enter the file name: ")
    
    with open(fileName1,'r') as a:
        data_a = a.read()
        print ("File 1 has", data_a)

    with open(fileName2, 'r') as b:
        data_b = b.read()
        print("File 2 has", data_b)

    with open(fileName1,'w') as a:
        a.write(data_b)
        print("File 1 has", data_b)

    with open(fileName2,'w') as b:
        b.write(data_a)
        print("File 2 has", data_a)

swapFileData()