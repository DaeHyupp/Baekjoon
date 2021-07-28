import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    appli = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]
    appli = sorted(appli, key=lambda x: x[1])
    ans = 1
    minor = appli[0][0]
    for i in range(1,N):
        minor = min(minor,appli[i-1][0])
        if minor > appli[i][0]:
            ans += 1
            minor = appli[i][0]
    print(ans)       
