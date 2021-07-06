R, C = map(int, input().split(" "))
matrix = [list(map(int,input().split(" "))) for i in range(R)]
dfsboard = [[0]*C for _ in range(R)]
one = 0
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 1:
            one += 1
checkboard = [0]*(C*R)
len_check = len(checkboard)

min_two = C*R

def dfs(r, c):
    global cnt
    dfsboard[r][c] = 1
    cnt += 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        nr = r+dr[i]
        nc = c +dc[i]
        if 0<=nr<R and 0<=nc<C and dfsboard[nr][nc] !=1 and (matrix[nr][nc] ==0 or matrix[nr][nc] ==2):
            cnt = dfs(nr,nc)
    return cnt

for i in range(0,len_check-2):
    if matrix[int(i/C)][int(i%C)] == 0:
        matrix[int(i/C)][int(i%C)] = 1
    else : continue

    for j in range(i,len_check-1):
        if matrix[int(j/C)][int(j%C)] == 0:
            matrix[int(j/C)][int(j%C)] = 1
        else : continue
        
        for k in range(j,len_check):
            if matrix[int(k/C)][int(k%C)] == 0:
                matrix[int(k/C)][int(k%C)] = 1
            else : continue
            
            twomin = 0
            for p in range(R):
                for q in range(C):
                    if matrix[p][q] == 2 and dfsboard[p][q] != 1:
                        cnt = 0
                        twomin += dfs(p,q)
                        
                       
            if min_two>=twomin:
                min_two = twomin
            dfsboard = [[0]*C for _ in range(R)]
                        

                            
            matrix[int(k/C)][int(k%C)] = 0
        matrix[int(j/C)][int(j%C)] = 0
    matrix[int(i/C)][int(i%C)] = 0

ans = C*R-min_two-one-3
if ans >= 0:
    print(ans)
else:
    print(0)


    

