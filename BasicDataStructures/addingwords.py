import sys

dict_nums = {}
dict_names = {}
for line in sys.stdin:
    arr = line.strip()
    if arr == "":
        break
    arr = arr.split(" ")
    if arr[0] == "clear":
        dict_nums.clear()
        dict_names.clear()
    elif arr[0] == "def":
        if arr[1] in dict_names:
            dict_nums.pop(dict_names[arr[1]],None)
        dict_nums[int(arr[2])] = arr[1]
        dict_names[arr[1]] = int(arr[2])
    else:
        num = 0
        ops = []
        unknown = False
        for i in arr:
            if i == "calc":
                continue
            print(i, end = " ")
            if i == "=":
                if num not in dict_nums or unknown:
                    print("unknown")
                else:
                    print(dict_nums[num])

            if not unknown:
                if i == "-" or i == "+":
                    ops.append(i)
                else:
                    if i in dict_names:
                        if len(ops) == 0:
                            num += dict_names[i]
                        else:
                            operator = ops.pop()
                            if operator == '-':
                                num -= dict_names[i]
                            elif operator == '+':
                                num += dict_names[i]
                    else:
                        unknown = True
