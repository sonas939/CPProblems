nHouses, nCases = [int(i) for i in input().split(" ")]
p = [i for i in range(nHouses+1)]
maxsize = [1 for i in range(nHouses+1)]
def parent(x):
    if x == p[x]:
        return x
    else:
        p[x] = parent(p[x])
        return p[x]

for i in range(nCases):
    x,y = [int(j) for j in input().split(" ")]
    parentX = parent(x)
    parentY = parent(y)
    if maxsize[parentX] >= maxsize[parentY]:
        p[parentY] = parentX
        maxsize[parentY] += maxsize[parentX]
    else:
        p[parentX] = parentY
        maxsize[parentX] += maxsize[parentY]

par1 = parent(p[1])
connected = True
count = 1
for i in p:
    if i == 0:
        continue
    elif i == par1:
        count += 1
        continue
    elif parent(i) == par1:
        count += 1
        continue
    else:
        connected = False
        print(count)
        count += 1
if connected:
    print("Connected")