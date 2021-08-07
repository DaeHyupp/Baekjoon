import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if mat[i][j] == 5:
            pror, proc = i, j
        elif mat[i][j] == 2:
            sungr,sungc = i, j

def solve():
    cnt = 0
    if pror==sungr:
        if abs(proc-sungc) <5:return 0
        for i in range(min(proc,sungc)+1,min(proc,sungc)+abs(proc-sungc)):
            if mat[pror][i]==1:
                cnt += 1
    elif proc==sungc:
        if abs(pror-sungr) <5:return 0
        for i in range(min(pror,sungr)+1,min(pror,sungr)+abs(pror-sungr)):
            if mat[i][proc]==1:
                cnt += 1
    else:
        if ((proc-sungc)**2)+((pror-sungr)**2) <25:return 0
        for i in range(min(pror,sungr),min(pror,sungr)+abs(pror-sungr)+1):
            for j in range(min(proc,sungc),min(proc,sungc)+abs(proc-sungc)+1):
                if mat[i][j]==1:
                    cnt +=1
    return cnt
if solve()>=3:print(1)
else: print(0)

