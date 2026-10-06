#change ClientAliveInterval to 1000

def changing_value(file_name,key,value):
    with open(file_name) as f:
        data = f.readlines()

    with open(file_name,'w') as file:
        for line in data:
            if key in line:
                file.write(key + "  " + value + '\n')
            else:
                file.write(line)


file_name = 'sshd.config'
key = 'ClientAliveInterval'
value = "1000"
changing_value(file_name,key,value)