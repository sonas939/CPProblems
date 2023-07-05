import sys
sys.setrecursionlimit(10**9)

class node:
    def __init__(self):
        self.end = False
        self.ch = [None for i in range(26)]
    
    def add(self,s):
        if len(s) == 0:
            self.end = True
            return
        c = s[0]
        if self.ch[ord(c)-ord('A')] == None:
            self.ch[ord(c)-ord('A')] = node()
        s2 = s[1:]
        self.ch[ord(c)-ord('A')].add(s2)

def isValid(i,j):
    if i < 0 or j < 0: 
        return False
    if i > 3 or j > 3:
        return False
    return True

def search(root,x,y,s,words=set()):
    if root.end:
        words.add(s)
    px = [0,0,1,1,1,-1,-1,-1]
    py = [-1,1,0,1,-1,1,0,-1]

    for i in range(26):
        visited[x][y] = True
        if root.ch[i] is not None:
            c = chr(i+ord('A'))
            for j in range(8):
                if isValid(x+px[j],y+py[j]):
                    if not visited[x+px[j]][y+py[j]] and b[x+px[j]][y+py[j]] == c:
                        search(root.ch[i],x+px[j],y+py[j],s+c,words)
            visited[x][y] = False
    
    visited[x][y] = False

n = int(input())

dict = []
root = node()
for i in range(n):
    dict.append(input())
    root.add(dict[-1])

#root.printout() TESTING TRIE

input()

numB = int(input())
for i in range(numB):
    b = []
    for j in range(4):
        b.append(input())
    words = set()
    for j in range(4):
        for k in range(4):
            if root.ch[ord(b[j][k])-ord('A')] is not None:
                visited = [[False for j in range(4)] for k in range(4)]
                search(root.ch[ord(b[j][k])-ord('A')],j,k,b[j][k],words)

    maxLen = 0
    maxWord = ""
    point = 0
    for j in words:
        length = len(j)
        if length == maxLen:
            if j < maxWord:
                maxWord = j
        elif length > maxLen:
            maxLen = length
            maxWord = j

        if length == 3 or length == 4:
            point += 1
        elif length == 5:
            point += 2
        elif length == 6:
            point += 3
        elif length == 7:
            point += 5
        elif length == 8:
            point += 11
    print("{} {} {}".format(point,maxWord,len(words)))
    if i != numB - 1:
        input()