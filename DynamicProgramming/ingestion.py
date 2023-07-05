import math
n,m = [int(i) for i in input().split(" ")]
courses = [int(i) for i in input().split(" ")]
grid = [[-1 for i in range(n)]for j in range(n+1)]
def dp(i,j):
    if i > n:
        return 0
    elif grid[i][j] != -1:
        return grid[i][j]
    else:
        validMax = min(courses[i-1],calculations[j])
        valJ = max(0,j-1)
        grid[i][j] = max(dp(i+1,j+1) + validMax,dp(i+1,valJ),dp(i+2,0))
        return grid[i][j]
calculations = [0 for i in range(n)]
calculations[0] = m
for i in range(1,n):
    calculations[i] = int(calculations[i-1] * (2/3))
print(dp(1,0))