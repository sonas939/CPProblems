from queue import Queue

class Node:
    def __init__(self):
        self.adj_list = []
        self.color = -1
        self.visited = False


dict = {}
nodes = []
numV = int(input())
for i in range(numV):
    list = input()
    dict[list] = Node()
    nodes.append(list)

numE = int(input())
for i in range(numE):
    s1,s2 = input().split(" ")
    dict[s1].adj_list.append(s2)
    dict[s2].adj_list.append(s1)

queue = Queue()
queue.put(nodes[0])
length = 0
walt = []
jess = []
isImpossible = False
for i in nodes:
    if dict[i].color != -1:
        continue
    else:
        dict[i].color = 0
        queue.put(i)
    while queue.qsize() > 0:
        ingred = queue.get()
        col = dict[ingred].color
        if dict[ingred].visited:
            continue
        dict[ingred].visited = True
        if col == 0:
            walt.append(ingred)
        else:
            jess.append(ingred)
        for j in dict[ingred].adj_list:
            if dict[j].color == -1:
                dict[j].color = not col
                queue.put(j)
            else:
                if dict[j].color != (not col):
                    isImpossible = True
                    break

    if isImpossible:
        break

if isImpossible:
    print("impossible")
else:
    for i in range(len(walt)):
        if i == len(walt)-1:
            print(walt[i])
        else:
            print(walt[i],end=" ")
    
    for i in range(len(jess)):
        if i == len(jess)-1:
            print(jess[i])
        else:
            print(jess[i],end=" ")
