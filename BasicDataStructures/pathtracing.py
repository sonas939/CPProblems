from sys import stdin

x, y = 0, 0
xMin, xMax, yMin, yMax = 0, 0, 0, 0
dir = [[0,0]]
for usrInput in stdin:
    if usrInput == '\n':
        break
    
    usrInput = usrInput.strip()
    if usrInput == 'down':
        y += 1
        if y > yMax:
            yMax = y
    elif usrInput == 'up':
        y -= 1
        if y < yMin:
            yMin = y
    elif usrInput == 'left':
        x -= 1
        if x < xMin:
            xMin = x
    elif usrInput == 'right':
        x += 1
        if x > xMax:
            xMax = x
    
    dir.append([x,y])

scaleX = 0
scaleY = 0
if xMin < 0:
    scaleX = 0 - xMin

if yMin < 0:
    scaleY = 0 - yMin

grid = [[' ']*(xMax-xMin+1) for i in range(yMax-yMin+1)]

for i in range(len(dir)):
    x = dir[i][0] + scaleX
    y = dir[i][1] + scaleY
    if i == 0:
        grid[y][x] = "S"
    elif i == len(dir) - 1:
        grid[y][x] = "E"
    elif grid[y][x] == ' ':
        grid[y][x] = "*"

border = ['#'] * (xMax-xMin+3)
print(''.join(border))
for row in grid:
    print('#',sep='',end='')
    for col in row:
        print(col,sep='',end='')
    print('#')
print(''.join(border))