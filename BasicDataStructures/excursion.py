str = list(input())
dict = {'1':0,'2':0}
countOne = str[0] == '1'
countTwo = str[0] == '2'
for char in range(1,len(str)):
    if str[char] == '1':
        countOne += 1
    if str[char] == '2':
        countTwo += 1
    if int(str[char]) < int(str[char-1]) or int(str[char]) - int(str[char-1]) > 1:
        if str[char] == '0':
            dict['1'] += 1 * countOne
            dict['2'] += 1 * countTwo
        elif str[char] == '1':
            dict['2'] += 1 * countTwo
        if str[char] != '2':
            temp = str[char-1]
            str[char-1] = str[char]
            str[char] = temp

        
print(dict['1']+dict['2'])