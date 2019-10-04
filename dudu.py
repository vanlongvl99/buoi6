
import sys
sys.setrecursionlimit(1000000)

def recursion(k, path, flag, visited):
    visited[k] = True
    for x in path[k]:
        if visited[x] == True:
            flag = 0
        elif visited[x] == False:
            flag = recursion(x, path, flag, visited) 
    
    visited[k] = None
    return flag

def checkLoops(n, m):
    path = [[] for i in range(n+1)] 
    for i in range(m):
        a, b = map(int, input().split())
        path[b].append(a)
    flag = 1
    visited = [False for i in range(n+1)]
    for i in range(1,n +1):
        if visited[i] == False:
            flag = recursion(i, path, flag, visited)
            # print(i)
            if flag == 0:
                return "YES"
    return"NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int,input().split())
        print(checkLoops(n, m))

