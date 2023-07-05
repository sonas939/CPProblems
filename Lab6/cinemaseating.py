r,c = [int(i) for i in input().split(" ")]
grid = [[False for i in range(c)]for j in range(r)]

n = int(input())
def isValid(row,col):
    if row < 0 or col < 0 or row >= r or col >= c:
        return False
    return True

for i in range(n):
    row,col = [int(j) for j in input().split(" ")]
    grid[row-1][col-1] = True

seats = [0 for i in range(9)]
for i in range(r):
    for j in range(c):
        if not grid[i][j]:
            continue
        count = 0
        if isValid(i-1,j-1):
            count += int(grid[i-1][j-1])
        if isValid(i-1,j):
            count += int(grid[i-1][j])
        if isValid(i-1,j+1):
            count += int(grid[i-1][j+1])
        if isValid(i,j-1):
            count += int(grid[i][j-1])
        if isValid(i,j+1):
            count += int(grid[i][j+1])
        if isValid(i+1,j-1):
            count += int(grid[i+1][j-1])
        if isValid(i+1,j):
            count += int(grid[i+1][j])
        if isValid(i+1,j+1):
            count += int(grid[i+1][j+1])
        seats[count] += 1

for i in range(9):
    if i == 8:
        print(seats[i])
    else:
        print(seats[i],end=" ")