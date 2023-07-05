import math
l,w,n,r = [int(i) for i in input().split(" ")]
cranes = []
l1 = -l/2
l2 = l/2
w1 = -w/2
w2 = w/2
needOne = False
def isValid(point):
    if point <= r:
        return "1"
    else:
        return "0"
for i in range(n):
    x,y = [int(i) for i in input().split(" ")]
    str = ""
    point1 = math.sqrt((x-l1)**2 + (y)**2)
    str += isValid(point1)
    
    point2 = math.sqrt((x-l2)**2 + (y)**2)
    str += isValid(point2)

    point3 = math.sqrt((x)**2 + (y-w1)**2)
    str += isValid(point3)

    point4 = math.sqrt((x)**2 + (y-w2)**2)
    str += isValid(point4)

    if str == "1111":
        print(1)
        needOne = True
        break
    else:
        cranes.append(int(str,2))

needTwo = False
if not needOne:
    for i in cranes:
        for j in cranes:
            if i | j == 15:
                print(2)
                needTwo = True
                break
        if needTwo == True:
            break

needThree = False
if not needOne and not needTwo:
    for i in cranes:
        for j in cranes:
            for k in cranes:
                if i | j | k == 15:
                    print(3)
                    needThree = True 
                    break
            if needThree:
                break
        if needThree:
            break

needFour = False
if not needOne and not needTwo and not needThree:
    for i in cranes:
        for j in cranes:
            for k in cranes:
                for h in cranes:
                    if i | j | k | h == 15:
                        print(4)
                        needFour = True
                        break
                if needFour:
                    break
            if needFour:
                break
        if needFour:
            break

if not needOne and not needTwo and not needThree and not needFour:
    print("Impossible")