maxNum = int(input())
num = [0 for i in range(maxNum+1)]
maxSum = -1
for i in range(maxNum):
    for j in range(i+1,maxNum):
        sum = i * i * i + j * j * j
        if sum <= maxNum:
            num[sum] += 1
        else:
            break
        if num[sum] >= 2:
            maxSum = max(maxSum,sum)
if maxSum == -1:
    print("none")
else:
    print(maxSum)