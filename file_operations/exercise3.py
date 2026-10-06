#Problem Statement: Write a Python program that reads a file called sshd.config and prints each line one at a time using a loop.

def read_linebyline(file_name):
    with open(file_name) as f:
        data = f.readlines()
      #  print(data)
        for line in data:
           print(line)

file_name = 'sshd.config'

read_linebyline(file_name)