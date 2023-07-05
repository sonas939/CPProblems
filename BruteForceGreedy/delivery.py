import math
line = input().split(" ")
n,numLetter = int(line[0]),int(line[1])
neg = []
pos = []
for i in range(n):
    line = [int(i) for i in input().split(" ")]
    if line[0] < 0:
        neg.append(line)
    else:
        pos.append(line)

neg.sort()
pos.sort(reverse=True)

remainingLetters = 0
dist = 0

while len(neg) > 0:
    if remainingLetters != 0: 
        neg[0][1] -= remainingLetters
        if neg[0][1] < 0: 
            remainingLetters = neg[0][1] * -1
            neg.pop(0)
            continue
        elif neg[0][1] == 0:
            remainingLetters = 0
            neg.pop(0)
            continue

    factor = math.ceil(neg[0][1]/numLetter)
    dist += factor * neg[0][0] * 2 * -1
    remainingLetters = numLetter * factor - neg[0][1] 
    neg.pop(0)


remainingLetters = 0
while len(pos) > 0:
    if remainingLetters != 0: 
        pos[0][1] -= remainingLetters
        if pos[0][1] < 0: 
            remainingLetters = pos[0][1] * -1
            pos.pop(0)
            continue
        elif pos[0][1] == 0:
            remainingLetters = 0
            pos.pop(0)
            continue

    factor = math.ceil(pos[0][1]/numLetter)
    dist += factor * pos[0][0] * 2
    remainingLetters = numLetter * factor - pos[0][1] 
    pos.pop(0)

print(dist)
