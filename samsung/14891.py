import sys
from collections import deque
input = sys.stdin.readline

wheels = [[0]*8]+[list(map(int,list(input().rstrip())))for _ in range(4)]
K = int(input())
operation = deque([])
for _ in range(K):
    operation.append(list(map(int,input().rstrip().split(" "))))

def movable():
    move = [0]*5
    wheel, rotate = operation.popleft()
    if wheel ==1:
        move[1]= rotate
        if wheels[1][2]!=wheels[2][6]:
            move[2]= -rotate
            if wheels[2][2]!=wheels[3][6]:
                move[3]= rotate
                if wheels[3][2]!=wheels[4][6]:
                    move[4]= -rotate
    elif wheel ==2:
        move[2]=rotate
        if wheels[1][2]!=wheels[2][6]: move[1]=-rotate
        if wheels[2][2]!=wheels[3][6]:
            move[3]=-rotate
            if wheels[3][2]!=wheels[4][6]:
               move[4]=rotate
    elif wheel==3:
        move[3]=rotate
        if wheels[3][2] !=wheels[4][6]: move[4]=-rotate
        if wheels[2][2]!=wheels[3][6]:
            move[2]=-rotate
            if wheels[1][2]!=wheels[2][6]:
               move[1]=rotate
    else:
        move[4]=rotate
        if wheels[4][6]!=wheels[3][2]:
            move[3]=-rotate
            if wheels[2][2]!=wheels[3][6]:
                move[2]=rotate
                if wheels[1][2]!=wheels[2][6]:
                    move[1]=-rotate
    return move

def rotate(move):
    for i in range(1,5):
        if move[i] ==1:
            tmp = wheels[i][7]
            for r in range(7,0,-1):
                wheels[i][r] = wheels[i][r-1]
            wheels[i][0] = tmp
        elif move[i] == -1:
            tmp = wheels[i][0]
            for r in range(0,7):
                wheels[i][r] = wheels[i][r+1]
            wheels[i][7] = tmp
def count():
    cnt = 0
    if wheels[1][0] == 1:
        cnt += 1
    if wheels[2][0] == 1:
        cnt += 2
    if wheels[3][0] == 1:
        cnt += 4
    if wheels[4][0] == 1:
        cnt += 8
    return cnt

while operation:
    rotate(movable())
print(count())
    
    

