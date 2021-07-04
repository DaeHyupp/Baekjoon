import sys
sys.setrecursionlimit(100000)
M, N, K = map(int, input().split(" "))
coord = [list(map(int,input().split(" "))) for _ in range(K)]
matrix = [[0]*N for _ in range(M)]
for i in range(K):
    for y in range(coord[i][1], coord[i][3]):
        for x in range(coord[i][0], coord[i][2]):
            matrix[y][x] = 1

def dfs(y,x):
    cnt = 0
    if matrix[y][x] ==1: return 0
    if matrix[y][x] ==0:
        matrix[y][x] = -1
        cnt +=1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if matrix[ny][nx] == 0:
                    cnt += dfs(ny,nx)

    return cnt

answers = []
for i in range(M):
    for j in range(N):
        ans=dfs(i,j)
        if ans>=1:
            answers.append(ans)

print(len(answers))

for i in range(len(answers)-1):
    for j in range(len(answers)-i-1):
        if answers[j]>= answers[j+1]:
            tmp = answers[j]
            answers[j] = answers[j+1]
            answers[j+1] = tmp

while len(answers)!=0:
    print(answers.pop(0), end=" ")

