c = int(input())
for i in range(c):
    line = input().split(" ")
    l = int(line[0]) * 100
    m = int(line[1])
    count = 0
    left = []
    right = []
    for j in range(m):
        line = input().split()
        if line[1] == "left":
            left.append(int(line[0]))
        else:
            right.append(int(line[0]))
    while len(left) > 0 or len(right) > 0:
        sum = l
        isRight = False
        while len(left) > 0:
            if sum - left[0] >= 0:
                sum -= left[0]
                left.pop(0)
            else:
                break
        count += 1
        sum = l
        while len(right) > 0:
            isRight = True
            if sum - right[0] >= 0:
                sum -= right[0]
                right.pop(0)
            else:
                break
        if not isRight and len(left) > 0:
            count += 1
        if isRight:
            count += 1
    print(count)