line = input().split(" ")
n = int(line[0])
queries = int(line[1])
list = [i for i in range(n+1)]
count = [1 for i in range(n+1)]
def find(x):
    if list[x] != x:
        list[x] = find(list[x])
        return list[x]
    else:
        return x

for i in range(queries):
    line = input().split(" ")
    if line[0] == "s":
        num = int(line[1])
        parent = find(num)
        print(count[parent])
    else:
        num1 = int(line[1])
        num2 = int(line[2])
        parent1 = find(num1)
        parent2 = find(num2)
        if parent1 == parent2:
            continue
        elif count[parent1] > count[parent2]:
            list[parent2] = parent1
            count[parent1] += count[parent2]
        else:
            list[parent1] = parent2
            count[parent2] += count[parent1]