import sys
input = sys.stdin.readline

N = int(input())
stair =[int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]

dp[0] = stair[0]
if N>=2:dp[1] = stair[0]+stair[1]
if N>=3:dp[2] = max(stair[1]+stair[2],stair[0]+stair[2])

if N ==1: print(dp[0])
elif N==2: print(dp[1])
elif N==3: print(dp[2])
else:
    for i in range(3, N):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[N-1])

