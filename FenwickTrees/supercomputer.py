line = input().split(" ")
n = int(line[0])
k = int(line[1])

tree = [0 for i in range(n+1)]
arr = [0 for i in range(n+1)]

def sum(index):
    sum = 0
    while index > 0:
        sum += tree[index]
        index -= index & -index
    return sum

def update(index,num):
    while index < len(tree):
        tree[index] += num
        index += index & -index

for i in range(k):
    line = input().split(" ")
    if line[0] == "F":
        index = int(line[1])
        if arr[index] == 0:
            update(index,1)
            arr[index] = 1
        else:
            update(index,-1)
            arr[index] = 0
    else:
        start = int(line[1])
        end = int(line[2])
        print(sum(end)-sum(start-1))