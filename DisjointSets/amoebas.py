class Pixel:
    def __init__(self,parent,maxsize = 0):
        self.parent = parent
        self.maxsize = maxsize

grid = []
def find(i,j,numRow,numCol):
    grid[i][j] = "."
    neighbors = checkVals(i,j,numRow,numCol)
    for i in neighbors:
        find(i[0],i[1],numRow,numCol)

def checkVals(row,col,numRow,numCol):
    neighbors = []
    if numRow > 1:
        if row != 0:
            if grid[row-1][col] == "#":
                neighbors.append([row-1,col])
        if row != numRow - 1:
            if grid[row+1][col] == "#":
                neighbors.append([row+1,col])
    if numCol > 1:
        if col != 0:
            if grid[row][col-1] == "#":
                neighbors.append([row,col-1])
        if col != numCol - 1:
            if grid[row][col+1] == "#":
                neighbors.append([row,col+1])
    if numRow > 1 and numCol > 1:
        if row != 0 and col != 0:
            if grid[row-1][col-1] == "#":
                neighbors.append([row-1,col-1])
        if row != 0 and col != numCol - 1:
            if grid[row-1][col+1] == "#":
                neighbors.append([row-1,col+1])
        if row != numRow - 1 and col != 0:
            if grid[row+1][col-1] == "#":
                neighbors.append([row+1,col-1])
        if row != numRow - 1 and col != numCol -1:
            if grid[row+1][col+1] == "#":
                neighbors.append([row+1,col+1])
    return neighbors

size = input().split(" ")
numRow = int(size[0])
numCol = int(size[1])
count = 0
for i in range(numRow):
    a = list(input())
    grid.append(a)

for i in range(numRow):
    for j in range(numCol):
        if grid[i][j] == "#":
            count += 1
            find(i,j,numRow,numCol)
            

print(count)
