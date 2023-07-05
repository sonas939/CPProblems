while True:
    n = int(input())
    if n == 0:
        break
    
    binary = str(bin(n-1))[2:]

    power = 1
    count = 0
    print("{ ", end="")
    for i in reversed(binary):
        num = int(i) * power
        if num != 0:
            if count == len(binary) - 1:
                print(int(num),end=" ")
            else:
                print(int(num), end = ", ")
        power *= 3
        count += 1
    
    print("}")