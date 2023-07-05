line = input().split(" ")
length = int(line[0])
dist = int(line[1])
numBirds = int(line[2])

birds = []
for i in range(numBirds):
    birds.append(int(input()))

birds.sort()
if length < 12:
    print(0)
elif numBirds == 0: 
    print(int((length-12)/dist + 1))
else:
    left = 6
    right = length - 6
    count = 0
    prevBird = birds[0]
    for i in range(1,len(birds)):
        count += int((birds[i] - prevBird)/(dist)) - 1
        prevBird = birds[i]
    count += int((birds[0] - left)/dist)
    count += int((right - birds[len(birds)-1])/dist)
    print(count)