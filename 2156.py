import sys
input = sys.stdin.readline

N = int(input())
drink = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
if N>=1: dp[0] = drink[0]
if N>=2: dp[1] = drink[0]+drink[1]
if N>=3: dp[2] = max(drink[0]+drink[2],drink[1]+drink[2],drink[0]+drink[1])
if N>=4:
    dp[3] = max(dp[0]+drink[2]+drink[3],dp[1]+drink[3],)
    for i in range(4,N):
        dp[i] = max(dp[i-4]+drink[i-1]+drink[i],dp[i-3]+drink[i-1]+drink[i],dp[i-2]+drink[i])
print(max(dp))

