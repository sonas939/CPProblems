n = int(input())
str = bin(n)[2:]
print(int(str[::-1],2))