n = int(input())
nums = input().split(" ")
nums = [int(i) for i in nums]
nums.sort(reverse=True)
totDays = nums[0]
maxDays = nums[0] - 1
nums.pop(0)
for i in range(n-1):
    if nums[0] > maxDays:
        totDays += nums[0] - maxDays
        maxDays = nums[0]
    nums.pop(0)
    maxDays -= 1
print(totDays+2)