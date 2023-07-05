line = input().split(" ")
while line[0] != "0":
    num1 = [int(line[0]),int(line[1])]
    num2 = [int(line[2]),int(line[3])]
    num1.sort(reverse=True)
    num2.sort(reverse=True)
    s0,s1 = num1
    r0,r1 = num2
    if num1 == [2,1] and num2 == [2,1]:
        print("Tie.")
    elif num1 == [2,1]:
        print("Player 1 wins.")
    elif num2 == [2,1]:
        print("Player 2 wins.")
    elif s0 == s1 and r0 == r1:
        if s0 == r0:
            print("Tie.")
        elif s0 > r0:
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")
    elif s0 == s1:
        print("Player 1 wins.")
    elif r0 == r1:
        print("Player 2 wins.")
    else:
        if s0 > r0:
            print("Player 1 wins.")
        elif r0 > s0:
            print("Player 2 wins.")
        elif s1 > r1:
            print("Player 1 wins.")
        elif r1 > s1:
            print("Player 2 wins.")
        else:
            print("Tie.")
    line = input().split(" ")