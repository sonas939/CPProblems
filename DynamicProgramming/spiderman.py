import sys
sys.setrecursionlimit(10**9)
n = int(input())

def dp(grid,dpGrid,nums,k,sumNums):
    for i in range(1,k): #already filled in first level
        for j in range(sumNums):
            if grid[i-1][j] != float('inf'):
                if nums[i] <= j:
                    if grid[i][j-nums[i]] > grid[i-1][j]:
                        grid[i][j-nums[i]] = grid[i-1][j]
                        dpGrid[i][j-nums[i]] = 'D'
                    
                    if grid[i][j+nums[i]] == float('inf'):
                        grid[i][j+nums[i]] = max(j+nums[i],grid[i-1][j])
                        dpGrid[i][j+nums[i]] = 'U'
                    elif j + nums[i] > grid[i-1][j]:
                        if grid[i][j+nums[i]] > j + nums[i]:
                            grid[i][j+nums[i]] = j + nums[i]
                            dpGrid[i][j+nums[i]] = 'U' 
                    else:
                        if grid[i][j+nums[i]] > grid[i-1][j]:
                            grid[i][j+nums[i]] = grid[i-1][j]
                            dpGrid[i][j+nums[i]] = 'U'
                else:
                    if grid[i][j+nums[i]] == float('inf'):
                        grid[i][j+nums[i]] = max(j+nums[i],grid[i-1][j])
                        dpGrid[i][j+nums[i]] = 'U'
                    elif j + nums[i] > grid[i-1][j]:
                        if grid[i][j+nums[i]] > j + nums[i]:
                            grid[i][j+nums[i]] = j + nums[i]
                            dpGrid[i][j+nums[i]] = 'U' 
                    else:
                        if grid[i][j+nums[i]] > grid[i-1][j]:
                            grid[i][j+nums[i]] = grid[i-1][j]
                            dpGrid[i][j+nums[i]] = 'U'
                

for i in range(n):
    k = int(input())
    nums = [int(i) for i in input().split(" ")]
    sumNums = sum(nums) + 1
    grid = [[float('inf') for j in range(sumNums)]for h in range(k)]
    dpGrid = [['' for j in range(sumNums)]for h in range(k)]
    grid[0][nums[0]] = nums[0]
    dpGrid[0][0] = 'U'
    dp(grid,dpGrid,nums,k,sumNums)
    if k == 1:
        print("IMPOSSIBLE")
    elif dpGrid[k-1][0] == '':
        print("IMPOSSIBLE")
    else:
        j = k - 1
        dist = 0
        s = ''
        while j >= 0:
            if dpGrid[j][dist] == 'D':
                dist += nums[j]
                s += 'D'
            else:
                dist -= nums[j]
                s += 'U'
            j -= 1
        print(s[::-1])
