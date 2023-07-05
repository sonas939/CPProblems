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

n = int(input())
for i in range(n):
    line = input().split(" ")
    m = int(line[0])
    r = int(line[1])
    queries = input().split(" ")
    tree = [0 for i in range(m+r+1)]
    arr = [m+1-i for i in range(m+1)]
    for j in range(1,m+1):
        update(j,1)

    tot = m + 1
    for j in queries:
        num = int(j)
        index = arr[num]
        if tot == m+r:
            print(m-sum(index))
        else:
            print(m-sum(index),end=" ")
        update(index,-1)
        arr[num] = tot
        update(tot,1)
        tot += 1