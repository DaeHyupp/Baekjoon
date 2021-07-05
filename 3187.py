import sys
sys.setrecursionlimit(100000)

R, C = map(int, input().split(" "))
matrix = [list(input()) for _ in range(R)]
board = [[0]*C for _ in range(R)]


def dfs(r,c):
    global v, k
    board[r][c] =1
    if matrix[r][c] == 'v':
        v += 1
    if matrix[r][c] == 'k':
        k += 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<R and 0<=nc<C and matrix[nr][nc] != '#' and board[nr][nc] != 1:
            v, k = dfs(nr,nc)
    return v, k

ans_v, ans_k = 0, 0
for i in range(R):
    for j in range(C):
        if (matrix[i][j] == 'v' or matrix[i][j] == 'k') and board[i][j] != 1:
            v, k = 0, 0
            v, k=dfs(i,j)
            if v>=k:
                ans_v +=v
            else:
                ans_k +=k
print(ans_k, ans_v)

