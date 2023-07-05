line = input().split(" ")
N = int(line[0])
t = int(line[1])

A = input().split(" ")
A = [int(x) for x in A]

if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    b = A[:3]
    b.sort()
    print(b[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    sum = 0
    for i in A:
        if i % 2 == 0:
            sum += i
    print(sum)
elif t == 6:
    output = []
    for i in A:
        output.append(chr(i%26+97))
    print(''.join(output))
elif t == 7:
    index = 0
    visited = set()
    
    while index not in visited:
        visited.add(index)

        index = A[index]
        if index >= len(A):
            print("Out")
            break
        elif index == len(A) - 1:
            print("Done")
            break
        elif index in visited:
            print("Cyclic")
            break