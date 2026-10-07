###advanced lambda functions
a,b = 10000,999

maximum = lambda a,b: a if a>b else b

print(f"maximum number among { a,b } is { maximum(a,b) }")

minimum = lambda a,b: a if a<b else b

print(f"minimum is { minimum(a,b) }")

x = 26

abs = lambda x: -x if x<0 else x

print(f"printing absolute value { abs(x) }")

check = lambda x: "Positive Even" if x>0 and x%2==0 else "Other"

print(f"positiveEven check for { x } is { check(x) } ")