from copy import deepcopy
import sys
sys.setrecursionlimit(100000)
def recursion(k, curPoint, flag):
    for i in range(8):
        x = k[0] + dx[i]
        y = k[1] + dy[i]
        if x in range(row) and y in range(colum):
            if matrix[x][y] == term[curPoint] and not visited[x][y]:
                visited[x][y] = True
                curPoint += 1
                if curPoint == len(term):
                    flag = 0
                    return flag
                flag = recursion([x, y], curPoint, flag)
                visited[k[0]][k[1]] = False
                curPoint = curPoint - 1
    return flag


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        row, colum = map(int, input().split())
        matrix = [[] for i in range(row)]
        A = []
        rowVisted = [False for i in range(colum)]
        visited = []
        for i in range(row):
            visited.append(deepcopy(rowVisted))
            characters = input()
            for j in range(colum):
                matrix[i].append(characters[j])
                if characters[j] == "A":
                    A.append([i, j])
        term = "ALLIZZWELL"
        curPoint = 1
        dx = [1, 1, 1, -1, -1, -1, 0, 0 ] 
        dy = [1, -1, 0, 1, -1, 0, -1, 1 ]
        flag = 1
        for k in A:
            flag = recursion(k, curPoint, flag)
        if flag == 0:
            print("YES")
        else:
            print("NO")
        print("")

