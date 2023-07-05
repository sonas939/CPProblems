n = int(input())

for i in range(n):
    totW,freightW,numL = [int(j) for j in input().split(" ")]
    numFreight = [int(j) for j in input().split(" ")]
    low = 1
    high = totW
    mid = int((low+high)/2)
    
    while high-low > 1:
        count = 0 
        freightIndex = 0
        remL = numL
        while count < totW:
            index = min(count+mid,totW)
            isFreight = False
            numF = 0
            for j in range(freightIndex,freightW):
                if numFreight[j] >= count + 1 and numFreight[j] <= index:
                    numF += 1
                    isFreight = True
                else:
                    break
            freightIndex += numF
            count = index
            if not isFreight:
                if freightIndex == freightW:
                    remL -= 1
                    break
                count = numFreight[freightIndex] - 1
            remL -=1 
        if remL < 0:
            low = mid
        else:
            high = mid
        mid = int((low+high)/2)


    count = 0 
    freightIndex = 0
    mid = low
    remL = numL
    while count < totW:
        index = min(count+mid,totW)
        isFreight = False
        numF = 0
        for j in range(freightIndex,freightW):
            if numFreight[j] >= count + 1 and numFreight[j] <= index:
                numF += 1
                isFreight = True
            else:
                break
        freightIndex += numF
        count = index
        if not isFreight:
            if freightIndex == freightW:
                remL -= 1
                break
            count = numFreight[freightIndex] - 1
        remL -=1
    if remL < 0:
        print(high)
    else:
        print(low)