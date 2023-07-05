import math
line = input().split(" ")
b = int(line[0])
k = int(line[1])
g = int(line[2])
groups = int(k/g)
print(math.ceil((b-1)/groups))