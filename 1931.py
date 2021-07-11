import sys
input = sys.stdin.readline

N = int(input())
time = []
for i in range(N):
    s, e = map(int,input().rstrip().split(" "))
    time.append((s,e))
time = sorted(time, key=lambda start:start[0])
time = sorted(time, key =lambda end: end[1])
cnt = 0
end_check = 0
for i in range(N):
    if end_check <= time[i][0]:
        end_check = time[i][1]
        cnt += 1
print(cnt)

