import sys
input = sys.stdin.readline

N = int(input().rstrip())
k = int(input().rstrip())

start = 1
end = k
ans = 0
while start <= end:
    mid = (start+end)//2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i,N)

    if cnt >= k:
       ans = mid
       end = mid-1
    else: start = mid+1

print(ans)

