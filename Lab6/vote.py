n = int(input())
for i in range(n):
    numCand = int(input())
    sum = 0
    max = 0
    index = 0
    isEqual = False
    for i in range(numCand):
        num = int(input())
        sum += num
        if num == max:
            isEqual = True
        if num > max:
            max = num
            index = i + 1
            isEqual = False

    if isEqual:
        print("no winner")
    elif max/sum > .5:
        print("majority winner",index)
    else:
        print("minority winner", index)
