class Building:
    def __init__(self,parent,maxsize = 0):
        self.parent = parent
        self.maxsize = maxsize

dict = {}
def find(x):
    if dict[x].parent != x:
        dict[x].parent = find(dict[x].parent)
        return dict[x].parent
    else:
        return dict[x].parent

n = int(input())
for i in range(n):
    bridges = input().split(" ")
    if bridges[0] not in dict and bridges[1] not in dict:
        dict[bridges[0]] = Building(bridges[0],2)
        dict[bridges[1]] = Building(bridges[0])
        print(2)
    elif bridges[0] in dict and bridges[1] in dict:
        parentA = find(bridges[0])
        parentB = find(bridges[1])
        count = 0
        if parentA == parentB:
            print(dict[parentA].maxsize)
        elif dict[parentA].maxsize > dict[parentB].maxsize:
            dict[parentB].parent = parentA
            dict[parentA].maxsize += dict[parentB].maxsize
            print(dict[parentA].maxsize)
        else:
            dict[parentA].parent = parentB
            dict[parentB].maxsize += dict[parentA].maxsize
            print(dict[parentB].maxsize)
    elif bridges[0] in dict:
        parent = find(bridges[0])
        dict[bridges[1]] = Building(parent)
        dict[parent].maxsize += 1
        print(dict[parent].maxsize)
    else:
        parent = find(bridges[1])
        dict[bridges[0]] = Building(parent)
        dict[parent].maxsize += 1
        print(dict[parent].maxsize)