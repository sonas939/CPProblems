import math
line = input().split(" ")
n = int(line[0])
maxRequests = int(line[1])
queue = []
max = 0
for i in range(n):
    time = int(input())
    while len(queue) > 0:
        if queue[0] + 1000 <= time:
            queue.pop(0)
        else:
            break
    queue.append(time)
    if len(queue) > max:
        max = len(queue)

print(math.ceil(max/maxRequests))