n = int(input())
max = 1
count_list = {}
num_instances = 0
for i in range(n):
    l = input().split(" ")
    l = [int(i) for i in l]
    l.sort()
    tup = tuple(l)
    if tup in count_list:
        count_list[tup] += 1
        if count_list[tup] > max:
            max = count_list[tup]
            num_instances = 1
        elif count_list[tup] == max:
            num_instances += 1
    else:
        count_list[tup] = 1

if max == 1:
    print(n)
else:
    print(max * num_instances)

