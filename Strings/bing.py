n = int(input())
dict = {}
for i in range(n):
    s = input()
    for j in range(1,len(s)+1):
        if s[:j] in dict:
            dict[s[:j]] += 1
        else:
            dict[s[:j]] = 1
    print(dict[s]-1)