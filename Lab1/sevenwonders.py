cards = input()
dict = {'T':0, 'C':0, 'G':0}
#sum up points
for char in cards:
    dict[char] += 1

sum = 0
min = dict['T']
for i in dict:
    sum += dict[i] * dict[i]
    if dict[i] < min:
        min = dict[i]

sum += min * 7
print(sum)   
        