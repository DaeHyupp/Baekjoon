import sys
sys.setrecursionlimit(1000000)
N, M = map(int, input().split(" "))
matrix = [list(map(int, input().split(" "))) for _ in range(N)]

def dfs_out(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    matrix[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny< M and matrix[nx][ny] ==0:
            dfs_out(nx,ny)
            
def melting_cheese(x,y):
    global cheese
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    if matrix[x][y] == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if matrix[nx][ny] == -1:
                cnt += 1
    if cnt >=2:
        matrix[x][y] = 2
        cheese.append([x,y])


time = 0
dfs_out(0,0)
cheese = []
while 1:
    time += 1
    for i in range(1,N):
        for j in range(1,M):
            melting_cheese(i,j)
    if len(cheese) == 0:
        time = time -1
        break
    while len(cheese)!=0:
        _x, _y = cheese.pop(0)
        dfs_out(_x,_y)


print(time)
            

