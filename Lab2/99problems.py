num = int(input())

remain = num % 100

if num < 100:
    print(99)
elif remain < 49:
    print(num-remain-1)
else:
    print(num+99-remain)