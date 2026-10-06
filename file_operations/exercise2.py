#Exercise 2: Read and Print Complete File
#Problem Statement: Write a Python program that opens a file called data.txt and prints its entire contents to the console.

def file_read(file_name):
    with open(file_name) as f:
        data=f.read()
        return data
file_name = input("enter file name\n")
print(file_read(file_name))