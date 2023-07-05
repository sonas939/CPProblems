n = int(input()) 
dict = {}
people = [i for i in range(n+1)]
maxsize = [1 for i in range(n+1)]

def parent(x):
    if x == people[x]:
        return x
    else:
        people[x] = parent(people[x])
        return people[x]

def merge(x,y):
    a = parent(x)
    b = parent(y)
    if a == b:
        return True
    if maxsize[a] == maxsize[b]:
        people[b] = a
        maxsize[a] += maxsize[b]
    elif maxsize[a] > maxsize[b]:
        people[b] = a
        maxsize[a] += maxsize[b]
    else:
        people[a] = b
        maxsize[b] += maxsize[a]
    return False

for i in range(n):
    line = [int(j) for j in input().split(" ")]
    for j in range(1,len(line)):
        if line[j] in dict:
            dict[line[j]].append(i+1)
        else:
            dict[line[j]] = [i+1]


pairs = []
for j in dict:    
    if len(dict[j]) == 1:
        continue
    else:
        par = parent(dict[j][0])
        for k in range(1,len(dict[j])):
            if merge(par,dict[j][k]) == False:
                pairs.append((dict[j][0],dict[j][k],j))

first = parent(people[1])
impossible = False
for i in range(2,len(people)):
    if first == parent(people[i]):
        continue
    else:
        print("impossible")
        impossible = True
        break
if not impossible:
    for i in pairs:
        print("{} {} {}".format(i[0],i[1],i[2]))