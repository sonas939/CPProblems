line = input()

numPeople = int(line.split(" ")[0])
budget = int(line.split(" ")[1])
numHotels = int(line.split(" ")[2])
weeks = int(line.split(" ")[3])

minPrice = 100000000
for i in range(numHotels):
    price = int(input())
    beds = input().split(" ")
    for i in range(weeks):
        if int(beds[i]) >= numPeople:
            calc = numPeople * price
            if calc < minPrice:
                minPrice = calc
            break

if minPrice <= budget:
    print(minPrice)
else:
    print("stay home")