n = int(input())
arr = input()
arr = arr.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()

while len(arr) != 0:
    count = 0
    if (len(arr) != 1):
        while (arr[count] + 1 == arr[count+1]):
            count += 1
            if count == len(arr)-1:
                break

    if (count >= 2):
        sent = str(arr[0]) + "-" + str(arr[count])
        print(sent,end=" ")
        if count < len(arr):
            arr = arr[count+1:]
    else:
        print(arr[0],end=" ")
        arr.remove(arr[0])