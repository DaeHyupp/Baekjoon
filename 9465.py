import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0]*N for _ in range(2)]
    sticker = [list(map(int,input().rstrip().split(" "))) for _ in range(2)]
    if N>=1: dp[0][0] =sticker[0][0]; dp[1][0]=sticker[1][0]
    if N>=2: dp[0][1] =sticker[1][0]+sticker[0][1] ; dp[1][1] = sticker[0][0]+sticker[1][1]
    if N>=3:
        for i in range(2,N):
            dp[0][i] = sticker[0][i] + max(dp[1][i-1],dp[1][i-2])
            dp[1][i] = sticker[1][i] + max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][N-1],dp[1][N-1]))

