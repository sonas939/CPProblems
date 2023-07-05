line = input()
firstSeat = line[0]
people = line[1:]

up = people.count('D') * 2
down = people.count('U') * 2
preference = 0
if firstSeat == 'U' and people[0] == 'U':
    down -= 1
elif firstSeat == 'U' and people[0] == 'D':
    down += 1
elif firstSeat == 'D' and people[0] == 'D':
    up -= 1
elif firstSeat == 'D' and people[0] == 'U':
    up += 1

for i in range(len(line)-1):
    if line[i] != line[i+1]:
        preference += 1

print(up)
print(down)
print(preference)
