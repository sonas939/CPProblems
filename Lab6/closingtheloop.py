n = int(input())

for i in range(n):
    s = int(input())
    red = []
    blue = []
    segment = input().split(" ")
    for j in segment:
        isRed = j.find("R")
        if isRed != -1:
            red.append(int(j[:isRed]))
        else:
            isBlue = j.find("B")
            blue.append(int(j[:isBlue]))
    if len(red) == 0 or len(blue) == 0:
        print("Case #{}: {}".format(i+1,0))
    else:
        red.sort(reverse=True)
        blue.sort(reverse=True)
        length = 0
        while len(red) > 0 and len(blue) > 0:
            length += red.pop(0) + blue.pop(0) - 2
        print("Case #{}: {}".format(i+1,length))
