numProf = int(input())
counts = input().split(" ")
counts = [int(i) for i in counts]
profs = list(range(1,numProf+1))
start = 0
while len(profs) > 1:
    start = start + counts[profs[start]-1] % numProf - 1
    if start == -1:
        start = numProf - 1
    if start >= numProf:
        start %= numProf
    numProf -= 1
    profs.pop(start) 
    if start >= numProf:
        start = 0

print(profs[0])