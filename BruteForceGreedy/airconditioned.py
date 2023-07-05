n = int(input())
nums = []
for i in range(n):
    line = input().split(" ")
    nums.append([int(line[0]),int(line[1])])

nums.sort()
start = nums[0][0]
end = nums[0][1]
val = nums[0][1]
count = 1
for i in range(1,n):
    if nums[i][0] < start or nums[i][0] > end:
        count += 1
        start = nums[i][0]
        end = nums[i][1]
    else:
        if nums[i][1] < end:
            end = nums[i][1]

print(count)