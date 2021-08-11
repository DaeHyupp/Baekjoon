import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int,input().rstrip().split(" "))
mat = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]
camera = []
checkboard=[[0]*M for _ in range(N)]
mina = 0

for i in range(N):
    for j in range(M):
        if 1<=mat[i][j]<=5: camera.append([i,j,mat[i][j]]);checkboard[i][j] = -2; mina+=1
        elif mat[i][j] == 6: checkboard[i][j] = -1;mina+=1

def check(r,c,direction):
    a=0
    dr = [0,1,0,-1,0,1,0,-1]
    dc = [1,0,-1,0,1,0,-1,0]
    nr = r +dr[direction]
    nc = c +dc[direction]
    while 0<=nr<=N-1 and 0<=nc<=M-1 and checkboard[nr][nc]!=-1:
        if checkboard[nr][nc] == -2:
            nr += dr[direction];nc += dc[direction]
            continue
        if checkboard[nr][nc] == 0:
            a+=1
        checkboard[nr][nc] += 1
        nr += dr[direction];nc += dc[direction]
    return a


def cctv(r,c,i,n):
    if n==1: return check(r,c,i)
    elif n==2: return check(r,c,i)+check(r,c,i+2)
    elif n==3: return check(r,c,i)+check(r,c,i+1)
    elif n==4: return check(r,c,i)+check(r,c,i+1)+check(r,c,i+2)
    else: return check(r,c,i)+check(r,c,i+1)+check(r,c,i+2)+check(r,c,i+3)
   
    
def solve():
    global checkboard
    cnt = 0
    ans = 0
    for i in product([0,1,2,3], repeat=len(camera)):
        for num,cam in enumerate(camera):
            cnt += cctv(cam[0],cam[1],i[num],cam[2])
        
        ans = max(cnt,ans)
        cnt = 0
        checkboard=[[0]*M for _ in range(N)]
        for l in range(N):
            for j in range(M):
                if 1<=mat[l][j]<=5: checkboard[l][j] = -2
                elif mat[l][j] == 6: checkboard[l][j] = -1
    return ans

print(M*N-solve()-mina)

