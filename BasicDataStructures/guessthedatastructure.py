from queue import PriorityQueue
import sys
for line in sys.stdin:
    if line.strip() == "":
        break
    num = int(line.strip())
    isQueue = True
    isPQ = True
    isStack = True
    stack = []
    queue = []
    pq = PriorityQueue()
    for i in range(num):
        ops = input().split(" ")
        if ops[0] == "1":
            stack.append(int(ops[1]))
            queue.append(int(ops[1]))
            pq.put((-int(ops[1]),int(ops[1])))
        else:
            if len(stack) <= 0:
                isPQ = False
                isQueue = False
                isStack = False
                continue
            num = int(ops[1])
            if num != pq.queue[0][1]:
                isPQ = False
            else:
                pq.get()
            if num != stack[len(stack)-1]:
                isStack = False
            else:
                stack.pop()
            if num != queue[0]:
                isQueue = False
            else:
                queue.pop(0)
    
    if not isQueue and not isStack and not isPQ:
        print("impossible")
    elif isQueue and isStack or isQueue and isPQ or isStack and isPQ:
        print("not sure")
    elif isQueue:
        print("queue")
    elif isStack:
        print("stack")
    else:
        print("priority queue")
    



