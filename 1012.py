import sys
sys.setrecursionlimit(1000000)
def dfs(r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    board[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<R and 0<=nc<C and matrix[nr][nc] ==1 and board[nr][nc] == 0:
            dfs(nr,nc)
    return

I = int(input())

for _ in range(I):
    R, C, L = map(int,input().split(" "))
    matrix = [[0]*C for j in range(R)]
    board = [[0]*C for j in range(R)]
    for j in range(L):
        r, c = map(int,input().split(" "))
        matrix[r][c] = 1
    cnt = 0
    for p in range(R):
        for q in range(C):
            if matrix[p][q] == 1 and board[p][q] == 0:
                dfs(p, q)
                cnt += 1
    print(cnt)


