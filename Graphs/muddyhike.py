from queue import PriorityQueue
def isValid(x,y):
    if x < 0 or y < 0:
        return False
    if x == numRow or y == numCol:
        return False
    return True

numRow,numCol = [int(i) for i in input().split(" ")]
grid = []
for i in range(numRow):
    grid.append([int(i) for i in input().split(" ")])

visited = [[float('inf') for j in range(numCol)] for k in range(numRow)]
q = PriorityQueue()
for i in range(numRow):
    visited[i][0] = grid[i][0]
    q.put((visited[i][0],i,0))

totMin = float('inf')
while not q.empty():
    val,row,col =  q.get()
    if val > visited[row][col]:
        continue
    if col == numCol-1:
        totMin = min(totMin,val)
    if isValid(row-1,col):
        if visited[row-1][col] > max(visited[row][col],grid[row-1][col]):
            visited[row-1][col] = max(visited[row][col],grid[row-1][col])
            q.put((visited[row-1][col],row-1,col))
    if isValid(row+1,col):
        if visited[row+1][col] > max(visited[row][col],grid[row+1][col]):
            visited[row+1][col] = max(visited[row][col],grid[row+1][col])
            q.put((visited[row+1][col],row+1,col))
    if isValid(row,col-1):
        if visited[row][col-1] > max(visited[row][col],grid[row][col-1]):
            visited[row][col-1] = max(visited[row][col],grid[row][col-1])
            q.put((visited[row][col-1],row,col-1))
    if isValid(row,col+1):
        if visited[row][col+1] > max(visited[row][col],grid[row][col+1]):
            visited[row][col+1] = max(visited[row][col],grid[row][col+1])
            q.put((visited[row][col+1],row,col+1))

print(totMin)