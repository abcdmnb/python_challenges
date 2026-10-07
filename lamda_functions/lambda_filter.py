##understanding lambda filter
##syntax filter(function, collection) syntax is same as like map but map applies on every item but filter applies only selected items

servers = [
    "web-prod-01",
    "web-dev-01",
    "db-prod-01",
    "app-test-01",
    "db-prod-02"
]

prod_servers = list(filter(lambda x: "prod" in x, servers))
print(prod_servers)

users = [
    "root",
    "oracle",
    "ansible_svc",
    "backup_svc",
    "bhagya",
    "deploy_svc"
]

svc_users = list(filter(lambda x: x.endswith("_svc"), users))

print(svc_users)

cpu_usage = [25, 45, 92, 67, 88, 95, 80, 30]

more_cpu_values = list(filter(lambda x: x>=80, cpu_usage))

print(more_cpu_values)