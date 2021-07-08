N = int(input())
mat = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int,input().split(" "))
    mat[start].append(end)
    mat[end].append(start)

check = [0]*(N+1)

iscorrect = list(map(int,input().split(" ")))

def dfs(s):
    if check[s] != 0:
        return
    check[s] = 1
    for idx in mat[s]:
        if check[idx] == 0:
            ans.append(idx)
            dfs(idx)
    return
            

rank = [-1 for i in range(N+1)]

for i in range(1,N+1):
    rank[iscorrect[i-1]]=i

for i in range(1, N+1):
    mat[i]=sorted(mat[i],key=lambda x: rank[x])

ans = []
ans.append(1)
dfs(1)
if ans == iscorrect:
    print(1)
else:
    print(0)
# c = len(ans)
# check =1
# for i in range(c):
#   if ans[i] != iscorrect[i]:
#       check = 0
#       break
#
#if check == 1:print(1)
#else:print(0)
