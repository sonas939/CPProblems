def main():
    N = int(input())
    string_val = ""
    # arr = []
    # bell_count = 0
    # count = 0

    # for i in range(N):
    #     val = input()
    #     arr.append(val)
    #     if val == 'O':
    #         count += 1

    # arr.reverse()

    # while (count != 0):

    #     bell_count += 1
    #     value = arr.index("O")
    #     count -= 1
    #     arr[value] = "Z"

    #     for i in range(value - 1, -1, -1):
    #         if arr[i] == "Z":
    #             arr[i] = "O"
    #             count += 1
        
    
    # print(bell_count)

    for i in range(N):
        val = input()
        if val == 'Z':
            string_val += '0'
        else:
            string_val += '1'
    
    val = int(string_val, 2)
    print(val)
    



main()