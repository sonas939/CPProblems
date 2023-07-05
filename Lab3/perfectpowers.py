import math
while True:
    x = int(input())
    if x == 0:
        break
    step = -1
    start = 32
    if x < 0:
        step = -2
        start = 31
        x *= -1
        
    for i in range(start,0,step):
        b = round(math.pow(x,1/i))
        if math.pow(b,i) == x:
            print(i)
            break