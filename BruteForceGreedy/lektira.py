word = input()


length = len(word)
correct = []
for j in range(1,length):
    for k in range(j+1,length):
        seg1 = word[:j]
        seg2 = word[j:k]
        seg3 = word[k:]
        correct.append(seg1[::-1]+seg2[::-1]+seg3[::-1])

correct.sort()
print(correct[0])