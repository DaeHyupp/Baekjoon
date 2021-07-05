R, C = map(int,input().split(" "))
matrix = [list(input()) for _ in range(R)]
board=[[0]*C for _ in range(R)]

def short_dfs(y, x):
    board[y][x]=1
    a=0
    if x == C-1: return 1
    dx = [ 1, 1, 1]
    dy = [-1, 0, 1]

    for i in range(3):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<=nx<C and 0<=ny<R and board[ny][nx]!=1 and matrix[ny][nx] != 'x':
            if short_dfs(ny,nx) == 1:
                return 1
    return 0


cnt = 0
for i in range(R):
    if short_dfs(i,0) ==1:
        cnt +=1
print(cnt)

