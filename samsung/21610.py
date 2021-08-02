import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))
mat = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1): mat[i] = [0]+list(map(int,input().rstrip().split(" ")))
moves = deque([list(map(int,input().rstrip().split(" "))) for _ in range(M)])
clouds = deque([[N,1],[N,2],[N-1,1],[N-1,2]])
checkboard=[[0]*(N+1) for _ in range(N+1)]
def cloudmove():
    dr = [0,0,-1,-1,-1,0,1,1,1] #cross point : 2,4,6,8
    dc = [0,-1,-1,0,1,1,1,0,-1]
    while moves:
        global clouds
        iteration = len(clouds)
        d,s = moves.popleft()
        nocloudzone = deque([])
        for i in range(iteration):
            nr,nc = clouds.popleft()
            
            nr += s * dr[d]
            nc += s * dc[d]
            while 1:
                if 1<=nr<=N and 1<=nc<=N: break
                if nr>N:nr -=N
                if nc>N:nc -=N
                if nr<1:nr +=N
                if nc<1:nc +=N
            nocloudzone.append([nr,nc])
            mat[nr][nc] += 1
        
        for r,c in nocloudzone:
            a = 2
            for _ in range(4):
                check_r = r+dr[a]
                check_c = c+dc[a]
                if 1<=check_r<=N and 1<=check_c<=N:
                    if mat[check_r][check_c]: mat[r][c]+=1
                a+=2
            checkboard[r][c] = 1
    
        for i in range(1,N+1):
            for j in range(1,N+1):
                if checkboard[i][j] == 1:
                    checkboard[i][j]=0
                    continue
                if mat[i][j] >=2:
                    clouds.append([i,j])
                    mat[i][j] -=2
cloudmove()
ans = 0
for i in range(N+1):
    ans+=sum(mat[i]) 
print(ans)

