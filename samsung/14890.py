import sys
input = sys.stdin.readline

N, L = map(int,input().rstrip().split(" "))
mat = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]

def solve_row(r):
    board = [0]*N
    start = mat[r][0]
    i=0
    while i!=N:
        if start == mat[r][i]:i+=1;continue
        elif abs(start-mat[r][i])>1:return 0
        else:
            if start>mat[r][i]:
                check = mat[r][i]
                if i+L-1>=N:return 0
                else:
                    for j in range(i,i+L):
                        if check != mat[r][j] or board[j] == 1:return 0
                    for j in range(i,i+L):
                        board[j]=1
                    start = mat[r][i+L-1]
                    i+=1
                    continue
            else:
                check = mat[r][i-1]
                if i-L<0:return 0
                else:
                    for j in range(i-1,i-L-1,-1):
                        if check != mat[r][j] or board[j]==1:return 0
                    for j in range(i-1,i-L-1,-1):
                        board[j]=1
                    start = mat[r][i]
                    i+=1
                    continue
    return 1

def solve_col(c):
    board = [0]*N
    start = mat[0][c]
    i=0
    while i!=N:
        if start == mat[i][c]:i+=1;continue
        elif abs(start-mat[i][c])>1:return 0
        else:
            if start>mat[i][c]:
                check = mat[i][c]
                if i+L-1>=N:return 0
                else:
                    for j in range(i,i+L):
                        if check != mat[j][c] or board[j] == 1:return 0
                    for j in range(i,i+L):
                        board[j]=1
                    start = mat[i+L-1][c]
                    i+=1
                    continue
            else:
                check = mat[i-1][c]
                if i-L<0:return 0
                else:
                    for j in range(i-1,i-L-1,-1):
                        if check != mat[j][c] or board[j]==1:return 0
                    for j in range(i-1,i-L-1,-1):
                        board[j]=1
                    start = mat[i][c]
                    i+=1
                    continue
    return 1

cnt = 0
for i in range(N):
    cnt += solve_row(i)
    cnt += solve_col(i)

print(cnt)

