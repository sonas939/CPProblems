from sys import stdin
class Node:
    def __init__(self):
        self.low = -1
        self.disc = -1
        self.visited = False
        self.adj_list = []

time = 0
numSCC = 0

def dfs(u,stack):
    global time
    global numSCC
    nodeList[u].disc = nodeList[u].low = time
    time += 1
    stack.append(u)
    nodeList[u].visited = True
    for i in nodeList[u].adj_list:
        if nodeList[i].disc == -1:
            dfs(i,stack)
        if nodeList[i].visited:
            nodeList[u].low = min(nodeList[u].low,nodeList[i].low)
    
    if nodeList[u].disc == nodeList[u].low:
        numSCC += 1
        while (True):
            item = stack.pop()
            nodeList[item].visited = False
            if item == u:
                break

case = 1
for line in stdin:
    if line.strip() == "":
        break
    numCities,numRoads = [int(i) for i in line.strip().split(" ")]
    nodeList = [Node() for i in range(numCities)]
    listRoads = []
    for i in range(numRoads):
        a,b = [int(i) for i in input().split(" ")]
        nodeList[a].adj_list.append(b)
        listRoads.append((a,b))

    for i in range(numCities):
        if nodeList[i].disc == -1:
            dfs(i,[])
    if numSCC == 1:
        print("Case {}: valid".format(case))
    else:
        valid = False
        for i in listRoads:
            for j in nodeList:
                j.disc = -1
                j.low = -1
                j.visited = False
            a,b = i
            prev = [a,b]
            nodeList[a].adj_list.remove(b)
            nodeList[b].adj_list.append(a)

            time = 0
            numSCC = 0
            for j in range(numCities):
                if nodeList[j].disc == -1:
                    dfs(j,[])
            if numSCC == 1:
                valid = True
                print("Case {}: {} {}".format(case,a,b))
                break
            nodeList[a].adj_list.append(b)
            nodeList[b].adj_list.remove(a)
        if not valid:
            print("Case {}: invalid".format(case))
    case += 1