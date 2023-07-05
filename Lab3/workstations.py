from queue import PriorityQueue
line = input().split(" ")
n = int(line[0])
m = int(line[1])

nums = []
for i in range(n):
    line = input().split(" ")
    nums.append([int(line[0]),int(line[1])])

nums.sort()

count = 0
workstations = PriorityQueue()
for i in nums:
    if workstations.empty() == False:
        while workstations.queue[0] + m < i[0]:
            workstations.get()
            if workstations.empty():
                break
    
    if workstations.empty():
        workstations.put(i[0]+i[1])
    else:
        if workstations.queue[0] <= i[0] and i[0] <= workstations.queue[0] + m:
            workstations.get()
            workstations.put(i[0] + i[1])
            count += 1
        else:
            workstations.put(i[0] + i[1])


print(count)