line = input().split(" ")
n = int(line[0])
q = int(line[1])

values = input().split(" ")
values = [int(i) for i in values]

trees = [[0 for i in range(n+1)]for j in range(6)]
arr = [0 for i in range(n+1)]
line = list(input())

def sum(index,tree):
    sum = 0
    while index > 0:
        sum += tree[index]
        index -= index & -index
    return sum

def update(index,num,tree):
    while index < len(tree):
        tree[index] += num
        index += index & -index

index = 1
for i in line:
    update(index,1,trees[int(i)-1])
    arr[index] = i
    index += 1

for i in range(q):
    line = input().split(" ")
    if line[0] == "1":
        index = int(line[1])
        newGem = int(line[2])
        update(index,-1,trees[int(arr[index])-1])
        update(index,1,trees[newGem-1])
        arr[index] = newGem
    elif line[0] == "2":
        valIndex = int(line[1])
        newVal = int(line[2])
        values[valIndex-1] = newVal
    else:
        start = int(line[1]) - 1
        end = int(line[2])
        a = 0
        b = 0
        j = 0
        for i in trees:
            a += sum(start,i) * values[j]
            b += sum(end,i) * values[j]
            j += 1
        print(b-a)
