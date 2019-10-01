n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
maxImpact = 0
visited = [False for i in range(n+1)]


def recursion(i, visited, graph,visit1, count):
    count += 1
    for x in graph[i]:
        if visit1[x] == False:
            visit1[x] = True
            visited[x] = True
            count = recursion(x, visited, graph, visit1, count)
    return count

for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        visit1 = [False for j in range(n+1)]
        visit1[i] = True
        count = 0
        count = recursion(i, visited, graph, visit1, count)
        maxImpact = max(maxImpact, count)
                
print(maxImpact)
