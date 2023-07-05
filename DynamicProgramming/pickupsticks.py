from queue import Queue

class Node:
    def __init__(self):
        self.indegree = 0
        self.adj_list = []

n,m = [int(i) for i in input().split(" ")]
if n == 1:
    print(1)
else:
    nodeList = [Node() for i in range(n+1)]
    for i in range(m):
        v1,v2 = [int(j) for j in input().split(" ")]
        nodeList[v1].adj_list.append(v2)
        nodeList[v2].indegree += 1

    queue = Queue()
    for i in range(1,n+1):
        if not nodeList[i].indegree:
            queue.put(i)

    if not queue.qsize():
        print("IMPOSSIBLE")
    else:
        topSort = []
        while queue.qsize() > 0:
            v = queue.get()
            topSort.append(v)
            for i in nodeList[v].adj_list:
                nodeList[i].indegree -= 1
                if not nodeList[i].indegree:
                    queue.put(i)
        
        if len(topSort) > n:
            print("IMPOSSIBLE")
        else:
            for i in topSort:
                print(i)