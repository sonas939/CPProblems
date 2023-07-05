numProblems, timePossible = [int(i) for i in input().split(" ")]

a,b,c,t0 = [int(i) for i in input().split(" ")]


if numProblems == 0:
    print(0,0)
else:
    t = [0] * numProblems
    t[0] = t0

    for i in range(1,numProblems):
        t[i] = ((a*t[i-1]+b)%c)+1

    t.sort()

    timeSpent = 0
    penalty = 0
    i = 0
    problemsSolved = 0
    while True:
        if problemsSolved + 1 <= numProblems:
            problemsSolved += 1
        else:
            break
        
        if timeSpent + t[i] <= timePossible:
            timeSpent += t[i]
            penalty = (penalty + timeSpent) % 1000000007
        else:
            problemsSolved -= 1
            break
        i += 1

    print(problemsSolved,penalty)