import math
from queue import PriorityQueue
class Node:
    def __init__(self):
        self.adj_list = []


sX,sY = [float(i) for i in input().split(" ")]
gX,gY = [float(i) for i in input().split(" ")]
n = int(input())

coords = [(sX,sY)]
nodeList = [Node() for i in range(n+2)]
dist = [float('inf') for i in range(n+2)]
dist[0] = 0
for i in range(n):
    x,y = [float(i) for i in input().split(" ")]
    coords.append((x,y))

coords.append((gX,gY))

for i in range(n+2):
    for j in range(i+1,n+2):
        length = math.sqrt((coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2)
        minDist = length/5
        if i != 0:
            minDist = min(minDist,abs(50-length)/5+2)
        nodeList[i].adj_list.append((minDist,j))
        nodeList[j].adj_list.append((minDist,i))

pq = PriorityQueue()
pq.put((-0,0))


while not pq.empty():
    nodeDist,node = pq.get()
    nodeDist = -nodeDist
    if (nodeDist > dist[node]):
        continue

    for i in nodeList[node].adj_list:
        newDist = dist[node] + i[0]
        if newDist < dist[i[1]]:
            dist[i[1]] = newDist
            pq.put((-newDist,i[1]))

print(dist[-1])