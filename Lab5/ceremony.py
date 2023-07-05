n = int(input())
buildings = [int(i) for i in input().split(" ")]
buildings.sort()
min = n
for i in range(n):
    if buildings[i] + n - i - 1 < min:
        min = buildings[i] + n - i - 1


print(min)