while True:
    n = int(input())
    if n == 0:
        break
    
    lines = [0 for i in range(n)]
    for i in range(n):
        lines[i] = [float(j) for j in input().split(" ")]
    

    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                #intersection between i and j
                x1,y1,x2,y2 = lines[i]
                x3,y3,x4,y4 = lines[j]
                denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                if denom == 0:
                    continue
                num1 = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
                num2 = (x1-x3)*(y1-y2)-(y1-y3)*(x1-x2)
                t = num1/denom
                u = num2/denom
                if t < 0 or t > 1 or u < 0 or u > 1:
                    continue
                #intersection between j and k
                x1,y1,x2,y2 = lines[j]
                x3,y3,x4,y4 = lines[k]
                denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                if denom == 0:
                    continue
                num1 = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
                num2 = (x1-x3)*(y1-y2)-(y1-y3)*(x1-x2)
                t = num1/denom
                u = num2/denom
                if t < 0 or t > 1 or u < 0 or u > 1:
                    continue
                #interesection between k and i
                x1,y1,x2,y2 = lines[k]
                x3,y3,x4,y4 = lines[i]
                denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                if denom == 0:
                    continue
                num1 = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
                num2 = (x1-x3)*(y1-y2)-(y1-y3)*(x1-x2)
                t = num1/denom
                u = num2/denom
                if t < 0 or t > 1 or u < 0 or u > 1:
                    continue
                
                count += 1
    print(count)

