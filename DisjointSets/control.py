n = int(input())
maxsize = [1 for i in range(500001)]
parent = [i for i in range(500001)]
recipes = 0

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    elif maxsize[a] > maxsize[b]:
        parent[b] = a
        maxsize[a] += maxsize[b]
    else:
        parent[a] = b
        maxsize[b] += maxsize[a]

for i in range(n):
    dict = {}
    count = 0
    line = input().split()
    numIngred = int(line[0])
    nums = line[1:]

    for j in nums:
        p = find(int(j))
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
        if dict[p] == maxsize[p]:
            count += maxsize[p]
    if count == numIngred:
        recipes += 1
        for j in dict:
            union(int(nums[0]),j)
print(recipes)