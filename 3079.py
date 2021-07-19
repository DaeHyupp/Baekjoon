import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split(" "))
judge = []
for _ in range(N):
    judge.append(int(input().rstrip()))
start = 1
end = max(judge) * M//N +1
print(end)
ans = 0
while start<=end:
    mid = (start+end)//2
    cnt = 0
    for i in judge:
        cnt += mid//i
    if cnt >= M:
        ans = mid
        end = mid -1
    else: start = mid+1

print(ans)

