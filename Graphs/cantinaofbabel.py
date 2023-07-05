class Node:
    def __init__(self,name):
        self.name = name
        self.low = -1
        self.disc = -1
        self.visited = False
        self.adj_list = []

n = int(input())
speak = {}
understand = {}
nodeList = []
for i in range(n):
    line = input().split(" ")
    nodeList.append(Node(line[0]))
    if line[1] not in speak:
        speak[line[1]] = [i]
        if line[1] not in understand:
            understand[line[1]] = [i]
        else:
            understand[line[1]].append(i)
    else:
        speak[line[1]].append(i)
        understand[line[1]].append(i)
    for j in line[2:]:
        if j not in understand:
            understand[j] = [i]
        else:
            understand[j].append(i)

#build graph
for i in speak:
    for j in speak[i]:
        for k in understand[i]:
            if j == k:
                continue
            nodeList[j].adj_list.append(k)

def dfs(u,stack,inStack,time,maxNum):
    nodeList[u].disc = nodeList[u].low = time
    stack.append(u)
    inStack[u] = True
    count = 1
    for i in nodeList[u].adj_list:
        if nodeList[i].disc == -1:
            dfs(i,stack,inStack,time+count,maxNum)
            nodeList[u].low = min(nodeList[u].low,nodeList[i].low)
        elif inStack[i]:
            nodeList[u].low = min(nodeList[u].low,nodeList[i].disc)
        count += 1
    
    if nodeList[u].disc == nodeList[u].low:
        numPop = 0
        while (stack[-1] != u):
            item = stack.pop()
            inStack[item] = False
            numPop += 1
        stack.pop()
        inStack[u] = False
        numPop += 1
        maxNum[0] = max(numPop,maxNum[0])

finalMax = 0
for i in range(n):
    if nodeList[i].disc == -1:
        maxNum = [1]
        dfs(i,[],[False for i in range(n)],0,maxNum)
        finalMax = max(finalMax,maxNum[0])

print(n-finalMax)
        