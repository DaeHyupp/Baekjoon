import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split(" "))

check = [0]*(10**5+1)
check[N] = 1

def bfs():
    global cnt
    dn = [-1, 1, 2]

    while q:
        level=len(q)
        cnt += 1
        for l in range(level):
            n = q.pop(0)
    
            for i in range(3):
                if i==2: nn = 2*n
                else: nn = n + dn[i]
            
                
                if 0<=nn<10**5+1 and check[nn] == 0:
                
                    if nn ==K: return
                    check[nn] = 1                  
                    q.append(nn)


q = []
q.append(N)
check[N] = 1
cnt = 0
if N == K :
    print(0)
else:
    bfs()
    print(cnt)

