import math
import heapq as hp

class Point:
    def __init__(self,angle,adj_list,x,y):
        self.angle = angle
        self.adj_list = adj_list 
        self.x = x
        self.y = y

def calcAngle(p1x,p1y,p2x,p2y,p3x,p3y):
    ax = p1x-p2x
    ay = p1y-p2y
    bx = p1x-p3x
    by = p1y-p3y
    ab = ax*bx + ay*by
    magA = math.sqrt(ax**2+ay**2)
    magB = math.sqrt(bx**2+by**2)
    return (180/math.pi) * math.acos((ab)/(magA*magB))


while True:
    line = [int(i) for i in input().split(" ")]
    num = line[0]
    line=line[1:]
    if num == 0:
        break
    points = []
    h = []
    count = 0
    for i in range(0,num*2,2):
        if count == num-1:
            angle = calcAngle(line[i],line[i+1],line[i-2],line[i-1],line[0],line[1])
            points.append(Point(angle,[0,count-1],line[i],line[i+1]))
        else:
            angle = calcAngle(line[i],line[i+1],line[i-2],line[i-1],line[i+2],line[i+3])
            points.append(Point(angle,[count+1,count-1],line[i],line[i+1]))
        hp.heappush(h,(angle,count))
        count += 1
    
    numPoints = num
    inShape = [True] * num
    while True:
        if numPoints == 3:
            break
        angle,count = hp.heappop(h)
        if not inShape[count]:
            continue
        point1 = points[points[count].adj_list[0]]
        point2 = points[points[count].adj_list[1]]
        #update adjanceny list
        if point1.adj_list[0] == count:
            point1.adj_list[0] = points[count].adj_list[1]
        else:
            point1.adj_list[1] = points[count].adj_list[1]
        
        if point2.adj_list[0] == count:
            point2.adj_list[0] = points[count].adj_list[0]
        else:
            point2.adj_list[1] = points[count].adj_list[0]

        point1.angle = calcAngle(point1.x,point1.y,points[point1.adj_list[0]].x,points[point1.adj_list[0]].y,points[point1.adj_list[1]].x,points[point1.adj_list[1]].y)
        point2.angle = calcAngle(point2.x,point2.y,points[point2.adj_list[0]].x,points[point2.adj_list[0]].y,points[point2.adj_list[1]].x,points[point2.adj_list[1]].y)
        if point1.angle < angle or point2.angle < angle:
            break
        inShape[count] = False
        numPoints -= 1
        hp.heappush(h,(point1.angle,points[count].adj_list[0]))
        hp.heappush(h,(point2.angle,points[count].adj_list[1]))
        

    first = True
    print(numPoints,end=" ")
    for i in range(num):
        if inShape[i]:
            if first:
                print(line[i*2],line[i*2+1],end="")
                first = False
            else:
                print(" " + str(line[i*2]),line[i*2+1],end="")
    print()
        
