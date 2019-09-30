from queue import Queue
import sys
sys.setrecursionlimit(10000000)

def dequi(i):
    for x in graph[i]:
        if visited[x] == False:
            visited[x] = True
            dequi(x)
testCases = int(input())
for i in range(testCases):
    n = int(input())
    e = int(input())
    graph = [[] for i in range(n)]
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for i in range(n)]
    cnt = 0
    
    for i in range(n):
        if visited[i] == False:
            cnt += 1
            visited[i] = True
            dequi(i)
    print(cnt)