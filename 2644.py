N = int(input())
start, end = map(int,input().split(' '))
M = int(input())
matrix = [[] for i in range(N+1)]

for i in range(M):
    pa, ch = map(int, input().split(' '))
    matrix[pa].append(ch)
    matrix[ch].append(pa)


counter = [-1] *(N+1)
counter[start]=0

def dfs(curr):
    global matrix, counter
    for dest in matrix[curr]:
        if counter[dest] == -1:
            counter[dest] = counter[curr]+1
            dfs(dest)

dfs(start)

if(counter[end] == -1):
    print(-1)
else:
    print(abs(counter[start]-counter[end]))

