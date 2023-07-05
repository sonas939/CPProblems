def main():
    
    n = int(input())
    grid = [[0 for j in range(501)] for i in range(501)]
    count = 0

    while n != 0:

        for i in range(n):

            x1, y1, x2, y2 = map(int, input().split())

            # total_area = ((x2 - x1) * (y2 - y1))

            for i in range(x1, x2):
                for j in range(y1,y2):
                    grid[i][j] = 1
        
        for i in grid:
            for j in i:
                if j == 1:
                    count += 1
        
        print(count)

        count = 0 
        grid = [[0 for j in range(501)] for i in range(501)]
        
        n = int(input())

main()