N = int(input())

ans = [0]*(N+1)
for i in range(N+1):
    if i==1: ans[i]=1
    elif i==2: ans[i]=3
    else: ans[i] = ans[i-1]+2*ans[i-2]

print(ans[N]%10007)

