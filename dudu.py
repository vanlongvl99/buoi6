def checkLoops(n, m):
    path = [[] for i in range(n+1)] 
    for i in range(m):
        a, b = map(int, input().split())
        path[b].append(a)
    for i in range(1,n +1):
        arr = [i]
        while len(arr) != 0:
            k = arr.pop()
            for x in path[k]: # duyệt tất cả các đường đi có thể đến được đỉnh i
                if x == i:      # nếu trong tất cả các đỉnh đó lại có i thì đồng nghĩa việc xuất hiện 1 loop
                    return "YES"
                arr.append(x)
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int,input().split())
        print(checkLoops(n, m))

