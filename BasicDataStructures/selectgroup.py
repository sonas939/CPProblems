import sys

vals = {}
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    line = line.split(" ")
    if line[0] == "group":
        vals[line[1]] = set([i for i in line[3:]])
    else:
        stack = []
        for i in reversed(line):
            if i == "union" or i == "intersection" or i == "difference":
                set1 = stack.pop()
                set2 = stack.pop()
                if i == "union":
                    stack.append(set1.union(set2))
                elif i == "intersection":
                    stack.append(set1.intersection(set2))
                elif i == "difference":
                    stack.append(set1.difference(set2))
            else:
                if str(i) in vals:
                    stack.append(vals[i])
                else:
                    stack.append(i)
        if str(stack[0]) in vals:
            newList = list(vals[stack[0]])
            newList.sort()
        else:
            newList = list(stack[0])
            newList.sort()
        for j in range(len(newList)):
            if j == len(newList) - 1:
                print(newList[j])
            else:
                print(newList[j], end = " ")
