import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
costs = list(map(int,input().rstrip().split(" ")))
if N>=1:dp[0] = costs[0]
if N>=2:dp[1] = max(costs[0]*2,costs[1])
if N>=3:
    dp[2] = max(costs[0]*3,costs[1]+costs[0],costs[2])
    maxi = 0
    for i in range(3,N):
        for j in range(0, i//2):
            maxi = max(maxi,dp[j]+dp[i-j-1])
        if i%2!=0:
            maxi = max(maxi,dp[i//2]*2)
        dp[i] = max(maxi,costs[i])
print(dp[N-1])

# More Pythonic and Compact
# 
# dp = [0] + list(map(int,input().split()))
# for i in range(1,N+1):
#     dp[i] = max(dp[j] + dp[i-j] for j in range(i//2, i+1))
# print(p[N])


