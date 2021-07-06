N = int(input())
E = int(input())
graph= [[] for i in range(N+1)]
for i in range(E):
    a, b = map(int,input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
board = [0]*(N+1)
q = []
q.append(1)
board[1] = 1
def bfs():
    global cnt
    while q:
        node=q.pop(0)
        for i,n in enumerate(graph[node]):
            if board[n] != 1:
                q.append(n)
                board[n] = 1
                cnt +=1
    return cnt
cnt = 0
print(bfs())

