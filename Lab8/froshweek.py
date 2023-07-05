n = int(input())

tree = [0 for i in range(n+1)]

def sum(index):
    sum = 0
    while index > 0:
        sum += tree[index]
        index -= index & -index
    return sum

def update(index,num):
    while index < len(tree):
        tree[index] += num
        index += index & -index

count = 0
swaps = 0
nums = []
order = []
for i in range(n):
    num = int(input())
    nums.append(num)
    order.append(num)
nums.sort()
dict = {}
for i in range(1,n+1):
    dict[nums[i-1]] = i

count = 0
for i in order:
    a = dict[i]
    update(a,1)
    swaps += count - sum(a-1)
    count += 1

print(swaps)