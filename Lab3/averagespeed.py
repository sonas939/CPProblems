import sys
dist = 0
speed = 0
lastTime = -1

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    line = line.split(" ")
    time = line[0].split(":")
    
    currTime = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    if lastTime != -1:
        diffTime = (currTime - lastTime) / 3600
        dist += diffTime * speed

    lastTime = currTime

    if len(line) > 1:
        speed = float(line[1])
    else:
        roundDist = round(dist,2)
        print(line[0],"{:.2f} km".format(roundDist))