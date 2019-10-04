from queue import Queue
from copy import deepcopy   

def checkLakes(q, visited):
    q[0] = (i,j)
    left = right = 0
    while left <= right:
        x, y = q[left]
        for k in range(4):
            r = x + dx[k]
            l = y + dy[k]
            if r in range(n) and l in range(m):
                if maxtrix[r][l] == 1 and not visited[r][l]:
                    visited[r][l] = True
                    right += 1
                    q[right] = (r,l)
        left += 1

if __name__ == "__main__":
    n, m , k = map(int, input().split())
    maxtrix = [[] for i in range(n)]
    rowVisited = [False for i in range(m)]
    visited = [deepcopy(rowVisited) for i in range(n)]
    for i in range(n):
        row = input()
        for x in row:
            if x == "*":
                maxtrix[i].append(0)
            else:
                maxtrix[i].append(1)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = [None]*(50*50+1)
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maxtrix[i][j] == 1 and (i ==0 or j == 0 or i == n - 1 or j == m -1):
                visited[i][j] = True
                checkLakes(q, visited)   
    amoutLakes = [[] for i in range(50*50+1)]
    count = 0
    for i in range(n):
        for j in range(m):
            if maxtrix[i][j] == 1 and not visited[i][j]:
                q = [None]*(50*50+1)
                cnt = 1
                locations = []
                visited[i][j] = True
                locations.append([i, j])
                q[0] = (i,j)
                left = right = 0
                while left <= right:
                    x, y = q[left]
                    for z in range(4):
                        r = x + dx[z]
                        l = y + dy[z]
                        if r in range(n) and l in range(m):
                            if maxtrix[r][l] == 1 and not visited[r][l]:
                                visited[r][l] = True
                                cnt += 1
                                locations.append([r, l])
                                right += 1
                                q[right] = (r,l)
                    left += 1
                amoutLakes[cnt].append(locations)
                count += 1
    amoutCells = 0
    for i in range(len(amoutLakes)):
        if len(amoutLakes[i]) !=0 :
            for x in amoutLakes[i]:
                if count > k:
                    count = count -1
                    for z in x:
                        amoutCells += 1
                        maxtrix[z[0]][z[1]] = 0
                else:
                    break
    print(amoutCells)
    for i in range(len(maxtrix)):
        for x in (maxtrix[i]):
            if x == 1:
                print(".",end="")
            else:
                print("*",end="")
        print("")

                
    

    