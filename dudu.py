t = int(input())

def checkLoops(n, m):
    visited = [False for i in range(n+1)]
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    for i in range(1,n +1):
        arr = []
        if visited[i] == False:
            visited1 = [False for i in range(n+1)]
            visited[i] = True
            visited1[i] = True
            arr.append(i)
            while len(arr) != 0:
                k = arr.pop()
                for x in graph[k]:
                    if visited1[x] == False:
                        visited1[x] = True
                        visited[x] = True
                        arr.append(x)
                    else:
                        return "YES"
    return "NO"
                        


for i in range(t):
    n, m = map(int,input().split())
    print(checkLoops(n, m))

