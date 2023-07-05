from queue import Queue

class Node:
    def __init__(self):
        self.value = -1
        self.adj_list = []

n,m = [int(i) for i in input().split(" ")]
if n == 1:
    print(0)
else:
    nodeList = [Node() for i in range(n+1)]
    for i in range(m):
        v1,v2 = [int(j) for j in input().split(" ")]
        nodeList[v1].adj_list.append(v2)
        nodeList[v2].adj_list.append(v1)

    queue = Queue()
    nodeList[1].value = 0
    queue.put(1)
    while queue.qsize() > 0:
        v = queue.get()
        val = nodeList[v].value
        for i in nodeList[v].adj_list:
            if nodeList[i].value == -1:
                nodeList[i].value = val + 1
                queue.put(i)

    print(nodeList[n].value - 1)