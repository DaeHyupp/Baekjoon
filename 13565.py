import sys
sys.setrecursionlimit(1000000)
R, C = map(int,input().split(" "))
matrix = [list(map(int,list(input()))) for _ in range(R)]
check = [[0]*C for _ in range(R)]


def dfs(r,c):
    if r == R-1: return 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    check[r][c]=1
    
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr <R and 0<=nc<C and matrix[nr][nc] ==0 and check[nr][nc] == 0:
            if dfs(nr,nc) ==1:
                return 1
    return 0

cnt = 0
count =0
for i in range(C):
    cnt = dfs(0,i)
    if cnt !=0: break

if cnt ==0: print("NO")
else : print("YES")

