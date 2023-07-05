n = int(input())
classSize = [int(i) for i in input().split(" ")]
sum = sum(classSize)
if sum % 3 != 0:
    print(-1)
else:
    a = sum/3
    x = 0
    count = []
    index = 0
    d = False
    for i in classSize:
        x += i
        if x == a:
            count.append(index+1)
            x = 0
        elif x > a:
            d = True
            break
        index += 1
    
    if d or len(count) != 3:
        print(-1)
    else:
        print(count[0],count[1])