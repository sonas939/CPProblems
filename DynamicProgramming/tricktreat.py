import math
n = int(input())
def euclidean_distance(x2,points):
    max = 0
    for i in points:
        dist = math.sqrt((i[1])**2+(x2-i[0])**2)
        if dist > max:
            max = dist
    
    return max


while n != 0:
    points = []
    low = 200000
    high = -200000
    for i in range(n):
        x,y = [float(j) for j in input().split(" ")]
        if x < low:
            low = x
        if x > high:
            high = x
        points.append((x,y))
    
    while abs(low-high) > 0.00000001:
        a = low + (high-low)/3
        b = low + ((high-low)*2)/3
        aPoint = euclidean_distance(a,points)
        bPoint = euclidean_distance(b,points)
        if aPoint < bPoint:
            high = b
        else:
            low = a
    time = euclidean_distance(low,points)
    print(f'{low:.12f}',f'{time:.12f}')

    input()
    n = int(input())