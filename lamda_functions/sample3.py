##understanding map function
##usage map(function,collection)

disk_usage = [50, 65, 70, 85, 90]

result = list(map(lambda x: x+5, disk_usage))
print(result)

memory_mb = [1024, 2048, 4096, 8192]

gb_result = list(map(lambda x: x/1024, memory_mb))

print(memory_mb)

print(f"given memory in gb is \n{ gb_result }")

servers = ["web01", "web02", "db01", "app01"]

result1 = list(map(lambda x: "server-"+x, servers))
print(result1)

servers = ["web-prod-01", "web-dev-01", "db-prod-01"]

convert = list(map(lambda x:x.upper(), servers))

print(convert)