usrInput = input().split(" ")
n = int(usrInput[0])
m = int(usrInput[1])
sizes = []
for i in range(n):
    sizes.append(int(input()))

colors = []
for i in range(m):
    colors.append(int(input()))

sizes.sort()
colors.sort()

sizeIndex = 0
sum = 0
i = 0
while i < len(colors):
    if colors[i] > sizes[sizeIndex]:
        sizeIndex += 1
    else:
        sum += sizes[sizeIndex] - colors[i]
        i += 1
print(sum)