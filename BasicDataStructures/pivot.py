n = int(input())
nums = input().split(" ")
nums = [int(i) for i in nums]

count = 0
max = nums[0]
maxArr = [nums[0]]
min = nums[len(nums)-1]
minArr = [min]
#first calculate max
b = len(nums) - 2
for a in range(1,len(nums)):
    if nums[a] > max:
        max = nums[a]
    if nums[b] < min:
        min = nums[b]
    maxArr.append(max)
    minArr.append(min)
    b -= 1

b = len(nums) - 1
for a in range(0,len(nums)):
    if nums[a] >= maxArr[a] and nums[a] <= minArr[b]:
        count += 1
    b -= 1

print(count)