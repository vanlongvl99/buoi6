# dist = 
def dfs(n):
    cnt = [0]*(n+1)
    visited = [False for i in range(n + 1)]
    # path = [-1 for i in range(n + 1)]
    graph = [[] for i in range(n+1)]
    for i in range(n -1):
        first, second = map(int,input().split())
        graph[first].append(second)
        graph[second].append(first)
    visited[1] = True
    stack = []
    stack.append(1)
    while len(stack) != 0:
        u = stack.pop()
        for x in graph[u]:
            if visited[x] == False:
                cnt[x] = cnt[u] + 1
                visited[x] = True
                stack.append(x)
    return cnt
if __name__ == "__main__":
    n = int(input())
    cnt = dfs(n)
    q = int(input())
    girls = [n]*(n+1)
    for i in range(q):
        numOfGirl = int(input())
        girls[numOfGirl] = cnt[numOfGirl]
    minDis = min(girls)
    result = n
    for i in range(len(girls)):
        if girls[i] == minDis:
            result = min(result, i)
    print(result)