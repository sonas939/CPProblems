while True:
    N = input()
    if int(N) == 0:
        break

    p = 11
    #count substring of N
    sum = 0
    for char in N:
        sum += int(char)
    while True:
        product = p * int(N)
        sumProd = 0
        for char in str(product):
            sumProd += int(char)
        if sumProd == sum:
            print(p)
            break
        p += 1