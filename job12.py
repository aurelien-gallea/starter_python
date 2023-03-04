import re

file = open("data.txt", "rt")
data = file.read()

res = len(re.findall(r'[a-zA-Z]+', data))

print(res)

