numA,numD = [int(i) for i in input().split(" ")]
aList = [[0,0]]
dList = [[0,0]]
totTimeA = 0
totTimeB = 0
totDist = 0
for i in range(numA):
    dist,time = [int(j) for j in input().split(" ")]
    totTimeA += time
    totDist += dist
    aList.append([totDist,totTimeA])

totB = 0
for i in range(numD):
    dist,time = [int(j) for j in input().split(" ")]
    totTimeB += time
    totB += dist
    dList.append([totB,totTimeB])

def calcDist(targetTime,arr):
    l = 0
    h = len(arr) - 1
    while True:
        mid = int((h+l)/2)
        if arr[mid][1] == targetTime:
            return arr[mid][0]
        elif arr[mid][1] < targetTime:
            if mid + 1 <= len(arr) - 1:
                if arr[mid+1][1] > targetTime:
                    diffTime = targetTime - arr[mid][1]
                    dist = (arr[mid+1][0] - arr[mid][0])/(arr[mid+1][1] - arr[mid][1])
                    a = diffTime*dist+arr[mid][0]
                    return a
            l = mid + 1
        else:
            if mid - 1 >= 0:
                if arr[mid-1][1] < targetTime:
                        diffTime = targetTime - arr[mid-1][1]
                        dist = (arr[mid][0] - arr[mid-1][0])/(arr[mid][1] - arr[mid-1][1])

                        return arr[mid-1][0] + dist * diffTime
            h = mid - 1

high = min(totTimeA,totTimeB)
low = 0
middle = (low+high)/2
aDist = calcDist(middle,aList)
bDist = totDist - calcDist(middle,dList)
lowest = float('inf')
while abs(high-low) > 0.00000001:
    if abs(aDist - bDist) <= 0.00000001:
        if lowest > middle:
            lowest = middle
            high = middle
            low = 0
    elif aDist < bDist:
        low = middle
    else:
        high = middle
    middle = (low+high)/2
    aDist = calcDist(middle,aList)
    bDist = totDist - calcDist(middle,dList)

print(f'{lowest:.6f}')