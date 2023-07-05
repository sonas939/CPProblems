import sys
sys.setrecursionlimit(10**9)
n,k = [int(i) for i in input().split(" ")]


grid = [[0 for i in range(2)]for j in range(n)]
dpGrid = [[[-1 for i in range(2)]for j in range(n)]for k in range(k)]
sum = 0
for i in range(n):
    x,y = [int(j) for j in input().split(" ")]
    grid[i][0] = x
    grid[i][1] = y
    sum += x + y


def dp(k,row,col):
    if k < 0:
        return 0
    elif row >= n:
        return float('inf')
    elif dpGrid[k][row][col] != -1:
        return dpGrid[k][row][col]
    else:
        dpGrid[k][row][col] = min(dp(k-1,row+1,col)+grid[row][col],dp(k,row+1,0),dp(k,row+1,1))

        return dpGrid[k][row][col]

n1 = dp(k-1,0,0)
n2 = dp(k-1,0,1)
if n1 < n2:
    print(sum - n1)
else:
    print(sum-n2)