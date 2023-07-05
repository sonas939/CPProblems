def isValid(i,j):
    if i < 0 or i > n+1:
        return False
    if j < 0 or j > m+1:
        return False
    return True

n,m = [int(i) for i in input().split(" ")]
grid = [[0 for i in range(m+2)]for i in range(n+2)]
visited = [[False for i in range(m+2)]for i in range(n+2)]
#fill grid
firstLand = -1
for i in range(1,n+1):
    line = input()
    for j in range(1,m+1):
        grid[i][j] = int(line[j-1])
else:
    stack = []
    stack.append((0,0))
    length = 0
    while len(stack) > 0:
        i,j = stack.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if isValid(i-1,j):
            if grid[i-1][j] == 1:
                length += 1
            else:
                if not visited[i-1][j]:
                    stack.append((i-1,j))
        if isValid(i+1,j):
            if grid[i+1][j] == 1:
                length += 1
            else:
                if not visited[i+1][j]:
                    stack.append((i+1,j))
        if isValid(i,j-1):
            if grid[i][j-1] == 1:
                length += 1
            else:
                if not visited[i][j-1]:
                    stack.append((i,j-1))
        if isValid(i,j+1):
            if grid[i][j+1] == 1:
                length += 1
            else:
                if not visited[i][j+1]:
                    stack.append((i,j+1))
    print(length)