c = input()
dict = {}
repeat = False
for char in c:
    if char not in dict:
        dict[char] = 1
    else:
        print(0)
        repeat = True
        break;

if not repeat:
    print(1)