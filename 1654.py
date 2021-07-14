import sys
K, N = map(int, input().split())
line = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(line)

while start <= end:
    mid = (start + end) // 2 
    lan = 0 
    for i in line:
        lan += i // mid
 
    if lan >= N:start = mid + 1
    else:end = mid - 1
print(end)

