import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int,input().rstrip().split(" "))) for _ in range(N)]
dp = []
for i in range(N):
    dp.append(schedule[i][1])
dp.append(0)
for i in range(N-1,-1,-1):
    if schedule[i][0]+i>N: dp[i]=dp[i+1]
    else: dp[i] = max(dp[i+1],dp[i]+dp[i+schedule[i][0]])

print(dp[0])

