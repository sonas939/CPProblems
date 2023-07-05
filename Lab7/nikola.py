import sys
sys.setrecursionlimit(10**9)

n = int(input())
grid = [[float('inf') for j in range(n+1)] for i in range(n+1)]
cost = [0]
for i in range(n):
    c = int(input())
    cost.append(c)
grid[1][0] = 0

def dp(i,j):
    if i <= 0 or i >= n + 1 or j >= n+1:
        return float('inf')
    elif i == n:
        return cost[i]
    elif grid[i][j] != float('inf'):
        return grid[i][j]
    grid[i][j] = cost[i] + min(dp(i+j+1,j+1),dp(i-j,j))
    return grid[i][j]

print(dp(2,1)) 