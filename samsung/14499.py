import sys
from collections import deque
input = sys.stdin.readline

N, M, r, c, K = map(int,input().rstrip().split(" "))
mat = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]
order = deque(list(map(int,input().rstrip().split(" "))))
dice = [0]*6 

def dice_move(i):
    tmp = dice[5]
    if i==1:dice[5] = dice[3];dice[3] = dice[2];dice[2] = dice[1];dice[1] = tmp
    elif i==2:dice[5] = dice[1];dice[1] = dice[2];dice[2] = dice[3];dice[3] = tmp
    elif i==3:dice[5]=dice[0];dice[0]=dice[2];dice[2]=dice[4];dice[4] = tmp
    else :dice[5] = dice[4];dice[4] = dice[2];dice[2] = dice[0];dice[0] = tmp
        

def move(r,c):
    dr = [0,0,0,-1,1]
    dc = [0,1,-1,0,0]
    while order:
        i = order.popleft()
        if not ((0<=r+dr[i]<=N-1) and(0<=c+dc[i]<=M-1)):continue
        r+=dr[i]
        c+=dc[i]
        if 0<=r<=N-1 and 0<=c<=M-1:
            dice_move(i)
            if mat[r][c] > 0:
                dice[5] = mat[r][c]
                mat[r][c]=0
            else: mat[r][c] = dice[5]
            print(dice[2])

move(r,c)

