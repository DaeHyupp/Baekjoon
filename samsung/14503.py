import sys
input = sys.stdin.readline

N, M = map(int,input().split(" "))
r, c, d = map(int, input().split(" "))
room = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]

cnt = 0

def able(r,c,d):        
    
    if room[r][c-1]!=0 and room[r][c+1]!=0 and room[r-1][c]!=0 and room[r+1][c]!=0:
        if d==0:
            if room[r+1][c] ==1:return 0 #nothing can do
            else: return 1 # can go backwards
        elif d==1:
            if room[r][c-1] ==1:return 0
            else: return 1
        elif d==2:
            if room[r-1][c] ==1:return 0
            else: return 1
        else:
            if room[r][c+1] ==1:return 0
            else: return 1
    
    if d==0:
        if room[r][c-1] == 0: return 3 #can clean left side
        else: return 2
    elif d==1:
        if room[r-1][c] == 0: return 3
        else: return 2
    elif d==2:
        if room[r][c+1] == 0: return 3
        else: return 2
    else:
        if room[r+1][c] == 0: return 3
        else: return 2
    

def clean(r,c,d):
    global cnt
    if room[r][c]!=2:
        cnt += 1
        room[r][c]=2
    check = able(r,c,d)
    if check == 0: return cnt
    elif check ==1:
        if d==0: clean(r+1,c,0)
        elif d==1: clean(r,c-1,1)
        elif d==2: clean(r-1,c,2)
        else: clean(r,c+1,3)
    elif check ==2:
        if d==0: clean(r,c,3)
        elif d==1: clean(r,c,0)
        elif d==2: clean(r,c,1)
        else: clean(r,c,2)
    elif check==3:
        if d==0: clean(r,c-1,3)
        elif d==1: clean(r-1,c,0)
        elif d==2: clean(r,c+1,1)
        else: clean(r+1,c,2)
    return cnt
print(clean(r,c,d))

        

