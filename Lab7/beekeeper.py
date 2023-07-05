n = int(input())
vowels = ['a','e','i','o','u','y']

while n != 0:
    max = 0
    maxWord = ""
    for i in range(n):
        word = input()
        count = 0
        i = 0
        while i < len(word) - 1:
            if word[i] in vowels:
                if word[i+1] == word[i]:
                    count += 1
                    i += 1
            i += 1
                
        if count >= max:
            max = count
            maxWord = word
    print(maxWord)
    n = int(input())