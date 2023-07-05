usrInput = input().split(" ")

start = int(usrInput[0])
end = int(usrInput[1])
nStops = int(usrInput[2])
transitTime = input().split(" ")
transitTime = [int(x) for x in transitTime]

busTime = input().split(" ")
busTime = [int(x) for x in busTime]

busInterval = input().split(" ")
busInterval = [int(x) for x in busInterval]

for index in range(nStops+1):
    start += transitTime[index]
    if index < nStops:
        if start % busInterval[index] != 0:
            start += busInterval[index]-start % busInterval[index]
        start += busTime[index]
if start <= end:
    print("yes")
else:
    print("no")