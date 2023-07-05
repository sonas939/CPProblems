colors = input()
blue = []
red = []
for i in colors:
    if i == 'B':
        blue.append(1)
        red.append(-1)
    else:
        blue.append(-1)
        red.append(1)

def purple_rain(color):
    start = 0
    end = 0
    totMax = 0
    curr = 0
    index = 0
    totStart = 0
    totEnd = 0
    for i in color:
        curr += i
        if curr < 0:
            curr = 0
            start = index + 1
        if curr > totMax:
            end = index
            totMax = curr
            totStart = start
            totEnd = end
        index += 1
    return [totStart,totEnd,totMax]

rStart, rEnd, rMax = purple_rain(red)
bStart, bEnd, bMax = purple_rain(blue)
if rMax > bMax:
    print(rStart + 1,rEnd + 1)
elif bMax > rMax:
    print(bStart + 1, bEnd + 1)
else: #check second paragrpah of output
    if rStart < bStart:
        print(rStart + 1, rEnd + 1)
    elif bStart < rStart:
        print(bStart + 1, bEnd + 1)
    else:
        if rEnd < bEnd:
            print(rStart + 1, rEnd + 1)
        else:
            print(bStart + 1, bEnd + 1)