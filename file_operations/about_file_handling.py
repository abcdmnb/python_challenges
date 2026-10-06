
name = input("enter user name\n")
##mode type X is just for file creation, below line will create a file called users_file.txt in current directory
##if using w mode immediately running w mode, it will earse everything in  file, so needs to be very careful while using w mode, only single below command will erase everything inside file
###r+ mode performs read and write operations
#f.tell() will tell the position of pointer
#w+ mode will perform read and write but unlike r+, immeditely after running line data will clear
#f.seek() will move the pointer cursor to the required position
#a+ will perform both read and append
f=open("users_file.txt","a+")
print(f.tell())
f.write("\nthis is sond line")
f.seek(0)
print(f.read())
f.close()





#def append_content_to_a_file(file_name,name):

