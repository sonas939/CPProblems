n = int(input())

availMoney = 100
bought = 0
stock = []
if n == 1:
    print(100)
else:
    for i in range(n):
        stock.append(int(input()))

    for i in range(n - 1):
        if stock[i] < stock[i+1]:
            if bought >= 100000:
                continue
            nStock = availMoney//stock[i]
            if nStock + bought > 100000:
                nStock = 100000 - bought
            if nStock != 0:
                availMoney -= nStock * stock[i]
                bought += nStock
        else:
            availMoney += stock[i] * bought
            bought = 0
    availMoney += stock[n-1] * bought
    print(availMoney)
    