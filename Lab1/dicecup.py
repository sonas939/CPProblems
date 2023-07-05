dice = input()
diceOne = int(dice.split(" ")[0])
diceTwo = int(dice.split(" ")[1])
dict = {}
for i in range(1,diceOne + diceTwo+1):
    dict[i] = 0

for i in range(1,diceOne + 1):
    for j in range(1, diceTwo + 1):
        sum = i + j
        dict[sum] += 1

arr = []
max = -1
for i in dict:
    if dict[i] > max:
        max = dict[i]
        arr = [i]
    elif dict[i] == max:
        arr.append(i)

for i in arr:
    print(i)