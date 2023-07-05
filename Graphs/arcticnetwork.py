import math
def par(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = par(parent[x])
        return parent[x]

def merge(a,b):
    x = par(a)
    y = par(b)
    if x == y:
        return 0
    elif maxsize[x] >= maxsize[y]:
        parent[y] = x
        maxsize[x] += maxsize[y]
        if maxsize[x] == p:
            return 1
    else:
        parent[x] = y
        maxsize[y] += maxsize[y]
        if maxsize[x] == p:
            return 1
    return 2
    
n = int(input())
for i in range(n):
    s,p = [int(i) for i in input().split(" ")]
    nodes = []
    for j in range(p):
        nodes.append([int(i) for i in input().split(" ")])
    edges = []
    parent = [i for i in range(p)]
    maxsize = [1 for i in range(p)]
    for j in range(p):
        for k in range(j+1,p):
            dist = math.sqrt((nodes[j][0]-nodes[k][0]) ** 2 + (nodes[j][1]-nodes[k][1]) ** 2)
            edges.append((dist,j,k))
    edges.sort(reverse=True)
    weights = []
    while edges:
        val = edges.pop()
        ans = merge(val[1],val[2])
        if ans == 1:
            weights.append(val[0])
            break
        elif ans == 2:
            weights.append(val[0])
    minus = s - 1
    print(format(weights[-1-minus],".2f"))