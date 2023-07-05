class Node:
    def __init__(self):
        self.adj_list = []
        self.depth = -1
        self.low = -1

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
                bridges.append((i,node))
        else:
            nodeList[node].low = min(nodeList[i].depth,nodeList[node].low)

while True:
    numP, c = [int(i) for i in input().split(" ")]
    if numP == 0 and c == 0:
        break
    nodeList = [Node() for i in range(numP)]
    for i in range(c):
        a,b = [int(i) for i in input().split(" ")]
        nodeList[a].adj_list.append(b)
        nodeList[b].adj_list.append(a)
    nodeList[0].depth = 0
    nodeList[0].low = 0
    bridges = []
    isConnected = True
    dfs(0,0,bridges)
    if len(bridges) == 0:
        for i in nodeList:
            if i.depth == -1:
                isConnected = False
                break
        if isConnected:
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")
    
