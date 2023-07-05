n = int(input())
grid = []
dpGrid = []
votes = {1:[2,3,5],2:[1,4,6],3:[1,4,7],4:[3,8,2],
        5:[1,6,7],6:[8,2,5],7:[8,5,3],8:[7,6,4]}

letters = {1:"NNN",2:"NNY",3:"NYN",4:"NYY",5:"YNN",6:"YNY",7:"YYN",8:"YYY"}

def dp(i,num,people):
    if i >= people+1:
        return float('inf')
    elif i == people:
        dpGrid[i][num] = grid[i][num]
        return num
    elif dpGrid[i][num] != float('inf'):
        return dpGrid[i][num]
    else:
        a = dp(i+1,votes[num][0],people)
        b = dp(i+1,votes[num][1],people)
        c = dp(i+1,votes[num][2],people)
        temp = min(grid[i+1][a],grid[i+1][b],grid[i+1][c])
        if temp == grid[i+1][a]:
            dpGrid[i][num] = a
        elif temp == grid[i+1][b]:
            dpGrid[i][num] = b
        else:
            dpGrid[i][num] = c
        return dpGrid[i][num]

for i in range(n):
    people = int(input())
    grid = [[0 for j in range(9)]]
    dpGrid = [[float('inf') for j in range(9)]for k in range(people+1)]
    for j in range(people):
        line = input().split(" ")
        positions = [0]
        for k in line:
            positions.append(int(k))
        grid.append(positions)
    print(letters[dp(0,1,people)])