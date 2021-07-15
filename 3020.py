import sys
input = sys.stdin.readline

N, H = map(int,input().rstrip().split(" "))
ground = [0]* (H+1)
ceiling= [0]* (H+1)
for i in range(N//2):
    ground[int(input().rstrip())] += 1
    ceiling[1+H-int(input().rstrip())] += 1

for i in range(H-1,0,-1):
    ground[i] += ground[i+1]
for i in range(1,H+1):
    ceiling[i] +=ceiling[i-1]

ans = [0]*(H+1)
for i in range(1, H+1):
    ans[i] = ground[i]+ceiling[i]
    print(ans[i])
pr = min(ans[1:H+1])
print(ans[1:H+1])
print(pr, ans[1:H+1].count(pr))

