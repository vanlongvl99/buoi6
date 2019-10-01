
def recursion(i, visited, graph,fakeVisited, count):
    count += 1
    for x in graph[i]:
        if fakeVisited[x] == False:
            fakeVisited[x] = True
            visited[x] = True
            count = recursion(x, visited, graph, fakeVisited, count)
    return count
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    maxImpact = 0
    visited = [False for i in range(n+1)]
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            fakeVisited = [False for j in range(n+1)]
            fakeVisited[i] = True
            count = 0
            count = recursion(i, visited, graph, fakeVisited, count)
            maxImpact = max(maxImpact, count)
    print(maxImpact)
