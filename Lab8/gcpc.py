te,events = [int(i) for i in input().split(" ")]
teams = [[0,0] for i in range(te+1)]
isabove = [False for i in range(te+1)]
above = []
score = [0,0]
for i in range(events):
    t,p = [int(i) for i in input().split(" ")]
    if t == 1:
        score[0] += 1
        score[1] += p
        length = len(above)
        index = 0
        while index < length:
            num = above[index]
            if teams[num][0] == score[0]:
                if teams[num][1] >= score[1]:
                    above.remove(num)
                    isabove[num] = False
                    index -= 1
                    length -= 1
            elif score[0] > teams[num][0]:
                above.remove(num)
                isabove[num] = False
                index -= 1
                length -= 1
            index += 1
    else:
        teams[t][0] += 1
        teams[t][1] += p
        if not isabove[t]:
            if teams[t][0] == score[0]:
                if teams[t][1] < score[1]:
                    above.append(t)
                    isabove[t] = True
            elif teams[t][0] > score[0]:
                above.append(t)
                isabove[t] = True
    
    print(len(above)+1)