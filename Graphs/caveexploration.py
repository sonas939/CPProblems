import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self):
        self.adj_list = []
        self.depth = -1
        self.low = -1
        self.visited = False


def dfs(node,parent,bridges=[]):
    for i in nodeList[node].adj_list:
        if i == parent:
            continue
        elif nodeList[i].depth == -1:
            nodeList[i].depth = nodeList[node].depth + 1
            nodeList[i].low = nodeList[i].depth
            dfs(i,node,bridges)
            nodeList[node].low = min(nodeList[i].low,nodeList[node].low)
            if nodeList[i].low > nodeList[node].depth:
                bridges.append(i)
        else:
            nodeList[node].low = min(nodeList[i].depth,nodeList[node].low)

n,m = [int(i) for i in input().split(" ")]

nodeList = [Node() for i in range(n)]
for i in range(m):
    a,b = [int(i) for i in input().split(" ")]
    nodeList[a].adj_list.append(b)
    nodeList[b].adj_list.append(a)
nodeList[0].depth = 0
nodeList[0].low = 0
bridges = []
dfs(0,0,bridges)
stack = [0]
count = 0
while stack:
    node = stack.pop()
    if nodeList[node].visited:
        continue
    count += 1
    nodeList[node].visited = True
    for i in nodeList[node].adj_list:
        if not nodeList[i].visited:
            if i not in bridges:
                stack.append(i)
print(count)