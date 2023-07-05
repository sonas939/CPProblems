numTestCases = int(input())
for i in range(numTestCases):
    numPrizes,numStickers = [int(i) for i in input().split(" ")]
    prizes = []
    for i in range(numPrizes):
        prizes.append([int(i) for i in input().split(" ")])
    stickers = [int(i) for i in input().split(" ")]
    total = 0
    for i in prizes:
        minStickers = float('inf')
        for j in range(1,i[0]+1):
            minStickers = min(minStickers,stickers[i[j]-1])
        total += minStickers * i[i[0]+1]
    print(total)
                