t = int(input())
for testcase in range(t):
    dictIngred = {}
    dictEnglish = {}
    m = int(input())
    for i in range(m):
        input() # pizza name do not need
        forIngred = input().split(" ")
        ingred = input().split(" ")
        for j in range(1,len(forIngred)):
            if forIngred[j] not in dictIngred:
                dictIngred[forIngred[j]] = ingred[1:]
            else:
                length = len(dictIngred[forIngred[j]])
                k = 0
                while k < length:
                    if dictIngred[forIngred[j]][k] not in ingred:
                        dictIngred[forIngred[j]].remove(dictIngred[forIngred[j]][k])
                        k -= 1
                        length -= 1
                    k += 1
        for j in range(1,len(ingred)):
            if ingred[j] not in dictEnglish:
                dictEnglish[ingred[j]] = forIngred[1:]
            else:
                length = len(dictEnglish[ingred[j]])
                k = 0
                while k < length:
                    if dictEnglish[ingred[j]][k] not in forIngred:
                        dictEnglish[ingred[j]].remove(dictEnglish[ingred[j]][k])
                        k -= 1
                        length -= 1
                    k += 1
    for x in dictIngred:
        dictIngred[x].sort()
    dictIngred = dict(sorted(dictIngred.items()))
    for j in dictIngred:
        for k in dictIngred[j]:
            if j in dictEnglish[k]:
                print("({}, {})".format(j,k))

    if testcase != t - 1:
        print()
