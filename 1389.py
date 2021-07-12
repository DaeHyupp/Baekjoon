import sys
input = sys.stdin.readline

N, M = map(int,input().split(" "))
mat = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    mat[a].append(b)
    mat[b].append(a)
for i in range(N+1):
    mat[i] = list(set(mat[i]))

def bfs():
    global cnt, ans
    while q:
        iteration=len(q)
        cnt += 1
        for _ in range(iteration):
            start = q.pop(0)
   
        
            for dest in mat[start]:
                if check[dest] == 0:
                    check[dest] = 1
                    ans += cnt
                    q.append(dest)
real = []
for i in range(1,N+1):
    cnt = 0
    ans = 0
    check = [0]*(N+1)
    check[i] = 1
    q = []
    q.append(i)
    bfs()
    real.append([i,ans])
real = sorted(real,key=lambda x:x[0])
real = sorted(real,key=lambda x:x[1])
print(real[0][0])

