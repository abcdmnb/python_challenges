###Execise1##########
#probem: Write a Python program that accepts a user’s name as input and writes it to a file called user.txt.
name=input("enter your name")
file_path = "user.txt"

def add_to_user_file(file_path,name):
    f=open(file_path,"a+")
    f.write(f"\n{name}")
    f.seek(0)
    data=f.read()
    f.close()
    return data


print(add_to_user_file(file_path,name))