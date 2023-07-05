n = int(input())

for i in range(n):
    length, numAnts = [int(i) for i in input().split(" ")]
    positions = []
    while len(positions) < numAnts:
        p1 = [int(i) for i in input().split(" ")]
        positions += p1
    median = length/2
    bestCase = -1
    for i in positions:
        if i <= median:
            if i > bestCase:
                bestCase = i
        else:
            if length - i > bestCase:
                bestCase  = length - i
    mins = min(positions)
    maxs = max(positions)
    worstCase = length - mins
    if maxs > worstCase:
        worstCase = maxs
    print(bestCase,worstCase)