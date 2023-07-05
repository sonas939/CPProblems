nWords,nJobs = [int(i) for i in input().split(" ")]

dict = {}
for i in range(nWords):
    line = input().split(" ")
    dict[line[0]] = int(line[1])

for i in range(nJobs):
    sum = 0
    line = [""]
    while line[0] != ".":
        line = input().split(" ")
        for i in line:
            if i in dict:
                sum += dict[i]
    print(sum)